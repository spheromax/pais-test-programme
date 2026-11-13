"""Canary for the loop-health test: re-derive three logged numbers from their written inputs only, with code that
does not import pais_math.py or run3_math.py.  A number that cannot be re-derived from the record is a degradation signal."""
import math, json
c = 299792458.0; eps0 = 8.8541878128e-12

checks = []
# 1. S_claim, CT-11: sphere example in US 10,135,366: sigma 5e4 C/m^2, R 2 m, 30 000 rpm, f_G 2/3 (sphere)
v = 2.0 * 30000 / 60 * 2 * math.pi
S = (2 / 3) * 5e4 ** 2 / eps0 * v
checks.append(('S_claim, W/m^2', 1.18e24, S, 'inputs in CT-11 and the patent example'))
# 2. FELBE spot at 400 uJ/cm^2: pulse energy = average power / repetition rate = 20 W / 13 MHz
E = 20.0 / 13e6; A = E / 4.0
checks.append(('FELBE spot diameter, mm', 0.69, 2 * math.sqrt(A / math.pi) * 1e3, 'needs FELBE 20 W at 13 MHz: in run 2 notes, not in the state file'))
# 3. rig ratio: Pais Eq. 2 (f_G = 1 for a disc, US 10,322,827 text) over Larmor, 1 uC, +/-80 nm, 100 MHz, t_op 1 s, 30 cm disk
Q, Rr, x0, w = 1e-6, 0.15, 80e-9, 2 * math.pi * 1e8
P_l = (Q * x0) ** 2 * w ** 4 / (12 * math.pi * eps0 * c ** 3)
sig = Q / (2 * math.pi * Rr ** 2)
P_p = sig ** 2 / eps0 * (x0 * w ** 2 * 1.0) * 2 * math.pi * Rr ** 2
checks.append(('rig ratio, Pais Eq. 2 / Larmor', 2.3e17, P_p / P_l, 'needs f_G = 1 (disc) from the 827 text and nu read as rad/s'))
out = []
for name, logged, got, note in checks:
    dev = abs(got / logged - 1)
    out.append(dict(name=name, logged=logged, rederived=got, deviation=dev, passed=dev <= 0.05, note=note))
    print(f'{name:34s} logged {logged:.3g}  re-derived {got:.4g}  dev {dev * 100:.1f} %  {"PASS" if dev <= 0.05 else "FAIL"}  ({note})')
json.dump(out, open('/home/claude/p3/sim/pais/canary.json', 'w'), indent=1)
