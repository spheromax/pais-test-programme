"""Run 11 of the Pais gap loop: the few numbers behind the run-11 notes in run-sheet part 8.  Run: python3 run11_math.py"""
import json, math
R, v = 2.0, 2000 * math.pi
out = {}
# I.34 note: entry angle from a gap g (rotor at R, wall at R + g, as I.30) and the gouging thresholds
out['entry_angle_deg'] = {f'{g} mm': math.degrees(math.asin(math.sqrt(1 - (R / (R + g * 1e-3))**2))) for g in (1, 5, 20)}
out['fsp_pitch_yaw_deg'] = {'end-on (two FSP types)': [4.7, 5.5], 'side-on (two FSP types)': [32.0, 43.0]}   # LANL/STAR LGG platform (OSTI 2004149)
out['gouge_threshold_kms'] = {'rocket-sled rails': 1.5, 'gun barrels': 4.0, 'Holloman example': 1.74}
out['b6_over_gouge'] = {k: v / 1e3 / t for k, t in out['gouge_threshold_kms'].items()}
# I.33 note: cyclotron first-harmonic tolerances as a fraction of the field
cyc = {'Kolkata (2-3 G first harmonic disturbs the beam)': [0.2, 0.3], 'RIKEN SRC (trim coils leave < 15 G)': [1.5, 1.5],
       'CYCIAE-230 (0.24 G per mm of trim-rod error)': [0.024, 0.024]}
out['cyclotron_first_harmonic_mT'] = cyc                         # absolute, compare with B6's 0.17-2.3 mT at n = 1 (I.33)
out['b6_allowed_n1_mT'] = [0.17, 2.31]
out['ubsc'] = dict(quench_A=250, design_A=540, Ic_A=700, frac_design=250 / 540, frac_Ic=250 / 700, design_T=1.6, T_op_K=30)
# III.10 note: a resonant detector's force resolution, F = m_eff * w^2 * x / Q  (ETH: 42 Hz, Q ~ 1e4, ~1 pm; m_eff assumed 1-4 kg)
w = 2 * math.pi * 42.0
out['eth_force_N'] = {f'm_eff {m} kg': m * w**2 * 1e-12 / 1e4 for m in (1.0, 4.0)}
out['eth_vs_dresden'] = {k: 1e-9 / f for k, f in out['eth_force_N'].items()}
json.dump(out, open('/home/claude/p3/sim/pais/run11_numbers.json', 'w'), indent=1)
for k, d in out.items(): print(k, {kk: (round(x, 4) if isinstance(x, float) else x) for kk, x in d.items()} if isinstance(d, dict) else d)
