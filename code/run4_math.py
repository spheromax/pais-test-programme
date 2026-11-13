"""Run 4 of the Pais gap loop: numbers for run-sheet items I.11-I.14, III.4, V.6, V.7 and sheets CT-24..CT-29.
SI units.  Inputs marked (assumed) are not from a measurement.  Writes run4_numbers.json."""
import math, json
c = 299792458.0; eps0 = 8.8541878128e-12; e = 1.602176634e-19; me = 9.1093837015e-31; amu = 1.66053906660e-27
h = 6.62607015e-34; Phi0 = h / (2 * e); G = 6.67430e-11; mu0 = 1.25663706212e-6
R = {}

# ---------------------------------------------------------------- I.11  the fibre ladder at buildable length (gap 2)
v_req = 2.0 * 30000 * 2 * math.pi / 60; spec_req = v_req ** 2           # 2 m radius, 30,000 rpm
fibres = [  # name, sigma/rho (J/kg = 1e-6 N/tex), gauge class, source key
    ('CNT yarn, commercial, 110 mm gauge', 0.911e6, '0.1 m', 'dessureault'),
    ('CNT yarn, continuous 150-500 m', 1.77e6, 'km-class yarn', 'liang23'),
    ('Kevlar 49', 3620e6 / 1440, 'metre', 'wiki'),
    ('Dyneema (UHMWPE)', 3600e6 / 970, 'metre', 'wiki'),
    ('Zylon (PBO)', 5800e6 / 1540, 'metre', 'wiki'),
    ('carbon fibre T1100G', 7000e6 / 1790, 'metre', 'wiki'),
    ('CNT bundle, ultralong (2 cm gauge)', 80e9 / 1300, '2 cm', 'bai'),
    ('graphene, ideal', 130e9 / 2200, 'nm', 'lee')]
R['fibres'] = [dict(name=n, spec=s, Ntex=s / 1e6, v=math.sqrt(s), gauge=g, src=src, short=spec_req / s) for n, s, g, src in fibres]
R['gap2'] = dict(v_req=v_req, spec_req=spec_req, Ntex_req=spec_req / 1e6, best_metre=7000e6 / 1790,
                 factor_spec=spec_req / (7000e6 / 1790), factor_speed=math.sqrt(spec_req / (7000e6 / 1790)),
                 cnt_yarn_short=(spec_req / 1.77e6, spec_req / 0.911e6))
def sig_f_needed(Vf, rho_f, rho_m=1200.0): return spec_req * (Vf * rho_f + (1 - Vf) * rho_m) / Vf
R['dilution'] = dict(cnt_Vf06_GPa=sig_f_needed(0.6, 1300) / 1e9, cnt_ratio=sig_f_needed(0.6, 1300) / 80e9,
                     graphene_Vf06_GPa=sig_f_needed(0.6, 2200) / 1e9, graphene_ratio=sig_f_needed(0.6, 2200) / 130e9)

# ---------------------------------------------------------------- I.12  Weibull: specimens, two-gauge estimator, m from scatter
k = math.sqrt(6) / math.pi                                               # sd(m_hat) = k m / sqrt(N)
def n_needed(m, dm, z=2.0): return (z * k * m / dm) ** 2
def cov(m): return math.sqrt(math.gamma(1 + 2 / m) / math.gamma(1 + 1 / m) ** 2 - 1)
def m_from_cov(cv, lo=1.0, hi=200.0):
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if cov(mid) > cv else (lo, mid)
    return 0.5 * (lo + hi)
R['weibull'] = dict(k=k, N_m10=n_needed(10, 4.5), N_m145=n_needed(14.5, 4.5), ratio_decade_m10=10 ** 0.1, ratio_decade_m145=10 ** (1 / 14.5),
                    m_dessureault=m_from_cov(0.137 / 0.911), cov_dessureault=0.137 / 0.911,
                    m_liang23=m_from_cov(0.07 / 1.77), cov_liang23=0.07 / 1.77,
                    cov_table={m: cov(m) for m in (3, 5, 8, 10, 14.5, 20, 30)})

# ---------------------------------------------------------------- I.13  shear lag: interface strength for a given ineffective length
def tau_needed(sig_f, d, delta): return sig_f * d / (2 * delta)          # delta = Kelly-Tyson critical length sig_f d / 2 tau
R['shearlag'] = dict(tau_d1um=tau_needed(80e9, 1e-6, 1e-4), tau_d100nm=tau_needed(80e9, 100e-9, 1e-4),
                     tau_d10nm=tau_needed(80e9, 10e-9, 1e-4),
                     delta_d1um_tau50=80e9 * 1e-6 / (2 * 50e6), delta_d100nm_tau50=80e9 * 100e-9 / (2 * 50e6))

# ---------------------------------------------------------------- I.14  cooldown: contraction mismatch of bands on REBCO (B1, K2)
s_tape = 0.26e-2; s_ss = 0.30e-2; s_cf = 0.0                             # shrinkage RT->4.2 K (tape pack: run-4 search; SS 304: Ekin; CF ~0)
E_tape = 150e9; E_cf = 0.6 * 540e9; E_ss = 193e9; eps_irr = 0.63e-2       # E_tape assumed (130-170 GPa); M55J hoop at Vf 0.6
def bonded(E1, s1, E2, s2, a2=1.0):                                      # tape strain (+ tension) when bonded to an equal-area (x a2) layer
    k1, k2 = E1, E2 * a2
    return k2 * (s1 - s2) / (k1 + k2)
eps_cf = bonded(E_tape, s_tape, E_cf, s_cf); eps_ss = bonded(E_tape, s_tape, E_ss, s_ss)
eps_c = 0.2e-2                                                           # compressive pre-strain allowed (assumed, low end)
R['cte'] = dict(s_tape=s_tape, s_ss=s_ss, s_cf=s_cf, mismatch_cf=s_tape - s_cf, prestress_cf_MPa=E_cf * (s_tape - s_cf) / 1e6,
                cowind_cf=eps_cf, cowind_cf_window=eps_cf / eps_irr, cowind_ss=eps_ss,
                band_t_over_R=0.05, p_rt_MPa=E_cf * (s_tape - s_cf) * 0.05 / 1e6,
                eps_c=eps_c, strain_gain=(eps_irr + eps_c) / eps_irr, B_gain=math.sqrt((eps_irr + eps_c) / eps_irr),
                B_hast=math.sqrt(2 * mu0 * 220e9 * eps_irr), B_hast_pre=math.sqrt(2 * mu0 * 220e9 * (eps_irr + eps_c)))

# ---------------------------------------------------------------- III.4  thrust per watt ladder (Biefeld-Brown)
mu_air = 2.0e-4; V = 30e3; d = 0.03; I = 1e-3                            # ion mobility in air; lifter-like geometry (assumed)
def v_ion(m_kg, V): return math.sqrt(2 * e * V / m_kg)
gam = 1 + e * V / (me * c ** 2); beta = math.sqrt(1 - 1 / gam ** 2)
R['thrust'] = dict(F_air=I * d / mu_air, FP_air=d / (mu_air * V), FP_H=2 / v_ion(1.00728 * amu, V), FP_Xe=2 / v_ion(131.29 * amu, V),
                   FP_Cu=2 / v_ion(63.546 * amu, V), FP_e=gam * beta / ((gam - 1) * c), FP_light=1 / c, claim_FP=1e-4)

# ---------------------------------------------------------------- V.6  what field enhancement buys (B5)
F_flu, tau_p = 4.0, 1e-12                                                # 400 uJ/cm^2 (Rowe); 1 ps (assumed)
I_pk = F_flu / tau_p; E_pk = math.sqrt(2 * I_pk / (c * eps0))
def frac(gap, arm, cell): return gap * arm / cell ** 2
f_srr = (frac(2.2e-6, 4e-6, 50e-6), frac(2.2e-6, 10e-6, 50e-6))           # SRR gap x arm width in a 50 um cell (assumed geometry)
cases = [('SRR, broadband pulse (time domain)', 4.0, f_srr), ('SRR on resonance', 15.0, f_srr),
         ('narrow-gap SRR (1 um)', 20.0, (frac(1e-6, 4e-6, 50e-6), frac(1e-6, 10e-6, 50e-6))),
         ('dipole gap, mid-gap 60', 60.0, (1e-6 * 5e-6 / (170e-6 * 100e-6),) * 2)]     # 1 um x 5 um gap, 170 x 100 um period (assumed)
R['b5'] = dict(E_pk_MVcm=E_pk / 1e8, F_needed=math.sqrt(10.0), E_inc_needed_MVcm=E_pk / math.sqrt(10.0) / 1e8,
               ladder_MVcm={'needed (hold field)': E_pk / 1e8, 'GaAs impact ionization': 0.64, 'electromigration damage seen': 2.0,
                            'narrow-gap SRR reached': 3.5, 'field emission': 10.0},
               cases=[dict(name=n, F=F, f_lo=min(fs), f_hi=max(fs), G_lo=min(fs) * F ** 2, G_hi=max(fs) * F ** 2) for n, F, fs in cases],
               dipole_edge_G=(1e-7 * 5e-6 * 2) / (170e-6 * 100e-6) * 170 ** 2)

# ---------------------------------------------------------------- V.7  London moment and the Tate anomaly
kL = 2 * me / e
B1000 = kL * 1e3; A = math.pi * 0.01 ** 2
Bg_req = 2 * (1.000084 - 0.999992)                                        # B_g = 2 omega (dm/m), per rad/s
Bg_classical = 4 * math.pi * G / c ** 2 * 8570 * 0.01 ** 2 / 2            # long rotating Nb cylinder, r = 1 cm (GEM order of magnitude)
R['london'] = dict(kL=kL, B_1000=B1000, dB_92ppm=B1000 * 92e-6, w_per_flux_quantum=Phi0 / A / kL, flux_quanta_1000=B1000 * A / Phi0,
                   tate=1.000084, tate_sigma=21e-6, theory=0.999992, excess_ppm=(1.000084 - 0.999992) * 1e6,
                   n_sigma=(1.000084 - 0.999992) / 21e-6, cabrera_tate_avg=1.000075, cabrera_tate_sigma=25e-6,
                   Bg_required=Bg_req, Bg_classical=Bg_classical, Bg_ratio=Bg_req / Bg_classical, claimant_model_factor=23,
                   craft_band_300rads_nT=kL * 300 * 1e9)

# ---------------------------------------------------------------- gap 3 re-check (E-320 tracker preprint, Apr 2026)
R['e320'] = dict(proxy_rate=0.120, proxy_stat=0.006, proxy_syst=0.056, nbw_expected=(0.01, 0.1))
json.dump(R, open('/home/claude/p3/sim/pais/run4_numbers.json', 'w'), indent=1, default=float)

if __name__ == '__main__':
    for f in R['fibres']: print(f"{f['name']:36s} {f['Ntex']:7.3f} N/tex  v {f['v']:5.0f} m/s  short x{f['short']:.3g}")
    for key in ('gap2', 'dilution', 'weibull', 'shearlag', 'cte', 'thrust', 'b5', 'london', 'e320'):
        val = R[key]
        print(key, {kk: (f'{vv:.4g}' if isinstance(vv, float) else vv) for kk, vv in val.items()})
