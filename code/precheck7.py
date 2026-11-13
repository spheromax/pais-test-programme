"""Pre-check run-7 query wording against every earlier run's queries (signal 1) and within the run (signal 14), before searching."""
import importlib.util
spec = importlib.util.spec_from_file_location('lh', '/home/claude/p3/sim/pais/loop_health.py'); lh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lh)
PLAN = [
 ('LDX floating coil vertical position control system growth time bandwidth sensors', 'b6-ctrl', 'f'),
 ('Beams magnetically suspended rotor vacuum ultracentrifuge rotational speed burst', 'b6-prior', 'f'),
 ('electrostatically suspended gyroscope rotor suspension servo bandwidth spin speed', 'b6-prior', 'x'),
 ('dynamic resistance coated conductor DC transport current alternating perpendicular field threshold', 'ac-loss', 'k'),
 ('passive stabilization levitated superconducting ring persistent current loop null flux coil', 'b6-passive', 'x'),
 ('REBCO superconducting joint resistance persistent mode decay time', 'b6-passive', 'k'),
 ('bulk YBCO superconducting bearing stiffness N/mm flywheel levitation gap', 'smb', 'x'),
 ('superconducting magnetic bearing flux creep drift rotational loss rotor inhomogeneity', 'smb', 'k'),
 ('production coated conductor 30 tesla 4.2 K amperes per centimetre width SuperPower Faraday Fujikura', 'rebco-je', 'f'),
 ('Bai 2018 nanotube bundles 80 GPa cross-sectional area calculation method', 'cnt', 'k'),
 ('REBCO tape thermal contraction room temperature to 4 K measured strain gauge', 'rebco-cte', 'f'),
 ('stainless steel co-wound REBCO coil degradation thermal cycling delamination', 'k2', 'k'),
 ('intracavity sample free electron laser oscillator mid-infrared experiment', 'gap9-ic', 'x'),
 ('Exodus Propulsion electrostatic pressure force test outside laboratory', 'x1', 'k'),
 ('magnetic sail small magnetosphere ion gyroradius thrust kinetic regime', 'magsail', 'x'),
 ('mini-magnetospheric plasma propulsion M2P2 thrust overestimate criticism', 'magsail', 'k'),
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
