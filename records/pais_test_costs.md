# Pais test programme: costs, funding path and film (14 Nov 2026)

Status: rough order of magnitude (ROM), ±50%, in USD. The estimates assume that magnet and FEL time is won by peer-reviewed proposal at no charge, and that staff cost about $150–250k per FTE-year. Test designs are in claude/pais_test_plans.md and claude/pais_test_drawings.md.

## Cost by test (recommended order)

| Test | What it decides | ROM cost | Main cost drivers |
| --- | --- | --- | --- |
| T5 · X1 with UV charge control | Whether the X1 force is trapped-charge electrostatics | $0.2–0.5M | Vacuum torsion balance, sealed grounded box, 254 nm UV / e-flood, staff. Much less at a partner lab that already has a balance. |
| T4 · Field–gravity null (T4a balance, T4b 42 Hz detector) | Whether any EM–gravity coupling exists at nN or pN | $0.7–1.3M | nN balance, resonant Ti-6Al-4V beam detector, shielding, staff |
| T2 · Conductor and stator field (T2a probe $0.3–0.5M, T2b ring $1.3–2.5M) | Whether the rotor stays quench-safe at about 20 K | $1.6–3.0M | 3.2 km of 12 mm REBCO, 20 K cryocooler, mapping arm, quench protection. MagLab time by proposal. |
| T3 · K₃C₆₀ film in an FEL cavity | Whether a light-driven state can be kept on, and whether it superconducts | $0.7–1.2M | MBE films, intracavity cryogenic station, diagnostics. FEL time by proposal. |
| T1 · Tangential coupon shot | Whether burst debris loads the wall no more than the held rotor did | $1.1–2.6M | Light-gas-gun range time (contract), track fixture, PDV, high-speed cameras |
| **All five** | | **≈ $4–9M, about 3 years** | |
| **First answers (T5 + T4)** | | **≈ $1–2M** | |

## Anchors with sources (checked 14 Nov 2026)

- **MagLab.** Magnet time is free of charge to researchers through a competitive proposal process, and proposals are accepted all year. https://nationalmaglab.org/user-resources/requesting-magnet-time/
- **FELIX (Nijmegen).** Beam time is by proposal, with deadlines on 15 May and 15 Nov. The next usable deadline for T3 is 15 May 2027. https://www.ru.nl/felix/facility/
- **HFML.** Industry can buy magnet time directly, as an alternative to the proposal route. https://www.ru.nl/hfml/use-our-facility/experimental/
- **REBCO tape.** Street prices are about $15–30/m (2025). Superconductivity 15 (2025) 100188: https://www.utupub.fi/bitstreams/01b51cb1-f538-49c6-a6c6-326cab10f847/download
  - T2b uses 3.2 km of 12 mm tape. At roughly 3× the 4 mm price, the tape alone is about $0.15–0.3M.
- **Light-gas guns.**
  - Much of the cost of each test is labour: setup, data and cleaning (NASA GSFC, IOC 2023). https://ntrs.nasa.gov/api/citations/20230015532/downloads/LGG%20Paper-%20IOC2023%20Hull.pdf
  - A complete 22 m two-stage gun reaching 6.5 km/s was built for £1.1M (First Light Fusion). https://firstlightfusion.com/media/first-light-fusion-installs-uks-biggest-two-stage-hyper-velocity-gas-gun/
- **Other anchors** used in the ROM (from the drafting session, not re-sourced here):
  - HPV-X2 camera about ¥29M
  - 20 K cryocooler cost about 9.3·R^0.41 k$, roughly $50k for 60 W
  - COTS 4-point PDV $120–140k
  - UHV transfer suitcase from CHF 54,500

## Funding path

- **Crowdfunding is small.** On Experiment.com the median project raised $3,105; a few raised tens of thousands and one more than $2.6M. https://cepr.org/voxeu/columns/crowdfunding-money-research-levels-playing-field
  - Crowdfund one concrete first step, not the whole $4–9M.
- **T5 first, at a partner lab.** TU Dresden's SpaceDrive torsion balance resolves at least 100 nN for thrusters up to 10 kg, with EM shielding. The group has already tested EmDrive and Mach-effect claims and traced them to artefacts. https://iafastro.directory/iac/archive/browse/IAC-18/C4/7-C3.5/46021/
  - T5 also needs an X1 device, either from the claimants or built from their filings.
- **T2:** MagLab proposal (T2a first).
- **T3:** FELIX proposal by 15 May 2027, ideally with the MBE-film group.
- **T1:** contract range time.

## IP route (not legal advice; user's decision pending)

**User's stated aim (14 Nov 2026).** Keep it open, with their name on it. It must not be used for war, greed or inhumane purposes. It is "for humans to become humane", for advancement in technology and spirit, in harmony and balance. They do not need to exclude anyone.

**Recommended: open, dated disclosure under an ethical licence. It costs nothing.**
- **Where to publish.**
  - Zenodo: free, gives a permanent DOI, and allows custom licences. https://help.zenodo.org/docs/deposit/describe-records/licenses
  - TDCommons: free defensive publication, indexed by Google Patents. https://www.tdcommons.org/faq.html
- **What it achieves.** It names the author and a date, and becomes prior art, so no one else can patent the same thing.
- **Licence.** Hippocratic License 3.0 with the MIL (military activities) module, plus the user's purpose statement. https://firstdonoharm.dev/
  - Licences with use restrictions are "ethical source", not OSI open source, which bars field-of-use restrictions. https://opensource.org/osd
- **Credit line.** "by [user], developed with Claude (Anthropic)". An AI cannot be an inventor or rights-holder.
- **Release order.** Publish the disclosure first, then the film and the campaign.

**Why not a patent.**
- A patent's power is to exclude.
- US government and contractor use cannot be enjoined; the owner can only claim compensation (28 U.S.C. § 1498). https://www.law.cornell.edu/uscode/text/28/1498
- Inventors must be natural persons who conceived the claims, and AI is treated as a tool. Incorrect inventorship risks invalidity (USPTO revised guidance, Nov 2025). https://www.mayerbrown.com/en/insights/publications/2025/12/united-states-patent-and-trademark-office-issues-revised-guidance-on-inventorship-for-ai-assisted-inventions

**If a patent option is still wanted:** file a US provisional the day before publishing. Fee $65 (micro entity), $130 (small) or $325 (large); it holds the date for 12 months. https://www.uspto.gov/sites/default/files/documents/USPTO-fee-schedule_current.pdf
- European patent law (the EPC, which covers the UK) has no grace period, so any disclosure before filing kills novelty. https://www.epo.org/en/legal/official-journal/1999/03/p155
- Candidates:
  1. T1's tangential-coupon containment test method
  2. T3's intracavity FEL drive (unproven)
  3. The B6 stator-held rotor (prior-art search first)
- The test rigs themselves mostly combine published methods.

## Film

- **File:** "PAIS GAP LOOP · TEST PROGRAMME", 1:52.5, 1080×1080, 60 fps.
- **Music and cut:** cut to "I Wish I Was Born A Cicada" at 141 BPM. The window starts at 2:43.8 in the track and covers eight 8-bar phrases plus a 3.6 s reverb tail.
- **Order:** T5 → T4 → T2 → T3 → T1. The drop lands on T1 at 1:08.1.
- **Labelling:**
  - On screen: "CONCEPT RIGS · SIMULATED" and costs "±50%".
  - The T2 field lines are computed by Biot–Savart; everything else is concept animation.
- **Mark:** original. It shows the T2b ring as a track, the T1 tangent shot line with the coupon, and five rays for five tests.
- **Before public release:** clear the music rights and settle any patent filing.

## Reminder

A scheduled task on 1 Feb 2027 re-checks the six loop-restart triggers listed in claude/pais_test_plans.md.
