# Pais gap loop: prompts (v12, after run 11: the loop stopped)

These are the three prompts the loop runs. Prompt A researches the gaps, Prompt B handles materials and engineering gaps, and Prompt C scores the run and rewrites the prompts. The loop's memory is in claude/pais_gap_research_loop.md (the state file). Every search is logged in claude/pais_search_log.md (runs 1–6), claude/pais_search_log_2.md (run 7), claude/pais_search_log_3.md (run 8), claude/pais_search_log_4.md (run 9) and claude/pais_search_log_5.md (runs 10–11), and the maths goes in claude/pais_math_runsheet.tex and its parts.

**The loop stopped after run 11 by its own rule** (every gap settled; run 11 moved nothing). Restart it only after one of the restart triggers listed at the end of the state file: say "Run the Pais gap loop" in a session attached to this project. That runs Prompt A v12 (health check first) on the gap the trigger touches, then B, then C. C saves the state as v13, the prompts as v13 (here), and appends the run's maths to the run sheet. The tests that now decide the open gaps are in claude/pais_test_plans.md.

## Prompt A v12

```text
PROMPT A · THE GAP LOOP · v12 · 13 Nov 2026 (after run 11)
Load claude/pais_gap_research_loop.md ("Errors caught" first), claude/pais_loop_prompts.md,
claude/pais_search_log_5.md (last run), claude/pais_math_runsheet.tex, the portfolio doc.
Goal: settle every gap: closed (a route meets it), proven unfillable (a wall no route crosses),
or reduced to one deciding experiment.
0 Health: score the last run with the loop_health signals. Any red → fix it in this run (repeat
  > 0.40: new phrasing or source class; topic > 0.50: cap it at 2 queries; exploration < 0.10:
  add explore queries; kill ratio < 0.5: one kill search per kept lead). Canary: re-derive one
  logged number from its written inputs. Re-checks: tag r, since-date phrasing, ≤ 2. Before
  searching, check each planned source against the run sheet's references and earlier logs
  (run 10 re-found FELICE and Jaroszynski 2025). [v11: run 10] On a restart, work only the gap
  its trigger touches. [v12: run 11]
For the gap named under "Next run":
1 Requirement: one number, units, conditions, and the claim it comes from.
2 Forward: record with date and source ("<quantity> record <year>", then the maker's or lab's
  own page; a summary table is not a record; extended search for latest results). If a paper
  proposes a path, start from its numbers. [v6: run 5 found T1200]
3 Backward: what must be true (inputs, mechanism, hidden assumptions); check the ledger.
4 Walls, atoms and vacuum first: atomic field 5.14×10¹¹ V/m, atomic pressure 2.94×10¹³ Pa,
  matter-made fields ≤ 2,800 T, Schwinger 1.32×10¹⁸ V/m, B_Q 4.41×10⁹ T, σ/ρ ≤ 6×10⁷ J/kg
  (self-supported rim ≤ 7.7 km/s; a stator-held rotor needs J_eBR/ρ ≥ v² and the craft
  ≥ ρ(2T+U)/σ of structure; field or spin Δm/M ≤ 2×10⁻⁹); thrust ≤ P/c with nothing ejected,
  2P/v with exhaust speed v; a body held by fields at fixed current has k_x+k_y+k_z = 0, so one
  translation needs control (rate ~ω√|n| for a spinning ring) or induced currents (flux-conserving
  loops add GᵀL⁻¹G ≥ 0); delayed feedback needs γτ < √2 and bandwidth ≥ 4.5γ; a supercritical
  rotor needs stator-side damping > (Ω/ω_n − 1) × rotor-side damping; it survives a loss of hold of
  only σ/ρv² (bursts within ms of a quench); debris above √(2e_vap) ≈ 3.9 km/s ends as heat, so
  contain by load: a containment needs no more tension than the rotor it held (3(γ−1)E ≤ 2T); in
  vacuum it sheds heat only as εσT⁴, so it tolerates field ripple ∝ (ε/n)^(1/3): field quality,
  not emissivity, decides. Then nature, materials, engineering, unknown physics. [v6–v11: runs 5–10]
5 Route. Atoms/vacuum/nature: what else reaches the GOAL (other effect, boosted frame,
  resonance, collective state, astrophysical source). Materials: Prompt B. Engineering: size
  it, name the limiting part and what its failure releases, B on that part. A deciding test
  must reach the regime it decides (e.g. ρv²/σ ≫ 1); a small test keeps full pressure if it keeps
  the section and the radius (coupon on a track of the craft's radius); sliding contact gouges above
  ~1.5 km/s (rails) to ~4 km/s (barrels). [v9–v12: runs 8, 10–11] Unknown physics: official tests and replication
  tables first, then anomalies; the smallest deciding experiment and what known physics
  predicts for the same rig. An unrepeated single measurement stays a lead and its repeat is
  the deciding experiment. [v5: run 4 Tate]
6 In between: pair two things already researched that nobody has tested together (material ×
  use, effect × source). Finding nothing is a finding. Invent freely (mechanism, combination,
  maths), derive the consequence with numbers, keep it only if it clears the walls, then search
  for prior art before crediting it; read each kill result against every lead; if cut, log why
  in "Paths cut". One bridge search per run (patents or research joining two leads). [v8–v10: runs 7–9]
7 Kill: one disconfirming search per kept lead, reaching a group other than the claimant's
  ("<author> <material> spurious OR artefact OR comment"; doping, size or scale dependence);
  read any reply. A thrust claim: compare with I√(2m_iV/e) for ejecta and P/c; with charged
  dielectrics in vacuum, modulate the charge (UV or electron flood; ionizers need gas) and fit
  F(Q). [v8–v10: runs 7, 9]
8 Grade: A replicated · B one peer-reviewed measurement · C preprint/conference · D theory or
  estimate · E patent/press/claim. Add "contested" and name the settling measurement.
9 Maths: every new derivation goes in the run sheet (canonical form, proof from first
  principles, numbers WITH inputs, verdict, references), chained to related items.
10 Write back (certain, factor, candidates + grades, dated sources, paths kept/cut). Run C.
Rules: numbers before adjectives; units and inputs with every number; claim ≠ measurement;
never close a gap on a press release; label speculation and estimates; log each search
(query, kind, title + URL found) in the search log as it returns; re-source an input whose
source was lost before reusing it. [v5–v6: runs 4–5]
```

## Prompt B v12

```text
PROMPT B · MATERIAL OR COMBINATION · v12 · 13 Nov 2026 (after run 11)
Run on every materials or engineering gap. If no atoms can meet it, give the number, the
closest material, and hand back to A.
Gap · requirement · side constraints (mass, temperature, pressure, lifetime, heat, cost)
1 Figure of merit for the real geometry AND size. Rims and magnet structure: σ/ρ (virial:
  stored energy per structural kg ≤ σ/ρ). Magnets: J_c(B,T), B²/2μ₀ × R/t. Charge: surface
  field. Superconductors: T_c, H_c2, pairing energy. Driven states: pulse energy × rep rate,
  then ΔT ≈ P/(π a k_sub) + q t/k_film; a field concentrator buys driven volume per watt
  f·F², not F². Strength at buildable length: Weibull σ(L) = σ_ref (L_ref/L)^(1/m), with
  ≥ 12 specimens per gauge; composites by chain-of-bundles and shear lag τ ≥ σ_f d/2δ.
  Layers bonded or banded through a cooldown: contraction mismatch × modulus comes off the
  strain budget first; a pre-strained member spends its pre-strain from its own failure
  strain (use the composite's, not the fibre's). Supported rotors: J_eBR/ρ, tilt margin 1 − β;
  J_e from the same source's width and thickness; closed loops need i ≤ 1/(1 + neighbour rise)
  (≈ 0.5 for stacked tapes; dynamic resistance binds only near 1), with J_e at the operating
  temperature (a radiative rotor sits at (P/εσA + T_s⁴)^¼; I_c ∝ e^(−T/T*), T* ≈ 22 K) and the
  source's thickness basis; check flux jumps at the operating temperature (β = μ₀J_c²a²/CT* < 3;
  warmer is safer; buy centre-slit tape with thicker Cu); self-forces: pinch
  μ₀J_e²A ln2/2π, screening edge loads ∝ filament width². Continuous lengths: production statistics (Schulz–Flory 2^(−L/L½)). Specific
  strength = force / mass per length; when a paper gives two areas, reproduce them from its own
  tables. [v5–v12: runs 4–11]
2 Ceiling: what atoms allow; above it → "no material" with the factor.
3 Record: best measured (conditions, date, source), then best at buildable size, with its
  gauge length.
4 Candidates: single materials; combinations (composites, laminates, heterostructures, doping
  and strain, pressure-quenched or driven metastable phases, metamaterials); systems (cooling,
  reinforcement, drive source and its recycling: inside a cavity the source pays (A + L) of a
  single pass, containment). Each: mechanism, number (grade), limit, distance, scale-up gap,
  facility vs compact. [v8: run 7]
5 Rank by gap left × grade × buildability; top three, each with a confirm-or-kill test.
6 Re-prompt: each top candidate's limit becomes a new requirement; run 1–5 once.
7 Write back. Run C.
```

## Prompt C v12

```text
PROMPT C · LEARN FROM THE RUN · v12 · 13 Nov 2026 (after run 11)
1 Score: per gap, factor before/after, grades, sources; per search, usable dated source or
  not; then the health signals (repeat and its yield, recycled sources, topic, exploration,
  kills, domain novelty, progress, repeated errors, too-easy, circularity, canary, prompt
  growth). Domain novelty < 0.50: next run, a third of sources from new classes (theses,
  national-lab reports, journal and maker sites, data sets); report it with and without input
  lookups added after the plan. [v8–v9: runs 7–8]
2 Learn: what worked, what wasted time, which assumption was wrong. Add every earlier-run
  error to "Errors caught" with its lesson.
3 Rewrite A and B: keep what paid off, add walls / figures of merit / candidate classes,
  retire dead ends with the reason; each edit cites its run; growth ≤ 30 % per version (cut
  text that no longer earns its place); ledger changes only on an overturning measurement.
4 Plan: next gap by (orders that could close) × (chance the lead holds) ÷ effort; 20–50 % of
  queries exploration; re-check dates for slow gaps; "waiting on data" for ready experiments
  and for any number searched three runs without result (stop searching it). [v9: run 8]
5 Save N+1: prompts, changelog, scorecard, health table, errors caught, paths kept/cut,
  run-sheet items added, next run; keep each file under ~30 KB (state, prompts and search
  log are separate files). [v6: run 5]
Stop when every gap is settled or two runs in a row move nothing; a gap moves when its status,
its best lead's grade or its deciding measurement changes. Say what would restart it. Health reds
on novelty and progress after a pass that moved nothing are stop signals, not faults. [v11–v12: runs 10–11]
```

## Changelog

- **v1** (8 Nov 2026): first versions, written from the CT-11 to CT-17 findings.
- **v2** (after run 1): record-search phrasing; walls tested first; unknown physics starts from official tests; pulse × repetition-rate check; scale-up field; hit-rate log.
- **v3** (after run 2): start from a paper's own path; extended search for latest results; kill-search phrasing; "contested" grade with the settling measurement; spot temperature rise replaces area heat flux; facility vs compact sources; "Errors caught" log; re-check dates; "waiting on data".
- **v4** (after run 3):
  - A0: health check on the last run, with fixes for each red; canary every run.
  - A4: new walls σ/ρ ≤ 6×10⁷ J/kg and thrust ≤ P/c (virial and centre-of-energy theorems).
  - A6: "in between" step: pair researched items never tested together; absences count; invent, derive, keep or cut with the reason.
  - A7: one kill search per kept lead; doping, size and scale dependence as kill angles.
  - A9: maths run sheet, inputs with every number.
  - B1: figure of merit at buildable size (Weibull, chain of bundles); σ/ρ for magnet structure; B²/2μ₀ × R/t.
  - C3: prompt growth capped at 30 % per version (v4: +5 %).
- **v5** (after run 4):
  - A0: planned re-checks tagged "r", since-date phrasing, at most two.
  - A4: thrust wall extended to 2P/v with exhaust speed v (run sheet III.4).
  - A5: an unrepeated single measurement stays a lead; its repeat is the deciding experiment (Tate).
  - A7: each kill search reaches a group other than the claimant's.
  - Rules: log each search with title + URL as it returns (run 4 lost its sources at a context reset).
  - B1: concentrators credited with f·F²; Weibull m from ≥ 12 specimens per gauge; shear lag; contraction mismatch before any cold strain budget.
  - B3: quote the gauge length with the buildable-size record.
  - C1: health list names repeat yield and recycled sources.
  - Health code: signal 14 (rework inside a run) and query kind "s".
  - Growth +10 % (5,430 → 5,984 characters).
- **v6** (after run 5, 11 Nov 2026):
  - Load line: prompts and search log are now separate files (claude/pais_loop_prompts.md, claude/pais_search_log.md).
  - A2: a record comes from the maker's or lab's own page; a summary table is not a record. Run 4 had used T1100G from a table; Toray's T1200 (Oct 2023) is 13 % stronger per kilogram.
  - A4: the rim wall applies to a rim carrying itself. A stator-held rotor needs J_eBR/ρ ≥ v², and the craft then needs ρ(2T+U)/σ of structure (run sheet I.17).
  - Rules: re-source an input whose source was lost before reusing it. Run 4's 0.26 % tape shrinkage had lost its source; the measurement implies 0.31–0.32 %.
  - B1: supported rotors (J_eBR/ρ, tilt margin 1 − β); continuous lengths by production statistics (Schulz–Flory, run sheet I.15).
  - C5: keep each file under ~30 KB, with state, prompts and search log as separate files. State v5 had reached 36.5 KB.
  - Growth +7.5 % (5,984 → 6,433 characters).
- **v7** (after run 6, 11 Nov 2026):
  - A4: a body held by fields at fixed current has k_x + k_y + k_z = 0, so one translation needs control, at a rate of about ω√|n| for a spinning ring (run sheet I.18); a supercritical rotor needs stator-side damping above (Ω/ω_n − 1) × rotor-side damping (I.19).
  - B1: a pre-strained member spends its pre-strain from its own failure strain, using the composite's value, not the fibre's (I.21; runs 4–5 had quoted 72 T for a band that reaches 50 T).
  - B1: strength figures name their cross-section (tube, wall or envelope) and pair it with the matching density (I.11 open check).
  - Growth +6.8 % (6,433 → 6,871 characters).
- **v8** (after run 7, 11 Nov 2026):
  - Load line: the search log continues in claude/pais_search_log_2.md.
  - A4: an unstable axis can also be held by induced currents (flux-conserving loops add GᵀL⁻¹G ≥ 0, run sheet I.23); delayed feedback needs γτ < √2 and bandwidth ≥ 4.5γ (I.22).
  - A6: search for prior art before crediting an invented mechanism (run 7's null-flux stabilizer had prior art from 1969 and 1980).
  - A7: check a thrust claim against the ejecta bound I√(2m_iV/e) and P/c (the X1 slide is 5.7×10⁵× over).
  - B1: J_e from the same source's width and thickness, at i ≤ 0.7–0.8 (dynamic resistance caps i near 1, I.24); specific strength = force / mass per length, reproducing a paper's areas from its own tables (K1 had been quoted at 61.5 N/tex; it is 35.4).
  - B4: recycling the drive: inside a cavity the source pays (A + L) of a single pass (V.9).
  - C1: when domain novelty falls below 0.50, a third of the next run's sources come from new classes (run 7: 0.47).
  - Growth +8.9 % (6,871 → 7,484 characters).
- **v9** (after run 8, 12 Nov 2026):
  - A4: a stator-held rotor survives a loss of hold of only σ/ρv² and bursts within ms of a fast quench; a catcher needs ≥ T/(60 kJ/kg); in vacuum a rotor sheds heat only as εσT⁴ (run sheet I.25, I.27).
  - A5: name what the limiting part's failure releases; a deciding test must reach the regime it decides (run 7's 500 m/s ring had ρv²/σ = 2.2; I.29).
  - A6: read each kill result against every lead (K2's screening-current search exposed B6's edge loads, I.26).
  - B1: closed loops need i ≤ 1/(1 + neighbour rise), about 0.5 for stacked tapes (I.25), replacing "i ≤ 0.7–0.8"; self-forces: pinch μ₀J_e²A ln2/2π and screening edge loads ∝ filament width².
  - C1: report domain novelty with and without input lookups added after the plan (run 8: 0.57 with, 0.49 without).
  - C4: a number searched three runs without result goes to "waiting on data" and is no longer searched (K2's free shrinkage).
  - Load line: the search log continues in claude/pais_search_log_3.md.
  - Standing item (user request): one patent-and-research bridge search per run.
  - Growth +8.0 % (7,484 → 8,081 characters).
- **v10** (after run 9, 13 Nov 2026):
  - Load line: the search log continues in claude/pais_search_log_4.md.
  - A4: debris above √(2e_vap) ≈ 3.9 km/s ends as heat, so containment is sized by load: it needs no more tension than the rotor it held, 3(γ−1)E ≤ 2T (run sheet I.30). Run 8 had sized a catcher by absorbed energy (7.2 t); the load bound gives 1.3–2.3× the craft.
  - A6: one bridge search per run (patents or research that join two leads), made standing.
  - A7: for charged dielectrics in vacuum, modulate the charge with UV or an electron flood and fit F(Q); air ionizers need gas (III.8; LISA Pathfinder practice).
  - B1: J_e at the operating temperature, with the source's thickness basis: a radiatively cooled rotor sits at (P/εσA + T_s⁴)^¼ and I_c falls as e^(−T/T*), T* ≈ 22 K (I.32). Production tape is never quench-safe for B6; thick film is, below 9–25 K depending on its basis.
  - Growth +5.6 % (8,079 → 8,534 characters).
- **v11** (after run 10, 13 Nov 2026):
  - Load line: the search log continues in claude/pais_search_log_5.md.
  - A0: check planned sources against the run sheet's references and earlier logs before searching (run 10 re-found two).
  - A4: a rotor cooled only by radiation tolerates ripple ∝ (ε/n)^(1/3), so the stator's field quality decides, not the coating (I.33).
  - A5: a small test keeps the full pressure if it keeps the section and the radius (I.34).
  - B1: check flux jumps at the operating temperature, β = μ₀J_c²a²/(C T*) < 3; warmer operation cuts β 18–50× at 15–20 K (I.35).
  - C: "moves" defined for the stop rule (status, best-lead grade or deciding measurement changes).
  - Growth +6.7 % (8,536 → 9,105 characters).
- **v12** (after run 11, 13 Nov 2026; the loop stopped by its rule):
  - Intro: the loop stopped; restart only on a trigger listed in the state file, and work only the gap it touches (A0).
  - A5: sliding contact gouges above ~1.5 km/s (sled rails) to ~4 km/s (gun barrels); B6's debris is 1.6–4.2× faster, so its test measures gouges.
  - B1: thick-film flux jumps: buy centre-slit tape with thicker Cu.
  - C: health reds on novelty and progress after a pass that moved nothing are stop signals, not faults.
  - Growth +3.2 % (9,105 → 9,392 characters).
