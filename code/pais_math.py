"""Pais patents, worked forward with known physics and backward from the claims.  Every number used on the CT-11..CT-17
sheets is computed here and written to pais_numbers.json.  SI units throughout."""
import math, json
import numpy as np

# ---------------------------------------------------------------- constants (CODATA 2018)
c = 299792458.0; eps0 = 8.8541878128e-12; mu0 = 1.25663706212e-6; G = 6.67430e-11
hbar = 1.054571817e-34; h = 6.62607015e-34; e = 1.602176634e-19; me = 9.1093837015e-31; kB = 1.380649e-23
kB_eV = 8.617333262e-5; alpha = 7.2973525693e-3; phi0 = h / (2 * e)
E_S = me ** 2 * c ** 3 / (e * hbar)                 # Schwinger field, V/m
B_Q = me ** 2 * c ** 2 / (e * hbar)                 # QED critical magnetic field, T
I_S = 0.5 * c * eps0 * E_S ** 2                     # flux carried by a field at E_S, W/m^2
YEAR = 3.15576e7
N = {}

def S_pais(fG, sigma, v): return fG * sigma ** 2 / eps0 * v          # Pais Eq. 1 / 2 structure: (sigma^2/eps0) x speed
def lg(x): return math.log10(x)

# ---------------------------------------------------------------- shared limits from known physics
E_evap_W = 5.7e10                                   # field evaporation of tungsten, V/m (5.7 V/A, FIM)
sig_evap = eps0 * E_evap_W                          # largest surface charge any metal surface holds, C/m^2
sig_vac = eps0 * 1e9                                # large-area vacuum surfaces: ~1 GV/m, C/m^2
v_rim_6061 = 319.7                                  # CT-9: rim speed limit for 6061 (yield/density)
v_rim_cfrp = 1100.0                                 # best carbon-fibre rotors, order of magnitude (assumed)
v_vib_max = 0.01 * 5000.0                           # vibration velocity: 1 % strain x 5 km/s sound speed (assumed)
I_laser = 1.1e23 * 1e4                              # CoReLS record, W/m^2 (1.1e23 W/cm^2)
E_laser = math.sqrt(2 * I_laser / (c * eps0))       # its peak electric field
N['limits'] = dict(E_S=E_S, B_Q=B_Q, I_S=I_S, E_evap_W=E_evap_W, sig_evap=sig_evap, sig_vac=sig_vac,
                   v_rim_6061=v_rim_6061, v_rim_cfrp=v_rim_cfrp, v_vib_max=v_vib_max, I_laser=I_laser, E_laser=E_laser)

# ================================================================ CT-11  US 10,135,366  EM field generator
s0, R0, rpm = 50000.0, 2.0, 30000.0
w0 = rpm * 2 * math.pi / 60; v0 = R0 * w0
S_claim = S_pais(2 / 3, s0, v0)
E_claim = s0 / eps0
P_es = s0 ** 2 / (2 * eps0)                          # outward electrostatic pressure on the shell
Q0 = s0 * 4 * math.pi * R0 ** 2; U0 = Q0 ** 2 / (8 * math.pi * eps0 * R0)
t_charge_10MW = U0 / 10e6
S_phys = S_pais(2 / 3, sig_evap, v_rim_6061)         # Eq. 1 with the evaporation-limited charge and a 6061 rim
S_phys_cf = S_pais(2 / 3, sig_evap, v_rim_cfrp)
S_vib_claim_lo, S_vib_claim_hi = 1e24, 1e28
# asteroid (Eq. 3)
M_A, M_KI, u_KI = 1e10, 1e4, 1e4
dv_KI = M_KI * u_KI / (M_A + M_KI)                  # Pais prints 0.001 m/s
V_sys = 1e3
dv_EM_claim = (S_claim / c ** 2) * V_sys / M_A      # Pais: (S/c^2) x volume -> 1 m/s
p_photon_year = 10e6 / c * YEAR                     # 10 MW of light absorbed for a year
dv_photon_year = p_photon_year / M_A
Cm = 45e-6                                          # laser ablation, N per absorbed W (Brashears/Lubin 2015, lower limit)
wallplug = 0.35                                     # electrical -> optical (assumed)
F_abl = 10e6 * wallplug * Cm
dv_abl_year = F_abl * YEAR / M_A
N['ct11'] = dict(S_claim=S_claim, v_rim=v0, w=w0, E_surface=E_claim, E_over_ES=E_claim / E_S, P_electrostatic=P_es,
                 Q=Q0, U=U0, U_Mt=U0 / 4.184e15, t_charge_10MW_yr=t_charge_10MW / YEAR,
                 S_phys_6061=S_phys, S_phys_cfrp=S_phys_cf, gap_S_orders=lg(S_claim / S_phys_cf),
                 sigma_gap_orders=lg(s0 / sig_evap), rim_over_6061=v0 / v_rim_6061, rim_over_cfrp=v0 / v_rim_cfrp,
                 P_es_over_6061=P_es / 276e6, dv_KI=dv_KI, dv_KI_pais=0.001, dv_EM_claim=dv_EM_claim,
                 dv_photon_year=dv_photon_year, F_ablation=F_abl, dv_ablation_year=dv_abl_year,
                 years_to_1ms_ablation=1.0 / dv_abl_year)

# ================================================================ CT-12  US 10,144,532  craft
S33 = 1e33
bracket_needed = S33 * eps0 / 1.0 ** 2              # Eq. 2 with sigma = 1 C/m^2: [R_v nu^2 t_op] (a speed)
E_sig1 = 1.0 / eps0
def schwinger_rate(E):                              # pairs per m^3 per s, first term of the series (log10)
    pref = (e * E) ** 2 / (4 * math.pi ** 3 * hbar ** 2 * c)
    return lg(pref) - math.pi * E_S / E / math.log(10)
rate_sig1 = schwinger_rate(E_sig1); rate_sig50k = schwinger_rate(s0 / eps0); rate_laser = schwinger_rate(E_laser)
rate_ES = schwinger_rate(E_S)
sigma_for_ES = eps0 * E_S
# Eq. 3: 2 gamma (dm/dt) c^2 = S A  with S = 1e33, A = 100 m^2
A_craft = 100.0
dmdt = S33 * A_craft / (2 * c ** 2)
# Eq. 4: S/c = hbar nu^4 / (8 pi^2 c^3) with S/c ~ eps0 E_S^2
u_ES = eps0 * E_S ** 2
nu_cut = (u_ES * 8 * math.pi ** 2 * c ** 3 / hbar) ** 0.25          # rad/s
f_cut = nu_cut / (2 * math.pi); f_compton = me * c ** 2 / h
rho_DE = 5.3e-10                                    # J/m^3, measured dark-energy density (Planck 2018, ~0.69 of critical)
# inertial / gravitational mass cancellation with p = -u (needs Mc^2/2 of it)
M_craft = 43.3 * 2700.0                             # solid 6061 TSC-Δ (10 m side, 1 m thick)
E_cancel = M_craft * c ** 2 / 2
u_field_sig1 = 1.0 ** 2 / (2 * eps0); E_field_sig1 = u_field_sig1 * A_craft * 1.0
world_energy_yr = 6.2e20                            # J per year, world primary energy (approx.)
N['ct12'] = dict(bracket_needed=bracket_needed, bracket_over_c=bracket_needed / c, E_sigma1=E_sig1, E_sigma1_over_ES=E_sig1 / E_S,
                 log_rate_sigma1=rate_sig1, log_rate_sigma50k=rate_sig50k, log_rate_laser=rate_laser, log_rate_ES=rate_ES,
                 sigma_for_ES=sigma_for_ES, dmdt_pairs=dmdt, nu_cut=nu_cut, f_cut=f_cut, f_compton=f_compton,
                 f_cut_over_compton=f_cut / f_compton, pais_f_cut=1e22, rho_DE=rho_DE, pais_vac=1e-15 * 1e6,
                 M_craft=M_craft, E_cancel=E_cancel, E_cancel_world_years=E_cancel / world_energy_yr,
                 E_field_sigma1=E_field_sig1, cancel_gap_orders=lg(E_cancel / E_field_sig1),
                 hayasaka_claim=6.8e-5, quinn_picard=2e-7, faller=9e-7, hayasaka_gap_orders=lg(6.8e-5 / 2e-7))

# ================================================================ CT-13  US 10,322,827  HFGW
K_JASON = 4 * math.pi * G / c ** 4                  # as printed in the patent (no 1/mu0)
K_SI = K_JASON / mu0                                # SI conversion fraction per (T m)^2  (4 pi G B^2 L^2 / mu0 c^4)
B0, L0, A0 = 1e10, 1.0, 1.0
P_in = S33 * A0
P_pais = K_JASON * B0 ** 2 * L0 ** 2 * P_in
P_SI = K_SI * B0 ** 2 * L0 ** 2 * P_in
f_grav = P_pais / 1e35 / h                          # frequency implied by 1e35 gravitons/s at 1e10 W
P_lab_pulse = K_SI * 45.0 ** 2 * 10.0 ** 2 * 1e15   # 45 T over 10 m, 1 PW laser pulse
P_lab_cw = K_SI * 45.0 ** 2 * 10.0 ** 2 * 1e6       # 45 T over 10 m, 1 MW microwave
BL_for_1MW = math.sqrt(1e6 / (K_SI * 1e15))
BL_lab = 45.0 * 10.0; BL_magnetar = 1e10 * 1e4
conv_magnetar = K_SI * BL_magnetar ** 2
def strain(P, r, f):
    F = P / (4 * math.pi * r ** 2); w = 2 * math.pi * f
    return math.sqrt(16 * math.pi * G * F / (c ** 3 * w ** 2))
h_pais_1m = strain(P_pais, 1.0, f_grav)
P_h1 = 4 * math.pi * 1.0 ** 2 * c ** 3 * (2 * math.pi * f_grav) ** 2 / (16 * math.pi * G)   # power for h ~ 1 at 1 m
L_GW150914 = 3.6e49
E_bind_earth = 0.6 * G * 5.972e24 ** 2 / 6.371e6
t_planet = E_bind_earth / P_pais / YEAR
N['ct13'] = dict(K_JASON=K_JASON, K_SI=K_SI, P_pais=P_pais, P_SI=P_SI, f_grav=f_grav, P_lab_pulse=P_lab_pulse,
                 P_lab_cw=P_lab_cw, BL_for_1MW=BL_for_1MW, BL_lab=BL_lab, BL_magnetar=BL_magnetar,
                 conv_magnetar=conv_magnetar, h_pais_1m=h_pais_1m, P_h1=P_h1, L_GW150914=L_GW150914,
                 E_bind_earth=E_bind_earth, t_planet_yr=t_planet, age_universe_yr=1.38e10,
                 gap_lab_orders=lg(P_pais / P_lab_pulse), gap_singularity_orders=lg(P_h1 / P_pais),
                 B0_over_BQ=B0 / B_Q, S33_over_IS=S33 / I_S)

# ================================================================ CT-14  US 2019/0295733  fusion
R_d = 0.05; A_face = math.pi * R_d ** 2
sig_1C = 1.0 / (2 * A_face)                         # 1 C on both faces of a 10 cm disk
def B_disk(sig, w, R): return mu0 * sig * w * R / 2   # centre field of a spinning charged disk
B_1C = B_disk(sig_1C, 1e4, R_d); B_evap = B_disk(sig_evap, 1e4, R_d); B_vac = B_disk(sig_vac, 1e4, R_d)
t_op_for_1e6 = math.sqrt(1e6 / (mu0 * sig_1C * R_d * 1e4 ** 3))      # what Eq. 10 needs to print 1e6 T
B_sparc = 12.2; B_rebco = 20.0
N['ct14'] = dict(sigma_1C=sig_1C, E_1C=sig_1C / eps0, E_1C_over_evap=sig_1C / eps0 / E_evap_W, B_1C=B_1C, B_evap=B_evap,
                 B_vac=B_vac, B_claim=1e6, t_op_for_1e6=t_op_for_1e6, gap_orders=lg(1e6 / B_vac),
                 gap_orders_1C=lg(1e6 / B_1C), B_rebco=B_rebco, B_sparc=B_sparc, gain_B3=1e6 ** 3,
                 Pf_ratio_vac=(B_vac / B_sparc) ** 4, lawson_DT=3e21)

# ================================================================ CT-15  US 2019/0058105 + 2019/0348597  superconductors
n_s = 1e20 * 1e6
lamL = math.sqrt(me / (mu0 * n_s * e ** 2))
alpha_pais = e / (phi0 * eps0 * c)
f_kT = kB * 300 / h
f_gap = 2 * 1.764 * kB * 300 / h                    # BCS 2Δ/h for Tc = 300 K
f_pzt = 1e8
N['ct15'] = dict(lambda_L=lamL, alpha_pais=alpha_pais, alpha=alpha, alpha_ratio=alpha_pais / alpha, f_kT=f_kT, f_gap=f_gap,
                 f_pzt=f_pzt, gap_orders=lg(f_gap / f_pzt), hw_over_kT_pzt=h * f_pzt / (kB * 300),
                 E_gap_meV=1.764 * kB_eV * 300 * 1e3, pais_emitters=1e14)

# ================================================================ CT-16  US 7,080,504  laser-augmented turbojet (Northrop, 2006)
fuel = 2.0 * 43e6                                   # 2 kg/s of jet fuel, W (assumed engine)
eta_gen, eta_laser, eta_th = 0.95, 0.35, 0.35       # generator, laser wall-plug, cycle (assumed)
round_trip = eta_gen * eta_laser * eta_th
N['ct16'] = dict(fuel_power=fuel, round_trip=round_trip, loss_per_MW=1 - round_trip,
                 headroom_cruise=fuel * 0.001, headroom_altitude=fuel * 0.05)

json.dump(N, open('/home/claude/p3/sim/pais/pais_numbers.json', 'w'), indent=1)
if __name__ == '__main__':
    for k, v in N.items():
        print('==', k)
        for kk, vv in v.items(): print(f'   {kk:24s} {vv:.4g}' if isinstance(vv, float) else f'   {kk:24s} {vv}')
