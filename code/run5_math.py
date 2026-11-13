"""Run 5 of the Pais gap loop: numbers for run-sheet items I.15-I.17, III.5 and the I.11/I.14 updates; sheets CT-30..CT-35.
SI units.  Inputs marked (assumed) are not from a measurement.  Writes run5_numbers.json."""
import math, json
c = 299792458.0; mu0 = 1.25663706212e-6; G = 6.67430e-11
R = {}
omega = 30000 * 2 * math.pi / 60; Rrim = 2.0; v = omega * Rrim; v2 = v * v; C = 2 * math.pi * Rrim

# ---------------------------------------------------------------- I.15  Schulz-Flory length budget of continuous nanotubes (K1)
L_half = 74.4e-3                                                   # s-CNT half-length (Zhu et al. 2019)
lam = L_half / math.log(2)                                         # mean length of the exponential
frac = lambda L: 2 ** (-L / L_half)
ends_per_path = C / lam
d_t, ell, Vf, A_rim = 2e-9, 0.02, 0.6, 1e-4                        # 2 nm tubes, 2 cm useful length, 1 cm^2 rim section (assumed)
N_tubes = Vf * A_rim * C / (math.pi * (d_t / 2) ** 2 * ell)
m_def, s0_def, L0_def = 2.7, 34e9, 1e-7                            # Pugno: defective-tube Weibull (m 2.7, 34 GPa at 100 nm)
R['sf'] = dict(L_half=L_half, lam=lam, frac_20mm=frac(0.02), frac_200mm=frac(0.2), frac_1m=frac(1.0), frac_hoop=frac(C),
               log10_frac_hoop=-C / L_half * math.log10(2), per_um_deactivation=math.log(2) * 1e-6 / L_half, ends_per_path=ends_per_path,
               N_tubes_per_cm2=N_tubes, longest_grown=0.55,
               weakest_1m_defective_GPa=s0_def * (L0_def / 1.0) ** (1 / m_def) * math.gamma(1 + 1 / m_def) / 1e9,
               daniels_m27=(m_def * math.e) ** (-1 / m_def), cable_cap_GPa=10.0, cable_cap_Ntex=10e9 / 1300 / 1e6)

# ---------------------------------------------------------------- I.11 update: the fibre ladder with the 2023 record and new classes
fib = [('T1200 (Toray, Oct 2023)', 8.0e9, 1820), ('T1100G', 7.0e9, 1790), ('M5 / PIPD, potential', 5.8e9, 1700),
       ('M5 / PIPD, filament average', None, None), ('graphene fibre filament', 1.4e9, 1930)]
lad = []
for n, s, rho in fib:
    spec = 3.6e6 if s is None else s / rho
    lad.append(dict(name=n, Ntex=spec / 1e6, short=v2 / spec, v=math.sqrt(spec)))
R['fibres'] = dict(ladder=lad, best=8.0e9 / 1820, factor_spec=v2 / (8.0e9 / 1820), factor_speed=math.sqrt(v2 / (8.0e9 / 1820)),
                   v_s_best=math.sqrt(8.0e9 / 1820))

# ---------------------------------------------------------------- I.14 update and I.16: cooldown with the measured tape shrinkage (K2)
s_ti = 0.17e-2; zero = dict(Bruker=0.152e-2, Fujikura=0.145e-2, SuNAM=0.148e-2, SuperOx=0.144e-2, SuperPower=0.149e-2)
s_tape = {k: s_ti + z for k, z in zero.items()}                    # stiff Ti-6Al-4V spring: tape strain ~ s_tape - s_spring
E_tape, E_cf, E_ss = 150e9, 0.6 * 540e9, 193e9
def bonded(E1, s1, E2, s2): return E2 * (s1 - s2) / (E1 + E2)
lo, hi = 0.26e-2, max(s_tape.values())
irr = dict(Bruker=0.71e-2, Fujikura=0.56e-2, SuNAM=0.68e-2, SuperOx=0.46e-2, SuperPower=0.67e-2)
def q_radial(ds, Rr=0.1, tw=0.02, Ew=150e9, tb=0.005, Eb=324e9): return ds / (Rr / (Ew * tw) + Rr / (Eb * tb))
R['k2'] = dict(s_tape=s_tape, s_tape_range=(min(s_tape.values()), hi),
               cf_cowind=(bonded(E_tape, lo, E_cf, 0.0), bonded(E_tape, hi, E_cf, 0.0)),
               ss_cowind=(bonded(E_tape, lo, E_ss, 0.30e-2), bonded(E_tape, hi, E_ss, 0.30e-2)),
               window_used_cf_hi={k: bonded(E_tape, hi, E_cf, 0.0) / w for k, w in irr.items()}, irr=irr,
               q_radial_MPa=(q_radial(lo) / 1e6, q_radial(hi) / 1e6), caxis_MPa=(18, 53))

# ---------------------------------------------------------------- I.17  stator-borne rotor (bridge B6): virial with external support
rho_r = 8900.0
Je = dict(commercial=0.6e9, record_2019=1.0e9, thick_film_RnD=4.6e9)   # A/m^2 at 4.2 K, 20 T (sources in run5_log)
Sm = {f'{k}@{B}T': J * B * Rrim / rho_r for k, J in Je.items() for B in (20, 30, 40)}  # J_e held constant with B (B||ab, optimistic)
t_r, h_r = 0.002, 0.1                                               # rotor ring 2 mm x 100 mm (assumed)
M_r = rho_r * t_r * h_r * C; T = 0.5 * M_r * v2
cf_hoop = (0.6 * 8.0e9) / (0.6 * 1820 + 0.4 * 1200)                 # T1200 hoop composite sigma/rho
U20 = 20 ** 2 / (2 * mu0) * C * 0.05 * h_r; U40 = 40 ** 2 / (2 * mu0) * C * 0.05 * h_r   # annular 5 cm gap field (assumed)
I_perp = 0.5 * M_r * Rrim ** 2; L_spin = M_r * Rrim ** 2 * omega
I_cur = M_r * omega ** 2 / (2 * math.pi) / 20.0                     # |I| B = M w^2 / 2pi at B = 20 T
K_tilt = I_cur * math.pi * Rrim ** 2 * 20.0
beta_max_rebco = 1.0 - 1.45e5 / v2                                  # rotor's own REBCO strength carries (1-beta) v^2
v_demo, R_demo, B_demo = 500.0, 0.1, 10.0
R['b6'] = dict(v2=v2, Sm=Sm, short={k: v2 / s for k, s in Sm.items()}, M_r=M_r, T=T, two_T=2 * T,
               M_stator_cf=2 * T / cf_hoop, M_stator_hast=2 * T / 1.45e5, cf_hoop=cf_hoop, U20=U20, U40=U40,
               L2=L_spin ** 2, fourIK=4 * I_perp * K_tilt, identity_ratio=L_spin ** 2 / (4 * I_perp * K_tilt),
               J_needed_20T=rho_r * v2 / (20 * Rrim), J_needed_40T=rho_r * v2 / (40 * Rrim),
               beta_max_rebco=beta_max_rebco, margin_rebco=1 - beta_max_rebco,
               demo_J_full=rho_r * v_demo ** 2 / (R_demo * B_demo), demo_selfburst=math.sqrt(1.45e5))

# ---------------------------------------------------------------- III.5  the flyby anomaly against frame dragging
wE, RE, JE = 7.2921159e-5, 6.371e6, 5.86e33
r_p, v_p = 6.371e6 + 539e3, 12.7e3                                  # NEAR perigee altitude 539 km; perigee speed ~12.7 km/s (assumed)
a_LT = 2 * G * JE * v_p / (c ** 2 * r_p ** 3)
R['flyby'] = dict(K=2 * wE * RE / c, NEAR_obs=13.46e-3, NEAR_formula=13.28e-3, a_LT=a_LT, dV_LT_1000s=a_LT * 1000,
                  ratio=13.46e-3 / (a_LT * 1000), rosetta2_pred='< 1 mm/s, not seen', juno_pred=7e-3)
json.dump(R, open('/home/claude/p3/sim/pais/run5_numbers.json', 'w'), indent=1, default=float)

if __name__ == '__main__':
    for k in ('sf', 'fibres', 'k2', 'b6', 'flyby'):
        print(k)
        for kk, vv in R[k].items():
            if isinstance(vv, float): print(f'   {kk}: {vv:.4g}')
            elif isinstance(vv, dict): print(f'   {kk}:', {a: (f'{b:.3g}' if isinstance(b, float) else b) for a, b in vv.items()})
            elif isinstance(vv, (list, tuple)): print(f'   {kk}:', [(f'{x:.3g}' if isinstance(x, float) else x) for x in vv])
            else: print(f'   {kk}: {vv}')
