# Pais gap research loop: state file (v12, after run 11: the loop stopped)

This file is the loop's memory. Prompts A, B and C load it at the start of a run, and Prompt C rewrites it at the end, so every run starts from what the last one learned.

- **Doc:** the readable write-up, with tables, the loop diagram, runs 1–11 and sheets CT-18 to CT-67; test plans: claude/pais_test_plans.md: https://claude.ai/artifact/FNM8P9V7vfkH6ijMxCserz
- **Other files:**
  - Prompts A, B and C, with the changelog: claude/pais_loop_prompts.md.
  - Every search, with its kind, title and URL: claude/pais_search_log.md (runs 1–6), claude/pais_search_log_2.md (run 7), claude/pais_search_log_3.md (run 8), claude/pais_search_log_4.md (run 9) and claude/pais_search_log_5.md (runs 10–11).
  - Upstream numbers: claude/pais_portfolio_forward_backward.md (sheets CT-11 to CT-17).
- **Maths run sheet** (LaTeX, grows every run):
  - claude/pais_math_runsheet.tex: front matter, chains I–II.
  - claude/pais_math_runsheet_part2.tex: chains III–V, standalone items, paths table, changelog.
  - claude/pais_math_runsheet_part3.tex: run-4 and run-5 items.
  - claude/pais_math_runsheet_part4.tex: run-6 items.
  - claude/pais_math_runsheet_part5.tex: run-7 items.
  - claude/pais_math_runsheet_part6.tex: run-8 items.
  - claude/pais_math_runsheet_part7.tex: run-9 items.
  - claude/pais_math_runsheet_part8.tex: run-10 items and run-11 notes.
  - claude/pais_math_runsheet_refs.tex: references.
  - To build, put all nine in one folder and run `pdflatex pais_math_runsheet.tex` twice (40 pages). New items go into a part 9 once part 8 passes ~30 KB (it is 17 KB).
- **Health test** (step 0 of Prompt A): claude/pais_loop_health.py. Copy it to a .py file, add the last run's queries from the search log and run `python3 pais_loop_health.py <run>`.

**The loop stopped after run 11 by its own rule** (every gap settled; run 11 moved nothing). Restart it with "Run the Pais gap loop" only after a restart trigger (last section); that runs Prompt A v12, then B, then C.

## Certain ledger (change an entry only if a new measurement overturns it)

1. Pais's flux formula S = f_G (σ²/ε₀) × speed is dimensionally right and reproduces his numbers (1.18×10²⁴ W/m² from the '366 inputs: σ 5×10⁴ C/m², R 2 m, 30,000 rpm, f_G 2/3).
2. It is not radiated power. A steadily spinning or uniformly breathing charged shell radiates 0 W; only a changing dipole or higher moment radiates.
3. His speed term is acceleration × time and grows without limit. A real oscillation peaks at R_v ω. For the run-2 rig at t_op = 1 s the "speed" is 105 c.
4. 5×10⁴ C/m² is about 2×10⁴ electron charges per surface atom. Its field, 5.6×10¹⁵ V/m, is 10⁴ × the atomic field of 5.14×10¹¹ V/m. Surfaces field-evaporate near 5.7×10¹⁰ V/m.
5. 10⁶ T carries a magnetic pressure of 4×10¹⁷ Pa, 1.35×10⁴ × the atomic unit of pressure (2.94×10¹³ Pa). Matter-made fields top out at 1,200 T indoors (100 µs, 2018) and 2,800 T with explosives (2001).
6. Vacuum pair production needs the Schwinger field, 1.32×10¹⁸ V/m.
7. EM-to-GW conversion is 4πG B²L²/(μ₀c⁴) = 8.26×10⁻³⁸ per (T·m)².
8. Earth's binding energy is 2.24×10³² J; at Pais's 1.04×10¹⁰ W, unbinding Earth takes 6.8×10¹⁴ years.
9. Kinetic impactor: the '366 inputs give 0.010 m/s, not the 0.001 it prints. DART measured β = 3.61 and Δv = 2.70 mm/s (Nature, 2023).
10. Fusion power density scales as B⁴. Compact fusion needs ~20 T on the coil; REBCO reached 20 T in 2021 and 35.6 T all-superconducting in January 2026.
11. A 100 MHz vibration has ħω/kT = 1.6×10⁻⁵ at 300 K. Pairing at 300 K needs ~22 THz (BCS: 2Δ = 3.528 k_B T_c).
12. Gyroscope weight loss: claimed 6.8×10⁻⁵, refuted to below 2×10⁻⁷ (1990).
13. EmDrive-type resonant-cavity thrust is refuted by at least 10³ (Tajmar et al., 2021).
14. NAWCAD tested the Pais Effect from 2016 to 2019 for about $0.5 M and could not prove it. Its rig spun but never vibrated.
15. Vibrating piezo-stack (Mach-effect) thrusters produce vibration artefacts, not thrust (Tajmar et al., 2021).
16. **Virial bound (run 3; scope corrected in run 5).** A closed system holding field energy U and kinetic energy T carries ∫Tr σ dV = 2T + U of net tension in all its matter together. So its structure has mass ≥ ρ(2T + U)/σ; energy per structural kilogram is ≤ σ/ρ ≤ 5.9×10⁷ J/kg (graphene's ideal strength); a rim that carries itself is ≤ 7.7 km/s; and a field or spin changes inertia by Δm/M ≤ 3σ/(ρc²) ≤ 2×10⁻⁹, always upward. A rotor held by a magnetic stator can exceed its own σ/ρ when the stator carries the load (I.2–I.7, I.17).
17. **No self-push (run 3).** A closed static system has zero total momentum (centre-of-energy theorem); thrust without propellant is at most P/c = 3.34 nN/W. TU Dresden's balances bound EMDrive and laser-resonator thrust below photon pressure for equal power. (III.1–III.2)
18. **Spinning-superconductor gravity (run 3).** The Podkletnov (1992) and Tajmar (2006) anomalies have not been seen independently in another laboratory (McCulloch 2011).
19. **Selection rule (run 3).** A charge distribution with C_n symmetry spinning at Ω radiates only at harmonics of nΩ, first from multipole l = n; an axisymmetric one radiates nothing. (II.5)
20. **Eq. 2 is falsified by existing devices (run 3).** A capacitive ultrasound transducer is a charged plate at ~10⁸ V/m vibrating at MHz. Eq. 2 predicts 8.7×10⁷ W per cm²; known physics gives 8.5×10⁻¹⁷ W; real probes draw watts. (II.8)
21. **Lifters push air (run 4).** An asymmetric-capacitor "lifter" (Biefeld–Brown) runs on ion wind, F = I d/μ, about 5 mN/W for a 3 cm gap at 30 kV in air, and gives no thrust in vacuum (Talley 1991; Tajmar 2004). In vacuum a device's thrust per watt is 2/v for what it ejects (singly charged ions at 30 kV: 0.8–9.5 µN/W), or P/c with nothing ejected. (III.4)
22. **London moment (run 4).** A superconductor rotating at ω carries B = 2m_eω/e = 1.137×10⁻¹¹ T per rad/s. Tate's pair-mass value (1989–90) is a lead (K5), not a ledger entry. (V.7)
23. **The cooldown offset is measured (run 5).** REBCO tapes from five makers soldered to a Ti-6Al-4V spring (which contracts 0.17 % to 4.2 K) sit in tension at 4.2 K and reach zero strain only after 0.144–0.152 % of compression. Free tape therefore shrinks 0.31–0.32 % (inferred, I.16). Irreversible tensile limits at 4.2 K and 19 T: 0.45–0.72 % (Barth et al., SuST 28, 045011, 2015).
24. **Nanotube length statistics (run 5).** Ultralong nanotube counts halve every 74.4 mm of growth (semiconducting tubes; Nat. Commun. 10, 4467, 2019); the longest grown is 550 mm (ACS Nano 7, 6156, 2013). One continuous tube round the 12.6 m hoop has a probability of 10⁻⁵¹ (I.15).
25. **Charge does not change weight (run 5, side research).** Conductors of about 1 kg charged from 10 V to 200 kV, in both polarities, showed no weight change within 2 g, i.e. 2×10⁻³ (Hathaway & Williams, Physics 3, 160, 2021; one measurement, B).
26. **Superconducting rings are held on feedback for hours (run 6).** LDX levitated a 560 kg superconducting coil by digital feedback (first flight Feb 2007; over 80 hours of flight by 2009); its floating coil is vertically unstable without the loop. APEX-LD holds a REBCO floating coil to σ_z < 20 µm for over three hours (arXiv 2511.07191, 2025).
27. **Zero-trace stiffness (run 6).** A rigid current loop at fixed current in a current-free field has k_x + k_y + k_z = 0 for translations, because ∇²B = 0; no field shape holds it in all three directions. Flux conservation adds (∂Φ/∂ξ)²/L ≥ 0, which is zero at symmetric positions (I.18, checked numerically to 10⁻⁵).
28. **Induced currents escape the zero trace (run 7).** Closed superconducting loops cooled at the equilibrium add GᵀL⁻¹G ≥ 0 (rank ≤ number of loops) to the stiffness, so a passive loop pair can hold the one axis fixed currents cannot (I.23; prior art: null-flux suspension 1969, superconducting loops for a levitated coil 1980).
29. **Delayed feedback (run 7).** PD feedback with delay τ holds an axis growing at γ only if γτ < √2; with peak sensitivity ≤ 2 it needs bandwidth ≥ πγ/ln 2 = 4.53γ (Bode's integral) (I.22, checked numerically).
30. **Best nanotube bundles (run 7).** Bai et al.'s 2 cm bundles (2018) reach 80 GPa on the tubes' wall area (43 GPa on the filled-tube area), i.e. 35.4 N/tex (B). A self-supported 6.3 km/s rim needs 39.5 N/tex.
31. **Loss of hold (run 8).** A stator-held rotor (J_eBR = ρv²) survives a fall in its hold of only δ = σ/ρv² (0.28 % for B6, whose ρv² is 351 GPa); a fast quench of rotor or stator bursts it within 0.13–85 ms, far faster than any brake (I.25). Its stored energy is 442 MJ = 106 kg of TNT; containment: ledger 34 (run 9 replaced the 7.2 t fibre-catcher model).
32. **A quenched loop's current (run 8).** In closed superconducting loops with inductance matrix L, a loop that goes normal hands the others ΔI = I₀L_ss⁻¹L_sq and dissipates ½I₀²(L_qq − L_qs L_ss⁻¹L_sq). In B6's 44 × 25 tape stack the radial neighbour (k = 0.9955) takes 50–98 %, so the loops survive only at i ≤ 0.51 (I.25).
33. **mB = T (run 8).** For a stress-free rotor the magnetic moment times the field equals the kinetic energy (I.28).
34. **Containment inherits the virial (run 9).** Debris sliding on a wall loads it exactly as the held rotor loaded its stator; debris turned into gas of adiabatic index γ needs ∫Tr σ dV = 3(γ−1)E ≤ 2T for γ ≤ 5/3. So a containment needs no more tension than the rotor it held (I.30, proved). Debris faster than √(2e_vap) ≈ 3.9 km/s carries more than its own vaporization energy.
35. **No field expulsion in driven K₃C₆₀ (run 9).** A Faraday-rotation search at ~50 nT found none: χ_v > −0.1 (de Vecchi et al., Phys. Rev. Research 7, 043270, 2025; claimant's group, B).
36. **Radiative rotor and ripple (run 10).** A rotor cooled only by radiation (ε, area A, wall T_s) stays at or below T_m only if the azimuthal ripple at harmonic n obeys ΔB ≤ B₀[εσA(T_m⁴ − T_s⁴)/nP₀]^(1/3) (P₀ = 1 W at B₀ = 6.3 mT for B6). Emissivity enters as ε^(1/3), so field quality decides: for B6, about 6–80 ppm of 30 T along 12.6 m (I.33, proved).

## Gap table after run 11 (final)

| # | Gap | Factor left | Wall | Status | Best lead (grade) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Shell charge, 5×10⁴ C/m² | 10⁵ (3×10⁴ even for bound charge) | Atoms | Settled | None |
| 2 | Rim speed, 6.3 km/s at 2 m (σ/ρ 3.95×10⁷ J/kg = 39.5 N/tex) | **Self-supported rim:** 9.0× short with T1200; continuous nanotubes impossible; best 2 cm bundles 0.90× (K1 cut).<br>**Stator-held rotor (B6):** no stress shortfall; containment 1.3–2.3× the 312 kg minimum (I.30, D). Run 10: the conditions are three measurements: stator azimuthal field within 6–80 ppm along 12.6 m (unshimmed REBCO ≥ 100 ppm; shimmed NMR/MRI ≤ 1 ppm; I.33, C); thick film at a 15–20 K wall, where flux-jump margin is 18–50× better (I.35, D); a tangential coupon shot at full wall pressure (I.34, C). Run 11: cyclotrons hold first harmonics at a few gauss (NbTi, iron); the one REBCO skeleton cyclotron quenched at 46 % of design; the coupon will gouge its track (1.6–4.2× above gouging thresholds). | Materials (self-supported); engineering (stator-held) | Open: B6 for a craft on paper (D); three measurements decide it | B6: stator field map, thick-film ramp at 15–25 K, coupon shot (C/D); tabletop ring (D) |
| 3 | Vacuum-polarizing field, 1.32×10¹⁸ V/m | 1,450× in field for a craft; invariants cannot be boosted by a craft | Vacuum | Settled for a craft; re-check about Feb 2027 | Probe particles: E-320 χ ≳ 0.5 (2025, C); single-positron tracker (Apr 2026, C) |
| 4 | Inertial mass reduction | Premise gone: Eq. 2 fails by 10²⁴; field or spin mass is positive and ≤ 2×10⁻⁹; charge leaves weight unchanged to 2×10⁻³ | Unknown physics, without a quantitative claim | Closed as stated; protocol on file. The '532 patent lapsed for an unpaid fee (effective 4 Dec 2022); it is cited only by three private filings (2020, 2023, 2026). Run 10: the 2023–2025 filings all fall under ledger 7, 16, 17, 21 or 25 (III.10) | None |
| 5 | GW power, B·L ≈ 10¹⁴ T·m | 10²⁷ in power | Nature | Settled; a generator claim is testable with HFGW cavities (Pais-scale flux 10⁵ above reach; III.9) | Magnetars only |
| 6 | Compact-fusion field, ~20 T | Closed. Hastelloy-class co-wind 59 T; a loose pre-strained M55J band 50 T (I.21). Co-wind caveats (run 7): delamination in dry-wound nested coils; turn-to-turn resistance drifts 10³× with load cycling; screening-current stress scales with J_eBr (run 8). | Materials | Closed | REBCO coils (A); metal co-wind (A, caveats) |
| 7 | 10⁶ T | 10³ | Atoms | Settled | None |
| 8 | Superconductor at 300 K and 1 atm | 2× in T_c at 1 atm (151 K record), or 260 GPa of pressure; strain gives ≤ 10 GPa (V.8); a dark cavity ≤ 10 % (V.11, cut) | Materials | Open; re-check about Feb 2027 | Hg-1223 151 K after pressure quench (B); LaSc₂H₂₄ onset to 298 K at 260 GPa, one group (C); nickelate films under strain, ~40–42 K (B) |
| 9 | Keeping a light-driven state on | Re-drive every lifetime. 100 K: 100 MHz, 3.1 W single pass, or 0.19–0.75 W in the FEL cavity (V.9); 300 K: 2 GHz, 63 W single pass, 3.8–15 W in a cavity. Lasing needs A < g − L (V.10). Run 9: a 10–20 nm film is 12–24 ML of MBE growth (films superconduct on Si down to ≥ 25 ML; driven K₃C₆₀ films exist); headroom at 30 µm: FELIX 0.45, FHI ~1.9 (computed), ELBE U100 0.15–0.40 (V.12); no watt-class tabletop source near 30 µm. Run 10: FELICE holds 81–133× the hold fluence at focus (V.13), but its stations are gas-phase. | Engineering | Open: experiment-ready and search-exhausted; film makeable; no cryogenic film station; the state contested (χ_v > −0.1) | B7 intracavity film (D; film B, hardware C); K₃C₆₀ at 10 THz (B, contested) |
| 10 | Asteroid deflection, ~1 m/s on 10¹⁰ kg | Closed over years | Engineering | Closed | Laser ablation 45 µN/W; impactor β 3.6 (A) |
| 11 | Laser turbojet | 0 | None | Nothing to do | Not applicable |

## Candidates and tests (paths kept)

- **B6, gap 2: stator-borne rotor: open for a craft on paper (D); tabletop experiment kept.** Stress-free when J_eB = ρv²/R; the stator carries 2T + U (≥ 289 kg of T1200 for T = 442 MJ).
  - **Hold and safety (runs 7–9).** Feedback (γτ < √2, bandwidth ≥ 4.53γ) or a superconducting null-flux pair (I.22, I.23). Loss-of-hold tolerance σ/ρv² = 0.28 %; a quenched tape hands 50–98 % of its current to a neighbour; quench-safe i ≤ 0.51 (I.25). Build: striated tape ≥ 10 filaments, section ≤ 0.6–1 cm², current uniform to 0.28 %, heat out by radiation only (I.26, I.27). mB = T; L = 2.8×10⁵ N m s; counter-rotating pairs (I.28).
  - **Containment and after a burst (run 9).** Debris at 19.7 MJ/kg ends as heat; its load is no larger than the rotor's own, so the stator can be the housing: craft 398–711 kg (1.3–2.3×) (I.30). Free-spinning liner; spin the survivor down (1 h at 123 kW) (I.31).
  - **Conductor (runs 8–10).** Production tape is never quench-safe at the radiative temperature; thick film (36.3 MA/cm², 4 µm, 30 T) is, below 9.2 K (0.1 mm basis) or 24.5 K (50 µm basis) (I.32). Run 10: thick films on thin stabilizers flux-jump (Jaroszynski 2025); a 15–20 K wall cuts the margin parameter 18–50× and still tolerates 0.7–1.8 mT of ripple (I.35, D).
  - **Field quality (run 10, I.33, ledger 36).** Allowed ripple ∝ (ε/n)^(1/3): 6–80 ppm of 30 T along 12.6 m, depending on tape and ε (unmeasured at 5–25 K; best coatings hold ε ≥ 0.95 only to ~30 K). Iseult (NbTi) measured 0.88 ppm on 22 cm; a 9.4 T all-REBCO NMR magnet was > 100 ppm off design before shimming, sub-ppm after. Open: no REBCO magnet shimmed along a 4 m ring; screening currents drift (C). Run 11: superconducting cyclotrons hold the first harmonic at 0.02–1.5 mT with coil centring, iron shims and trim coils (NbTi, a few tesla), the level B6 needs; the REBCO Ultra-Baby Skeleton Cyclotron quenched at 250 of 540 A and damaged coils (screening-current and contraction stress).
  - **Deciding tests.** (1) Tabletop ring (I.29): 10 cm ring at 970 m/s in an 8 T, 300 mm bore; production tape at i = 0.47–0.65. (2) Tangential coupon shot (I.34, run 10): a 20 × 25 × 2.2 mm coupon (8.9 g) on a 2 m-radius track feels the craft's 351 MPa at any size; exit speed gives μ = −ln(v_out/v_in)/θ (±0.027 at 30°, 1 % velocimetry); 3 and 6.3 km/s bracket vaporization; SwRI-class 38 mm gun (C). Run 11: debris at 6.28 km/s is 1.6–4.2× above rail and barrel gouging thresholds (1.5, 4 km/s), so measure gouges and pick the track's material pair from the gouging literature; fly the coupon along its length (fragment simulants: 4.7–5.5° end-on vs 32–43° side-on); gap entry angles 1.8–8.1°. (3) Stator field map of a REBCO ring coil after overshoot and shims; thick-film ramps at spin-up rates at 4.2 and 15–25 K.
- **B7, gap 9: intracavity drive (D; film B, hardware C).** Inside a cavity the source pays (A + L) of the single-pass power (V.9); lasing needs A < g − L (V.10); a 10–20 nm film is pumped uniformly (answers Dodge's depth critique). Film makeable by MBE (12–24 ML); headroom at 30 µm: FELIX 0.45, FHI ~1.9, ELBE U100 0.15–0.40 (V.12). Run 10: FELICE holds 33–53 mJ/cm² per 400 µJ micropulse at focus, 81–133× the 0.4 mJ/cm² hold fluence, so a film can sit 0.6–0.7 m off focus on an 8 mm spot (V.13); but its stations are gas-phase (molecular beam, FTICR) with limited access. Kill read: no field expulsion at ~50 nT (χ_v > −0.1); films exist only in the claimant group. Needs: a cryogenic film station in an FEL cavity, with magnetic and transport readouts. Run 11: no independent experiment as of Nov 2026 (reviews call the evidence not definitive).
- **K2, gap 6: metal co-wind (kept with caveats; waiting on data).** Strain-neutral through cooldown; NHMFL caveats (delamination, turn-to-turn drift). Missing: a measured free shrinkage of a named tape (stop searching, C4 v9).
- **X1: Buhler's charged-dielectric thrust (E, contested).** Claims 5–10 mN in vacuum, persisting after power-off; the slide equals the pull of 5.6 µC/m² of trapped charge (III.6, III.7). Run 10: no third-party test or peer review as of mid-2026 (NextBigFuture 31 Mar 2026; a July 2026 article); one page claims verification by "two outside groups" but names neither (E); the team has moved to battery-driven charge injection. Run 11: still no paper or outside test (early Nov 2026). Deciding test: sealed box on a torsion balance in high vacuum, charge modulated by UV or an electron flood, F(Q) fitted (III.8). Waiting on data.
- **K3/B4 (folded into B7):** facility 10 THz drive. **K4, gap 4:** balance protocol on file; known physics ≤ 3.7×10⁻¹⁶ N; sharper instrument (run 11): ETH's 42 Hz resonant detector (Q ~ 10⁴, pm), ~7–28 pN (estimate), with a shielded EM source driven at 21 Hz. **B5 (waiting).** **K5:** Tate's +92 ppm, 4.4σ; repeat at ≤ 10 ppm. **Gap 8:** Meissner data on LaSc₂H₂₄; a hydride pressure-quenched below 100 GPa.
- **Bridges (one search per run).** Pais's vibrate-to-pair idea ~ 10 THz phononics (B7); launch loop (B6); rotatable flywheel liners, NASA IPACS, LISA Pathfinder UV, MBE fulleride films (run 9); MRI/NMR shimming, the SPARC model coil, light-gas guns, axion-haloscope cavities, ETH resonating beams (run 10); cyclotron harmonic correction, gouging literature, fragment-simulant launches (run 11).
- **Side thread (runs 9–10; not scored): gravity–EM claims.** Every claim overlaps the ledger and every independent test was null. US 12,417,870 (Zhang, 2025): a coil pair moves a ball on a thread; no data. The 2023–2025 filings all fall under ledger 7, 16, 17, 21 or 25 (III.10); US 3,095,167 is 226× short. HFGW-generator claims are testable with cavities: Pais's flux as GW gives h ~ 10⁻¹⁵, 10⁵ above reach; known physics 10²⁰ below (III.9). Open edge: high-frequency coupling (K4).

## Paths cut (with why, and what would revive them)

| Path | Why cut | Revive only if |
| --- | --- | --- | --- |
| H1 spinning charged triangle (TSC-Δ) | C₃ symmetry: octupole 1.6×10⁻³⁵ W; 1 W needs a 0.024 c rim (II.5) | σ/ρ ~10⁶× graphene |
| H2 rotating in-plane ferroelectric | 1.4×10⁻¹⁰ W, but the disk bursts first (II.6) | never |
| Mass reduction by stored field or spin | Δm > 0 and Δm/M ≤ 2×10⁻⁹ (I.7) | a measured violation of von Laue's theorem |
| Pais Eq. 2 flux | ultrasound transducers would emit 10²⁴× what they do (II.8) | never: the devices exist |
| B3 vibrate the hull at 10 THz | acoustic λ = 0.5 nm; sasers ≲ 1 THz (V.5) | none |
| B2 light-drive the quenched Hg-1223 | the light-induced state vanishes at optimal doping (YBCO) | a light-enhanced state at optimal doping |
| Spinning-superconductor gravity | never replicated elsewhere (ledger 18); every test found in run 9's side thread was null | an independent replication |
| Self-supported rim materials (runs 4–7) | CNT yarn 0.9–1.8 N/tex at ≥ 0.1 m; one tube round 12.6 m has p = 10⁻⁵¹; M5/PIPD 3.4–3.6, graphene fibre 0.73; best 2 cm bundles 35.4 N/tex = 0.90× (I.11, I.15) | a material above 40 N/tex at metre gauge |
| Carbon bands on REBCO (runs 4–6) | bonded: +0.18–0.22 % of the tape's window and 27–34 MPa radial tension; pre-strained: 50 T, below a metal co-wind's 59 T (I.14, I.16, I.21) | a cold-slipping bond, or a band fibre ≥ 1 % at ≥ 300 GPa |
| Lifters and rotating electrostatics (runs 4–5) | ion wind, nothing in vacuum; axisymmetric spinning charge neither radiates nor self-pushes (III.4) | thrust in hard vacuum with no ejecta |
| B5 as a power route (run 4) | driven volume per watt changes by f·F² ≈ 0.1–2 (V.6) | f·F² ≫ 1 with connected driven regions |
| Earth flyby anomaly (run 5) | no mechanism; absent at Rosetta II–III and Juno (III.5) | a dedicated flyby tracked through perigee that shows it |
| Strain as pressure for superhydrides (run 6) | clamping gives ≤ 10 GPa; superhydrides need 100–260 GPa (V.8) | a superhydride stable below ~10 GPa |
| Passive electrodynamic hold, axisymmetric rotor (run 6) | spin induces no current; a patterned rotor pays ~16 W of drag per newton | superseded by I.23's superconducting null-flux pair |
| The craft's magnet as a magnetic sail (run 7) | kinetic regime, 1.5 µN–0.21 mN at 1 AU (S.4) | a moment ≳ 4×10¹⁴ A·m² |
| A dark cavity for gaps 8–9 (run 8) | T_c shifts ≤ 10 %; 2026 no-go theorem (V.11) | a passive cavity that raises a T_c ≥ 2× or above 77 K |
| Tabletop 10 THz source for B7 (run 9) | best difference-frequency sources: watts near 3 µm, far less beyond 10 µm | a watt-class source near 30 µm at ≥ 100 MHz |
| Emissivity as B6's decider (run 10) | allowed ripple ∝ ε^(1/3): field quality decides (I.33) | a rotor heat input that does not scale with ripple |
| Revived | B6 held passively (cut run 6, revived run 7, I.23); B6 as the craft's rim (blocked run 8, reopened run 9 on paper, D: I.30, I.32) | — |

## Loop health test (step 0 of every run)

Thresholds were fixed before any run was scored. Code: claude/pais_loop_health.py (runs 1–5 are scored there and on CT-60). Signal 14 was added in run 4 and pre-registered from run 5.

| Signal | Green if | Red if | Run 6 | Run 7 | Run 8 | Run 9 | Run 10 | Run 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Repeated queries | ≤ 0.25 | > 0.40 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Repeat yield | ≥ 0.75 | < 0.50 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Recycled sources | ≤ 0.15 | > 0.30 | 0.08 | 0.12 | 0.10 | 0.12 | 0.19 amber | 0.20 amber |
| Topic concentration | ≤ 0.30 | > 0.50 | 0.15 | 0.12 | 0.10 | 0.06 | 0.12 | 0.30 |
| Exploration | 0.20–0.50 | < 0.10 or > 0.60 | 0.23 | 0.29 | 0.24 | 0.35 | 0.31 | 0.40 |
| Kill ratio | ≥ 1 | < 0.5 | 1.00 | 1.75 | 1.50 | 1.00 | 1.25 | 1.50 |
| Domain novelty | ≥ 0.50 | < 0.30 | 0.68 | 0.47 amber | 0.57 (0.49 planned only) | 0.48 amber (0.48 planned only) | 0.46 amber (0.46 planned only) | 0.29 red (0.28 planned) |
| Progress (gaps changed) | ≥ 2 | 0 | 2 | 2 | 2 | 2 | 1 amber | 0 red |
| Repeated errors | 0 | ≥ 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Too easy | no | — | no | no | no | no | no | no |
| Circularity | ≤ 0.10 | > 0.25 | 0.08 | 0.07 | 0.05 | 0.06 | 0.11 amber | 0.09 |
| Canary | pass | fail | 13/13 | 14/14 | 15/15 | 21/21 | 15/15 | 15/15 |
| Prompt growth | ≤ 30 % | > 60 % | +6.8 % | +8.9 % | +8.0 % | +5.6 % | +6.7 % | +3.2 % |
| 14 Rework | ≤ 0.07 | > 0.15 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

- **Canary, run 11:** fifteen run-10 numbers re-derived by new code (ripple bounds, T_m, ε sensitivity, Iseult loss, 100 ppm rotor temperature, coupon mass and force, capstan, β ratio, warm design point, HFGW threshold, Pais h, US 3,095,167, FELICE fluence): all exact.
- **Run 10:** 10 green, 4 amber, 0 red (novelty 0.46, recycled 0.19, progress 1, circularity 0.11). **Run 11:** 11 green, 1 amber, 2 red: domain novelty 0.29 and progress 0. Both reds are the stop signals: the literature is exhausted and nothing moved, so the loop stops rather than searching harder.

## Errors caught (read before every run)

- **Runs 1–5 (one line each):** check the figure of merit against the real geometry (spot ΔT, not area flux) · quote strength at the buildable length · hoop stress = pressure × R/t · inputs with every number · subtract contraction mismatch × modulus from cold strain budgets · credit concentrators with f·F² · log title + URL as each search returns · take records from the maker's or lab's own page · state which body a bound applies to · re-source a lost input before reusing it.
- **Runs 6–7:** a pre-strained member spends its pre-strain from its own failure strain (B1 v7) · specific strength = force / mass per length, from the paper's own areas (B1 v8) · conductor dimensions from the same source as the current (B1 v8).
- **Run 8:** closed loops set i by quench hand-off, i ≤ 0.51 (B1 v9) · a deciding test must reach the regime it decides (A5 v9).
- **Run 10:** the gap-entry speed first used the small-gap form v√(2g/R) instead of I.30's exact geometry (889 vs 882 m/s at 20 mm); two "new" sources were already cited (FELICE numbers, run 7; Jaroszynski 2025, run 6). Lessons: reuse the earlier item's formula; check planned sources against the references first (A0 v11).
- **Run 11:** first-harmonic tolerances were nearly quoted as ppm of fields the sources did not give. Lesson: compare in absolute units when a source omits the base value.
- **Run 8, found in run 9:** a catcher sized by absorbed energy (7.2 t) where only the load must be held (contain by load above ~3.9 km/s, A4 v10) · thick-film J_e quoted without its thickness basis (state it with every J_e, B1 v10).

## Scorecards

- **Runs 1–7:** see the doc (gap 8 to 2×, gap 9 reframed, gap 4's premise falsified, gap 3 settled, B6 found and made a control problem, gap 6 closed, B7 found).
- **Run 8:** B6 blocked for a craft (later reopened); B7's lasing condition; dark cavity cut; X1's lingering force explained; 14 of 14 green.
- **Run 9:** gap 2: B6 for a craft reopened on paper (D): the stator can be the containment (I.30, 1.3–2.3× the craft), thick-film tape below 9–25 K (I.32), liner and spin-down after a burst (I.31); tabletop ring eased (i 0.47–0.65 at 8 T); gap 9: B7 film makeable (12–24 ML by MBE) with headroom at three FELs; Meissner null read (χ_v > −0.1); X1 control by UV charge modulation (III.8); a 30 µm tabletop source cut; 13 green, 1 amber; run sheet +5 items (35 pages).
- **Run 10:** gap 2: B6's conditions became three measurements (stator field 6–80 ppm, I.33; thick film at a 15–20 K wall, I.35; a full-pressure coupon shot, I.34); emissivity folded into field quality (ledger 36); gap 9: FELICE fluence ample, no film station (V.13); X1 unchanged; side thread: HFGW cavity null test (III.9), patent sweep adds nothing (III.10); 10 green, 4 amber; run sheet +6 items (38 pages).
- **Run 11 (last literature pass):** no gap moved. Precedent and caution for B6's field quality (cyclotrons; the REBCO skeleton-cyclotron quench); the coupon shot will gouge; a sharper K4 instrument (ETH detector); B7 and X1 unchanged; health reds on novelty and progress; the loop stopped by its rule; run sheet notes (40 pages).

## Maths run sheet

Chains: I stress and stored energy (I.1–I.35), II radiation (II.1–II.8), III momentum (III.1–III.10), IV vacuum (IV.1–IV.5), V pairing and drive (V.1–V.13), S standalone (S.1–S.4). Run 10 added I.33 the field quality the stator needs (proposition), I.34 a tangential fragment test (similarity and capstan law), I.35 flux-jump margin and a warm design point, III.9 HFGW cavities as a null test of EM-to-GW claims, III.10 the 2023–2025 patent sweep and V.13 FELICE intracavity fluence. Run 11 added notes on I.33–I.35 and K4 and the stop verdict (part 8). Earlier runs: see the run-sheet changelog (part 2).

## The loop stopped (after run 11)

- **Why.** Prompt C's rule: stop when every gap is settled or two runs in a row move nothing. Every gap is settled in the loop's sense: closed (4, 6, 10), against a wall (1, 3, 5, 7), nothing to do (11), or reduced to deciding experiments (2: stator field map, thick-film ramp, coupon shot; 9: the FEL film test); gap 8 waits on a dated re-check. Run 11 moved nothing, and its health reds (novelty 0.29, progress 0) say the same.
- **What decides the open gaps now:** the test plans in claude/pais_test_plans.md: B6 coupon shot (I.34) and conductor measurement (I.32, I.35) with a stator field map (I.33); B7 film test at an FEL (V.12, V.13); null tests: gap 4 balance or resonant detector (K4, III.3) and X1 with UV charge modulation (III.8).
- **Restart triggers:** (1) re-checks from February 2027 (gap 8: a ≥ 151 K ambient record or a pressure-quenched hydride; E-320: nonlinear Breit–Wheeler positrons); (2) an outside test or paper on Exodus/X1; (3) an independent driven-K₃C₆₀ result; (4) a field map of a large REBCO ring or a REBCO cyclotron reaching its design field; (5) any measurement from the test plans. On a restart, run Prompt A v12 on the gap the trigger touches only.
