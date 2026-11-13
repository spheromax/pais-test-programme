"""Pre-check run-9 query wording against every earlier run's queries (signal 1) and within the run (signal 14), before searching."""
import importlib.util
spec = importlib.util.spec_from_file_location('lh', '/home/claude/p3/sim/pais/loop_health.py'); lh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lh)
PLAN = [
 ('Iseult 11.7 tesla whole-body magnet field homogeneity ppm measured', 'field-homog', 'f'),
 ('high emissivity black coating cryogenic 20 K hemispherical emissivity measurement', 'emissivity', 'f'),
 ('oblique hypervelocity impact grazing angle ricochet debris sliding along plate', 'b6-graze', 'k'),
 ('two-stage light gas gun flat plate projectile orientation sabot facility 7 km/s', 'lgg', 'f'),
 ('long-length thick REBCO tape critical current uniformity variability performance drop', 'rebco-thick', 'k'),
 ('thick-film coated conductor lift factor versus temperature Houston tape 30 kelvin', 'rebco-ic-T', 'f'),
 ('alkali fulleride thin film ultrafast optical spectroscopy pump probe molecular beam epitaxy', 'k3c60-film', 'f'),
 ('Rb3C60 photoexcitation metastable superconductivity mid-infrared pressure', 'k3c60', 'k'),
 ('FELIX laboratory intracavity FELICE user experiment solid state sample', 'b7-fel', 'f'),
 ('Exodus Buhler thruster third-party verification latest', 'x1', 'k'),
 ('high-frequency electromagnetic field gravity coupling experiment balance search', 'hf-grav', 'x'),
 ('gravitational field generator patent electromagnetic granted 2023 2024 2025', 'grav-patents', 'x'),
 ('SPARC toroidal field model coil 20 tesla stored energy quench test result', 'bridge', 'x'),
 ('high-frequency gravitational wave detector MHz GHz upper limit superconducting cavity', 'hfgw', 'x'),
 ('Espacenet antigravity propulsion device patent electrostatic coil', 'grav-patents-2', 'x'),
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
