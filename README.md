# Five Experiments to Settle What Is Left of the Pais Patents

**Open designs, costs and what each result would mean: the final report of the Pais gap research loop**

Spheromax · version 1.0 · 14 November 2026

**Landing page with the film:** https://spheromax.github.io/pais-test-programme/

> This work is for humanity. It may not be used for war, for greed, or for any inhumane purpose. It is offered so that people can become more humane, and for our advancement in technology and in spirit, in harmony and balance.

**Licence:** Hippocratic License 3.0 with the Military Activities module, written "Hippocratic 3.0 (HL3-MIL)". See [LICENSE.md](LICENSE.md). The author has filed no patent on this work. Publishing it openly is meant to keep it free for everyone.

## Who did what

This is one person's project, carried out with an AI research assistant.

- **The author** conceived the project and chose the patents and the questions. They directed every pass of the review, decided which paths to keep and which to cut, and decided when it should stop. They also designed the sheet style, made the film's music, and set the purpose and the licence.
- **Claude (Anthropic)**, a large language model, worked under that direction: it ran and logged the literature searches, derived and computed the results, drew the concept rigs and drawings, cut the film and drafted the text.

AI tools are not listed as authors. Every number can be checked against the code and sources in this record. Please report errors.

## What this is

A research loop examined, gap by gap, the physics claims in Salvatore Pais's US Navy patents, plus related claims of propellantless thrust and light-driven superconductivity. The patents cover:
- an "inertial mass reduction" craft
- a high-energy electromagnetic field generator
- a high-frequency gravitational-wave generator
- a plasma compression fusion device
- a room-temperature superconductor

**Scale of the work.** The loop ran 11 times and logged 162 searches with sources. It built a ledger of 36 settled results and a 40-page mathematics run sheet, then stopped by its own rule.

**The result.** Nothing in the patents survives as physics. What survives is engineering:
- a magnetically held rotor (B6)
- a light-driven film kept on inside a laser cavity (B7)

Two other claims can only be settled by null tests. Five experiments decide what is left:

| Test | What it decides | Rough cost |
| --- | --- | --- |
| T5 | Is the "X1" thrust claim just static electricity from trapped charge? | $0.2–0.5M |
| T4 | Do electromagnetic fields couple to gravity at nN or pN? (null predicted) | $0.7–1.3M |
| T2 | Can a superconducting rotor and stator stay quench-safe at about 20 K? | $1.6–3.0M |
| T3 | Can a light-driven state in a K3C60 film be kept on in a laser cavity, and is it a superconductor? | $0.7–1.2M |
| T1 | Does burst-rotor debris load its wall no more than the spinning rotor did? | $1.1–2.6M |

All five together come to about $4–9M over about 3 years; the first two answers (T5 and T4) to about $1–2M. These are rough-order-of-magnitude costs (±50%). They assume magnet and laser time is won by peer-reviewed proposal.

## What may be new

Three ideas in this record may be new. They are candidates, not claims: the review searched the literature and patents as it went, but no exhaustive prior-art search has been done.

- **A rotor held by its stator (B6).** The stator's magnetic field carries the load that would burst a self-supporting rim, so the rotor is not limited by the strength of its material. Sheets CT-33 to CT-61; run sheet I.17 onward.
- **Driving a film inside a laser cavity (B7, test T3).** A K3C60 film sits inside a free-electron-laser cavity, which cuts the source power needed to keep its light-driven state on. Unproven. Sheets CT-46, CT-52, CT-57, CT-64; run sheet V.9 to V.13.
- **A tangential coupon shot (test T1).** A small coupon fired along a curved track tests how burst-rotor debris loads its wall, without spinning a full rotor. Sheet CT-62; run sheet I.34.

They are published openly on 14 November 2026, with no patent filed, so that they stay free for everyone to use under the licence.

## Contents

| Path | What it is |
| --- | --- |
| `report/PTP_open_report_v1.0.pdf` | The report (8 pages); LaTeX source and figures in `report/latex_source/` |
| `supplements/S1_maths_run_sheet_run11.pdf` | **S1** Mathematics run sheet, 40 pages: every derivation with its inputs, proofs and references; source in `supplements/S1_latex_source/` |
| `supplements/S2_A3_drawing_set_PTP-000_to_PTP-902.pdf` | **S2** 20 A3 concept drawings: general arrangements, sections, schematics, block diagrams, equipment lists |
| `supplements/S3_CAD_package.zip` | **S3** 8 STEP assemblies, DXF views, renders, model and drawing scripts, computed numbers, equipment list |
| `supplements/S4_research_sheets.pdf` | **S4** 40 illustrated research sheets, grouped by the test each one feeds, with a contents page and bookmarks |
| `records/` and `code/` | **S5** Final loop state file, test plans, costs, drawing notes, loop prompts, search logs (with sources), run logs; the Python that computes and cross-checks every number (`run*_math.py`, independent re-derivations `canary*`, loop health tests) |
| `film/PTP_film_v1.0.mp4` | **S6** 1:52 film of the simulated concept rigs, with soundtrack (the music is not covered by the licence: all rights reserved) |

## Status and limitations

- The rigs are concept designs for review, not for manufacture. Facility items (guns, magnets, lasers) are drawn indicatively.
- Costs are rough order of magnitude, ±50%.
- The renders and the film show simulated rigs. Only the T2 field lines are computed physics (Biot–Savart).
- The X1 and driven-K3C60 claims belong to others and are described here from public sources.
- Side research outside the scored loop has been left out of this record.
- The sheet set (S4) leaves out 17 sheets about the loop's own process (health checks and run summaries). A few records still cite those sheet numbers; their data is in `records/` and `code/`.

## What would restart the loop

The loop restarts if any of these happen:
- the re-checks due from February 2027 find something: a new ambient-pressure superconducting record above 151 K, a pressure-quenched hydride, or nonlinear Breit–Wheeler pair production at SLAC E-320
- an outside test or paper on the X1 claim appears
- another group independently reproduces driven K3C60
- someone publishes a field map of a large REBCO ring, or a REBCO cyclotron reaches its design field
- any result comes from T1–T5

## How to cite

Spheromax (2026). *Five Experiments to Settle What Is Left of the Pais Patents: open designs, costs and what each result would mean.* Version 1.0.
