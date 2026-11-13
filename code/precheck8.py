"""Pre-check run-8 query wording against every earlier run's queries (signal 1) and within the run (signal 14), before searching."""
import importlib.util
spec = importlib.util.spec_from_file_location('lh', '/home/claude/p3/sim/pais/loop_health.py'); lh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lh)
PLAN = [
 ('closed-loop REBCO coil persistent mode quench current decay redistribution between turns', 'b6-quench', 'f'),
 ('LDX floating coil warm-up during levitation heat leak temperature rise hours', 'b6-thermal', 'f'),
 ('flywheel rotor burst containment housing energy absorbed per kilogram test', 'b6-contain', 'k'),
 ('inductively coupled parallel superconducting loops one loop quenches current transfer neighbours', 'b6-redund', 'x'),
 ('flywheel energy storage system specific energy Wh/kg including housing best demonstrated', 'b6-store', 'x'),
 ('counter-rotating flywheel pair vehicle gyroscopic torque cancellation manoeuvre', 'b6-gyro', 'x'),
 ('large warm bore 10 tesla superconducting magnet user facility 300 mm', 'b6-test', 'f'),
 ('FELIX free electron laser single-pass gain cavity round-trip loss mid-infrared', 'b7', 'f'),
 ('K3C60 film infrared optical conductivity absorption thickness 41 meV', 'k3c60-film', 'f'),
 ('photoexcited K3C60 superconductivity alternative explanation inhomogeneous conductivity critique', 'k3c60', 'k'),
 ('fulleride light-driven superconducting state reproduced different laboratory', 'k3c60', 'k'),
 ('manufacturer specification sheet second-generation HTS wire integral linear contraction from room temperature', 'rebco-cte', 'f'),
 ('screening current induced stress plastic deformation high-field insert coil damage mitigation', 'k2', 'k'),
 ('Buhler propellantless electrostatic thrust independent test after June 2026', 'x1', 'k'),
 ('electret trapped charge vacuum decay time force on grounded electrode after power removed', 'x1-electret', 'x'),
 ('cavity vacuum field changes superconducting transition temperature experiment fulleride Fabry-Perot', 'cavity-qed', 'x'),
 ('cavity-modified superconductivity claim null result vacuum fluctuations no Tc change', 'cavity-qed', 'k'),
]
earlier = [(q, r) for r in sorted(lh.RUNS) for q, _, _ in lh.RUNS[r]['queries']]
worst = 0
for i, (q, tag, kind) in enumerate(PLAN):
    t = lh.toks(q)
    best = max(((lh.jac(t, lh.toks(e)), e, r) for e, r in earlier), key=lambda x: x[0])
    within = max([lh.jac(t, lh.toks(PLAN[j][0])) for j in range(i)] or [0])
    worst = max(worst, best[0])
    flag = 'REPEAT' if best[0] >= 0.30 else ('rework?' if within >= 0.30 and kind != 'k' else 'ok')
    print(f'{i + 1:2d} [{kind}] {best[0]:.2f} vs run {best[2]} | within {within:.2f} | {flag} | {q}')
print('max similarity to earlier runs:', round(worst, 2))
from collections import Counter
k = Counter(kind for _, _, kind in PLAN); tags = Counter(t for _, t, _ in PLAN)
print('kinds', dict(k), 'explore', round(k['x'] / len(PLAN), 3), 'top topic share', round(max(tags.values()) / len(PLAN), 3),
      'b6 share', round(sum(v for t, v in tags.items() if t.startswith('b6')) / len(PLAN), 3))
