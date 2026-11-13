"""Run-4 canary: re-derive three run-3 numbers from the inputs written in the state file v4, with code that imports
nothing from run3_math.py.  Pass = within 5 %."""
import math, json
c = 299792458.0; eps0 = 8.8541878128e-12; e = 1.602176634e-19; me = 9.1093837015e-31; hbar = 1.054571817e-34

checks = []
# 1. Gap 2: Weibull modulus needed. Inputs (state v4): 80 GPa bundles at 2 cm gauge; hoop R 2 m at 30,000 rpm; density 1,300 kg/m^3
v = 2.0 * 30000 * 2 * math.pi / 60
sig_req = 1300 * v ** 2
L_hoop = 2 * math.pi * 2.0
m_min = math.log(L_hoop / 0.02) / math.log(80e9 / sig_req)
checks.append(('Weibull m needed for the rim', 14.5, m_min, 'inputs: 80 GPa at 2 cm, R 2 m, 30,000 rpm, 1,300 kg/m3'))
# 2. Gap 9: room-temperature re-drive. Inputs: 400 uJ/cm2, 100 um spot, tau 0.5 ns, diamond k 2,000 W/m/K, centre rise P/(pi a k)
E_pulse = 400e-6 * 1e4 * math.pi * (50e-6) ** 2
P = E_pulse / 0.5e-9
dT = P / (math.pi * 50e-6 * 2000)
checks.append(('room-temperature drive power, W', 63.0, P, 'inputs: 400 uJ/cm2, 100 um, 2 GHz'))
checks.append(('room-temperature spot rise, K', 200.0, dT, 'inputs: diamond k 2,000 W/m/K, a 50 um'))
# 3. Gap 3: lab field for chi = 0.5 at E-320. Inputs: 10 GeV electrons, 150 deg between beam and laser directions
gam = 10e9 / 0.51099895e6; beta = math.sqrt(1 - 1 / gam ** 2)
E_S = me ** 2 * c ** 3 / (e * hbar)
E_lab = 0.5 * E_S / (gam * (1 - beta * math.cos(math.radians(150))))
checks.append(('E-320 lab field for chi 0.5, V/m', 1.8e13, E_lab, 'inputs: 10 GeV, 150 deg'))
out = []
for name, logged, got, note in checks:
    dev = abs(got / logged - 1)
    out.append(dict(name=name, logged=logged, rederived=got, deviation=dev, passed=dev <= 0.05, note=note))
    print(f'{name:38s} logged {logged:.3g}  re-derived {got:.4g}  dev {dev * 100:.1f} %  {"PASS" if dev <= 0.05 else "FAIL"}')
json.dump(out, open('/home/claude/p3/sim/pais/canary4.json', 'w'), indent=1)
