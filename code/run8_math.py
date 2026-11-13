"""Run 8 maths: B6 loss of hold, self-forces, heat, flywheel/gyro, tabletop test; B7 thin-film condition; cavity vacuum; X1 relaxation.
Every number printed here goes to run8_numbers.json and into run-sheet part 6 with its inputs."""
import json, math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipk, ellipe
from scipy.optimize import brentq

mu0 = 4e-7 * math.pi * 1.00000000055
eps0, hbar, c, kB, sSB = 8.8541878128e-12, 1.054571817e-34, 299792458.0, 1.380649e-23, 5.670374419e-8
out = {}

# ---------------- B6 rotor (I.17 inputs) ----------------
R, rho, B = 2.0, 8900.0, 30.0
w_spin = 30000 * 2 * math.pi / 60; v = w_spin * R
tr, hz = 0.002, 0.100                       # stack 2 mm radial x 100 mm axial
A = tr * hz
M = rho * A * 2 * math.pi * R
Je = rho * v ** 2 / (B * R)                 # stress-free engineering current density
Itot = Je * A
T = 0.5 * M * v ** 2
Nr, Nz = 44, 25; N = Nr * Nz
wt, tt = 0.004, 45e-6                       # tape 4 mm x 45 um
I0 = Itot / N
Ic_tape = 1500.0                            # LBC6, 4.2 K, 30 T, B//ab
out['b6'] = dict(M=M, v=v, Je=Je, Itot=Itot, T=T, N=N, I0=I0, i=I0 / Ic_tape, rho_v2=rho * v ** 2)

# ---------------- I.25 (a) local quench in a stack of coupled closed loops ----------------
pitch = tr / Nr
def lng(dr, dz):
    """ln of the geometric mean distance between two thin strips of width wt (along z), offset dr (radial) and dz (axial)."""
    if dr == 0 and dz == 0:
        return math.log(wt) - 1.5
    f = lambda u: (wt - abs(u)) * 0.5 * math.log((u + dz) ** 2 + dr ** 2)
    pts = [p for p in (-dz, 0.0) if -wt < p < wt]
    val, _ = quad(f, -wt, wt, points=pts or None, limit=400)
    return val / wt ** 2
tab = np.zeros((Nr, Nz))
for kr in range(Nr):
    for kz in range(Nz):
        tab[kr, kz] = lng(kr * pitch, kz * wt)
ir = np.repeat(np.arange(Nr), Nz); iz = np.tile(np.arange(Nz), Nr)
DR = np.abs(ir[:, None] - ir[None, :]); DZ = np.abs(iz[:, None] - iz[None, :])
L = mu0 * R * (math.log(8 * R) - tab[DR, DZ] - 2.0)
eig_min = float(np.linalg.eigvalsh(L).min())
Leq = float(L.sum()) / N ** 2
def quench(q):
    s = np.array([j for j in range(N) if j != q])
    Lss = L[np.ix_(s, s)]; Lsq = L[s, q]
    dI = I0 * np.linalg.solve(Lss, Lsq)
    leak = 0.5 * I0 ** 2 * (L[q, q] - Lsq @ np.linalg.solve(Lss, Lsq))
    k = int(np.argmax(dI))
    return dict(q=(int(ir[q]), int(iz[q])), max_rise=float(dI.max() / I0), at=(int(ir[s[k]]), int(iz[s[k]])),
                i_after=float((I0 + dI.max()) / Ic_tape), deficit_frac_of_total=float((I0 - dI.sum()) / Itot),
                leak_J=float(leak), n_above_5pc=int((dI / I0 > 0.05).sum()))
cases = {'outer top corner': (Nr - 1) * Nz + (Nz - 1), 'inner top corner': 0 * Nz + (Nz - 1), 'middle': (Nr // 2) * Nz + Nz // 2,
         'outer middle': (Nr - 1) * Nz + Nz // 2}
def dI_map(q):
    s = np.array([j for j in range(N) if j != q])
    dI = I0 * np.linalg.solve(L[np.ix_(s, s)], L[s, q]); m = np.zeros(N); m[s] = dI / I0; m[q] = -1.0
    return m.reshape(Nr, Nz)
np.savez('run8_quench.npz', outer_top=dI_map((Nr - 1) * Nz + (Nz - 1)), middle=dI_map((Nr // 2) * Nz + Nz // 2))
out['i25_local'] = dict(L_self=float(L[0, 0]), k_radial_nbr=float(L[0, Nz] / L[0, 0]), k_axial_nbr=float(L[0, 1] / L[0, 0]),
                        k_far=float(L[0, N - 1] / L[0, 0]), eig_min=eig_min, Leq=Leq, U_self=0.5 * Leq * Itot ** 2,
                        cases={k: quench(q) for k, q in cases.items()})

# cables: the 44 radial tapes at each axial position soldered into one conductor (current shared), 25 closed loops
ncab = Nz
Lc = np.zeros((ncab, ncab))
for a_ in range(ncab):
    ia = np.where(iz == a_)[0]
    for b_ in range(ncab):
        ib = np.where(iz == b_)[0]
        Lc[a_, b_] = L[np.ix_(ia, ib)].mean()
Ic_cab = Nr * Ic_tape; Ic0 = Itot / ncab
def quench_cab(q):
    s = np.array([j for j in range(ncab) if j != q])
    dI = Ic0 * np.linalg.solve(Lc[np.ix_(s, s)], Lc[s, q])
    return dict(q=q, max_rise=float(dI.max() / Ic0), i_after=float((Ic0 + dI.max()) / Ic_cab),
                deficit_frac=float((Ic0 - dI.sum()) / Itot), leak_J=float(0.5 * Ic0 ** 2 * (Lc[q, q] - Lc[s, q] @ np.linalg.solve(Lc[np.ix_(s, s)], Lc[s, q]))))
out['i25_cables'] = dict(k_axial_cable_nbr=float(Lc[0, 1] / math.sqrt(Lc[0, 0] * Lc[1, 1])), end=quench_cab(ncab - 1), middle=quench_cab(ncab // 2),
                         i_max_safe_end=None, defect_bypass_rise=1 / (Nr - 1))
out['i25_cables']['i_max_safe_end'] = 1 / (1 + out['i25_cables']['end']['max_rise'])
out['i25_local']['i_max_safe_corner'] = 1 / (1 + out['i25_local']['cases']['outer top corner']['max_rise'])
out['i25_local']['i_max_safe_middle'] = 1 / (1 + out['i25_local']['cases']['middle']['max_rise'])

# ---------------- I.25 (b) global loss of hold ----------------
sig_a = 1.0e9                                # Hastelloy-substrate tape yields ~0.9-1.1 GPa (Bang et al. 2024)
delta_max = sig_a / (rho * v ** 2)
v_self = math.sqrt(sig_a / rho)
rows = []
for rho_cu in (2e-10, 1e-9, 2e-9):          # copper at 20-30 K: RRR ~100 zero-field to x10 magnetoresistance at 30 T (estimate)
    G = (wt * 10e-6) / rho_cu + (wt * 30e-6) / 1.24e-6 + (wt * 2e-6) / 3e-10   # Cu 10 um total, Hastelloy 30 um, Ag 2 um
    R_tape = (2 * math.pi * R) / G
    R_b = R_tape / N
    tau = Leq / R_b
    t_fail = delta_max * tau
    rows.append(dict(rho_cu=rho_cu, R_tape=R_tape, R_bundle=R_b, tau_q=tau, t_fail=t_fail,
                     P_brake=(T - 0.5 * M * v_self ** 2) / t_fail))
stator = [dict(tau_s=ts, t_fail=delta_max * ts, P_brake=(T - 0.5 * M * v_self ** 2) / (delta_max * ts)) for ts in (1, 10, 30)]
out['i25_global'] = dict(sig_a=sig_a, delta_max=delta_max, v_self=v_self, E_frac_at_vself=(v_self / v) ** 2,
                         rotor=rows, stator=stator, slow_spin_down_1h_W=T / 3600, TNT_kg=T / 4.184e6)
# ---------------- I.25 (c) containment bound ----------------
e_abs = dict(UHMWPE_SK75=3.4e9 * 0.035 / (2 * 970), UHMWPE_SK75_elastic=3.4e9 ** 2 / (2 * 113e9 * 970))
out['i25_contain'] = dict(e_abs=e_abs, M_min_t={k: T / e / 1e3 for k, e in e_abs.items()}, craft_min_kg=312,
                          rotor_specific_J_per_kg=T / M, Ni_vaporize_J_per_kg=7.5e6)

# ---------------- I.26 rotor self-forces and current uniformity ----------------
K = Itot / hz
p_JB = (Ic_tape / wt) * B                    # radial pull per tape at J_c
p_c = rho * tt * w_spin ** 2 * R              # centrifugal pressure per tape
i_op = I0 / Ic_tape
strip = (1 - i_op) / 2 * wt
q_edge = p_JB + p_c
def bend(L_strip): return 3 * q_edge * L_strip ** 2 / tt ** 2
Br = lambda d: mu0 * K / (2 * math.pi) * math.log((hz - d) / d)   # 2D sheet, distance d from an end
Bp = mu0 * (Ic_tape / wt) / math.pi
pinch = mu0 * Itot ** 2 * math.log(2) / (2 * math.pi * A)
A_max = lambda s: 2 * math.pi * s / (mu0 * Je ** 2 * math.log(2))
out['i26'] = dict(delta_max=delta_max, p_JB=p_JB, p_c=p_c, i_op=i_op, check_iop_pJB=i_op * p_JB, strip_mm=strip * 1e3, q_edge=q_edge,
                  bend_1fil=bend(strip), bend_nf={nf: bend(strip / nf) for nf in (4, 10, 20, 40)},
                  Br_end_1mm=Br(0.001), Br_end_2mm=Br(0.002), Br_quarter=mu0 * K / (2 * math.pi) * math.log(3), B_pen=Bp,
                  K=K, B_face=mu0 * K / 2, pinch=pinch, A_max_300MPa=A_max(3e8), A_max_500MPa=A_max(5e8),
                  ctrans_substrate=rho * 30e-6 * w_spin ** 2 * R, ctrans_stab=rho * 7e-6 * w_spin ** 2 * R)

# ---------------- I.27 heat budget of a rotor in vacuum ----------------
Asurf = 2 * (2 * math.pi * R * hz) + 2 * (2 * math.pi * R * tr)
rad = {f'{Tk} K': {f'eps {e}': e * sSB * Asurf * (Tk ** 4 - 4.2 ** 4) for e in (0.1, 0.5)} for Tk in (10, 20, 30, 40, 50)}
ripple = {f'{b} mT': 1.0 * (b / 6.3) ** 3 for b in (1, 2, 3, 6.3)}   # I.20: 1 W at 6.3 mT, 500 Hz (R&D tape, below penetration ~B^3)
out['i27'] = dict(A_surf=Asurf, P_rad=rad, ripple_loss_W=ripple, ldx=dict(T_from=5, T_to=10, hours='6-8'))

# ---------------- I.28 flywheel and gyroscope ----------------
Lang = M * R ** 2 * w_spin
mB = Itot * math.pi * R ** 2 * B
out['i28'] = dict(rotor_MJ_per_kg=T / M / 1e6, rotor_Wh_per_kg=T / M / 3600, thin_ring_T1200_MJ_per_kg=4.40e6 / 2 / 1e6,
                  system_MJ_per_kg=T / (M + 289) / 1e6, system_Wh_per_kg=T / (M + 289) / 3600, virial_cap_MJ_per_kg=4.40,
                  L=Lang, torque_at_0p1=Lang * 0.1, mB=mB, tilt_rad=Lang * 0.1 / mB)

# ---------------- I.29 tabletop deciding test ----------------
def tabletop(Rt, Bt, vt, sec=(0.001, 0.004), n=0.03, rw=0.001, sig=1.0e9):
    At = sec[0] * sec[1]; Mt = rho * At * 2 * math.pi * Rt; wt_ = vt / Rt
    Jt = rho * vt ** 2 / (Bt * Rt); It = Jt * At; Tt = 0.5 * Mt * vt ** 2
    ku = n * Mt * wt_ ** 2; g = wt_ * math.sqrt(n)
    def Mco(a, b, z):
        k2 = 4 * a * b / ((a + b) ** 2 + z ** 2); k = math.sqrt(k2)
        return mu0 * math.sqrt(a * b) * ((2 / k - k) * ellipk(k2) - (2 / k) * ellipe(k2))
    def dM(a, b, z, h=1e-7): return (Mco(a, b, z + h) - Mco(a, b, z - h)) / (2 * h)
    Ll = mu0 * Rt * (math.log(8 * Rt / rw) - 2)
    kc = lambda d: (2 * It * dM(Rt, Rt, d)) ** 2 / (2 * Ll - 2 * Mco(Rt, Rt, 2 * d))
    d3 = brentq(lambda d: kc(d) - 3 * ku, 0.005, 1.0)
    Lp = 2 * Ll - 2 * Mco(Rt, Rt, 2 * d3)
    return dict(R=Rt, B=Bt, v=vt, omega=wt_, rpm=wt_ * 60 / (2 * math.pi), M_g=Mt * 1e3, Je_kA_mm2=Jt / 1e9, I=It, T_J=Tt,
                rho_v2_over_sig=rho * vt ** 2 / sig, delta_max=sig / (rho * vt ** 2), gamma=g, f_bw_Hz=math.pi * g / math.log(2) / (2 * math.pi),
                f_spin_Hz=wt_ / (2 * math.pi), d_nullflux=d3, w_z=math.sqrt(2 * ku / Mt), whirl=math.sqrt(2 / n) - 1,
                drift_s_at_1e12=Lp * 2 / 1e-12, pinch=mu0 * It ** 2 * math.log(2) / (2 * math.pi * At),
                TNT_g=Tt / 4.184e6 * 1e3)
out['i29'] = dict(slow=tabletop(0.1, 8.0, 500.0), fast=tabletop(0.1, 8.0, 970.0),
                  Je_8T_assumed_kA_mm2=15.0, note='J_e(8 T, 4.2 K, B//ab) ~15 kA/mm2 assumed (2x the 30 T value); operate at 0.7 of it')

# ---------------- V.10 B7: thin film inside the cavity ----------------
Z0 = math.sqrt(mu0 / eps0)
def A_film(sig1, t, ns=1.0):
    y = Z0 * sig1 * t
    return 4 * y / ((1 + ns + y) ** 2) if ns == 1.0 else 4 * y / (1 + ns + y) ** 2
films = []
for sig1 in (1e4, 3e4, 1e5):
    for t in (5e-9, 10e-9, 22e-9, 50e-9, 100e-9, 220e-9):
        films.append(dict(sigma1=sig1, t_nm=t * 1e9, A=A_film(sig1, t)))
t_for_A = {f'{s:.0e}': {f'A={a}': brentq(lambda t: A_film(s, t) - a, 1e-12, 1.0 / (Z0 * s) * 2) * 1e9 for a in (0.05, 0.1, 0.2)} for s in (1e4, 3e4, 1e5)}
fel = dict(ELBE=dict(g=0.06, L=0.07), FELIX=dict(g=0.50, L=0.05))
for k, d in fel.items(): d['A_max'] = d['g'] - d['L']
out['v10'] = dict(Z0=Z0, films=films, t_nm_for_A=t_for_A, fel=fel, pump_depth_nm=220, uniform_t_nm=22,
                  G_at_A={a: 1 / (a + 0.05) for a in (0.05, 0.1, 0.2, 0.4)})

# ---------------- V.11 cavity vacuum field ----------------
f10 = 10e12; lam = c / f10; om = 2 * math.pi * f10
Evac = lambda V: math.sqrt(hbar * om / (2 * eps0 * V))
out['v11'] = dict(lambda_um=lam * 1e6, E_vac_halfwave_cube=Evac((lam / 2) ** 3), E_vac_1e3_lam3=Evac(1e-3 * lam ** 3),
                  E_vac_1e6_lam3=Evac(1e-6 * lam ** 3), E_drive=(1e8, 1e9), shift_reported=0.10, gap8_needs=2.0)

# ---------------- III.7 X1 lingering force ----------------
tau = lambda er, rho_e: eps0 * er * rho_e
out['iii7'] = dict(PTFE_tau_s=tau(2.1, 1e16), PTFE_tau_days=tau(2.1, 1e16) / 86400,
                   PI_tau_s=(tau(3.4, 1e13), tau(3.4, 1.5e15)), PI_tau_h=(tau(3.4, 1e13) / 3600, tau(3.4, 1.5e15) / 3600),
                   sigma_t_C_m2=math.sqrt(2 * eps0 * 4.46e-3 / 0.0025), E_t=math.sqrt(2 * 4.46e-3 / (eps0 * 0.0025)))

json.dump(out, open('run8_numbers.json', 'w'), indent=1, default=float)
def p(k):
    print('==', k); print(json.dumps(out[k], indent=1, default=lambda x: float(x))[:2500])
for k in out: p(k)
