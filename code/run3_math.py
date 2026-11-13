"""Run 3 of the Pais gap loop: every number used in the maths run sheet (LaTeX) and on sheets CT-18..CT-23.
SI units, CODATA 2018 constants.  Inputs that are assumptions are marked (assumed) and carried into the outputs."""
import math, json

c = 299792458.0; eps0 = 8.8541878128e-12; mu0 = 1.25663706212e-6; G = 6.67430e-11
hbar = 1.054571817e-34; h = 6.62607015e-34; e = 1.602176634e-19; me = 9.1093837015e-31; kB = 1.380649e-23
gammaE = 0.5772156649015329; g0 = 9.80665
E_S = me ** 2 * c ** 3 / (e * hbar); B_Q = me ** 2 * c ** 2 / (e * hbar)
E_at = 5.14220674763e11            # atomic unit of field, V/m
P_at = 2.9421015697e13             # atomic unit of pressure, Pa
R = {}

# ============================================================== I. specific strength: rims, magnets, field mass
# (name, sigma Pa, rho kg/m^3, gauge/scale, source)
MATS = [
    ('6061-T6 aluminium, yield', 276e6, 2700, 'bulk', 'handbook'),
    ('REBCO tape, irreversible stress, 4.2 K', 0.80e9, 8900, 'tape', 'Barth et al. 2015: 0.74-0.84 GPa'),
    ('REBCO coil, reversible hoop stress', 1.288e9, 8900, 'coil', 'JCSJ 46(5) 2011: 1288 MPa / 0.63 %'),
    ('carbon-fibre hoop, T1000G at Vf 0.6', 0.6 * 6.37e9, 1560, 'metre', 'fibre 6.37 GPa (Sandia 2012 slide) x Vf'),
    ('CNT composite, 2012 coupon', 1.2e9, 1400, 'coupon', 'Sandia 2012 slide (assumed density)'),
    ('CNT fibre, static record', 8.2e9, 1300, 'mm gauge', 'run 1 record (assumed density)'),
    ('CNT bundle, ultralong tubes', 80e9, 1300, 'cm gauge', 'Bai et al. 2018 (assumed density)'),
    ('graphene, ideal strength', 130e9, 2200, 'nm', 'Lee et al. 2008'),
]
mats = []
for name, s, rho, scale, src in MATS:
    sr = s / rho
    mats.append(dict(name=name, sigma=s, rho=rho, scale=scale, src=src, spec=sr, v_ring=math.sqrt(sr),
                     B_thick=math.sqrt(2 * mu0 * s), M_per_GJ=rho * 1e9 / s,          # kg of structure per GJ stored (uniaxial)
                     dm_over_M_uni=sr / c ** 2, dm_over_M_tri=3 * sr / c ** 2))
R['mats'] = mats
v_req = 2.0 * 30000 * 2 * math.pi / 60               # CT-11 rim: R 2 m at 30 000 rpm
R['gap2'] = dict(v_req=v_req, spec_req=v_req ** 2, sigma_req_1300=v_req ** 2 * 1300, sigma_req_1560=v_req ** 2 * 1560,
                 speed_factor_cf=v_req / mats[3]['v_ring'], speed_factor_cntfibre=v_req / mats[5]['v_ring'],
                 measured_tip=965.0, measured_spec=310e3)  # SAE 981282: 965 m/s tip, >310 kJ/kg
R['ceiling'] = dict(B_atomic_pressure=math.sqrt(2 * mu0 * P_at), spec_graphene=130e9 / 2200,
                    v_graphene=math.sqrt(130e9 / 2200), spec_over_c2=130e9 / 2200 / c ** 2,
                    TNT=4.184e6, H2O2=1.34e7)
# magnet example: 35 T in a 2 cm bore, 10 cm long (field energy only inside)
U35 = 35.0 ** 2 / (2 * mu0) * math.pi * 0.01 ** 2 * 0.10
R['magnet'] = dict(p35=35.0 ** 2 / (2 * mu0), U35=U35, M35_rebco=8900 * U35 / 0.8e9, B45=math.sqrt(2 * mu0 * 0.8e9),
                   B57=math.sqrt(2 * mu0 * 1.288e9))
# rotating virial: thin ring K = 1/2, constant-stress disk K = 1
R['flywheel'] = dict(K_ring=0.5, K_disk=1.0, Emax_cf_ring=0.5 * mats[3]['spec'], Emax_cf_disk=mats[3]['spec'])
# Pais rig field mass, and the bound
C_disk = 8 * eps0 * 0.15; U_rig = (1e-6) ** 2 / (2 * C_disk)
R['fieldmass'] = dict(C_disk=C_disk, V_rig=1e-6 / C_disk, U_rig=U_rig, dm_rig=U_rig / c ** 2)

# ============================================================== I.7-9 size effects: Weibull, Daniels, Rosen
L_ref, L_ring = 0.010, 2 * math.pi * 2.0
weib = {}
for m in (3, 5, 10, 20):
    ratio = (L_ref / L_ring) ** (1 / m)
    daniels = (m * math.e) ** (-1 / m) / math.gamma(1 + 1 / m)     # bundle strength / mean fibre strength (same length)
    rosen = lambda delta: (L_ref / (delta * m * math.e)) ** (1 / m)  # chain-of-bundles, in units of the 10 mm Weibull scale
    weib[m] = dict(ratio_ring=ratio, cnt_8p2_at_ring=8.2e9 * ratio, bundle_80_at_ring=80e9 * (0.02 / L_ring) ** (1 / m),
                   daniels=daniels, rosen_100um=rosen(1e-4), rosen_1mm=rosen(1e-3))
R['weibull'] = dict(L_ref=L_ref, L_ring=L_ring, by_m=weib)
# gap 2 closes with dry 80 GPa bundles (2 cm gauge) only if the Weibull modulus m satisfies 80 (0.02/L_ring)^(1/m) >= sigma_req
R['gap2']['m_min_bundle'] = math.log(0.02 / L_ring) / math.log(R['gap2']['sigma_req_1300'] / 80e9)
rho_c = 0.6 * 1300 + 0.4 * 1200                              # bundle composite at Vf 0.6, epoxy 1200 kg/m^3
R['gap2'].update(rho_comp=rho_c, sigma_req_comp=v_req ** 2 * rho_c, sigma_comp_max=0.6 * 80e9,
                 comp_margin=0.6 * 80e9 / (v_req ** 2 * rho_c))

# ============================================================== II. radiation from charged moving bodies
def larmor_osc(p0, w): return p0 ** 2 * w ** 4 / (12 * math.pi * eps0 * c ** 3)     # p = p0 cos wt, time average
def larmor_rot(p0, w): return p0 ** 2 * w ** 4 / (6 * math.pi * eps0 * c ** 3)      # rotating dipole of magnitude p0
def dfact(n):
    out = 1
    for k in range(n, 0, -2): out *= k
    return out
def P_E_lm(l, Qlm, k):   # Jackson 9.155 + 9.169, long-wavelength electric multipole, time-averaged power
    return (c / (2 * eps0)) * ((l + 1) / l) * k ** (2 * l + 2) * abs(Qlm) ** 2 / dfact(2 * l + 1) ** 2
# check: oscillating dipole along z, Q_10 = sqrt(3/4pi) p
chk = P_E_lm(1, math.sqrt(3 / (4 * math.pi)) * 1.0, 1.0) / larmor_osc(1.0, c)
# H1: equilateral triangle, charge Q/3 at each vertex, circumradius a, spin Omega
a_tri, Q_tri = 1.0, 1e-3                                   # 1 m, 1 mC (assumed: near vacuum-breakdown charge for a 1 m body)
v6061 = math.sqrt(276e6 / 2700); Om = v6061 / a_tri
Y33 = (1 / 8) * math.sqrt(35 / math.pi)                    # |Y_33(pi/2, 0)|
Q33 = 2 * 3 * (Q_tri / 3) * a_tri ** 3 * Y33               # factor 2: complex amplitude of the e^{-3i Omega t} component
k3 = 3 * Om / c
P_oct = P_E_lm(3, Q33, k3)
Om_1W = Om * (1.0 / P_oct) ** (1 / 8)
eps_asym = 1e-3; p_asym = eps_asym * (Q_tri / 3) * a_tri
P_asym = larmor_rot(p_asym, Om)
R['H1'] = dict(a=a_tri, Q=Q_tri, Omega=Om, v_rim=v6061, ka=k3 * a_tri, Q33=Q33, P_oct=P_oct, Om_for_1W=Om_1W,
               v_for_1W=Om_1W * a_tri, v_for_1W_over_c=Om_1W * a_tri / c, eps=eps_asym, p_asym=p_asym, P_asym=P_asym,
               jackson_check=chk, U_static=Q_tri ** 2 / (8 * math.pi * eps0 * a_tri))
# H2: rotating in-plane ferroelectric disk (BiFeO3)
Rd, td = 0.05, 1e-3; Vd = math.pi * Rd ** 2 * td
Ps_bulk, Ps_film = 1.0, 1.5
sig_bfo, rho_bfo = 100e6, 8340                             # ceramic strength (assumed), density
v_burst = math.sqrt(sig_bfo / rho_bfo); Om_burst = v_burst / Rd
N_dep = (math.pi / 4) * td / (2 * Rd)                      # thin oblate spheroid, in-plane depolarizing factor
R['H2'] = dict(R=Rd, t=td, V=Vd, p_bulk=Ps_bulk * Vd, p_film=Ps_film * Vd, P_1e4_bulk=larmor_rot(Ps_bulk * Vd, 1e4),
               P_1e4_film=larmor_rot(Ps_film * Vd, 1e4), v_burst=v_burst, Om_burst=Om_burst,
               P_burst_bulk=larmor_rot(Ps_bulk * Vd, Om_burst), N_dep=N_dep, E_dep=N_dep * Ps_bulk / eps0)
# the decisive rig (run 2 design) and Pais Eq. 2 for it, f_G = 1 for a disc ('827 text)
Qr, Rr, x0, f_v, t_op = 1e-6, 0.15, 80e-9, 1e8, 1.0
w_v = 2 * math.pi * f_v
P_rig = larmor_osc(Qr * x0, w_v)
sig_r = Qr / (2 * math.pi * Rr ** 2)                       # mean charge per face
S_eq2 = 1.0 * sig_r ** 2 / eps0 * (x0 * w_v ** 2 * t_op)
P_eq2 = S_eq2 * 2 * math.pi * Rr ** 2
E_center = Qr / (4 * math.pi * Rr ** 2) / eps0
R['rig'] = dict(P_known=P_rig, P_eq2=P_eq2, ratio=P_eq2 / P_rig, sigma_face=sig_r, E_center=E_center,
                v_eq2=x0 * w_v ** 2 * t_op, v_eq2_over_c=x0 * w_v ** 2 * t_op / c,
                F_photon_known=P_rig / c, F_photon_eq2=P_eq2 / c, W_fieldmass=R['fieldmass']['dm_rig'] * g0,
                p_es=0.5 * eps0 * E_center ** 2, F_es_face=0.5 * eps0 * E_center ** 2 * math.pi * Rr ** 2)
R['rig']['symmetry_for_100nN'] = 1e-7 / R['rig']['F_es_face']

# ============================================================== III. momentum: photon rocket, balance floor
I_bal, T_bal, Q_bal, L_arm, tau = 0.5, 30.0, 100.0, 0.25, 100.0  # assumed torsion balance
w0b = 2 * math.pi / T_bal
F_th = math.sqrt(4 * kB * 300 * I_bal * w0b / (Q_bal * tau)) / L_arm
R['momentum'] = dict(F_per_W=1 / c, F_100W=100 / c, F_1kW=1e3 / c, F_thermal=F_th, F_tajmar=1e-7, F_soni=1e-8,
                     Cm_ablation=45e-6, ablation_over_photon=45e-6 * c)

# ============================================================== IV. vacuum thresholds
def schwinger(E): return (e * E) ** 2 / (4 * math.pi ** 3 * hbar ** 2 * c) * math.exp(-math.pi * E_S / E)
gam = 10e9 / 0.51099895e6
alpha_c = math.radians(150.0)                               # crossing angle between e-beam and laser propagation
boost = gam * (1 - math.sqrt(1 - 1 / gam ** 2) * math.cos(alpha_c))
E_lab_chi05 = 0.5 * E_S / boost
w_l = 2 * math.pi * c / 800e-9
a0_peak = e * E_lab_chi05 / (me * c * w_l)
R['vacuum'] = dict(E_S=E_S, B_Q=B_Q, rate_ES=schwinger(E_S), rate_01=schwinger(0.1 * E_S), rate_003=schwinger(0.03 * E_S),
                   rate_evap=0.0, evap_over_ES=5.7e10 / E_S, exponent_evap=math.pi * E_S / 5.7e10,
                   gamma=gam, boost=boost, E_lab_chi05=E_lab_chi05, I_chi05_Wcm2=0.5 * c * eps0 * E_lab_chi05 ** 2 / 1e4,
                   a0_peak=a0_peak, a0_rms_sq=a0_peak ** 2 / 2, E_lab_over_atomic=E_lab_chi05 / E_at,
                   gertsenshtein=4 * math.pi * G / (mu0 * c ** 4), zpe_10THz=hbar * (2 * math.pi * 1e13) ** 4 / (8 * math.pi ** 2 * c ** 3))

# ============================================================== V. pairing and drive
ratio_bcs = 2 * math.pi * math.exp(-gammaE)
R['bcs'] = dict(ratio=ratio_bcs, f300=ratio_bcs * kB * 300 / h, f_K3C60=ratio_bcs * kB * 20 / h,
                drive_over_gap_K3C60=10e12 / (ratio_bcs * kB * 20 / h), E41meV_THz=0.041 * e / h)
F_hold = 4.0                                                # 400 uJ/cm^2 in J/m^2
def spot_d(E): return 2 * math.sqrt(E / F_hold / math.pi)
R['drive'] = dict(F_hold=F_hold,
                  felbe_E=20.0 / 13e6, felbe_d=spot_d(20.0 / 13e6), felbe_d_2uJ=spot_d(2e-6), felbe_I_Wcm2=F_hold * 13e6 / 1e4,
                  plan_E=F_hold * math.pi * (50e-6) ** 2, plan_P=F_hold * math.pi * (50e-6) ** 2 * 1e8,
                  shanghai_E=1e3 / 83.33e6, shanghai_d=spot_d(1e3 / 83.33e6), shanghai_I_Wcm2=F_hold * 83.33e6 / 1e4,
                  plan_dT_diamond=F_hold * math.pi * (50e-6) ** 2 * 1e8 / (math.pi * 50e-6 * 2000),
                  felbe_dT_diamond=20.0 / (math.pi * spot_d(20.0 / 13e6) / 2 * 2000),
                  plan_P_10x=0.1 * F_hold * math.pi * (50e-6) ** 2 * 1e8,
                  saser_max_THz=1.0, acoustic_lambda_10THz_nm=5000.0 / 10e12 * 1e9)

json.dump(R, open('/home/claude/p3/sim/pais/run3_numbers.json', 'w'), indent=1, default=float)
if __name__ == '__main__':
    for m in mats:
        print(f"{m['name']:44s} s/r {m['spec']:.3g} J/kg  v {m['v_ring']:.0f} m/s  B {m['B_thick']:.1f} T  M/GJ {m['M_per_GJ']:.3g} kg  dm/M {m['dm_over_M_tri']:.2g}")
    for k in ('gap2', 'ceiling', 'magnet', 'flywheel', 'fieldmass', 'H1', 'H2', 'rig', 'momentum', 'vacuum', 'bcs', 'drive'):
        print(k, {kk: (f'{vv:.4g}' if isinstance(vv, float) else vv) for kk, vv in R[k].items()})
    for m, d in R['weibull']['by_m'].items(): print('weibull m', m, {kk: f'{vv:.3g}' for kk, vv in d.items()})

# ============================================================== II.9  Pais Eq. 2 against capacitive ultrasound transducers (CMUTs)
E_gap, f_cm, x_cm, A_cm, t1 = 1e8, 5e6, 10e-9, 1e-4, 1.0     # gap field ~1e8 V/m (review); 5 MHz; 10 nm (assumed); 1 cm^2; 1 s
w_cm = 2 * math.pi * f_cm
sig_cm = eps0 * E_gap
S_cm = 1.0 * sig_cm ** 2 / eps0 * x_cm * w_cm ** 2 * t1        # f_G = 1 (flat)
Q_cm = sig_cm * A_cm
P_cm_known = (Q_cm * x_cm) ** 2 * w_cm ** 4 / (12 * math.pi * eps0 * c ** 3)
R['cmut'] = dict(E_gap=E_gap, f=f_cm, x0=x_cm, sigma=sig_cm, u=sig_cm ** 2 / eps0, S_eq2=S_cm, P_eq2_cm2=S_cm * A_cm,
                 P_eq2_cm2_1h=S_cm * A_cm * 3600, Q=Q_cm, P_known=P_cm_known, ratio=S_cm * A_cm / P_cm_known,
                 sigma_over_rig=sig_cm / R['rig']['sigma_face'])
json.dump(R, open('/home/claude/p3/sim/pais/run3_numbers.json', 'w'), indent=1, default=float)
print('cmut', {k: f'{v:.4g}' for k, v in R['cmut'].items()})

# ============================================================== I.10  strain-matched reinforcement around REBCO (band strain = winding strain)
eps_irr = 0.0063                                           # coil test reversible to 0.63 % hoop strain (JCSJ 2011, coil A)
bands = [('Hastelloy C-276', 220e9, 8890), ('T1000G hoop, Vf 0.6', 0.6 * 294e9, 1560), ('M55J high-modulus hoop, Vf 0.6', 0.6 * 540e9, 1640),
         ('CNT-bundle composite, Vf 0.6', 0.6 * 1.0e12, 1260)]
R['strain'] = dict(eps=eps_irr, bands=[dict(name=n, E=E, rho=rho, sigma=E * eps_irr, B_thick=math.sqrt(2 * mu0 * E * eps_irr),
                                            M_per_GJ=rho * 1e9 / (E * eps_irr)) for n, E, rho in bands])
json.dump(R, open('/home/claude/p3/sim/pais/run3_numbers.json', 'w'), indent=1, default=float)
for b in R['strain']['bands']: print('strain', b['name'], f"{b['sigma']/1e9:.2f} GPa {b['B_thick']:.0f} T {b['M_per_GJ']:.0f} kg/GJ")

# ============================================================== V.3 addendum: re-drive before the state decays (rep rate = 1/lifetime)
E_plan = R['drive']['plan_E']
for tag, tau in (('100K', 10e-9), ('300K', 0.5e-9)):
    f = 1 / tau; P = E_plan * f
    R['drive'][f'rep_{tag}'] = f; R['drive'][f'P_{tag}'] = P
    R['drive'][f'dT_{tag}'] = P / (math.pi * 50e-6 * 2000); R['drive'][f'P_{tag}_10x'] = P / 10
    R['drive'][f'dT_{tag}_10x'] = P / 10 / (math.pi * 50e-6 * 2000)
json.dump(R, open('/home/claude/p3/sim/pais/run3_numbers.json', 'w'), indent=1, default=float)
print('redrive', {k: f'{v:.3g}' for k, v in R['drive'].items() if k.startswith(('rep_', 'P_', 'dT_'))})
