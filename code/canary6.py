"""Canary for run 6: re-derive run-5 logged numbers from the inputs written in state v6 and run-sheet part 3, with new code
(no import from run5_math.py). Pass if every number is within 1 % of its logged value (or within the logged rounding)."""
import json, math

c = 299_792_458.0
eps0 = 8.8541878128e-12

def check(name, got, logged, tol=0.01, note=''):
    dev = abs(got - logged) / abs(logged)
    return dict(name=name, rederived=got, logged=logged, deviation=dev, passed=dev <= tol, note=note)

out = []
# 1. Schulz-Flory survival at 200 mm and 1 m (I.15): L_half 74.4 mm
Lh = 0.0744
out.append(check('fraction of tubes reaching 200 mm', 2 ** (-0.200 / Lh), 0.155, note='I.15: L_half 74.4 mm; logged 16 % (0.155)'))
out.append(check('fraction of tubes reaching 1 m', 2 ** (-1.0 / Lh), 9.0e-5, note='I.15'))
# 2. tubes per cm2 of rim section (I.15): Vf 0.6, d 2 nm, l_t 2 cm, A 1 cm2, hoop 2*pi*2 m
Vf, d, lt, A, C = 0.6, 2e-9, 0.02, 1e-4, 2 * math.pi * 2.0
N = Vf * A * C / (math.pi * d ** 2 / 4 * lt)
out.append(check('tubes 2 cm long per cm2 of section', N, 1.2e16, tol=0.02, note='I.15, logged to 2 figures'))
# 3. B6 magnetic specific strength, R&D tape at 30 T (I.17): J_e 4.6 kA/mm2, R 2 m, rho 8900
v = 2 * math.pi * 2.0 * 30000 / 60
Sm = 4.6e9 * 30 * 2.0 / 8900
out.append(check('S_m, R&D tape at 30 T (J/kg)', Sm, 3.1e7, tol=0.01, note='I.17'))
out.append(check('shortfall v^2/S_m at 30 T', v ** 2 / Sm, 1.27, tol=0.01, note='I.17 (logged 1.3x, 1.27 in run5_numbers)'))
# 4. stator mass >= 2T/(sigma/rho) with a T1200 hoop at Vf 0.6, matrix 1200 (I.17)
M_r = 2e-3 * 0.100 * 2 * math.pi * 2.0 * 8900
T = 0.5 * M_r * v ** 2
s_rho_hoop = 0.6 * 8.0e9 / (0.6 * 1820 + 0.4 * 1200)
out.append(check('rotor kinetic energy T (MJ)', T / 1e6, 442, tol=0.005, note='I.17: 2 x 100 mm, rho 8900'))
out.append(check('stator mass, T1200 hoop (kg)', 2 * T / s_rho_hoop, 289, tol=0.01, note='I.17'))
# 5. radial tension at a bonded band (I.16): R 0.1 m, pack 20 mm at 150 GPa, band 5 mm at 0.6*540 GPa
R = 0.1
comp = R / (150e9 * 0.020) + R / (0.6 * 540e9 * 0.005)
out.append(check('radial tension at ds 0.26 % (MPa)', 0.0026 / comp / 1e6, 27.4, note='I.16'))
out.append(check('radial tension at ds 0.322 % (MPa)', 0.00322 / comp / 1e6, 33.9, note='I.16'))
# 6. Anderson's flyby constant (III.5)
out.append(check("Anderson K = 2 w_E R_E / c", 2 * 7.2921150e-5 * 6.371e6 / c, 3.099e-6, note='III.5'))
# 7. charge density for 10 mN on a 5 x 5 cm face (III.6)
out.append(check('sigma for 10 mN on 25 cm2 (uC/m2)', math.sqrt(2 * eps0 * 0.010 / 0.0025) * 1e6, 8.4, tol=0.01, note='III.6'))
# 8. B6 tabletop test (I.17): full support current density rho v^2/(B R) at 500 m/s, 10 T, R 0.1 m; self-burst speed
out.append(check('demo full-support J (kA/mm2)', 8900 * 500 ** 2 / (10 * 0.1) / 1e9, 2.2, tol=0.02, note='I.17, logged 2.2'))
out.append(check('REBCO self-burst speed sqrt(1.45e5) (m/s)', math.sqrt(1.45e5), 381, tol=0.002, note='I.3 table'))

for o in out:
    print(f"{'PASS' if o['passed'] else 'FAIL'}  {o['name']:45s} {o['rederived']:.4g} vs {o['logged']:.4g}  ({o['deviation'] * 100:.2f} %)")
print('canary:', sum(o['passed'] for o in out), 'of', len(out))
json.dump(out, open('/home/claude/p3/sim/pais/canary6.json', 'w'), indent=1)
