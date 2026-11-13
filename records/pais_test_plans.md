# Pais gap loop: test plans (after run 11, 13 Nov 2026)

The loop stopped after run 11 by its own rule. Every gap is now closed, against a wall, or reduced to experiments, and searching no longer changes the picture. These five tests decide what is left. Item numbers (I.30, V.13, …) refer to the maths run sheet (claude/pais_math_runsheet.tex, parts 1–8). Grades: A replicated · B one peer-reviewed measurement · C preprint or conference · D theory or estimate · E claim.

| Test | Decides | Scale | Grade of the path it tests |
| --- | --- | --- | --- |
| T1 B6 tangential coupon shot | whether a burst rotor's debris loads its wall no more than the held rotor did (I.30) | two-stage light-gas gun, 2 m-radius track | D (theorem untested) |
| T2 B6 conductor and stator field | whether a rotor can stay quench-safe at its radiative temperature (I.32, I.33, I.35) | high-field lab (30 T, variable temperature); a REBCO ring coil and a field-mapping rig | C/D |
| T3 B7 film in an FEL cavity | whether a light-driven state can be kept on, and whether it superconducts at all (V.9–V.13) | FEL beam time (FELIX/FELICE or the FHI FEL), MBE film growth | D (film B, hardware C, state contested) |
| T4 Gap 4 / K4 null test | whether any electromagnetic–gravity coupling exists at nN or pN (III.3) | vacuum balance, or a 42 Hz resonant gravity detector | null predicted |
| T5 X1 with UV charge control | whether the Exodus force is trapped-charge electrostatics (III.6–III.8) | torsion balance in high vacuum with UV LEDs | E (claim) |

Cheapest and fastest first: T5 and T4 are small-laboratory tests; T2 needs a high-field user facility; T3 needs FEL beam time and a new cryogenic station; T1 needs a light-gas-gun range and a curved track.

## T1 · B6 tangential coupon shot (tests I.30; design I.34)

**What it decides.** I.30 says sliding debris presses on a wall with the held rotor's own line load, λv²/R, and a debris gas needs no more tension than the rotor did. If that holds, the stator can be the containment and the craft is 1.3–2.3× its 312 kg minimum. If not, containment is far heavier.

**Why a small shot is a full test.** A coupon cut from the rotor's section, sliding on a track of the rotor's radius, presses with the craft's own pressure λv²/(Rh) whatever its height and length (I.34). Its exit speed after an arc θ is v·e^(−μθ), so one shot measures the friction that sets how fast debris slows.

**Setup.**
- Coupon: a piece of the real tape stack, 20 mm high × 25 mm long × 2.2 mm thick (8.9 g at an assumed 8,000 kg/m³), flown along its length in a separating sabot (fragment simulants fly with 4.7–5.5° mean pitch and yaw end-on, 32–43° side-on).
- Track: a concave arc of radius 2.0 m, 30–90° long, backed by a massive block; surface as the craft's wall (liner or ablator over the stator material). Entry tangent to the barrel at a gap of 1, 5 or 20 mm (wall met at 1.8°, 4.0° or 8.1°; radial impact 199, 443 or 882 m/s).
- Gun: a two-stage light-gas gun with a ≥ 38 mm launch tube (SwRI class: 7 km/s top speed, 0.5 kg at 3 km/s). The full-speed package (coupon + 20 g sabot) carries 0.57 MJ.

**Shot matrix.** Two speeds × three gaps × two wall materials, repeated:
- 3.0 km/s: 80 MPa on the wall, 4.5 MJ/kg (0.6 of vaporization).
- 6.28 km/s: 351 MPa (the craft's), 19.7 MJ/kg (2.6× vaporization).

**Measurements.**
- Entry and exit speed (photonic Doppler velocimetry or flash X-ray): μ = −ln(v_out/v_in)/θ. Over 30°, μ = 0.1, 0.3, 0.5 give v_out/v_in = 0.949, 0.855, 0.770; 1 % velocimetry resolves μ to ±0.027.
- Back-face strain gauges along the arc: line load against time.
- Coupon attitude at entry (flash X-ray), and its state along the arc (high-speed imaging: solid, melt or vapour).
- Witness plates on the track's inner side: anything that leaves inward, with its energy.
- The track afterwards: gouges (shape, depth) and erosion against the ablator budget of I.30 (7–59 kg over the craft's 1.26 m² wall, i.e. 6–47 kg/m²).

**Predictions.** Known physics (I.30): after the entry transient, the line load stays near λv²/R and falls as v²; debris stays pressed to the concave wall. Gouging is expected: sled rails gouge above 1.5 km/s and gun barrels above 4 km/s, and 6.28 km/s is 1.6–4.2× faster.

**Pass or fail for I.30.** It fails if the load stays well above λv²/R after the entry impact, if debris escapes inward and strikes elsewhere with more than its share of energy, or if gouging cuts through the ablator budget. It passes if the load follows λv²/R within about 20 % and the erosion stays within the ablator.

**Hazards.** Track fragments, metal vapour, sabot debris; standard light-gas-gun range practice.

## T2 · B6 conductor and stator field (I.32, I.33, I.35)

**What it decides.** A rotor cooled only by radiation runs at the temperature its field ripple sets. B6 is quench-safe only if the tape's current density at that temperature keeps i ≤ 0.506, and only if the stator's field is even enough along the rotor's path.

**T2a · Conductor.**
- Tape: thick-film A-MOCVD REBCO (4 µm film, Hf/Zr-doped), on 50 µm and 0.1 mm bases, centre-slit, with a thicker copper stabilizer (edge-slit tapes fluctuate in I_c; metal layers suppress flux avalanches).
- Measure I_c at 30 T with B parallel to ab and at small tilts, at 4.2, 10, 15, 20 and 25 K, in a variable-temperature insert at a 31–45 T facility; and lengthwise uniformity of 40 m pieces (each gives three 12.57 m rotor loops).
- Pass: J_e at the operating temperature ≥ 5.856/0.506 = 11.6 kA/mm². With T* = 22 K (21–23), the 50 µm basis should pass up to 24.5 K (23.5–25.4) and the 0.1 mm basis up to 9.2 K (9.0–9.4); production tape never passes.
- Flux jumps: ramp the field at the rates spin-up would impose, at 4.2 K and at 15–25 K, with voltage taps and Hall probes. Prediction (I.35, D): the margin parameter μ₀J_c²a²/(C T*) falls 18–50× between 4.2 and 15–20 K, so jumps seen at 4.2 K should vanish warm. Fail if jumps persist at 15–25 K.

**T2b · Stator field map.**
- Requirement (I.33, ledger 36): azimuthal ripple at harmonic n ≤ B₀[εσA(T_m⁴ − T_s⁴)/nP₀]^(1/3): about 6–80 ppm of 30 T at n = 1 (0.17–2.3 mT), depending on tape and emissivity; emissivity matters only as ε^(1/3).
- Rig: a REBCO ring coil of at least 1 m diameter, first at a few tesla; map the field on the orbit radius with a rotating search coil or a Hall array; charge with current overshoot; correct with shims and trim coils, as superconducting cyclotrons do (they hold the first harmonic at 0.02–1.5 mT).
- Pass: n = 1 ripple within the target and drift (screening-current relaxation) within it over 24 h; then scale up in field. Fail: no correction below about 100 ppm, or drift beyond the target. Caution: the one REBCO cyclotron magnet built for field accuracy quenched at 250 of 540 A and damaged coils; protect and instrument the ring accordingly.
- Option (I.35): run the stator wall at 15–20 K (cryocooler practice of the 20 T SPARC model coil); the rotor then tolerates 0.7–1.8 mT.

## T3 · B7 film in an FEL cavity (V.9–V.13)

**What it decides.** Whether a light-driven, superconducting-like state in K₃C₆₀ can be kept on by re-driving it inside a laser cavity, and whether it is a superconductor at all. Driven K₃C₆₀ shows superconducting-like optics, pressure dependence and nonlinear transport, but a field-expulsion search found none at about 50 nT (χ_v > −0.1), and no independent group has reproduced the state.

**Setup.**
- Film: 10–20 nm K₃C₆₀ by MBE (12–24 monolayers at about 2 ML/h, 6–12 h), on sapphire or diamond, capped against air; equilibrium T_c 19 K.
- Laser: 30 µm (10 THz, the resonant drive). Inside a cavity the source pays only (A + L) of single-pass power; lasing needs the film's absorption A (0.1–0.2) below the cavity's headroom g − L: FELIX 0.45, the FHI FEL about 1.9 (computed), ELBE U100 0.15–0.40.
- Placement: FELICE holds 33–53 mJ/cm² per 400 µJ micropulse at focus, 81–133× the 0.4 mJ/cm² hold fluence, so the film can sit 0.6–0.7 m off focus on an 8 mm spot. Its stations are built for gas-phase samples: a cryogenic film station is new hardware.
- Re-drive: within the state's lifetime (about 10 ns at 100 K; at least 0.5 ns predicted at room temperature), i.e. ≥ 100 MHz at 100 K. FELICE's 1 GHz micropulse trains inside 8 µs macropulses re-drive the film about 8,000 times.

**Measurements.** Through the macropulse: mid- and far-infrared reflectivity (σ₁, σ₂); transport (an on-chip ultrafast voltmeter); and a magnetic readout (Faraday-rotation magnetometry at ~50 nT or better).

**Controls.** Off-resonance drive (e.g. 41 THz), fluence below threshold, an undoped C₆₀ film, base temperatures from below T_c to 300 K, and the cavity with no film.

**Pass or fail.** Pass: zero resistance and field expulsion (χ_v well below −0.1) held through the macropulse at 100 K or above: a sustained light-driven superconductor, and gap 9 met at that temperature. Fail: no expulsion at the resolution: the state is not superconducting (a high-mobility metal), and B7 is cut.

## T4 · Gap 4 / K4 null test (III.3, III.9; run-11 notes)

**What it decides.** Whether electromagnetic fields couple to gravity or inertia beyond known physics, the premise of the Pais "inertial mass reduction" patents. Known physics predicts nothing measurable: the field mass of a lab rig is +5.2×10⁻¹⁹ kg (ledger 16) and its radiated thrust ≤ 3.7×10⁻¹⁶ N (ledger 17).

**T4a · Balance (steady and modulated fields).** A shielded, battery-powered rig in high vacuum on a nN-class balance (TU Dresden practice): the run-2 Pais-type rig (30 cm disk, 1 µC, 94 kV, vibrated ±80 nm at 100 MHz) or a capacitor and coil set. Protocol (III.3): face-to-face symmetry better than 2×10⁻⁶ (the image pressure pulls 0.050 N per face), polarity reversal, the device rotated 180° in vacuum, then discharged, spin-only and vibration-only runs. TU Dresden found no coupling at about 1 nN with steady fields and named high-frequency fields as their next step.

**T4b · Resonant dynamic-gravity detector.** ETH's 42 Hz bending-beam detector (Q ≈ 10⁴, ~1 pm) measured dynamic gravity to about 3 % of theory and resolves roughly 7–28 pN (estimate for a 1–4 kg effective mass), 36–140× below a nN balance. Replace the moving-mass transmitter with a shielded electromagnetic source whose field energy oscillates at 42 Hz (drive at 21 Hz), with its own mechanical motion measured and its Newtonian signal computed.

**Pass or fail.** Any reproducible signal that survives reversal, rotation and shielding, and exceeds the computed Newtonian and electromagnetic crosstalk, is new physics; a null bounds the coupling at the instrument's floor and closes the Pais premise experimentally as it is already closed in theory.

## T5 · X1 with UV charge control (III.6–III.8)

**What it decides.** Whether the Exodus "new force" is ordinary electrostatics from trapped charge. The claimed 4.46 mN at 228 µW is 5.7×10⁵× what ejected ions could give; it equals the pull of 5.6 µC/m² of trapped charge, which relaxes in minutes (polyimide) to days (PTFE).

**Setup.** The thruster inside a sealed, grounded conducting box on a torsion balance in high vacuum; UV LEDs at 254 nm (4.88 eV, above the work function) or an electron flood to change its trapped charge (air ionizers do not work in vacuum); LISA Pathfinder's charge-control practice.

**Numbers (III.8).** Trapped charge Q = 1.41×10⁻⁸ C (8.8×10¹⁰ e); force constant c = 2.26×10¹³ N/C², so F = cQ². Photocurrents of 1, 10 and 100 nA discharge it in 14, 1.4 and 0.14 s. At 30, 10 and 1 % of Q the force is 401, 44.6 and 0.45 µN; the claimed ±20 µN resolution is reached at 6.7 % of Q.

**Pass or fail.** Fit F against Q. If F ∝ Q² and goes to zero as the charge is removed, the force is electrostatic (X1 cut). If a force stays with the charge removed, inside a sealed box, in vacuum, with reversals, it is anomalous and should go to an outside laboratory for replication.

## What would restart the loop

Re-checks from February 2027 (gap 8: an ambient-pressure T_c record or a pressure-quenched hydride; E-320: nonlinear Breit–Wheeler positrons); an outside test or paper on Exodus; an independent driven-K₃C₆₀ result; a field map of a large REBCO ring or a REBCO cyclotron reaching its design field; and any result from T1–T5.

## Sources

- Run sheet items I.30–I.35, III.3, III.6–III.10, V.9–V.13 and their references (claude/pais_math_runsheet_refs.tex); searches in claude/pais_search_log.md to claude/pais_search_log_5.md.
- SwRI large two-stage light-gas gun: https://Swri.org/sites/default/files/brochures/large-two-stage-light-gas.pdf
- Fragment-simulating projectiles in a two-stage gun (OSTI 2004149): https://www.osti.gov/servlets/purl/2004149
- Gouge initiation in high-velocity sliding contact (Sandia, 1991): https://www.sandia.gov/research/publications/details/an-investigation-of-gouge-initiation-in-high-velocity-sliding-contact-1991-11-01/
- 40 m thick-film REBCO tapes (Superconductivity 9, 100081, 2024): https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2025/01%20Newly%20Entered%20Pubs%20January%202025/2024%20cited/2024_40-meter-long%20REBCO%20tapes.pdf
- Lengthwise fluctuations and flux jumps in REBCO to 45 T (arXiv 2502.02706): https://arxiv.org/pdf/2502.02706
- Harmonic errors of a 9.4 T all-REBCO NMR magnet (Sci. Rep. 2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11333634
- Kolkata superconducting cyclotron field imperfections (Cyclotrons 2010): https://epaper.kek.jp/Cyclotrons2010/papers/mopcp078.pdf
- REBCO skeleton cyclotron, quench at 250 A (ASC 2024): https://indico.cern.ch/event/1431972/contributions/6420498
- SPARC Toroidal Field Model Coil Program (arXiv 2308.12301): https://arxiv.org/pdf/2308.12301
- FELICE (FELIX Laboratory): https://wiki.felix.science.ru.nl/FELICE
- Probing optically driven K₃C₆₀ thin films (Struct. Dyn. 12, 024503, 2025): https://qcmd.mpsd.mpg.de/wp-content/uploads/2025/03/Adelina-structural-dynamics-2025.pdf
- In-depth search for a gravity–EM coupling with steady fields (Sci. Rep. 2024): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11339412/
- Dynamic measurement of gravitational coupling at 42 Hz (ETH): https://www.research-collection.ethz.ch/handle/20.500.11850/557791
- Exodus status, March 2026: https://www.nextbigfuture.com/2026/03/exodus-propulsion-and-the-electrostatic-pressure-force.html
