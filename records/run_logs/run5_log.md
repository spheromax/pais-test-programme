# Run 5 search log (written as each search returns; merged into state v6 at the end)
Kinds: f forward, k kill, x exploration, r re-check, s source recovery. Fetches are listed under the search they follow.

1. [f] K1 "half-meter ultralong carbon nanotubes growth Schulz-Flory catalyst" (tag cnt-sf)
   - Zhang, ..., Wei, "Growth of half-meter long CNTs based on Schulz–Flory distribution", ACS Nano 7, 6156 (2013): 550 mm tubes; length set by catalyst deactivation probability per growth step. https://www.qianggroup.com/wp/pdf/ACS%20Nano-2013-Growth%20of%20Half-Meter%20Long%20Carbon%20Nanotubes%20Based%20on%20Schulz%20Flory%20Distribution.pdf · https://core.ac.uk/works/49392737
   - Zhu, ..., Wei, Nat. Commun. 10, 4467 (2019): tube count falls exponentially with length for any α; half-length L0.5 of s-CNTs 74.4 mm. https://pmc.ncbi.nlm.nih.gov/articles/PMC6775125 · https://acris.aalto.fi/ws/portalfiles/portal/37819320/s41467_019_12519_5_1.pdf
2. [k] K1 "Pugno nanoscale Weibull statistics nanotube defects" (tag cnt-stat; group: Pugno/Ruoff, not the claimant)
   - Pugno & Ruoff, J. Appl. Phys. 99, 024301 (2006), doi:10.1063/1.2158491: nanoscale Weibull modulus ~3 for nanotubes. https://arxiv.org/abs/cond-mat/0504518v1
   - Pugno, Bosia, Carpinteri, Small 4, 1044 (2008): multiscale stochastic simulations, macroscopic CNT cables ≤ ~10 GPa vs ~100 GPa theoretical; inputs σ0 34 GPa, m 2.7. https://pugno.dicam.unitn.it/NP_PDF/98-Small08.pdf
3. [f] K2 "REBCO pancake cooldown measured hoop strain gauges stainless cowind" (tag rebco-cold)
   - NHMFL Large Scale Coil, IEEE TAS 36(3) 4601805 (May 2026): stainless + copper co-wind, stainless overband, inboard/outboard gauges, 2024–25 tests; gauges zeroed at start of outsert charge. https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2026/02%20Newly%20Entered%20Pubs%20February%202026/2026%20cited/2026_Measured%20and%20Simulated%20Strain%20in.pdf · abstract with cooldown comparison https://indico.cern.ch/event/1431972/contributions/6420158
   - Barth et al., SuST 28 045011 (2015): tape soldered to a Walters spring; zero-strain point found at −0.14 to −0.15 % (the cooldown offset the holder imposes). https://arxiv.org/pdf/1502.06713
   - H800 insert: 304 stainless overband 76 µm strips keeps hoop strain < 0.6 % at 30.5 T. https://typeset.io/pdf/test-of-an-8-66-t-rebco-insert-coil-with-overbanding-radial-2t1j0w52xm.pdf
4. [k] K2 "REBCO delamination c-axis tensile strength epoxy impregnated coil cooldown" (tag rebco-delam)
   - Park et al.: c-axis tensile strength of coated conductors 18–53 MPa. https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........1df8ade45320f2cee1ad4c42cea76db5
   - Delamination strengths and radial thermal stress of impregnated pancakes (IEEE TAS): radial stress from anisotropic contraction degrades coils above the delamination strength. https://manuscript.isc.ac/inventory/49/11009.htm
   - 3D delamination model: tensile radial stress mainly from thermal-contraction mismatch during cooling. https://vufind-test.katalog.k.utb.cz/SummonRecord/FETCH-LOGICAL-c230t-cef1afbbb6e3e7b9ecbcbfd4be3bc12c8542d24c2586587b2ddef3733a8c7d423
   - fetch (under 3): NHMFL LSC paper gives NO cooldown strain value (only the 614 A dual-operation test; thermal contraction "considered" in the model, values not given) — informative absence.
   - fetch (under 3): Barth et al. 2015, arXiv:1502.06713: Walters spring is Ti-6Al-4V, contraction −0.17 % at 4.2 K, −0.16 % at 77 K; tape soldered to it is held in TENSION by the mismatch; zero strain at 4.2 K: Bruker 0.152, Fujikura 0.145, SuNAM 0.148, SuperOx 0.144, SuperPower 0.149 % (77 K: 0.138–0.145 %). Irreversible tensile limits at 4.2 K, 19 T: Bruker 0.70–0.72, Fujikura 0.55–0.57, SuNAM 0.67–0.69, SuperOx 0.45–0.47, SuperPower 0.66–0.68 %. → free-tape shrinkage to 4.2 K ≈ 0.17 + 0.148 = 0.31–0.32 % (inferred), above run 4's 0.26 % input.
5. [x] gap 2 "PIPD M5 rigid-rod polymer filament tenacity" (tag fibre)
   - US 8,419,989 (citing Sikkema 1998 etc.): PIPD "potential" tenacity up to ~5.8 GPa, modulus ~310 GPa. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8419989
   - EP 1614778: filament average 3600 mN/tex (3.6 N/tex) and 320 GPa over 25–75 filaments. https://data.epo.org/publication-server/rest/v1.2/patents/EP1614778NWA1/document.pdf
   - Taylor & Francis topic page: Akzo → Magellan → DuPont; "unclear if this fibre will ever become commercially available". https://taylorandfrancis.com/knowledge/Engineering_and_technology/Materials_science/M5_fiber
6. [x] gap 2 "graphene oxide wet-spun filament highest GPa" (tag fibre)
   - Large-scale graphene fibre filaments: 1.4 GPa at 1.93 g/cm3 (0.73 N/tex). https://bohrium.dp.tech/paper/arxiv/39274571
   - LC GO fibres 0.15 GPa (arXiv 2602.14290, 2026). https://arxiv.org/pdf/2602.14290 · knittable GO fibres 0.14 GPa (Sci. Rep. 2015) https://www.nature.com/articles/srep14946
   - RSC Adv. 2017 snippet "7 N/tex" for as-spun GO fibre: text extraction looks garbled; not used. https://pubs.rsc.org/en/content/articlepdf/2017/ra/c7ra03975a
7. [f] gap 2 "Toray newest carbon fiber grade strongest MPa announced" (tag fibre)
   - Toray T1200 (29 Oct 2023): 1,160 ksi (8.0 GPa), density 1.82 g/cm3, 46 Msi, 2.5 % strain; T1100 1,015 ksi, 1.79. https://www.toraytac.com/newsroom/news-item/2023/10/29/Toray-Develops-TORAYCA™-T1200,-the-Ultra-High_Strength-Carbon-Fiber · https://texdata.com/news/Yarn&Fiber/19659.html
   → best metre-scale fibre is 4.40 N/tex, not T1100G's 3.91 (run-4 table was stale).
8. [x] gap 2 in-between "launch loop Lofstrom dynamic structure stream supported" (tag dynamic)
   - Dynamic-support structures carry loads far above the stream material's static strength; Lofstrom 1985 iron rotor 14 km/s. https://engrxiv.org/preprint/download/6639/10868/9202 · https://toughsf.blogspot.com/2023/12/the-loftstrom-loop-bridge-to-space.html
   - Lofstrom interview: rotor faster than orbital speed, held down with ~2x its weight; Forward named "dynamic structures". https://www.nextbigfuture.com/2012/10/server-sky-concept-could-put-millions.html
9. [k] B6 "superconducting levitated ring rotor Earnshaw stability eddy losses high speed" (tag levitation; other groups)
   - Earnshaw: no stable levitation with static fields alone; superconductors (diamagnetic) and dynamic effects evade it. https://core.ac.uk/download/71164777.pdf · https://www.osti.gov/servlets/purl/632846 · https://www.magneticbearings.org/app/uploads/publications/ismb14/ismb14_submission_106.pdf
   - Spinning top levitation without control (spin changes the static result). https://www.magneticbearings.org/app/uploads/publications/ismb5/ismb5_submission_83.pdf
   - Levitated superconducting current ring needed feedback + eddy-current damping (Cooper et al. 1970). https://scilit.com/publications/3964b2c304d2e605ace9862feea81fac
   - HTS flywheel: rotation losses from eddy currents in field inhomogeneity (Physica C 483, 178, 2012). https://www.scribd.com/doc/229625328/1-s2-0-S0921453412002705-main
10. [x] anomaly "Earth flyby anomaly Anderson formula spacecraft" (tag flyby)
   - Anderson et al., PRL 100, 091102 (2008): six flybys, empirical formula; predicted < 1 mm/s for Rosetta 2007. https://link.aps.org/doi/10.1103/PhysRevLett.100.091102
   - Lense–Thirring negligibly small. https://arxiv.org/pdf/0809.1888 · no velocity-independent force field reproduces the formula (Hasse et al.). https://ar5iv.arxiv.org/html/0903.0109 · review https://arxiv.org/pdf/1711.02875
11. [k] anomaly "Juno flyby anomaly absent tracking result" (tag flyby; other groups)
   - Iorio review: anomaly absent at Galileo II, Rosetta II and III; formula predicted ~7 mm/s for Juno. https://arxiv.org/pdf/1412.7673
   - Juno Earth flyby 2013: anomaly at threshold or absent (Acedo et al.). https://ar5iv.labs.arxiv.org/html/1711.08893 · pre-flyby prediction −6 to −8 mm/s https://arxiv.org/pdf/1312.1139
12. [f] B6 "REBCO engineering current density 4.2 K 20 T tape kA/mm2 thin substrate" (tag rebco-je)
   - Bruker BHTS (ARIES): J_E 600 A/mm2 at 4.2 K, 20 T; nearly 1000 A/mm2 record (spring 2019), low yield. https://acceleratingnews-archive.web.cern.ch/acceleratingnews-archive/node/154.html
   - STAR round wire 586 A/mm2 at 4.2 K, 20 T (SuST 32 10LT01, 2019). https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2019/12%20Newly%20Entered%20Pubs%20December%202019/2019%20cited/2019_Next%20generation%20highly%20flexible%20round.pdf
   - Houston thick-film R&D: short samples J_e ~4,600 A/mm2 (0.1 mm tape) at 4.2 K, 20 T; 40 m tapes >4,000 A/12 mm at 4.2 K, 13 T. https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2025/01%20Newly%20Entered%20Pubs%20January%202025/2024%20cited/2024_40-meter-long%20REBCO%20tapes.pdf
   - B||ab: I_c falls only ~22 % from self-field to 31.2 T (4 µm Hf-doped film). https://scite.ai/authors/mehdi-kochat-zlyd3
