"""Canary for run 7: re-derive run-6 logged numbers from the inputs written in state v7 and run-sheet part 4, with new code
(no import from run6_math.py). Pass if every number is within 1 % of its logged value (or within the logged rounding)."""
import json, math
from scipy.optimize import brentq

mu0 = 4e-7 * math.pi * 1.00000000055

def check(name, got, logged, tol=0.01, note=''):
    dev = abs(got - logged) / abs(logged)
    return dict(name=name, rederived=got, logged=logged, deviation=dev, passed=dev <= tol, note=note)

out = []
# B6 rotor (I.17/I.18 inputs): R 2 m, 30,000 rpm, 2 x 100 mm REBCO section, rho 8900, beta 1
R, rho = 2.0, 8900.0
w = 30000 * 2 * math.pi / 60
M = 0.002 * 0.100 * (2 * math.pi * R) * rho
out.append(check('rotor mass M (kg)', M, 22.4, tol=0.005, note='part 4 nums: 22.4 kg'))
for n, g_log in ((0.1, 993), (1e-3, 99)):
    out.append(check(f'vertical growth rate at |n|={n} (1/s)', w * math.sqrt(n), g_log, tol=0.006, note='cor:rates, logged to 3 or 2 figures'))
out.append(check('force to hold 20 um at |n|=1e-3 (N)', 1e-3 * M * w ** 2 * 20e-6, 4.4, tol=0.01, note='I.18 nums'))
# I.19 whirl: c_n/c_r > sqrt(2/|n|) - 1
out.append(check('stator/rotor damping ratio at |n|=0.1', math.sqrt(2 / 0.1) - 1, 3.5, tol=0.01, note='I.19, logged 3.5'))
out.append(check('stator/rotor damping ratio at |n|=1e-3', math.sqrt(2 / 1e-3) - 1, 44, tol=0.01, note='I.19, logged 44'))
# I.20 Brandt-Indenbom: ripple for 1 W at 500 Hz, R&D tape (K_c = 4.6e9 * 1e-4), 4 mm wide, 6,283 m of tape
a, Kc, f, Ltape = 0.002, 4.6e9 * 1e-4, 500.0, 500 * 2 * math.pi * R / 2 * 2 / 2
Ltape = 500 * (2 * math.pi * R)      # 500 tapes of 12.57 m
def P(Bm):
    Hm = Bm / mu0; x = Hm / (Kc / math.pi)
    g = (2 / x) * math.log(math.cosh(x)) - math.tanh(x)
    return 4 * mu0 * a ** 2 * Kc * Hm * g * f * Ltape
B1W = brentq(lambda B: P(B) - 1.0, 1e-5, 0.1)
out.append(check('ripple for 1 W, R&D tape, 500 Hz (mT)', B1W * 1e3, 6.3, tol=0.01, note='I.20 nums'))
# I.21 band ceilings
out.append(check('M55J band B_max, pre-strain 0.32 % (T)', math.sqrt(2 * mu0 * 338e9 * (0.0061 - 0.0032)), 49.6, tol=0.002, note='I.21'))
out.append(check('Hastelloy-class co-wind B_max (T)', math.sqrt(2 * mu0 * 220e9 * 0.0063), 59.0, tol=0.002, note='I.21'))
# V.8 strain as pressure at 2 %
out.append(check('P_eq at 2 % biaxial strain (GPa)', 2 * 200e9 * 0.02 / (3 * 0.7) / 1e9, 3.8, tol=0.01, note='V.8'))
# K1 area check (I.11 note): 80 GPa / 1300 and the density threshold
v2 = (w * R) ** 2
out.append(check('K1 at 80 GPa and 1,300 kg/m3 (N/tex)', 80e9 / 1300 / 1e6, 61.5, tol=0.002, note='I.11 note'))
out.append(check('K1 density threshold (kg/m3)', 80e9 / v2, 2030, tol=0.005, note='I.11 note, logged 2,030'))
# I.18 flux conservation: z0 = sqrt(I L / (2 pi |n| B0)), L = mu0 R (ln(8R/a) - 2), a = 8 mm, I = f/B0
I30 = (M * v2 / (2 * math.pi * R ** 2)) / 30.0
L = mu0 * R * (math.log(8 * R / 0.008) - 2)
out.append(check('flux-conservation offset at |n|=0.1, 30 T (m)', math.sqrt(I30 * L / (2 * math.pi * 0.1 * 30)), 0.94, tol=0.01, note='I.18'))
# Inductrack drag (run-6 exploration): L/R 1 ms, wavelength 0.1 m, rim speed
LD = 2 * math.pi * (w * R) * 1e-3 / 0.1
out.append(check('Inductrack drag at L/R 1 ms, 0.1 m (W/N)', (w * R) / LD, 15.9, tol=0.005, note='run 6 log'))

for o in out:
    print(f"{'PASS' if o['passed'] else 'FAIL'}  {o['name']:46s} {o['rederived']:.4g} vs {o['logged']:.4g}  ({o['deviation'] * 100:.2f} %)")
print('canary:', sum(o['passed'] for o in out), 'of', len(out))
json.dump(out, open('/home/claude/p3/sim/pais/canary7.json', 'w'), indent=1)
