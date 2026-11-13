"""Pre-check run-11 query wording against every earlier run's queries (signal 1) and within the run (signal 14), before searching."""
import importlib.util
spec = importlib.util.spec_from_file_location('lh', '/home/claude/p3/sim/pais/loop_health.py'); lh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lh)
PLAN = [
 ('toroidal field model coil REBCO measured field map error compared with design', 'field-homog', 'k'),
 ('coated conductor thick superconducting layer flux jump instability 20 K magnetization avalanche', 'rebco-fj', 'k'),
 ('hypervelocity gouging sled track slipper rail damage onset velocity', 'b6-graze', 'k'),
 ('photoinduced superconductivity fulleride confirmed by another group November 2026', 'k3c60', 'k'),
 ('Buhler electrostatic thrust peer reviewed journal paper published', 'x1', 'k'),
 ('superconducting cyclotron first harmonic field error gauss trim coil correction', 'cyclotron', 'x'),
 ('compact cyclotron coated-conductor coil orbit field uniformity measured', 'cyclotron', 'x'),
 ('dynamic gravitational field measurement electromagnetic source anomalous coupling resonant detector', 'hf-grav', 'x'),
 ('flywheel burst fragment light gas gun test containment liner tangential impact', 'bridge', 'x'),
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
print('kinds', dict(k), 'explore', round(k['x'] / len(PLAN), 3), 'top topic share', round(max(tags.values()) / len(PLAN), 3))
