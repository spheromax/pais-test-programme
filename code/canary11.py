"""Canary for run 11: re-derive fifteen run-10 numbers from the inputs written in state v11 and run-sheet part 8, with new code,
and compare with run10_numbers.json."""
import json, math
L = json.load(open('/home/claude/p3/sim/pais/run10_numbers.json'))
sig = 5.670374419e-8; A = 2.5635; B0 = 6.3e-3; Bf = 30.0; c = 299792458.0; G = 6.67430e-11
def dB_allow(eps, Ts, Tm, n=1):           # 1 W at 6.3 mT, cubic, harmonic n
    return B0 * (eps * sig * A * (Tm**4 - Ts**4) / n)**(1 / 3)
def Tr(dB, eps, Ts=4.2):
    return ((dB / B0)**3 / (eps * sig * A) + Ts**4)**0.25
# T_m from i <= 0.5063 with J_need 5.856 kA/mm2, J_e(4.2 K) = 36.3 MA/cm2 x 4 um / basis, T* = 22 K
Tm = lambda basis: 4.2 + 22.0 * math.log(0.5063 * 3.63e11 * 4e-6 / basis / 5.856e9)
lam = 22.368171106800702 / (4 * math.pi)  # M / 2 pi R with R = 2
v = 2000 * math.pi
C = lambda T: 0.11925 * T + 12 * math.pi**4 / 5 * 8.314462618 / 400.0**3 / 0.0587 * T**3
checks = [
 ('T_m, 50 um basis (K)', Tm(50e-6), L['i33']['Tmax_K']['thick film, 50 um basis']),
 ('ripple 4.2 K wall, 50 um, eps 0.05 (mT)', dB_allow(0.05, 4.2, Tm(50e-6)) * 1e3, [r for r in L['i33']['table'] if r['Ts'] == 4.2 and r['eps'] == 0.05 and r['tape'].endswith('50 um basis')][0]['dB_mT']),
 ('ripple 4.2 K wall, 0.1 mm, eps 0.02 (mT)', dB_allow(0.02, 4.2, Tm(0.1e-3)) * 1e3, [r for r in L['i33']['table'] if r['Ts'] == 4.2 and r['eps'] == 0.02 and r['tape'].endswith('0.1 mm basis')][0]['dB_mT']),
 ('eps sensitivity 0.95/0.02', (0.95 / 0.02)**(1 / 3), L['i33']['eps_sensitivity']),
 ('Iseult-class loss at 30 T (W)', (0.88e-6 * Bf / B0)**3, L['i33']['Iseult measured (NbTi, shimmed passively)']['P_W']),
 ('100 ppm rotor temperature, eps 0.1 (K)', Tr(100e-6 * Bf, 0.1), L['i33']['REBCO NMR, design vs measured, unshimmed']['T_r']['eps 0.1']),
 ('coupon mass (g)', lam * 0.2 * 0.025 * 1e3, L['i34']['coupon']['m_g']),
 ('coupon normal force (kN)', lam * 0.2 * 0.025 * v**2 / 2 / 1e3, L['i34']['coupon']['N_kN']),
 ('capstan 30 deg, mu 0.3', math.exp(-0.3 * math.pi / 6), L['i34']['capstan']['30 deg']['mu 0.3']['v_ratio']),
 ('beta ratio at 20 K', math.exp(-2 * 15.8 / 22) * C(4.2) / C(20.0), [r for r in L['i35']['rows'] if r['T'] == 20.0][0]['beta_ratio']),
 ('warm design 20 K, eps 0.5 (mT)', dB_allow(0.5, 20.0, Tm(50e-6)) * 1e3, L['i35']['warm_design_ripple_mT']['Ts 20 K']['eps 0.5']),
 ('HFGW flux for h 1e-21 at 300 MHz (W/m2)', c**3 * (2 * math.pi * 3e8)**2 * 1e-42 / (32 * math.pi * G), L['iii9']['threshold_flux_W_m2']['RADES ~1e-21 at 300 MHz']),
 ('Pais flux as GW, h at 1 GHz', math.sqrt(32 * math.pi * G * 1.18e24 / c**3) / (2 * math.pi * 1e9), L['iii9']['pais_flux_h']['1 GHz']),
 ('US 3,095,167 shortfall', (9.80665 / 130.0) / (4 * math.pi * 8.8541878128e-12 * 3e6), L['iii10']['ratio']),
 ('FELICE peak fluence, zR 55 mm (mJ/cm2)', 2 * 400e-6 / (math.pi * 30e-6 * 0.055 / math.pi) / 10, L['v13']['zR 55 mm']['F_peak_mJ_cm2']),
]
out = []
for name, new, logged in checks:
    ok = abs(new / logged - 1) < 2e-3
    out.append(dict(name=name, new=new, logged=logged, ok=ok))
    print(f"{'ok ' if ok else 'BAD'} {name:44s} new {new:.5g}  logged {logged:.5g}  dev {abs(new / logged - 1) * 100:.3f} %")
json.dump(out, open('/home/claude/p3/sim/pais/canary11.json', 'w'), indent=1)
print(sum(o['ok'] for o in out), 'of', len(out))
