# Pais gap loop: test drawing set (PTP-000 to PTP-902)

13 Nov 2026. Concept A3 drawings, CAD and equipment lists for tests T1–T5 (see claude/pais_test_plans.md). Status: concept design for review, not for manufacture; facility items (guns, magnets, FELs) drawn indicatively.

## What exists
- **A3 set:** `PTP_test_programme_A3_drawing_set.pdf`, 20 sheets.
  - 000: cover, index and programme.
  - T1: 101 range GA · 102 track fixture assembly · 103 section, channel detail and entry geometry · 104 coupon and sabot · 105 instrumentation and timing.
  - T2: 201 I_c probe GA · 202 I_c / flux-jump schematic and matrix · 203 REBCO ring + mapping arm GA · 204 ring power, protection, cryogenics and mapping.
  - T3: 301 FEL film-station GA · 302 holder, Brewster plate, sensors · 303 timing, readout, sample transfer.
  - T4: 401 nN balance GA · 402 42 Hz resonant detector GA · 403 schematics.
  - T5: 501 µN balance and charge-control GA · 502 charge control and F–Q test.
  - Equipment lists: 901 (T1, T2) · 902 (T3, T4, T5, common).
- **Package:** `PTP_test_programme_CAD_package.zip`.
  - 8 colour STEP assemblies: T1 fixture, T1 coupon/sabot, T2a probe, T2b ring, T3 station, T4a balance, T4b detector, T5 balance.
  - 8 DXF view sets at 1:1; renders; sheet PNGs.
  - CadQuery and drawing scripts, and JSON of every computed number.
  - Equipment list as CSV and markdown.

## Design checks raised while drawing (carry into the test plans)
1. **T3 placement.**
   - At Brewster incidence (θ_B = 67.2°, diamond n = 2.38) the film plane receives cos θ_B = 0.39 of the beam fluence.
   - The plan's 8 mm spot (1/e² radius, 0.4 mJ/cm² in the beam) at 0.58–0.73 m from focus gives only 0.155 mJ/cm² on the film.
   - For 0.4 mJ/cm² on the film plane: w ≈ 5.0 mm at 0.36–0.45 m from focus, footprint 25.6 × 9.9 mm. Confirm which fluence the hold criterion refers to.
2. **T3 heating.**
   - Each 8 µs macropulse makes 16,000 passes at 1 GHz in both directions; with A = 0.1–0.2 that deposits 0.64–1.28 J per macropulse, or 6.4–12.8 W at 10 Hz.
   - The 0.5 mm diamond column under the footprint rises from 100 K to about 155–180 K per macropulse (Debye upper bound). With 2 µs macropulses the rise is to 122–135 K.
   - Low-temperature controls (below T_c 19 K) are possible only at reduced power.
   - Station response: on-chip Pt RTD and a 2 µs-macropulse fallback.
3. **T2b.**
   - Single ring, not a split pair: at the same orbit field, two coils would attract with about 2 MN.
   - Ring: 4 × 250 turns of 12 mm REBCO (3.2 km), r 500–530 mm, 20 K. L = 2.09 H.
   - At 300 A: 1.15 T on the orbit (r 450), 2.7 T peak, about 210 MPa hoop stress, 94 kJ stored. Run at 300 A; 400 A (1.53 T, about 370 MPa) only after checks.
   - The n = 1 target of 6–80 ppm corresponds to 7–92 µT at 300 A.
4. **T2a.**
   - A 0.5 mm bridge at about 726 A has almost no copper, so quench detection must trip in under 100 µs and drive an IGBT diverter. Use 1–10 ms pulses for the highest currents.
   - The Ø36 probe fits a ≥ Ø38 VTI (50 mm-bore 31 T magnet). A Ø26 variant with 0.2 mm bridges suits 32 mm bores.
5. **T1.**
   - Target tank ≤ 1 mbar (at 1 atm, drag costs about 0.3 % of speed per metre).
   - Track: R 2000, 45° arc, contact 31.9–38.2°.
   - Fixture 668 kg (CAD). Coupon 8.8 g (CAD, ρ 8.0); sabot 17.6–22.4 g; package KE 0.52–0.62 MJ at 6.28 km/s. PDV beat 6.7–8.1 GHz.
   - Witness plates are polycarbonate so the cameras can see the channel.
6. **T4 / T5.**
   - T4a: co-moving grounded cans make image forces internal. Disk C = 10.6 pF, so 1 µC sits at 94 kV.
   - T4b: Ti-6Al-4V beam 1200 × 150 × 11.6 gives f₁ = 42.0 Hz and τ = 76 s. A 1 pm readout means 7–28 pN; the thermal floor is about 1 pN in 1000 s.
   - T5: F = 4.46 mN × (Q/Q₀)². The ±20 µN resolution is reached at 6.7 % of Q₀; discharge takes 14 / 1.4 / 0.14 s at 1 / 10 / 100 nA.
