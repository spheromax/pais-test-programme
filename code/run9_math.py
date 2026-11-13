"""Run 9 of the Pais gap loop: new maths.  I.30 containment inherits the virial; I.31 angular momentum after a burst;
I.32 conductor at the radiative temperature (+ I.29 note: J_e at 8 T); V.12 lasing headroom at 30 um and the film in monolayers;
III.8 UV charge-modulation control for X1.  Writes run9_numbers.json.  Inputs are written next to each number."""
import math, json
mu0 = 4e-7 * math.pi * 1.00000000055; eps0 = 8.8541878128e-12; sSB = 5.670374419e-8; e = 1.602176634e-19
out = {}
# ---------------------------------------------------------------- B6 baseline (state v9; run sheet I.17, I.25, I.28)
R, rps = 2.0, 500.0; v = 2 * math.pi * R * rps; w = 2 * math.pi * rps
T = 441.53e6; M = 2 * T / v**2; L = 2 * T / w
craft_min, stator_min = 312.0, 289.0          # state v9: craft minimum 312 kg; stator >= 289 kg of T1200 carrying 2T
s_st = 2 * T / stator_min                      # specific strength that 289 kg implies (J/kg)
h = 0.10                                       # rotor height: 25 axial tapes of 4 mm
A_w = 2 * math.pi * R * h
e_vap = 7.5e6                                  # Ni-class heating + vaporisation (run 8 input)
out['b6'] = dict(v=v, M=M, L=L, T=T, s_stator=s_st, e_debris=v**2 / 2, e_vap=e_vap, debris_over_vap=v**2 / 2 / e_vap)
# ---------------------------------------------------------------- I.30 containment inherits the virial
i30 = {}
i30['hoop_force_N'] = M * v**2 / (2 * math.pi * R)             # sliding debris: same hoop force as the held rotor
i30['p_debris_Pa'] = M * v**2 / (2 * math.pi * R**2 * h)       # on a wall of height h at R
i30['p_field_30T_Pa'] = 30.0**2 / (2 * mu0)
i30['virial'] = {lab: dict(trace_over_2T=3 * (g - 1) / 2, hoop_over_2T=(g - 1), ends_kg=(g - 1) * T / s_st)
                 for g, lab in ((5 / 3, 'gamma 5/3'), (1.4, 'gamma 1.4'), (1.2, 'gamma 1.2'))}
sig_c, E_c, rho_c = 3.82e9, 0.6 * 294e9, 1560.0               # T1000G hoop at V_f 0.6 (run sheet I.3)
v_allow = sig_c / math.sqrt(E_c * rho_c); i30['v_allow'] = v_allow
imp = {}
for g in (1e-3, 5e-3, 20e-3):
    sth = math.sqrt(1 - (R / (R + g))**2); vr = v * sth; ia = M * vr / A_w
    ma = stator_min / (2 * math.pi * (R + g) * h); vw = ia / ma
    imp[f'{g * 1e3:.0f} mm'] = dict(v_r=vr, impulse_Ns_m2=ia, stator_kg_m2=ma, v_wall=vw, energy_ratio=(vw / v_allow)**2, m_a_needed=ia / v_allow)
i30['impact'] = imp
c_c = math.sqrt(E_c / rho_c); i30['T_breathe_ms'] = 2 * math.pi * R / c_c * 1e3
i30['friction'] = {f'mu {mu}': dict(t_ms=R / (mu * v) * 1e3, P_peak_W=mu * M * v**3 / R) for mu in (0.1, 0.3, 0.5)}
i30['ablate_kg'] = {'carbon, 59.8 MJ/kg': T / 59.8e6, 'iron, 7.5 MJ/kg': T / 7.5e6}
i30['liner'] = {f'{Ml} kg': dict(v_f=M * v / (M + Ml), dissipated=1 - M / (M + Ml), hoop_left=M / (M + Ml)) for Ml in (25, 50, 100, 200)}
low = M + stator_min * 1.0 + i30['virial']['gamma 1.2']['ends_kg'] + 50 + T / 59.8e6
high = M + stator_min * 1.5 + i30['virial']['gamma 5/3']['ends_kg'] + 100 + T / 7.5e6
i30['craft_kg'] = dict(minimum=craft_min, run8=craft_min + 7198, low=low, high=high, low_x=low / craft_min, high_x=high / craft_min,
                       run8_x=(craft_min + 7198) / craft_min)
E10 = 10 * 4.184e6; PV = 0.3 * E10; s_hy = 690e6 / 7850          # LANL M-9: 10 kg TNT, <= 75 t of HY-100; products gamma ~1.3
i30['blast_vessel'] = dict(PV=PV, M_static_kg=1.5 * PV / s_hy, M_limit_kg=75e3, ratio=75e3 / (1.5 * PV / s_hy))
i30['v_vap'] = math.sqrt(2 * e_vap)                            # debris faster than this carries more than its vaporisation energy
out['i30'] = i30
# ---------------------------------------------------------------- I.31 angular momentum after a burst
Ic = stator_min * (R + 0.05)**2
out['i31'] = dict(L=L, I_craft=Ic, omega=L / Ic, rpm=L / Ic * 60 / (2 * math.pi), rim=L / Ic * (R + 0.05),
                  torque_120s=L / 120, bias_torque_0p1=0.1 * L, spin_down_1h_W=T / 3600)
# ---------------------------------------------------------------- I.32 conductor at the radiative temperature
J_need, i_safe, A_rot, Ts = 5.856e9, 0.5063, 2.5635, 4.2
Jt = {'production (LBC6, 45 um)': 8.3e9, 'thick film, 0.1 mm basis': 3.63e11 * 4e-6 / 0.1e-3, 'thick film, 50 um basis': 3.63e11 * 4e-6 / 50e-6}
def T_rot(dB, eps):
    P = 1.0 * (dB / 6.3e-3)**3                                   # ripple loss: 1 W at 6.3 mT, cubic (run 8, I.27)
    return (P / (eps * sSB * A_rot) + Ts**4)**0.25, P
rows = []
for dB in (0.3e-3, 0.5e-3, 1e-3, 2e-3):
    for eps in (0.1, 0.3, 0.5):
        Tr, P = T_rot(dB, eps); f = math.exp(-(Tr - 4.2) / 22.0)
        rows.append(dict(dB_mT=dB * 1e3, eps=eps, P_W=P, T_r=Tr, f=f, J_req_kA_mm2=J_need / (i_safe * f) / 1e9,
                         i={k: J_need / (J * f) for k, J in Jt.items()},
                         f_range=[math.exp(-(Tr - 4.2) / t) for t in (21.0, 23.0)]))
lim = {}
for k, J in Jt.items():
    # highest rotor temperature at which i <= i_safe, T* = 22 K (21, 23)
    lim[k] = {f'T*={t}': 4.2 + t * math.log(J * i_safe / J_need) if J * i_safe > J_need else None for t in (21.0, 22.0, 23.0)}
out['i32'] = dict(Je_4K=Jt, rows=rows, T_max_for_safe=lim, loop_m=2 * math.pi * R, loops_per_40m=int(40 // (2 * math.pi * R)),
                  pieces_40m=math.ceil(1111 / int(40 // (2 * math.pi * R))))
J30 = 8.3e9; Jring = 10.4675e9
out['i29_note'] = {f'alpha {a}': dict(Je_8T=J30 * (30 / 8)**a, i=Jring / (J30 * (30 / 8)**a)) for a in (0.5, 0.75)}
# ---------------------------------------------------------------- V.12 lasing headroom at 30 um; film in monolayers
fel = {'FELIX FEL-2': (0.50, 0.05), 'FHI mid-IR FEL (computed)': (2.0, 0.08), 'ELBE U100 at 30 um, low': (0.25, 0.10),
       'ELBE U100 at 30 um, high': (0.50, 0.10), 'ELBE U27 at 10 um': (0.06, 0.07)}
def y_of_A(A):
    return (2 * (1 - A) - 2 * math.sqrt(1 - 2 * A)) / A if A <= 0.5 else 2.0
Z0 = 376.730313668; s1 = 3e4
d111 = 14.24e-10 / math.sqrt(3)
out['v12'] = dict(headroom={k: g - Lo for k, (g, Lo) in fel.items()},
                  t_max_nm={k: (y_of_A(min(g - Lo, 0.5)) / (Z0 * s1) * 1e9 if g - Lo > 0 else 0) for k, (g, Lo) in fel.items()},
                  d111_nm=d111 * 1e9, ML={f'{t} nm': t * 1e-9 / d111 for t in (10, 20, 22.5)},
                  MBE_hours={f'{t} nm': t * 1e-9 / d111 / 2.0 for t in (10, 20, 22.5)}, Delft_min_ML=25, Delft_min_nm=25 * d111 * 1e9,
                  meissner_chi_limit=-0.1, meissner_res_nT=50)
# ---------------------------------------------------------------- III.8 UV charge-modulation control for X1
A1, sig_t, F0 = 25e-4, 5.6207e-6, 4.46e-3
Q = sig_t * A1
out['iii8'] = dict(Q_C=Q, N_e=Q / e, LPF_e=2.35e8, ratio_LPF=Q / e / 2.35e8, c_N_per_C2=1 / (2 * eps0 * A1),
                   t_discharge_s={f'{I:.0e} A': Q / I for I in (1e-9, 1e-8, 1e-7)},
                   F_at={f'{p} of Q': F0 * p**2 for p in (0.3, 0.1, 0.01)}, resolution_N=20e-6,
                   frac_for_resolution=math.sqrt(20e-6 / F0), photon_eV_254nm=1239.84193 / 254)
json.dump(out, open('run9_numbers.json', 'w'), indent=1)
b, z = out['b6'], out['i30']
print(f"B6: M {b['M']:.2f} kg, L {b['L']:.3g}, debris {b['e_debris']/1e6:.2f} MJ/kg = {b['debris_over_vap']:.2f}x vaporisation; stator s {b['s_stator']:.3g} J/kg")
print(f"I.30 hoop force {z['hoop_force_N']:.3g} N; debris pressure {z['p_debris_Pa']/1e6:.0f} MPa vs field pressure {z['p_field_30T_Pa']/1e6:.0f} MPa; v_vap {z['v_vap']:.0f} m/s")
for k, d in z['virial'].items(): print('  virial', k, {kk: round(vv, 3) for kk, vv in d.items()})
for k, d in z['impact'].items(): print('  impact', k, {kk: round(vv, 3) for kk, vv in d.items()})
print('  breathe', round(z['T_breathe_ms'], 3), 'ms; friction', {k: (round(d['t_ms'], 2), f"{d['P_peak_W']:.2e}") for k, d in z['friction'].items()})
print('  ablate', {k: round(v_, 1) for k, v_ in z['ablate_kg'].items()}, '; liner', {k: (round(d['v_f']), round(d['dissipated'], 3)) for k, d in z['liner'].items()})
print('  craft', {k: round(v_, 2) for k, v_ in z['craft_kg'].items()}, '; blast vessel', {k: round(v_, 1) for k, v_ in z['blast_vessel'].items()})
print('I.31', {k: round(v_, 3) for k, v_ in out['i31'].items()})
print('I.32 Je(4.2K, 30T)', {k: round(v_ / 1e9, 2) for k, v_ in Jt.items()}, '; T_max', lim)
for r in out['i32']['rows']:
    print(f"  dB {r['dB_mT']:.1f} mT eps {r['eps']}: P {r['P_W']*1e3:.2f} mW T_r {r['T_r']:.1f} K f {r['f']:.3f} ({r['f_range'][0]:.3f}-{r['f_range'][1]:.3f}) J_req {r['J_req_kA_mm2']:.1f} | i", {k[:10]: round(vv, 2) for k, vv in r['i'].items()})
print('  loops', out['i32']['loop_m'], out['i32']['loops_per_40m'], out['i32']['pieces_40m'], '; I.29 note', out['i29_note'])
print('V.12', {k: (round(v_, 3)) for k, v_ in out['v12']['headroom'].items()}, {k: round(v_, 1) for k, v_ in out['v12']['t_max_nm'].items()})
print('  d111', round(out['v12']['d111_nm'], 4), 'nm; ML', {k: round(v_, 1) for k, v_ in out['v12']['ML'].items()}, 'hours', {k: round(v_, 1) for k, v_ in out['v12']['MBE_hours'].items()}, 'Delft 25 ML =', round(out['v12']['Delft_min_nm'], 1), 'nm')
print('III.8', {k: (v_ if isinstance(v_, dict) else f'{v_:.3g}') for k, v_ in out['iii8'].items()})
