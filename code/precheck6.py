"""Pre-check run-6 query wording against every earlier run's queries (signal 1) and within the run (signal 14), before searching."""
import importlib.util
spec = importlib.util.spec_from_file_location('lh', '/home/claude/p3/sim/pais/loop_health.py'); lh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lh)
PLAN = [
 ('Levitated Dipole Experiment floating coil levitation feedback vertical instability', 'b6-ldx', 'f'),
 ('rotating damping whirl instability supercritical rotor magnetic bearing eddy current', 'b6-whirl', 'k'),
 ('REBCO critical current 40 T field parallel ab measurement tape 4.2 K', 'rebco-je', 'f'),
 ('AC loss thin superconducting strip perpendicular field Brandt Indenbom', 'ac-loss', 'f'),
 ('coated conductor integrated thermal expansion 4 K measurement Hastelloy copper stabilizer', 'rebco-cte', 'f'),
 ('Toray M55J tensile strength modulus elongation', 'fibre', 'k'),
 ('Tsinghua Wei group superstrong nanotube fiber centimetre bundle', 'cnt', 'f'),
 ('Exodus Propulsion Buhler thrust independent replication', 'x1', 'x'),
 ('charged dielectric thruster sealed enclosure vacuum torsion balance null', 'x1', 'k'),
 ('epitaxial compressive strain equivalent hydrostatic pressure nickelate film superconductivity', 'strain-p', 'x'),
 ('metal hydride epitaxial film lattice mismatch maximum strain GPa equivalent', 'strain-p', 'k'),
 ('Inductrack passive electrodynamic levitation lift drag ratio speed stability', 'inductrack', 'x'),
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
