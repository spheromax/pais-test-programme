"""Run 7 of the Pais gap loop: numbers for run-sheet items I.22-I.24, V.9, S.4 and the notes on I.11, I.17, III.6.  Writes run7_numbers.json.
I.22  holding B6's unstable axis actively: critical delay of delayed PD control, Bode's integral -> bandwidth, runout, sensor and actuator sizing
I.23  holding it passively: flux-conserving null-flux loops, K = K0 + G^T L^-1 G; stiffness, drift with joint resistance, eddy damping
I.24  dynamic resistance: transport current near I_c in a ripple field (B6 kill search)
I.11  note: K1 specific strength from the SI areas (open check closed)
I.17  note: production tape at 30 T (open check closed)
III.6 note: Exodus slide numbers against ejecta bounds
V.9   intracavity drive for a light-held state (gap 9 in-between)
S.4   the craft's magnet as a magnetic sail (exploration)"""
import json, math
import numpy as np
from scipy.special import ellipk, ellipe
from scipy.optimize import brentq

mu0 = 4e-7 * math.pi * 1.00000000055
eps0 = 8.8541878128e-12
c = 299_792_458.0
e = 1.602176634e-19
m_p = 1.67262192e-27
out = {}

# ---------------------------------------------------------------- B6 rotor (inputs as runs 5-6, I.17/I.18)
R, rpm, rho = 2.0, 30000, 8900.0
w = 2 * math.pi * rpm / 60
v = w * R
M = 2e-3 * 0.100 * 2 * math.pi * R * rho
f_load = M * v ** 2 / (2 * math.pi * R ** 2)             # N/m at beta = 1
I_r = f_load / 30.0                                      # ampere-turns at 30 T
out['b6'] = dict(M=M, w=w, v=v, f_load=f_load, I_r=I_r, m_rotor=I_r * math.pi * R ** 2)

def gamma(n): return w * math.sqrt(abs(n))              # growth rate of the unstable translation (beta = 1)
def k_u(n): return abs(n) * M * w ** 2                   # destabilizing stiffness magnitude (vertical for n < 0)

# ---------------------------------------------------------------- I.22 active hold
# (a) critical delay of PD control with delay tau for x'' = g^2 x - p x(t-tau) - d x'(t-tau): tau_c = sqrt(2)/g.
#     numerical check: Chebyshev collocation of the delay equation (normalized g = 1), scan (p, d) for any stable point.
def cheb(N):
    x = np.cos(np.pi * np.arange(N + 1) / N)
    cc = np.hstack([2, np.ones(N - 1), 2]) * (-1) ** np.arange(N + 1)
    X = np.tile(x, (N + 1, 1)).T
    dX = X - X.T
    D = np.outer(cc, 1 / cc) / (dX + np.eye(N + 1))
    D = D - np.diag(D.sum(axis=1))
    return D, x

def rightmost(p, d, tau, N=24):
    """rightmost eigenvalue of y' = A0 y(t) + A1 y(t - tau), y = (x, x'), A0 = [[0,1],[1,0]], A1 = [[0,0],[-p,-d]] (Breda's method)."""
    D, x = cheb(N)                      # nodes on [-1, 1]; theta = tau (x - 1)/2 in [-tau, 0]; x[0] = 1 is theta = 0
    Dt = D * 2 / tau
    n = 2
    A = np.zeros(((N + 1) * n, (N + 1) * n))
    A0 = np.array([[0, 1], [1, 0]]); A1 = np.array([[0, 0], [-p, -d]])
    for i in range(1, N + 1):          # rows for theta_i < 0: derivative of the state function
        for j in range(N + 1):
            A[i * n:(i + 1) * n, j * n:(j + 1) * n] = Dt[i, j] * np.eye(n)
    A[0:n, 0:n] = A0                    # theta = 0: the delay equation
    A[0:n, N * n:(N + 1) * n] += A1     # x[N] = -1 is theta = -tau
    return np.max(np.linalg.eigvals(A).real)

def stable_exists(tau, P=np.linspace(1.0, 2.2, 49), Dd=np.linspace(0.0, 2.5, 51)):
    best = (9, None)
    for p in P:
        for d in Dd:
            r = rightmost(p, d, tau)
            if r < best[0]: best = (r, (p, d))
    return best

delay_check = []
for tau in (1.30, 1.38, 1.45, 1.55):
    r, pd = stable_exists(tau)
    delay_check.append(dict(tau_norm=tau, best_rightmost=r, at=pd, stable=bool(r < 0)))
out['i22_delay_check'] = delay_check

# (b) Bode: int_0^inf ln|S| dw = pi*gamma  ->  with the loop dead above w_a, |S|max >= exp(pi*gamma/w_a); |S|max <= 2 needs w_a >= pi*gamma/ln 2
rows = []
for n in (1e-3, 3e-3, 1e-2, 3e-2, 1e-1):
    g = gamma(n); wa = math.pi * g / math.log(2)
    rows.append(dict(n=n, gamma=g, tau_c=math.sqrt(2) / g, w_a_min=wa, f_a_min=wa / (2 * math.pi), spin_over_wa=w / wa,
                     k_u=k_u(n), F_20um=k_u(n) * 20e-6,
                     noise_10nm=10e-9 * math.sqrt(wa / (2 * math.pi)), noise_1um=1e-6 * math.sqrt(wa / (2 * math.pi))))
out['i22_table'] = rows
n_sep = (w / 3 / (math.pi / math.log(2)) / w) ** 2       # |n| at which w_a,min = spin/3
out['i22_n_for_spin_over_3'] = n_sep
# (c) actuator: radial field per newton at the rotor, and an anti-Helmholtz pair of radius R at +-h (near-wire limit B_r = mu0 I/(pi h))
Br_per_N = 1 / (2 * math.pi * R * I_r)
h = 0.3
act = dict(Br_per_N=Br_per_N)
for lab, F in (('hold 20 um at 1e-3', k_u(1e-3) * 20e-6), ('0.1 g', 0.1 * 9.80665 * M), ('1 g', 9.80665 * M)):
    Br = F * Br_per_N
    act[lab] = dict(F=F, Br=Br, amp_turns=Br * math.pi * h / mu0)
out['i22_actuator'] = act
# (d) eddy delay of a cryostat wall between coil and rotor: tau_w ~ mu0 sigma t l (stainless, 5 mm, 0.3 m)
out['i22_wall_tau'] = mu0 * 1.4e6 * 0.005 * 0.3

# ---------------------------------------------------------------- I.23 passive hold: superconducting null-flux pair
def Mcoax(a, b, z):
    """mutual inductance of coaxial thin loops (radii a, b, axial separation z)."""
    m = 4 * a * b / ((a + b) ** 2 + z ** 2)
    k = math.sqrt(m)
    return mu0 * math.sqrt(a * b) * ((2 / k - k) * ellipk(m) - 2 / k * ellipe(m))

def dMdz(a, b, z, h=1e-6):
    return (Mcoax(a, b, z + h) - Mcoax(a, b, z - h)) / (2 * h)

def Lloop(a, rw): return mu0 * a * (math.log(8 * a / rw) - 2.0)

rw = 0.005           # effective conductor radius of a loop (a few stacked tapes), m
def pair(d, a=R):
    g = -2 * I_r * dMdz(R, a, d)                          # dPhi_pair/dz at z = 0 (per turn of the pair)
    L = 2 * Lloop(a, rw) - 2 * Mcoax(a, a, 2 * d)         # loops in series opposition, per turn^2
    return g, L, g ** 2 / L

# numerical check of K = K0 + g^2/L by the energy route: U(z) = -k_u z^2/2 + (Phi_pair(z))^2 / (2 L)
def U_pair(z, d, a=R):
    g, L, _ = pair(d, a)
    Phi = I_r * (Mcoax(R, a, z - d) - Mcoax(R, a, z + d))
    return Phi ** 2 / (2 * L)
d_chk = 0.3
hz = 1e-4
k_num = (U_pair(hz, d_chk) - 2 * U_pair(0, d_chk) + U_pair(-hz, d_chk)) / hz ** 2
out['i23_check'] = dict(d=d_chk, k_analytic=pair(d_chk)[2], k_numeric=k_num)

ptab = []
for d in (0.08, 0.1, 0.15, 0.2, 0.3, 0.5, 0.75, 1.0):
    g, L, kc = pair(d)
    ptab.append(dict(d=d, g=g, L=L, k_c=kc, i_20um=g * 20e-6 / L, i_1mm=g * 1e-3 / L,
                     B_rotor_at_loop=mu0 * I_r / (2 * math.pi * d)))
out['i23_table'] = ptab

def d_for(kc_target):
    return brentq(lambda d: pair(d)[2] - kc_target, 0.05, 5.0)

design = []
for n in (1e-3, 1e-2, 1e-1):
    ku = k_u(n)
    d3 = d_for(3 * ku)
    g, L, kc = pair(d3)
    wz = math.sqrt((kc - ku) / M)
    kp = 0.5 * n * M * w ** 2                                  # in-plane stiffness for n<0
    design.append(dict(n=n, k_u=ku, d_for_3x=d3, k_c=kc, w_z=wz, wz_over_spin=wz / w, f_z=wz / (2 * math.pi),
                       w_inplane=math.sqrt(kp / M), whirl_ratio=math.sqrt(2 / n) - 1))
out['i23_design'] = design

# drift with joint resistance: slow root s ~ (R/L) k_u/(k_c - k_u); cubic M L s^3 + M Rj s^2 + (g^2 - k_u L) s - k_u Rj = 0
drift = []
for n in (1e-3, 1e-1):
    ku = k_u(n); d3 = d_for(3 * ku); g, L, kc = pair(d3)
    for Rj in (1e-13, 1e-12, 1e-9, 1e-8):
        roots = np.roots([M * L, M * Rj, g ** 2 - ku * L, -ku * Rj])
        slow = max(r.real for r in roots if abs(r.imag) < 1e-9)
        drift.append(dict(n=n, Rj=Rj, L_over_R_s=L / Rj, slow_rate=slow, tau_drift_s=1 / slow,
                          approx=(Rj / L) * ku / (kc - ku)))
out['i23_drift'] = drift

# eddy damper: a copper null-flux pair (g_n = g_s/2 at the same geometry scale) tuned in R_n; coupled eigenvalues
def damped(n, frac=0.5):
    ku = k_u(n); d3 = d_for(3 * ku); gs, Ls, kc = pair(d3)
    gn, Ln = frac * gs, Ls            # a weaker copper pair (fewer turns' worth of coupling), same inductance scale
    best = (0, None, None)
    for Rn in np.logspace(-9, -1, 400):
        # state: x, xdot, i_s, i_n ; M x'' = ku x - gs i_s - gn i_n ; Ls i_s' = gs x' ; Ln i_n' = -Rn i_n + gn x'
        A = np.array([[0, 1, 0, 0],
                      [ku / M, 0, -gs / M, -gn / M],
                      [0, gs / Ls, 0, 0],
                      [0, gn / Ln, 0, -Rn / Ln]])
        ev = np.linalg.eigvals(A)
        osc = [z for z in ev if abs(z.imag) > 1e-6]
        if not osc: continue
        z = max(osc, key=lambda q: q.real)
        zeta = -z.real / abs(z)
        if zeta > best[0] and max(ev.real) < 1e-9: best = (zeta, Rn, abs(z))
    return dict(n=n, zeta_max=best[0], Rn_opt=best[1], w_mode=best[2], Rn_over_Ln_opt=(best[1] / Ls) if best[1] else None)
out['i23_damper'] = [damped(1e-3), damped(1e-1)]

# ---------------------------------------------------------------- I.24 dynamic resistance
# B_th(i) = kappa mu0 K_c (1 - i), K_c = I_c/width; kappa 0.5 (slab theory) .. 1.5 (perpendicular measurements 2-3x slab, ST194)
Ic30, width = 1500.0, 0.004
Kc = Ic30 / width
dyn = dict(Ic=Ic30, width=width, Kc=Kc, mu0Kc=mu0 * Kc)
rows = []
for i in (0.5, 0.7, 0.9, 0.95, 0.98, 0.99, 0.995):
    rows.append(dict(i=i, Bth_low=0.5 * mu0 * Kc * (1 - i), Bth_high=1.5 * mu0 * Kc * (1 - i)))
dyn['rows'] = rows
for Brip in (3e-3, 6e-3):
    dyn[f'i_max_{int(Brip*1e3)}mT'] = (1 - Brip / (0.5 * mu0 * Kc), 1 - Brip / (1.5 * mu0 * Kc))
# loss above threshold (slab form R_dyn/L = 4 a f (B - B_th)/I_c), one tape of 12.57 m at i = 0.995, 6 mT, 500 Hz
a_half, f = width / 2, 500.0
i = 0.995; Bth = 0.5 * mu0 * Kc * (1 - i); Rd = 4 * a_half * f * (6e-3 - Bth) / Ic30 * (2 * math.pi * R)
dyn['above_threshold_example'] = dict(i=i, Bth=Bth, R_dyn_per_tape=Rd, P_per_tape=(i * Ic30) ** 2 * Rd)
out['i24'] = dyn

# ---------------------------------------------------------------- I.17 note: B6 conductor with production tape at 30 T
tape_w, tape_t = 0.004, 45e-6
Je_prod = Ic30 / (tape_w * tape_t)
n_tapes = (0.002 * 0.100) / (tape_w * tape_t)
out['i17_tape'] = dict(Ic_30T=Ic30, width=tape_w, thickness=tape_t, Je=Je_prod, J_needed=rho * v ** 2 / (30 * R),
                      i_needed=(rho * v ** 2 / (30 * R)) / Je_prod, n_tapes=n_tapes, I_per_tape=I_r / n_tapes,
                      tape_km=n_tapes * 2 * math.pi * R / 1e3,
                      UH_thick_film_Ic=5812.0, UH_Je_if_0p1mm=5812.0 / (0.004 * 1e-4))

# ---------------------------------------------------------------- I.11 note: K1 from the SI tables
def A1(ds): return sum(math.pi * d * 0.34 for d in ds)
def A2(ds): return sum(math.pi * d ** 2 / 4 for d in ds)
si = []
for name, ds, a1, a2 in (('CNTB-2', (1.6, 1.8), 3.6298, 4.5553), ('CNTB-3', (1.5, 2.6, 1.8), 6.2988, 9.6211)):
    si.append(dict(name=name, d=ds, A1_calc=A1(ds), A1_SI=a1, A2_calc=A2(ds), A2_SI=a2))
rho_wall = 2260.0
need = v ** 2
out['i11_k1'] = dict(si=si, rho_wall=rho_wall, Ntex=80e9 / rho_wall / 1e6, need=need / 1e6, ratio=80e9 / rho_wall / need,
                     v_max=math.sqrt(80e9 / rho_wall), rho_envelope_for_43=rho_wall * 43 / 80,
                     mean_d_implied=4 * 0.34 * 80 / 43)

# ---------------------------------------------------------------- III.6 note: Exodus slide numbers
F_ex, V_ex, I_ex, A_face = 4.46e-3, 3500.0, 0.065e-6, 0.0025
E_needed = math.sqrt(2 * F_ex / (eps0 * A_face))
ion = lambda amu: I_ex * math.sqrt(2 * amu * 1.66053907e-27 * V_ex / e)
out['iii6_exodus'] = dict(F=F_ex, P=V_ex * I_ex, E_for_F_on_25cm2=E_needed, gap_at_3500V=V_ex / E_needed,
                          F_ions_N2=ion(28), F_ions_200amu=ion(200), F_photons=V_ex * I_ex / c,
                          ratio_to_ion_bound=F_ex / ion(200))

# ---------------------------------------------------------------- V.9 intracavity drive (gap 9)
F_hold, spot = 4.0, 100e-6
S = math.pi * (spot / 2) ** 2
E_p = F_hold * S
v9 = dict(E_pulse=E_p, P_ext_100MHz=E_p * 1e8, P_ext_2GHz=E_p * 2e9)
L_m = 0.04
v9['gain'] = [dict(A=A, G=1 / (A + L_m), P_100MHz=E_p * 1e8 * (A + L_m), P_2GHz=E_p * 2e9 * (A + L_m)) for A in (0.02, 0.05, 0.1, 0.2)]
v9['felice'] = dict(out_uJ=10, intra_uJ=400, ratio=40, implied_outcoupling=1 / 40, spot_diam_at_4Jm2=2 * math.sqrt(400e-6 / (math.pi * F_hold)))
# FELICE-type test: 8 us macropulse at 1 GHz on K3C60/diamond, absorbed fraction A = 0.1: surface rise for constant flux on a half-space
A_abs, t_mp = 0.1, 8e-6
q = A_abs * F_hold * 1e9                     # W/m2 during the macropulse
k_d, rc_d = 2000.0, 3510 * 509.0
dT = 2 * q * math.sqrt(t_mp / (math.pi * k_d * rc_d))
v9['felice_test'] = dict(A=A_abs, flux_W_m2=q, t=t_mp, dT_surface=dT, pulses=int(t_mp * 1e9))
out['v9'] = v9

# ---------------------------------------------------------------- S.4 the craft's magnet as a magnetic sail (1 AU)
n_sw, v_sw = 5e6, 4.0e5
rhov2 = n_sw * m_p * v_sw ** 2
B_mp = math.sqrt(mu0 * rhov2)                          # B^2/2mu0 = rho v^2 / 2
d_i = c / math.sqrt(n_sw * e ** 2 / (eps0 * m_p))      # ion inertial length
s4 = dict(rho_v2=rhov2, B_mp=B_mp, d_i=d_i, r_L_at_mp=m_p * v_sw / (e * B_mp))
cases = []
for lab, mom in (('rotor alone (1.17 MA-turns, R 2 m)', I_r * math.pi * R ** 2), ('uncompensated stator (I.18 pair scaled to 30 T)', 2.1e9)):
    R_mhd = (mu0 * mom / (4 * math.pi * B_mp)) ** (1 / 3)
    C_st = math.sqrt(mu0 * mom * e / (4 * math.pi * m_p * v_sw))
    cases.append(dict(label=lab, moment=mom, R_MHD=R_mhd, R_MHD_over_di=R_mhd / d_i, C_stormer=C_st,
                      F_MHD=rhov2 * math.pi * R_mhd ** 2, F_kinetic=rhov2 * math.pi * C_st ** 2))
s4['cases'] = cases
s4['craft_mass_min'] = M + 289.2
s4['dv_per_year'] = [cs['F_kinetic'] / (M + 289.2) * 3.156e7 for cs in cases]
s4['solar_sail_100m2'] = 9.08e-6 * 100
out['s4'] = s4

json.dump(out, open('/home/claude/p3/sim/pais/run7_numbers.json', 'w'), indent=1, default=float)

# ---------------------------------------------------------------- print a digest
print('B6: M %.2f kg, I_r %.4g A-turns, rotor moment %.3g A m2' % (M, I_r, out['b6']['m_rotor']))
print('I.22 delay check (normalized tau_c = sqrt2 = 1.414):', [(x['tau_norm'], round(x['best_rightmost'], 4), x['stable']) for x in delay_check])
for r in rows if False else out['i22_table']:
    print('  n %.0e gamma %.1f tau_c %.2f ms  w_a>=%.0f rad/s (%.0f Hz) spin/w_a %.2f  F20um %.1f N  noise10nm %.0f nm  noise1um %.1f um' % (
        r['n'], r['gamma'], r['tau_c'] * 1e3, r['w_a_min'], r['f_a_min'], r['spin_over_wa'], r['F_20um'], r['noise_10nm'] * 1e9, r['noise_1um'] * 1e6))
print('  |n| for w_a = spin/3: %.2e' % n_sep)
print('  actuator', {k: (v if not isinstance(v, dict) else {kk: '%.3g' % vv for kk, vv in v.items()}) for k, v in act.items()})
print('  wall delay %.2f ms' % (out['i22_wall_tau'] * 1e3))
print('I.23 check: k analytic %.4g vs energy route %.4g' % (out['i23_check']['k_analytic'], out['i23_check']['k_numeric']))
for p in ptab:
    print('  d %.2f m: g %.3g Wb/m, L %.3g H, k_c %.3g N/m, i(20um) %.1f A, i(1mm) %.0f A, B_rotor at loop %.2f T' % (
        p['d'], p['g'], p['L'], p['k_c'], p['i_20um'], p['i_1mm'], p['B_rotor_at_loop']))
for dsg in design:
    print('  design n %.0e: k_u %.3g, d(3x) %.3f m, w_z %.0f rad/s (%.2f spin), in-plane %.0f rad/s, whirl ratio %.1f' % (
        dsg['n'], dsg['k_u'], dsg['d_for_3x'], dsg['w_z'], dsg['wz_over_spin'], dsg['w_inplane'], dsg['whirl_ratio']))
for dr in drift:
    print('  drift n %.0e Rj %.0e: L/R %.3g s, tau_drift %.3g s (%.3g h; approx %.3g s)' % (dr['n'], dr['Rj'], dr['L_over_R_s'], dr['tau_drift_s'], dr['tau_drift_s'] / 3600, 1 / dr['approx']))
print('  damper', out['i23_damper'])
print('I.24', {k: v for k, v in dyn.items() if k != 'rows'})
for r in dyn['rows']: print('   i %.3f: B_th %.1f-%.1f mT' % (r['i'], r['Bth_low'] * 1e3, r['Bth_high'] * 1e3))
print('I.17 tape', out['i17_tape'])
print('I.11 K1', out['i11_k1'])
print('III.6', out['iii6_exodus'])
print('V.9', v9)
print('S.4', {k: v for k, v in s4.items() if k != 'cases'})
for cs in cases: print('   ', cs)
