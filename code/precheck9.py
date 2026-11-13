"""Pre-check run-9 query wording against every earlier run's queries (signal 1) and within the run (signal 14), before searching."""
import importlib.util
spec = importlib.util.spec_from_file_location('lh', '/home/claude/p3/sim/pais/loop_health.py'); lh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lh)
PLAN = [
 ('Faraday Factory tape in-field critical current 20 K 30 K data sheet', 'rebco-ic-T', 'f'),
 ('thick film REBCO production length 30 tesla engineering current density Houston advanced MOCVD', 'rebco-thick', 'f'),
 ('HTS wire critical current database Robinson Research Institute angular field temperature', 'hts-db', 'f'),
 ('momentum-supported structure stream break failure consequences energy release analysis', 'b6-dyn', 'k'),
 ('explosive containment vessel rated charge kg TNT vessel weight composite', 'b6-vessel', 'f'),
 ('virial theorem pressure vessel minimum mass gas energy containment bound', 'b6-virial', 'x'),
 ('rotatable containment liner flywheel torque transmitted housing reduction', 'b6-torque', 'x'),
 ('Whipple shield ballistic limit equation areal density 7 km/s aluminum projectile', 'b6-hvi', 'f'),
 ('K3C60 thin film MBE growth superconducting transition temperature encapsulation air', 'k3c60-film', 'f'),
 ('FELIX FEL-2 small-signal gain outcoupling hole losses 30 micron wavelength', 'b7-fel', 'f'),
 ('optically driven K3C60 2026 magnetic expulsion transport measurement independent group', 'k3c60', 'k'),
 ('30 micron difference frequency generation high average power watt laser source', 'b7-src', 'x'),
 ('asymmetric electrostatic pressure thruster replication attempt university vacuum chamber', 'x1', 'k'),
 ('micro-thrust balance electrostatic artifact charged dielectric residual charge neutralization ionizer', 'x1-ctrl', 'k'),
 ('patents citing US10144532 inertial mass reduction craft cited by', 'bridge', 'x'),
 ('integrated power and attitude control system flywheel spacecraft NASA counter-rotating', 'b6-ipacs', 'x'),
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
