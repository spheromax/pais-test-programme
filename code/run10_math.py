"""Run 10 of the Pais gap loop: every number in run-sheet part 8 (I.33-I.35, III.9-III.10, V.13).  Run: python3 run10_math.py"""
import json, math

c = 299792458.0; G = 6.67430e-11; mu0 = 4e-7 * math.pi * 1.00000000055; eps0 = 8.8541878128e-12; sSB = 5.670374419e-8
out = {}

# ------------------------------------------------------------------ B6 inputs (run 8/9)
R, h, v, M, B = 2.0, 0.10, 2 * math.pi * 1000.0, 22.368171106800702, 30.0
lam = M / (2 * math.pi * R)                     # rotor line density, kg/m
A_rot, P0, dB0 = 2.5635, 1.0, 6.3e-3            # radiating area; ripple loss 1 W at 6.3 mT (n = 1, 500 Hz), cubic (I.27)
J_need, i_safe, Tstar = 5.856e9, 0.5063, 22.0
Je4 = {'thick film, 0.1 mm basis': 3.63e11 * 4e-6 / 0.1e-3, 'thick film, 50 um basis': 3.63e11 * 4e-6 / 50e-6}
Tmax = {k: 4.2 + t * math.log(i_safe * J / J_need) for k, J in Je4.items() for t in (Tstar,)}
Tmax_rng = {k: [4.2 + t * math.log(i_safe * J / J_need) for t in (21.0, 23.0)] for k, J in Je4.items()}

def ripple_allowed(eps, Ts, Tm, n=1):
    """largest ripple (T) whose loss the rotor can radiate while staying at or below Tm"""
    P = eps * sSB * A_rot * (Tm**4 - Ts**4)
    return dB0 * (max(P, 0) / (P0 * n))**(1 / 3), P

def T_rotor(dB, eps, Ts, n=1):
    P = P0 * n * (dB / dB0)**3
    return (P / (eps * sSB * A_rot) + Ts**4)**0.25, P

# ------------------------------------------------------------------ I.33 field quality the stator needs
i33 = {'Tmax_K': Tmax, 'Tmax_range_K': Tmax_rng, 'table': []}
for Ts in (4.2, 15.0, 20.0):
    for k, Tm in Tmax.items():
        if Tm <= Ts: continue
        for eps in (0.02, 0.05, 0.1, 0.5, 0.95):
            dB, P = ripple_allowed(eps, Ts, Tm)
            i33['table'].append(dict(Ts=Ts, tape=k, Tm=Tm, eps=eps, P_W=P, dB_mT=dB * 1e3, ppm=dB / B * 1e6))
i33['eps_sensitivity'] = (0.95 / 0.02)**(1 / 3)          # allowed ripple scales as eps^(1/3)
# evidence: Iseult (NbTi, 11.72 T) 0.88 ppm peak to peak on a 22 cm sphere; 9.4 T all-REBCO NMR > 100 ppm before shimming
for name, ppm in (('Iseult measured (NbTi, shimmed passively)', 0.88), ('REBCO NMR, design vs measured, unshimmed', 100.0)):
    dB = ppm * 1e-6 * B
    i33[name] = dict(ppm=ppm, dB_mT=dB * 1e3, P_W=P0 * (dB / dB0)**3,
                     T_r={f'eps {e}': T_rotor(dB, e, 4.2)[0] for e in (0.05, 0.1, 0.5)})
i33['iseult_dB_at_11p72T_uT'] = 0.88e-6 * 11.72 * 1e6
i33['scf_fraction_sim'] = 0.8 / 10.26                    # 0.8 T of screening-current field, 7.8 % (simulation)
out['i33'] = i33

# ------------------------------------------------------------------ I.34 tangential fragment test
rho_r = 8000.0                                            # assumed mean rotor density (Hastelloy, Cu, Ag, REBCO), kg/m^3
i34 = dict(lam=lam, p_wall_Pa=lam * v**2 / (R * h), t_radial_mm=lam / (rho_r * h) * 1e3, rho_assumed=rho_r)
hc, lc = 0.020, 0.025                                     # coupon height and length (fits a 38 mm bore with sabot)
m_c = lam * hc / h * lc
i34['coupon'] = dict(h_mm=hc * 1e3, l_mm=lc * 1e3, m_g=m_c * 1e3, N_kN=m_c * v**2 / R / 1e3,
                     p_check_Pa=m_c * v**2 / R / (hc * lc), KE_kJ=0.5 * m_c * v**2 / 1e3)
cap = {}
for th_deg in (30, 60, 90):
    th = math.radians(th_deg)
    cap[f'{th_deg} deg'] = {f'mu {mu}': dict(v_ratio=math.exp(-mu * th), KE_lost=1 - math.exp(-2 * mu * th)) for mu in (0.1, 0.3, 0.5)}
cap['full turn'] = {f'mu {mu}': math.exp(-2 * math.pi * mu) for mu in (0.1, 0.3, 0.5)}
i34['capstan'] = cap
i34['mu_resolution_30deg_1pc'] = 0.01 * math.sqrt(2) / math.radians(30)
i34['transit_30deg_ms'] = R * math.radians(30) / v * 1e3
i34['gap_entry_v_r'] = {f'{g} mm': v * math.sqrt(1 - (R / (R + g * 1e-3))**2) for g in (1, 5, 20)}   # rotor at R, wall at R + g (as I.30)
sabot = 0.020
i34['speeds'] = {}
for vv in (3000.0, v):
    i34['speeds'][f'{vv/1e3:.2f} km/s'] = dict(e_MJ_per_kg=vv**2 / 2 / 1e6, over_vap=vv**2 / 2 / 7.5e6,
                                               p_wall_MPa=lam * vv**2 / (R * h) / 1e6,
                                               package_kJ=0.5 * (m_c + sabot) * vv**2 / 1e3)
i34['swri_3kms_MJ'] = 0.5 * 0.5 * 3000**2 / 1e6
i34['long_coupon_3kms'] = dict(l_m=0.25, m_g=lam * hc / h * 0.25 * 1e3, KE_kJ=0.5 * lam * hc / h * 0.25 * 3000**2 / 1e3)
out['i34'] = i34

# ------------------------------------------------------------------ I.35 flux-jump margin against temperature
gam = 7.0e-3 / 0.0587                                     # Ni-like electronic coefficient, J/(kg K^2)  (assumed for Hastelloy)
thD = 400.0; aD = 12 * math.pi**4 / 5 * 8.314462618 / thD**3 / 0.0587   # Debye T^3 coefficient, J/(kg K^4)
Cm = lambda T: gam * T + aD * T**3                         # J/(kg K)
rows = []
for T in (4.2, 10.0, 15.0, 20.0, 25.0):
    rows.append(dict(T=T, Jc2=math.exp(-2 * (T - 4.2) / Tstar), C_ratio=Cm(T) / Cm(4.2),
                     beta_ratio=math.exp(-2 * (T - 4.2) / Tstar) * Cm(4.2) / Cm(T)))
Jc, a = 3.63e11, 2e-6                                     # thick film, 30 T B||ab, 4.2 K; half thickness of a 4 um film
Cv_film, Cv_comp = 0.1 * 6300, Cm(4.2) * 8890              # J/(m^3 K): REBCO alone (assumed), Hastelloy-dominated tape
q = mu0 * Jc**2 * a**2
i35 = dict(rows=rows, C_4K=Cm(4.2), C_20K=Cm(20.0), q_J_m3=q,
           beta_film=q / (Cv_film * Tstar),
           beta_tape_50um=q * (4 / 50) / (Cv_comp * Tstar), beta_tape_100um=q * (4 / 100) / (Cv_comp * Tstar))
dp = {}
for Ts in (15.0, 20.0):
    Tm = Tmax['thick film, 50 um basis']
    dp[f'Ts {Ts:.0f} K'] = {f'eps {e}': ripple_allowed(e, Ts, Tm)[0] * 1e3 for e in (0.05, 0.5)}
i35['warm_design_ripple_mT'] = dp
out['i35'] = i35

# ------------------------------------------------------------------ III.9 high-frequency GW cavities as a test of EM->GW claims
S_of = lambda h_, f: c**3 * (2 * math.pi * f)**2 * h_**2 / (32 * math.pi * G)
h_of = lambda S, f: math.sqrt(32 * math.pi * G * S / (c**3 * (2 * math.pi * f)**2))
thr = {'RADES ~1e-21 at 300 MHz': (1e-21, 300e6), 'cavities ~1e-20 at 3 GHz': (1e-20, 3e9), 'CAPP re-analysis 3.9e-21 at 5.311 GHz': (3.9e-21, 5.311e9)}
i39 = {'threshold_flux_W_m2': {k: S_of(h_, f) for k, (h_, f) in thr.items()}}
S_pais = 1.18e24
i39['pais_flux_h'] = {f'{f/1e9:g} GHz': h_of(S_pais, f) for f in (0.3e9, 1e9, 5.311e9)}
kappa = 4 * math.pi * G / (mu0 * c**4)
P_gw = kappa * 10.0**2 * 1e6                               # 10 T m, 1 MW of EM power
S_known = P_gw / (4 * math.pi * 1.0**2)
i39.update(kappa=kappa, P_gw_W=P_gw, S_known_1m=S_known, h_known_1GHz=h_of(S_known, 1e9),
           margin_claim_over_threshold=h_of(S_pais, 5.311e9) / 3.9e-21, margin_threshold_over_known=1e-21 / h_of(S_known, 0.3e9))
out['iii9'] = i39

# ------------------------------------------------------------------ III.10 patent sweep: the one claim with a number to check (US 3,095,167)
E_atm, E_b, r = 130.0, 3.0e6, 1.0
q_max = 4 * math.pi * eps0 * r**2 * E_b
out['iii10'] = dict(q_needed_1kg=9.80665 / E_atm, q_max_1m=q_max, ratio=9.80665 / E_atm / q_max, lift_g=q_max * E_atm / 9.80665 * 1e3)

# ------------------------------------------------------------------ V.13 FELICE intracavity fluence against the hold fluence
E_in, E_out, lam_ir, F_hold = 400e-6, 10e-6, 30e-6, 4.0
v13 = dict(intracavity_factor=E_in / E_out, F_hold_mJ_cm2=F_hold / 10)
for zR in (0.050, 0.055, 0.082):
    w0 = math.sqrt(lam_ir * zR / math.pi); Fp = 2 * E_in / (math.pi * w0**2)
    w_h = math.sqrt(2 * E_in / (math.pi * F_hold)); z_h = zR * math.sqrt((w_h / w0)**2 - 1)
    v13[f'zR {zR*1e3:.0f} mm'] = dict(w0_mm=w0 * 1e3, F_peak_mJ_cm2=Fp / 10, ratio=Fp / F_hold, w_hold_mm=w_h * 1e3, z_hold_mm=z_h * 1e3)
out['v13'] = v13

json.dump(out, open('/home/claude/p3/sim/pais/run10_numbers.json', 'w'), indent=1)

# ------------------------------------------------------------------ print
print('I.33 Tmax', {k: round(t, 2) for k, t in Tmax.items()}, 'range', {k: [round(x, 1) for x in r_] for k, r_ in Tmax_rng.items()})
for r_ in i33['table']:
    print(f"  Ts {r_['Ts']:4.1f} {r_['tape'][:22]:22s} eps {r_['eps']:4.2f}: P {r_['P_W']*1e3:8.3f} mW  dB {r_['dB_mT']:5.2f} mT = {r_['ppm']:5.1f} ppm")
print('  eps sensitivity', round(i33['eps_sensitivity'], 2))
for k in ('Iseult measured (NbTi, shimmed passively)', 'REBCO NMR, design vs measured, unshimmed'):
    d = i33[k]; print(' ', k, f"{d['dB_mT']:.4f} mT P {d['P_W']:.2e} W", {kk: round(t, 2) for kk, t in d['T_r'].items()})
print('I.34', {k: (round(v_, 3) if isinstance(v_, float) else v_) for k, v_ in i34.items() if k not in ('capstan', 'speeds', 'coupon', 'gap_entry_v_r', 'long_coupon_3kms')})
print('  coupon', {k: round(v_, 2) for k, v_ in i34['coupon'].items()})
print('  capstan 30 deg', {k: round(d['v_ratio'], 3) for k, d in cap['30 deg'].items()}, 'full turn', {k: round(x, 3) for k, x in cap['full turn'].items()})
print('  gap v_r', {k: round(x, 0) for k, x in i34['gap_entry_v_r'].items()}, 'speeds', {k: {kk: round(x, 2) for kk, x in d.items()} for k, d in i34['speeds'].items()})
print('  long coupon', i34['long_coupon_3kms'], 'SwRI MJ', i34['swri_3kms_MJ'])
print('I.35', [{k: round(x, 3) for k, x in r_.items()} for r_ in rows])
print('  C 4K/20K', round(Cm(4.2), 3), round(Cm(20.0), 3), 'q', f'{q:.3e}', 'beta film', round(i35['beta_film'], 1), 'tape 50/100', round(i35['beta_tape_50um'], 2), round(i35['beta_tape_100um'], 2))
print('  warm design ripple', {k: {kk: round(x, 2) for kk, x in d.items()} for k, d in dp.items()})
print('III.9 thresholds', {k: f'{x:.2e}' for k, x in i39['threshold_flux_W_m2'].items()})
print('  pais h', {k: f'{x:.2e}' for k, x in i39['pais_flux_h'].items()}, 'kappa', f'{kappa:.3e}', 'P_gw', f'{P_gw:.2e}', 'S 1 m', f'{S_known:.2e}', 'h 1 GHz', f"{i39['h_known_1GHz']:.2e}")
print('  margins', f"{i39['margin_claim_over_threshold']:.2e}", f"{i39['margin_threshold_over_known']:.2e}")
print('III.10', {k: f'{x:.3e}' for k, x in out['iii10'].items()})
print('V.13', {k: ({kk: round(x, 2) for kk, x in d.items()} if isinstance(d, dict) else d) for k, d in v13.items()})
