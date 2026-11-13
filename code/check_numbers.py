# Independent re-derivation of the sheet numbers with scipy.constants (CODATA), compared with pais_numbers.json
import json, math, scipy.constants as k
N = json.load(open('/home/claude/p3/sim/pais/pais_numbers.json'))
c, e, me, hb, h, e0, m0, G, kB = k.c, k.e, k.m_e, k.hbar, k.h, k.epsilon_0, k.mu_0, k.G, k.k
yr = 365.25 * 86400
ES = me**2 * c**3 / (e * hb); BQ = me**2 * c**2 / (e * hb); IS = 0.5 * c * e0 * ES**2
sev = e0 * 5.7e10
w = 30000 * 2 * math.pi / 60; S = (2/3) * 5e4**2 / e0 * 2 * w
Q = 5e4 * 4 * math.pi * 4; U = Q**2 / (8 * math.pi * e0 * 2)
Kj = 4 * math.pi * G / c**4; Ks = Kj / m0; Pp = Kj * 1e20 * 1e33; fg = Pp / 1e35 / h
wg = 2 * math.pi * fg; hs = math.sqrt(16 * math.pi * G * (Pp / (4 * math.pi)) / (c**3 * wg**2))
s1 = 1 / (2 * math.pi * 0.05**2)
chk = {
 ('limits', 'E_S'): ES, ('limits', 'B_Q'): BQ, ('limits', 'I_S'): IS, ('limits', 'sig_evap'): sev,
 ('ct11', 'S_claim'): S, ('ct11', 'E_surface'): 5e4 / e0, ('ct11', 'P_electrostatic'): 5e4**2 / (2 * e0), ('ct11', 'U'): U,
 ('ct11', 't_charge_10MW_yr'): U / 1e7 / yr, ('ct11', 'S_phys_cfrp'): (2/3) * sev**2 / e0 * 1100,
 ('ct11', 'dv_KI'): 1e4 * 1e4 / (1e10 + 1e4), ('ct11', 'dv_EM_claim'): S / c**2 * 1e3 / 1e10,
 ('ct11', 'dv_photon_year'): 1e7 / c * yr / 1e10, ('ct11', 'dv_ablation_year'): 1e7 * 0.35 * 45e-6 * yr / 1e10,
 ('ct12', 'bracket_needed'): 1e33 * e0, ('ct12', 'E_sigma1'): 1 / e0, ('ct12', 'sigma_for_ES'): e0 * ES,
 ('ct12', 'dmdt_pairs'): 1e33 * 100 / (2 * c**2), ('ct12', 'nu_cut'): (8 * math.pi**2 * c**3 * e0 * ES**2 / hb) ** 0.25,
 ('ct12', 'E_cancel'): 43.3 * 2700 * c**2 / 2, ('ct12', 'log_rate_sigma1'): math.log10((e / e0)**2 / (4 * math.pi**3 * hb**2 * c)) - math.pi * ES * e0 / math.log(10),
 ('ct13', 'K_SI'): Ks, ('ct13', 'P_pais'): Pp, ('ct13', 'f_grav'): fg, ('ct13', 'P_lab_pulse'): Ks * 45**2 * 10**2 * 1e15,
 ('ct13', 'BL_for_1MW'): math.sqrt(1e6 / (Ks * 1e15)), ('ct13', 'h_pais_1m'): hs, ('ct13', 'P_h1'): c**3 * wg**2 / (4 * G),
 ('ct13', 'E_bind_earth'): 0.6 * G * 5.972e24**2 / 6.371e6,
 ('ct14', 'sigma_1C'): s1, ('ct14', 'B_1C'): m0 * s1 * 1e4 * 0.05 / 2, ('ct14', 'B_vac'): m0 * e0 * 1e9 * 1e4 * 0.05 / 2,
 ('ct14', 't_op_for_1e6'): math.sqrt(1e6 / (m0 * s1 * 0.05 * 1e12)),
 ('ct15', 'lambda_L'): math.sqrt(me / (m0 * 1e26 * e**2)), ('ct15', 'alpha_pais'): e / ((h / (2 * e)) * e0 * c),
 ('ct15', 'f_kT'): kB * 300 / h, ('ct15', 'hw_over_kT_pzt'): h * 1e8 / (kB * 300),
}
worst = 0
for (s, key), v in chk.items():
    r = abs(v / N[s][key] - 1); worst = max(worst, r)
    flag = '' if r < 2e-3 else '   <-- CHECK'
    print(f'{s:6s} {key:22s} json {N[s][key]: .4e}  indep {v: .4e}  rel {r:.1e}{flag}')
print('items', len(chk), 'worst relative deviation', f'{worst:.1e}')
