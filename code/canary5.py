"""Run 5 canary: re-derive six logged run-4 numbers from the inputs as written in state v5 and run-sheet part 3.
Independent code (does not import run4_math.py).  Pass = within 2 % of the logged value."""
import json, math

def composite_fibre_need():                       # I.11: v = R * 2*pi*rpm/60; sigma_f >= v^2 (Vf rho_f + (1-Vf) rho_m)/Vf
    v = 2.0 * 30000 / 60 * 2 * math.pi
    return v * v * (0.6 * 1300 + 0.4 * 1200) / 0.6 / 1e9          # GPa

def cowind_carbon_strain():                       # I.14: eps1 = k2 (s1 - s2)/(k1 + k2), equal areas
    k1, k2 = 150.0, 0.6 * 540.0
    return k2 * (0.26 - 0.0) / (k1 + k2)                           # percent

def weibull_specimens(m):                         # I.12: N >= (z sqrt6 m / (pi dm))^2, z = 2, dm = 4.5
    return (2 * math.sqrt(6) * m / (math.pi * 4.5)) ** 2

def srr_gain_hi():                                # V.6: G = f F^2, F = 15, f = 2.2 um x 10 um / (50 um)^2
    return (2.2 * 10 / 50 ** 2) * 15 ** 2

def xenon_thrust_per_watt():                      # III.4: F/P = sqrt(2 m / (q V)), Xe+ at 30 kV, in uN/W
    m = 131.293 * 1.66053906660e-27; q = 1.602176634e-19
    return math.sqrt(2 * m / (q * 30e3)) * 1e6

def london_coefficient():                         # V.7: B/omega = 2 m_e / e
    return 2 * 9.1093837015e-31 / 1.602176634e-19

checks = [('composite bundle fibre needs (GPa)', composite_fibre_need(), 82.9, 'I.11: 2 m, 30,000 rpm, Vf 0.6, 1300 / 1200 kg/m3'),
          ('carbon co-wind tape strain (%)', cowind_carbon_strain(), 0.178, 'I.14: s 0.26 %, E 150 and 0.6x540 GPa, equal areas'),
          ('Weibull pulls, m = 10', weibull_specimens(10), 12, 'I.12: z 2, dm 4.5'),
          ('Weibull pulls, m = 14.5', weibull_specimens(14.5), 25, 'I.12: z 2, dm 4.5'),
          ('split-ring G on resonance (upper)', srr_gain_hi(), 2.0, 'V.6: F 15, 2.2 x 10 um gap in 50 um cell'),
          ('Xe+ thrust per watt at 30 kV (uN/W)', xenon_thrust_per_watt(), 9.5, 'III.4'),
          ('London coefficient (T per rad/s)', london_coefficient(), 1.137e-11, 'V.7')]
out = []
for name, got, logged, note in checks:
    dev = abs(got - logged) / logged
    out.append(dict(name=name, rederived=got, logged=logged, deviation=dev, passed=dev <= 0.02, note=note))
    print(f'{name:40s} re-derived {got:.4g}  logged {logged:.4g}  dev {dev * 100:.2f} %  {"pass" if dev <= 0.02 else "FAIL"}')
json.dump(out, open('/home/claude/p3/sim/pais/canary5.json', 'w'), indent=1)
print('passed', sum(o['passed'] for o in out), 'of', len(out))
