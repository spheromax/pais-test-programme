"""Canary, run 9: re-derive sixteen run-8 numbers with new code, from inputs written in state v9 and run-sheet part 6 only."""
import math, json
mu0, eps0, sSB, hbar, c = 4e-7 * math.pi * 1.00000000055, 8.8541878128e-12, 5.670374419e-8, 1.054571817e-34, 299792458.0
logged = json.load(open('run8_numbers.json'))
R, rps, B6B, rho_tape = 2.0, 500.0, 30.0, 8900.0          # B6: R 2 m, 30,000 rpm, 30 T, tape density 8.9 g/cc
T6 = 441.5e6                                              # stored kinetic energy (state v9: 442 MJ)
v = 2 * math.pi * R * rps; w = 2 * math.pi * rps
checks = []
def chk(name, new, old, tol=0.02):
    checks.append((name, new, old, abs(new / old - 1) <= tol))
chk('rotor mass 2T/v^2 (kg)', 2 * T6 / v**2, logged['b6']['M'])
chk('rho v^2 (Pa)', rho_tape * v**2, logged['b6']['rho_v2'])
chk('loss-of-hold tolerance sigma_a/rho v^2', 1e9 / (rho_tape * v**2), logged['i25_global']['delta_max'])
chk('self-supporting speed sqrt(sigma_a/rho) (m/s)', math.sqrt(1e9 / rho_tape), logged['i25_global']['v_self'])
chk('TNT equivalent (kg, 4.184 MJ/kg)', T6 / 4.184e6, logged['i25_global']['TNT_kg'])
e_abs = 3.4e9 * 0.035 / (2 * 970)                         # Dyneema SK75: 3.4 GPa, 3.5 % elongation, 970 kg/m3
chk('catcher mass T/e_abs (t)', T6 / e_abs / 1e3, logged['i25_contain']['M_min_t']['UHMWPE_SK75'])
chk('rotor specific energy v^2/2 (J/kg)', v**2 / 2, logged['i28']['rotor_MJ_per_kg'] * 1e6)
chk('angular momentum 2T/omega (N m s)', 2 * T6 / w, logged['i28']['L'])
Je = rho_tape * v**2 / (B6B * R)                          # stress-free condition J_e B R = rho v^2
chk('J_e = rho v^2/(B R) (A/m2)', Je, logged['b6']['Je'])
chk('self-pinch at 2 cm2 (Pa)', mu0 * Je**2 * 2e-4 * math.log(2) / (2 * math.pi), logged['i26']['pinch'])
chk('max section at 0.3 GPa (m2)', 0.3e9 * 2 * math.pi / (mu0 * Je**2 * math.log(2)), logged['i26']['A_max_300MPa'])
chk('safe fraction 1/(1+0.975)', 1 / (1 + 0.97506), logged['i25_local']['i_max_safe_corner'])
chk('radiated heat 30 K, eps 0.1, 2.5635 m2 (W)', 0.1 * sSB * 30**4 * 2.5635, logged['i27']['P_rad']['30 K']['eps 0.1'])
vt, Rt, Bt, Mt = 970.0, 0.1, 8.0, 0.0223681               # tabletop ring
chk('tabletop J_e (kA/mm2)', rho_tape * vt**2 / (Bt * Rt) / 1e9, logged['i29']['fast']['Je_kA_mm2'])
chk('tabletop energy (J)', 0.5 * Mt * vt**2, logged['i29']['fast']['T_J'])
chk('tabletop tolerance', 1e9 / (rho_tape * vt**2), logged['i29']['fast']['delta_max'])
y = 376.730313668 * 3e4 * 22.477e-9                         # thin film: Z0 sigma1 t
chk('film absorption 4y/(2+y)^2 at 22.5 nm', 4 * y / (2 + y)**2, 0.2)
lam = 29.9792458e-6; Vc = (lam / 2)**3
chk('vacuum field, half-wave cube (V/m)', math.sqrt(hbar * 2 * math.pi * c / lam / (2 * eps0 * Vc)), logged['v11']['E_vac_halfwave_cube'])
chk('PTFE relaxation eps0 eps_r rho (s)', eps0 * 2.1 * 1e16, logged['iii7']['PTFE_tau_s'])
chk('trapped charge sqrt(2 eps0 F/A) (C/m2)', math.sqrt(2 * eps0 * 4.46e-3 / 25e-4), logged['iii7']['sigma_t_C_m2'])
m_rotor = (Je * 2e-4 * 0 + logged['b6']['Itot']) * math.pi * R**2
chk('identity m B = T (J)', m_rotor * B6B, logged['i28']['mB'])
for n, a, b, ok in checks:
    print(f"{'PASS' if ok else 'FAIL'} {n}: new {a:.5g} vs logged {b:.5g} ({(a / b - 1) * 100:+.2f} %)")
print(sum(ok for *_, ok in checks), 'of', len(checks), 'within 2 %; max dev', round(max(abs(a / b - 1) for _, a, b, _ in checks) * 100, 2), '%')
json.dump([dict(name=n, new=a, logged=b, ok=ok) for n, a, b, ok in checks], open('canary9.json', 'w'), indent=1)
