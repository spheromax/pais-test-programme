"""Canary, run 10: re-derive fifteen run-9 numbers with new code, from inputs written in state v10 and run-sheet part 7 only."""
import math, json
L9 = json.load(open('run9_numbers.json')); out = []
def chk(n, new, old, tol=0.02): out.append((n, new, old, abs(new / old - 1) <= tol))
T, R, v = 441.53e6, 2.0, 2 * math.pi * 2.0 * 500
M = 2 * T / v**2; h = 0.1
chk('debris energy / vaporization (7.5 MJ/kg)', v**2 / 2 / 7.5e6, L9['b6']['debris_over_vap'])
chk('hoop force M v^2 / 2 pi R (N)', M * v**2 / (2 * math.pi * R), L9['i30']['hoop_force_N'])
chk('debris pressure on 0.1 m wall (Pa)', M * v**2 / (2 * math.pi * R**2 * h), L9['i30']['p_debris_Pa'])
chk('end closures gamma 5/3 (kg)', (2 / 3) * T / (2 * T / 289), L9['i30']['virial']['gamma 5/3']['ends_kg'])
g = 5e-3; chk('gap-crossing speed at 5 mm (m/s)', v * math.sqrt(1 - (R / (R + g))**2), L9['i30']['impact']['5 mm']['v_r'])
chk('wall allowable speed sigma/sqrt(E rho) (m/s)', 3.82e9 / math.sqrt(176.4e9 * 1560), L9['i30']['v_allow'])
chk('friction time mu 0.3 (ms)', R / (0.3 * v) * 1e3, L9['i30']['friction']['mu 0.3']['t_ms'])
chk('liner 100 kg final speed (m/s)', M * v / (M + 100), L9['i30']['liner']['100 kg']['v_f'])
chk('craft high (kg)', M + 289 * 1.5 + 96.33 + 100 + T / 7.5e6, L9['i30']['craft_kg']['high'])
chk('craft spin if L dumped (rad/s)', (2 * T / (2 * math.pi * 500)) / (289 * 2.05**2), L9['i31']['omega'])
P = (1e-3 / 6.3e-3)**3; Tr = (P / (0.5 * 5.670374419e-8 * 2.5635) + 4.2**4)**0.25
chk('rotor T at 1 mT, eps 0.5 (K)', Tr, [r for r in L9['i32']['rows'] if r['dB_mT'] == 1.0 and r['eps'] == 0.5][0]['T_r'])
chk('thick film 50 um: T_max for i <= 0.506, T* 22 (K)', 4.2 + 22 * math.log(29.04e9 * 0.5063 / 5.856e9), L9['i32']['T_max_for_safe']['thick film, 50 um basis']['T*=22.0'])
chk('J_e(8 T) alpha 0.75 (A/m2)', 8.3e9 * (30 / 8)**0.75, L9['i29_note']['alpha 0.75']['Je_8T'])
y = (2 * (1 - 0.45) - 2 * math.sqrt(1 - 0.9)) / 0.45; chk('FELIX t_max (nm)', y / (376.730313668 * 3e4) * 1e9, L9['v12']['t_max_nm']['FELIX FEL-2'])
chk('X1 discharge at 10 nA (s)', 5.6207e-6 * 25e-4 / 1e-8, L9['iii8']['t_discharge_s']['1e-08 A'])
for n, a, b, ok in out: print(f"{'PASS' if ok else 'FAIL'} {n}: {a:.5g} vs {b:.5g}")
print(sum(o for *_, o in out), 'of', len(out), '; max dev', round(max(abs(a / b - 1) for _, a, b, _ in out) * 100, 3), '%')
json.dump([dict(name=n, new=a, logged=b, ok=ok) for n, a, b, ok in out], open('canary10.json', 'w'), indent=1)
