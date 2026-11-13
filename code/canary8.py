"""Canary for run 8: re-derive run-7 logged numbers from the inputs written in state v8 and run-sheet part 5, with new code
(no import from run7_math.py). Pass if every number is within 1 % of its logged value (or within the logged rounding)."""
import json, math
import numpy as np
from scipy.special import ellipk, ellipe
from scipy.optimize import brentq

mu0 = 4e-7 * math.pi * 1.00000000055
eps0, e, mp, c = 8.8541878128e-12, 1.602176634e-19, 1.67262192e-27, 299792458.0

def check(name, got, logged, tol=0.01, note=''):
    dev = abs(got - logged) / abs(logged)
    return dict(name=name, rederived=got, logged=logged, deviation=dev, passed=bool(dev <= tol), note=note)

out = []
# rotor of I.17: R 2 m, 30,000 rpm, 2 mm x 100 mm REBCO stack at 8,900 kg/m3, B 30 T, stress-free J_e B R = rho v^2
R, rho, B = 2.0, 8900.0, 30.0
w = 30000 * 2 * math.pi / 60; v = w * R
M = rho * 0.002 * 0.100 * 2 * math.pi * R
Ir = rho * v ** 2 / (B * R) * 0.002 * 0.100          # A-turns
# I.22 (state v8: gamma tau < sqrt2; bandwidth >= pi gamma / ln 2)
g3 = w * math.sqrt(1e-3)
out.append(check('growth rate at |n|=1e-3 (1/s)', g3, 99, tol=0.006, note='state v8: 99 1/s'))
out.append(check('critical delay at |n|=1e-3 (ms)', math.sqrt(2) / g3 * 1e3, 14.2, tol=0.006, note='state v8: 14 ms; part 5: 14.2'))
out.append(check('minimum loop bandwidth at |n|=1e-3 (Hz)', math.pi * g3 / math.log(2) / (2 * math.pi), 72, tol=0.006, note='>= 72 Hz'))
out.append(check('|n| where the loop reaches spin/3', (1 / (3 * math.pi / math.log(2))) ** 2, 5.4e-3, tol=0.006, note='5.4e-3'))
out.append(check('control field per newton (T/N)', 1 / (Ir * 2 * math.pi * R), 6.8e-8, tol=0.01, note='6.8e-8 T/N'))
# I.23 null-flux pair: coaxial loops a = R at +-d, r_w 5 mm, series opposition; k_c = g^2/L_pair, sized for 3 k_u
def Mco(a, b, z):
    k2 = 4 * a * b / ((a + b) ** 2 + z ** 2); k = math.sqrt(k2)
    return mu0 * math.sqrt(a * b) * ((2 / k - k) * ellipk(k2) - (2 / k) * ellipe(k2))
def dM(a, b, z, h=1e-5): return (Mco(a, b, z + h) - Mco(a, b, z - h)) / (2 * h)
a, rw = R, 0.005
Lloop = mu0 * a * (math.log(8 * a / rw) - 2)
def kc(d): return (2 * Ir * dM(R, a, d)) ** 2 / (2 * Lloop - 2 * Mco(a, a, 2 * d))
ku = 1e-3 * M * w ** 2
d3 = brentq(lambda d: kc(d) - 3 * ku, 0.2, 3.0)
out.append(check('null-flux distance for 3 k_u at |n|=1e-3 (m)', d3, 1.08, tol=0.006, note='state v8: 1.08 m'))
out.append(check('vertical mode at |n|=1e-3 (rad/s)', math.sqrt((3 * ku - ku) / M), 140, tol=0.006, note='140 rad/s'))
Lp = 2 * Lloop - 2 * Mco(a, a, 2 * d3)
yr = 365.25 * 86400
out.append(check('drift time at 1e-12 ohm (yr)', Lp * (3 * ku - ku) / (1e-12 * ku) / yr, 1.8, tol=0.02, note='1.8 yr (2 figures)'))
# I.24 dynamic-resistance threshold: mu0 I_c / w with 1,500 A on 4 mm; i_max at 3 mT for kappa = 0.5
mk = mu0 * 1500 / 0.004
out.append(check('mu0 I_c / w (T)', mk, 0.47, tol=0.005, note='0.47 T'))
out.append(check('i_max at 3 mT ripple, kappa 0.5', 1 - 0.003 / (0.5 * mk), 0.987, tol=0.001, note='0.975-0.996 band; 0.987 at 3 mT'))
# I.17 note: J_e of 4 mm x 45 um tape at 1,500 A and the operating fraction
Je = 1500 / (0.004 * 45e-6)
out.append(check('operating fraction i', rho * v ** 2 / (B * R) / Je, 0.70, tol=0.005, note='i = 0.70'))
# I.11 note: 80 GPa on wall area at 2,260 kg/m3
out.append(check('K1 specific strength (N/tex)', 80e9 / 2260 / 1e6, 35.4, tol=0.002, note='35.4 N/tex'))
# III.6 note: gap at 3.5 kV for 4.46 mN on 25 cm2
out.append(check('electrostatic gap for 4.46 mN at 3.5 kV on 25 cm2 (mm)', 3500 * math.sqrt(eps0 * 0.0025 / (2 * 4.46e-3)) * 1e3, 5.5, tol=0.006, note='5.5 mm'))
# S.4 identity: proton gyroradius at the standoff field equals the ion inertial length (n 5 cm-3, v 400 km/s)
n, vsw = 5e6, 4e5
Bmp = math.sqrt(mu0 * n * mp * vsw ** 2)
di = c / math.sqrt(n * e ** 2 / (eps0 * mp))
out.append(check('ion inertial length at 5 cm-3 (km)', di / 1e3, 101.8, tol=0.002, note='~100 km; 101.8'))
out.append(check('r_L(B_mp) / d_i', mp * vsw / (e * Bmp) / di, 1.0, tol=1e-6, note='identity'))
res = dict(run=8, checks=out, passed=sum(o['passed'] for o in out), total=len(out))
json.dump(res, open('canary8.json', 'w'), indent=1)
for o in out: print(f"{'PASS' if o['passed'] else 'FAIL'}  {o['name']}: {o['rederived']:.6g} vs {o['logged']} ({o['deviation']*100:.2f} %)")
print(res['passed'], 'of', res['total'])
