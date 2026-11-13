"""Run 6 of the Pais gap loop: numbers for run-sheet items I.18-I.21 and V.8.  Writes run6_numbers.json.
I.18  translational stability of a current ring in an axisymmetric field (Earnshaw trace, growth rates, flux conservation)
I.19  supercritical whirl: rotating vs non-rotating damping
I.20  ripple (hysteresis) loss of a spinning REBCO rotor, Brandt-Indenbom thin strip
I.21  a pre-strained band: the pre-strain comes out of the band's own failure strain (correction to I.6/I.14)
V.8   strain as pressure: biaxial film strain vs hydrostatic pressure (gap 8 in-between)
plus the K1 area check (I.11 open input) and the Inductrack drag cost (B6 exploration)."""
import json, math
import numpy as np
from scipy.special import ellipk, ellipe

mu0 = 1.25663706212e-6
c = 299_792_458.0
out = {}

# ---------------------------------------------------------------- full-scale B6 rotor (inputs as run 5, I.17)
R, rpm, rho = 2.0, 30000, 8900.0
w = 2 * math.pi * rpm / 60
v = w * R
M = 2e-3 * 0.100 * 2 * math.pi * R * rho
IB_full = M * v ** 2 / (2 * math.pi * R ** 2)            # inward force per unit length for beta = 1, N/m  (= I*B0)
J30 = rho * v ** 2 / (30 * R)                              # J_e needed at 30 T, A/m2
out['b6'] = dict(w=w, v=v, M=M, a_c=v ** 2 / R, g_c=v ** 2 / R / 9.80665, IB_full=IB_full, J_needed_30T=J30,
                 Mw2=M * w ** 2)

# ---------------------------------------------------------------- I.18 analytic stiffnesses and rates
def rates(n, beta=1.0):
    """fixed-current ring, field index n = -(R/B) dB/dr, share beta of the load magnetic.
    k_perp = -n beta M w^2 / 2 (each in-plane axis), k_z = n beta M w^2; trace 0."""
    kp = -n * beta * M * w ** 2 / 2
    kz = n * beta * M * w ** 2
    return kp, kz

tab = []
for n in (-0.3, -0.1, -0.03, -0.01, -0.003, -0.001, 0.001, 0.01, 0.1):
    kp, kz = rates(n)
    unstable = 'z' if kz < 0 else 'x,y'
    kun = kz if kz < 0 else kp
    kst = kp if kz < 0 else kz
    tab.append(dict(n=n, k_perp=kp, k_z=kz, trace=2 * kp + kz, unstable=unstable,
                    growth=math.sqrt(-kun / M), stable_freq=math.sqrt(kst / M),
                    F_at_20um=abs(kun) * 20e-6, whirl_ratio=(w / math.sqrt(kp / M) - 1) if kp > 0 else None))
out['i18_table'] = tab

# numerical check of the Earnshaw trace and of the analytic forms: rotor ring (R) in the field of two coaxial stator loops
def loop_field(a, zs, I, r, z):
    """B_r, B_z of a circular loop (radius a, at height zs, current I) at (r, z); r > 0."""
    dz = z - zs
    den = (a + r) ** 2 + dz ** 2
    m = 4 * a * r / den
    K, E = ellipk(m), ellipe(m)
    q = (a - r) ** 2 + dz ** 2
    pre = mu0 * I / (2 * math.pi * np.sqrt(den))
    Bz = pre * (K + (a ** 2 - r ** 2 - dz ** 2) / q * E)
    Br = pre * dz / r * (-K + (a ** 2 + r ** 2 + dz ** 2) / q * E)
    return Br, Bz

STATOR = [(2.5, +0.6, 1.0e7), (2.5, -0.6, 1.0e7)]           # (radius, height, ampere-turns): an assumed outer coil pair
def B_at(x, y, z):
    r = np.hypot(x, y)
    Br, Bz = 0 * r, 0 * r
    for a, zs, I in STATOR:
        br, bz = loop_field(a, zs, I, r, z); Br, Bz = Br + br, Bz + bz
    return Br * x / r, Br * y / r, Bz

Nphi = 4000
phi = np.linspace(0, 2 * math.pi, Nphi, endpoint=False)
def ring_force(dx, dz, Iring):
    x, y, z = R * np.cos(phi) + dx, R * np.sin(phi), 0 * phi + dz
    dlx, dly = -R * np.sin(phi) * (2 * math.pi / Nphi), R * np.cos(phi) * (2 * math.pi / Nphi)
    Bx, By, Bz = B_at(x, y, z)
    Fx = Iring * np.sum(dly * Bz - 0 * By)
    Fy = Iring * np.sum(0 * Bx - dlx * Bz)
    Fz = Iring * np.sum(dlx * By - dly * Bx)
    return Fx, Fy, Fz

_, _, Bz0 = B_at(np.array([R]), np.array([0.0]), np.array([0.0])); Bz0 = float(Bz0[0])
h = 1e-4
_, _, Bzp = B_at(np.array([R + h]), np.array([0.0]), np.array([0.0])); _, _, Bzm = B_at(np.array([R - h]), np.array([0.0]), np.array([0.0]))
n_num = float(-(R / Bz0) * (Bzp[0] - Bzm[0]) / (2 * h))
Iring = -1.0e4 * np.sign(Bz0)        # sign chosen so the force on each element points inward (moment antiparallel to B)
f_in = abs(Iring * Bz0)               # inward force per unit length at the ring
d = 1e-3
Fx_p = ring_force(d, 0, Iring)[0]; Fx_m = ring_force(-d, 0, Iring)[0]
Fz_p = ring_force(0, d, Iring)[2]; Fz_m = ring_force(0, -d, Iring)[2]
kx_num = -(Fx_p - Fx_m) / (2 * d); kz_num = -(Fz_p - Fz_m) / (2 * d)
out['i18_check'] = dict(stator=STATOR, Bz_at_rotor=Bz0, n=n_num, f_inward=f_in,
                        kx_num=kx_num, kz_num=kz_num, trace_num=2 * kx_num + kz_num,
                        kx_analytic=-math.pi * n_num * f_in, kz_analytic=2 * math.pi * n_num * f_in,
                        trace_over_kz=(2 * kx_num + kz_num) / abs(kz_num))

# flux conservation: offset z0 needed for (dPhi/dz)^2/L to cancel the fixed-current vertical instability
a_eq = math.sqrt(2e-3 * 0.100 / math.pi)                       # equivalent round conductor radius of the 2 x 100 mm section
L1 = mu0 * R * (math.log(8 * R / a_eq) - 2)                    # single-turn-equivalent self inductance
fc = []
for B0 in (20.0, 30.0):
    I1 = IB_full / B0
    for n in (0.1, 0.3, 1.0):
        z0 = math.sqrt(I1 * L1 / (2 * math.pi * n * B0))
        fc.append(dict(B0=B0, n=n, I_turns=I1, z0=z0, z0_over_R=z0 / R))
out['i18_flux'] = dict(a_eq=a_eq, L1=L1, self_flux_30T=IB_full / 30 * L1, B_self_30T=mu0 * (IB_full / 30) / (2 * R), cases=fc)

# levitated-dipole comparison: gravity-scale instability rate sqrt(g / l) for l = 0.1-1 m
out['ldx_rate'] = [math.sqrt(9.80665 / l) for l in (0.1, 0.3, 1.0)]

# ---------------------------------------------------------------- I.19 whirl: Omega < omega_n (1 + c_n / c_r)
wh = []
for n in (0.3, 0.1, 0.03, 0.01, 0.003, 0.001):
    wn = w * math.sqrt(n / 2)
    wh.append(dict(n=n, omega_n=wn, ratio=w / wn, cn_over_cr_needed=w / wn - 1))
out['i19'] = wh
# check the threshold by eigenvalues of M s^2 + (cn + cr) s + k - i Omega cr = 0
def max_re(Mm, k, cn, cr, Om):
    roots = np.roots([Mm, cn + cr, k - 1j * Om * cr]); return float(max(roots.real))
k_ = M * (w * math.sqrt(0.1 / 2)) ** 2; cr_ = 10.0
thr = w * math.sqrt(0.1 / 2) * (1 + 3.0)   # cn = 3 cr: threshold at 4 omega_n
out['i19_check'] = dict(below=max_re(M, k_, 3 * cr_, cr_, 0.99 * thr), above=max_re(M, k_, 3 * cr_, cr_, 1.01 * thr))

# ---------------------------------------------------------------- I.20 ripple (hysteresis) loss, Brandt-Indenbom thin strip
def g(x):
    x = np.asarray(x, dtype=float)
    return np.where(x < 1e-3, x ** 3 / 6, (2 / np.where(x == 0, 1, x)) * np.log(np.cosh(x)) - np.tanh(x))

def Q_cycle(Hm, a, Kc):
    """loss per cycle per unit length, strip width 2a, sheet critical current Kc = Jc d (A/m)."""
    Hc = Kc / math.pi
    return 4 * mu0 * a ** 2 * Kc * Hm * g(Hm / Hc)

a_t, t_t = 2e-3, 1e-4                                          # 4 mm x 0.1 mm tape (assumed)
n_tapes = round(2e-3 / t_t) * round(0.100 / (2 * a_t))         # 2 mm x 100 mm section
L_tape = n_tapes * 2 * math.pi * R
rip = dict(tape_width=2 * a_t, tape_thick=t_t, n_tapes=n_tapes, L_tape=L_tape, cases=[])
for label, Je in (('R&D 4.6 kA/mm2', 4.6e9), ('record 1.0 kA/mm2', 1.0e9), ('commercial 0.6 kA/mm2', 0.6e9)):
    Kc = Je * t_t
    for f in (500.0, 12000.0):
        # small-amplitude closed form: Q = (2/3) pi^3 mu0 a^2 Hm^4 / Kc^2  -> amplitude for 1 W
        Hm1W = (1.0 * Kc ** 2 / (f * L_tape * (2 / 3) * math.pi ** 3 * mu0 * a_t ** 2)) ** 0.25
        P = {f'{b}mT': float(f * L_tape * Q_cycle(b * 1e-3 / mu0, a_t, Kc)) for b in (1, 3, 10, 30)}
        rip['cases'].append(dict(tape=label, Kc=Kc, Bc=mu0 * Kc / math.pi, f=f, B_1W=mu0 * Hm1W, x_1W=Hm1W / (Kc / math.pi), P=P))
rip['carnot_4K'] = (300 - 4.2) / 4.2
out['i20'] = rip

# ---------------------------------------------------------------- I.21 band failure strain (correction)
eps_irr = 0.0063
cases = []
def Bmax(E, eps): return math.sqrt(2 * mu0 * E * eps)
cases.append(dict(name='Hastelloy-class co-wind', E=220e9, rho=8900, eps_f=None, pre=0.0, eps_work=eps_irr))
cases.append(dict(name='M55J band, run-4 claim', E=0.6 * 540e9, rho=1630, eps_f=None, pre=0.0, eps_work=eps_irr))
for pre in (0.0026, 0.0031, 0.0032):
    cases.append(dict(name=f'M55J UD band, pre-strain {pre * 100:.2f} %', E=338e9, rho=1630, eps_f=0.0061, pre=pre,
                      eps_work=min(eps_irr, 0.0061 - pre)))
cases.append(dict(name='M55J UD band, bonded, no pre-strain', E=338e9, rho=1630, eps_f=0.0061, pre=0.0, eps_work=min(eps_irr, 0.0061)))
for cs in cases:
    cs['Bmax'] = Bmax(cs['E'], cs['eps_work'])
    cs['t_per_GJ'] = cs['rho'] / (cs['E'] * cs['eps_work']) * 1e9 / 1e3
    cs['band_stress_total_GPa'] = cs['E'] * (cs['pre'] + cs['eps_work']) / 1e9
out['i21'] = dict(cases=cases, fibre=dict(strength=4.02e9, E=540e9, elong=0.008, rho=1910),
                  ud_composite=dict(E=338e9, strain=0.0061, strength_55Vf=1.896e9))

# ---------------------------------------------------------------- V.8 strain as pressure
def P_eq(E, nu, eps):      # volume-equivalent hydrostatic pressure of a biaxially clamped film (free out of plane)
    return 2 * E * abs(eps) / (3 * (1 - nu))
def sig_inplane(E, nu, eps):
    return E * abs(eps) / (1 - nu)
E_ox, nu_ox = 200e9, 0.3     # assumed oxide film modulus and Poisson ratio
v8 = dict(E=E_ox, nu=nu_ox, rows=[])
for eps in (0.012, 0.020, 0.030):
    v8['rows'].append(dict(eps=eps, P_eq_GPa=P_eq(E_ox, nu_ox, eps) / 1e9, sigma_inplane_GPa=sig_inplane(E_ox, nu_ox, eps) / 1e9,
                           volume_strain=2 * eps * (1 - 2 * nu_ox) / (1 - nu_ox)))
v8['nickelate_bulk_need_GPa'] = 14.0
v8['hydride_film_max_GPa'] = 10.0
v8['superhydride_need_GPa'] = (100.0, 260.0)
v8['shortfall_hydride'] = (100 / 10, 260 / 10)
out['v8'] = v8

# ---------------------------------------------------------------- K1 open input (I.11): which area goes with 80 GPa
out['k1_area'] = dict(tube_area_GPa=80.0, engineering_GPa=43.0, ratio=80 / 43,
                      Ntex_80_at_1300=80e9 / 1300 / 1e6, Ntex_43_at_1300=43e9 / 1300 / 1e6,
                      Ntex_43_at_envelope=43e9 / (1300 * 43 / 80) / 1e6, need=v ** 2 / 1e6)

# ---------------------------------------------------------------- Inductrack drag cost at rim speed (B6 exploration)
ind = []
for LR in (1e-4, 1e-3, 1e-2):
    for lam in (0.05, 0.1, 0.2):
        LD = 2 * math.pi * v * LR / lam
        ind.append(dict(L_over_R=LR, wavelength=lam, LD=LD, W_per_N=v / LD))
out['inductrack'] = ind
out['inductrack_note'] = 'an axisymmetric rotor presents a static field to the stator: spin alone induces no current; passive EDS needs a patterned rotor'

# ---------------------------------------------------------------- X1 bookkeeping (run 6 update)
out['x1'] = dict(claimed_mN=(5, 10), photon_power_for_10mN_MW=0.010 * c / 1e6, Pc_nN_per_W=1e9 / c)

json.dump(out, open('/home/claude/p3/sim/pais/run6_numbers.json', 'w'), indent=1, default=float)

# ---------------------------------------------------------------- print a digest
b = out['b6']
print(f"rotor M {b['M']:.2f} kg, w {b['w']:.1f} rad/s, centripetal {b['g_c']:.3g} g, I*B {b['IB_full']:.4g} N/m, J_e at 30 T {b['J_needed_30T'] / 1e6:.0f} A/mm2, M w^2 {b['Mw2']:.4g}")
for t in out['i18_table']:
    print(f"n {t['n']:+.3f}: k_perp {t['k_perp']:+.3e} k_z {t['k_z']:+.3e} trace {t['trace']:+.1e} unstable {t['unstable']:4s} growth {t['growth']:.1f}/s stable {t['stable_freq']:.1f} rad/s F(20um) {t['F_at_20um']:.1f} N whirl {t['whirl_ratio']}")
ck = out['i18_check']
print('numerical check:', {k: (round(v_, 4) if isinstance(v_, float) else v_) for k, v_ in ck.items() if k != 'stator'})
print('flux conservation:', out['i18_flux']['L1'], [(cs['B0'], cs['n'], round(cs['z0'], 3), round(cs['z0_over_R'], 3)) for cs in out['i18_flux']['cases']])
print('LDX-like rates', [round(x, 2) for x in out['ldx_rate']])
print('whirl', [(x['n'], round(x['omega_n'], 1), round(x['cn_over_cr_needed'], 2)) for x in out['i19']], out['i19_check'])
print('ripple tapes', rip['n_tapes'], 'length', round(rip['L_tape']), 'm; carnot', round(rip['carnot_4K'], 1))
for cs in rip['cases']:
    print(f"  {cs['tape']:22s} f {cs['f']:7.0f} Bc {cs['Bc'] * 1e3:6.1f} mT  B(1 W) {cs['B_1W'] * 1e3:5.2f} mT (x {cs['x_1W']:.3f})  P: {', '.join(f'{k} {v_:.3g} W' for k, v_ in cs['P'].items())}")
for cs in cases:
    print(f"  {cs['name']:38s} work {cs['eps_work'] * 100:.2f} %  Bmax {cs['Bmax']:.1f} T  {cs['t_per_GJ']:.2f} t/GJ  band stress {cs['band_stress_total_GPa']:.2f} GPa")
for r_ in v8['rows']:
    print(f"  strain {r_['eps'] * 100:.1f} %: P_eq {r_['P_eq_GPa']:.2f} GPa, in-plane {r_['sigma_inplane_GPa']:.2f} GPa, dV/V {r_['volume_strain'] * 100:.2f} %")
print('K1 area', {k: round(v_, 2) for k, v_ in out['k1_area'].items()})
print('inductrack', [(x['L_over_R'], x['wavelength'], round(x['LD']), round(x['W_per_N'], 1)) for x in ind])
print('x1', out['x1'])
