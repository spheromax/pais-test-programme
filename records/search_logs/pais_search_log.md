# Pais gap loop: search log

Prompt A logs every search here as it returns: the query, its kind, and the title and URL of what it found. Prompt C reads the last run's section for the health test: query wording feeds signals 1 and 14, source domains feed novelty. The state file is claude/pais_gap_research_loop.md and the prompts are in claude/pais_loop_prompts.md.

Kinds: f forward · k kill · x exploration · r planned re-check · s source recovery. Fetches are listed under the search they follow. Side research run at the user's request is logged in its own section and is not scored.

## Hit rates

- Run 1: 14 of 14. Run 2: 12 of 12. Run 3: 14 of 14.
- Run 4: 16 of 16, with two informative absences: no large-gauge Weibull data on ultralong bundles, and no conventional resolution of the Tate anomaly.
- Run 5: 12 of 12, plus 2 fetches. One informative absence: the NHMFL 40 T test-coil paper reports no cooldown strain.
- Run 6: 13 of 13, plus 4 fetches (3 refused: two off the allowlist, one browser check). Informative absences: no measured free shrinkage of a named REBCO tape; no nanotube-bundle data past a few cm since 2018; no outside replication of X1.
- Total: 81 of 81.

## What worked (carried forward)

- **Records:** "<quantity> record <year>", then the lab's own press page. In run 5, "<maker> newest <product> grade strongest announced" found Toray's T1200 page; a summary table had given a 2014 grade.
- **Latest results:** use extended search mode.
- **Scale kills:** "<material> strength gauge length size effect". At engineering scale, "<material> tensile strength N/tex gauge length". For length statistics (run 5), "<growth process> Schulz-Flory".
- **Drive-bridge kills:** "<effect> doping dependence underdoped optimally doped".
- **Testing a claim against existing devices:** "<device> <field> <frequency> <displacement>". This found the CMUT test of Eq. 2.
- **Re-checks:** "<experiment> <signal> arXiv <year>".
- **Damage ceilings:** "<structure> field enhancement damage threshold MV/cm".
- **Kill phrasing:**
  - "<author> <material> spurious OR artefact OR comment"; doping and size dependence (run 3).
  - "<anomaly> explanation" reached only the claimant group in run 4. Read that as "no independent resolution" and look for a repeat.
  - Run 5: "<anomaly> absent <later event> tracking result" (flybys); "<structure> Earnshaw stability eddy losses" (levitated rotors).
  - Run 6: rotordynamics as a kill angle for anything spinning on fields ("rotating damping whirl instability supercritical"); maker data sheets for failure strain ("<fibre> tensile strength modulus elongation"); "<claim> independent replication" for single-group claims.
- **Run 6 fetch notes:** pmc.ncbi.nlm.nih.gov can return a browser check; nature.com and arxiv.org/abs/<id> may be off the allowlist; arxiv.org/html/<id>v2 from a search result fetches, in parts (use offset).
- **Productive primary sites:**
  - Runs 1–3: english.iop.cas.cn, nationalmaglab.org, issp.u-tokyo.ac.jp, arXiv, nature.com abstract pages, qcmd.mpsd.mpg.de, infoscience.epfl.ch, fis.tu-dresden.de, fels-of-europe.eu, escholarship.org, jstage.jst.go.jp, pmc.ncbi.nlm.nih.gov, indico event pages.
  - Run 4: digitallibrarynasampe.org, par.nsf.gov, public.magnet.fsu.edu, link.aps.org, core.ac.uk.
  - Run 5: qianggroup.com, pugno.dicam.unitn.it, toraytac.com, data.epo.org, image-ppubs.uspto.gov, magneticbearings.org, acceleratingnews-archive.web.cern.ch.
- **Fetch notes:**
  - patents.google.com/.../en is off the fetch allowlist. The bare /patent/<number> URL fetches when it came from a search result.
  - Justia works for published applications.
  - arXiv /abs/ pages fetch. The arXiv and Crossref APIs are blocked.

## Run-4 query log

Wording of 1–12 was reconstructed after a context reset. Where a source did not survive, the finding is marked "source lost".

1. Ultralong CNT bundle strength against gauge length, Weibull [f]: no data past 2 cm; Bai et al., Nat. Nanotechnol. 13, 589 (2018).
2. Weibull shape of CNT yarns at several gauges [k]: strength and spread fall with gauge length (source lost).
3. CNT-yarn composite ring or NOL hoop test [f]: none at hoop scale (source lost).
4. REBCO with a carbon-fibre overband [f]: overbands keep strain below ~0.6 %; friction matters for thick overbands (source lost).
5. REBCO compressive strain limit and pre-compression [k]: compressive irreversible limit 0.2–0.75 %; I_c reversible about −0.6 % to +0.65 % (source lost).
6. THz split-ring field enhancement on superconducting films [x]: see 16.
7. THz gap heating and damage [k]: see 16.
8. E-320 positrons, arXiv 2026 [r]: positron-tracker preprint arXiv:2604.23805 (April 2026), single positrons resolved with a foil proxy (0.120 per shot); nonlinear Breit–Wheeler expected at 0.01–0.1 per shot, not yet reported. https://arxiv.org/abs/2604.23805
9. Biefeld–Brown in vacuum [x]: null in vacuum, corona wind (Talley 1991, PL-TR-91-3009; Tajmar, AIAA J. 42, 315, 2004).
10. Tate Cooper-pair mass anomaly [x]: m*/2m_e = 1.000084(21) against 0.999992 (Tate et al., PRL 62, 845, 1989; PRB 42, 7885, 1990).
11. Thermal contraction of Hastelloy, REBCO and carbon fibre to 4 K [k]: tape pack 0.26–0.27 %, stainless 0.30 %, carbon along the fibre ≈ 0 (Ekin 2006 for the last two; pack source lost; run 5 measured 0.31–0.32 % for free tape, see run-5 item 3).
12. Specific strength of commercial fibres [x]: T1100G 3.91, Zylon 3.77, Dyneema 3.71, Kevlar 2.51 N/tex (maker data as tabulated in Wikipedia, "Specific strength"; stale, see run-5 item 7).
13. "Tate Cooper pair mass anomaly explanation" [k]: only the gravitomagnetic group answers; its density model is 23× short. https://arxiv.org/abs/gr-qc/0607086 · https://arxiv.org/pdf/gr-qc/0603033 · https://arxiv.org/pdf/gr-qc/0603032 · review https://arxiv.org/pdf/2206.07574
14. "carbon nanotube yarn tensile strength N/tex gauge length 2020" [s]: 0.911 ± 0.137 N/tex at 100–120 mm, https://www.digitallibrarynasampe.org/data/pdfs/s2020_pdfs/TP20-0000000156.pdf · 1.77 ± 0.07 N/tex, yarns 150–500 m long, https://pmc.ncbi.nlm.nih.gov/articles/PMC10353548 · untwisted-yarn shear-lag model, https://www.jstage.jst.go.jp/article/matertrans/62/9/62_MT-Z2021005/_html/-char/en
15. "REBCO coil co-wound Hastelloy strain reduction screening current stress" [s]: https://arxiv.org/pdf/1909.07553 · Hastelloy co-wind in a 20 T insert design, https://www.mdpi.com/2079-9292/10/14/1741 · screening-current stress falls with co-wind thickness, https://aminer.org/pub/62d170545aee126c0fd977e3 · NHMFL 40 T test coil with stainless and copper co-wind (2026), https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2026/02%20Newly%20Entered%20Pubs%20February%202026/2026%20cited/2026_Measured%20and%20Simulated%20Strain%20in.pdf
16. "terahertz metamaterial gap field enhancement damage threshold MV/cm" [s]: dipole gap 170× at the edge, 60× mid-gap, field emission above ~10 MV/cm, https://arxiv.org/pdf/1508.04737 · split rings on GaAs, 2.2 µm gaps, enhancement ∝ 1/g, https://link.aps.org/accepted/10.1103/PhysRevLett.110.217404 · electromigration above 2 MV/cm in the gap, https://core.ac.uk/download/43246148.pdf

## Run-5 query log (11 Nov 2026, logged as each search returned)

1. [f] K1 "half-meter ultralong carbon nanotubes growth Schulz-Flory catalyst"
   - Zhang, ..., Wei, ACS Nano 7, 6156 (2013): 550 mm tubes; length set by the catalyst's deactivation probability per growth step. https://www.qianggroup.com/wp/pdf/ACS%20Nano-2013-Growth%20of%20Half-Meter%20Long%20Carbon%20Nanotubes%20Based%20on%20Schulz%20Flory%20Distribution.pdf · https://core.ac.uk/works/49392737
   - Zhu, ..., Wei, Nat. Commun. 10, 4467 (2019): tube count falls exponentially with length; half-length 74.4 mm for semiconducting tubes. https://pmc.ncbi.nlm.nih.gov/articles/PMC6775125
2. [k] K1 "Pugno nanoscale Weibull statistics nanotube defects" (Pugno/Ruoff group, not the claimant)
   - Pugno & Ruoff, J. Appl. Phys. 99, 024301 (2006): nanoscale Weibull modulus ~3 for nanotubes. https://arxiv.org/abs/cond-mat/0504518v1
   - Pugno, Bosia, Carpinteri, Small 4, 1044 (2008): stochastic multiscale simulations cap macroscopic CNT cables near 10 GPa; inputs σ₀ 34 GPa, m 2.7. https://pugno.dicam.unitn.it/NP_PDF/98-Small08.pdf
3. [f] K2 "REBCO pancake cooldown measured hoop strain gauges stainless cowind"
   - NHMFL Large Scale Coil, IEEE TAS 36(3) 4601805 (2026): stainless and copper co-wind, stainless overband, gauges zeroed at the start of the charge. https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2026/02%20Newly%20Entered%20Pubs%20February%202026/2026%20cited/2026_Measured%20and%20Simulated%20Strain%20in.pdf · https://indico.cern.ch/event/1431972/contributions/6420158
   - Barth et al., SuST 28, 045011 (2015): tape soldered to a Walters spring. https://arxiv.org/pdf/1502.06713
   - H800 insert: a 304 stainless overband keeps hoop strain below 0.6 % at 30.5 T. https://typeset.io/pdf/test-of-an-8-66-t-rebco-insert-coil-with-overbanding-radial-2t1j0w52xm.pdf
   - Fetch, NHMFL paper: no cooldown strain value is given (informative absence).
   - Fetch, Barth et al.:
     - The spring is Ti-6Al-4V, which contracts 0.17 % to 4.2 K.
     - Tape soldered to it sits in tension at 4.2 K. Zero strain is reached at Bruker 0.152, Fujikura 0.145, SuNAM 0.148, SuperOx 0.144 and SuperPower 0.149 %.
     - Irreversible limits at 4.2 K, 19 T: 0.70–0.72, 0.55–0.57, 0.67–0.69, 0.45–0.47 and 0.66–0.68 %.
     - From these, free-tape shrinkage is 0.31–0.32 % (inferred).
4. [k] K2 "REBCO delamination c-axis tensile strength epoxy impregnated coil cooldown"
   - Park et al.: c-axis tensile strength of coated conductors 18–53 MPa. https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........1df8ade45320f2cee1ad4c42cea76db5
   - Impregnated pancakes degrade when radial stress from contraction mismatch exceeds the delamination strength. https://manuscript.isc.ac/inventory/49/11009.htm
5. [x] gap 2 "PIPD M5 rigid-rod polymer filament tenacity"
   - US 8,419,989: PIPD potential tenacity up to ~5.8 GPa, modulus ~310 GPa. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8419989
   - EP 1614778: filament average 3.6 N/tex, 320 GPa. https://data.epo.org/publication-server/rest/v1.2/patents/EP1614778NWA1/document.pdf
   - Akzo, then Magellan, then DuPont; it is unclear whether the fibre will ever be sold. https://taylorandfrancis.com/knowledge/Engineering_and_technology/Materials_science/M5_fiber
6. [x] gap 2 "graphene oxide wet-spun filament highest GPa"
   - Graphene fibre filaments at scale: 1.4 GPa at 1.93 g/cm³ (0.73 N/tex). https://bohrium.dp.tech/paper/arxiv/39274571
   - LC GO fibres 0.15 GPa (arXiv 2602.14290). https://arxiv.org/pdf/2602.14290 · knittable GO fibres 0.14 GPa (Sci. Rep. 2015). https://www.nature.com/articles/srep14946
   - A "7 N/tex" snippet in RSC Adv. 2017 looked garbled; not used.
7. [f] gap 2 "Toray newest carbon fiber grade strongest MPa announced"
   - Toray T1200 (29 Oct 2023): 1,160 ksi (8.0 GPa), 1.82 g/cm³, giving 4.40 N/tex. https://www.toraytac.com/newsroom/news-item/2023/10/29/Toray-Develops-TORAYCA™-T1200,-the-Ultra-High_Strength-Carbon-Fiber · https://texdata.com/news/Yarn&Fiber/19659.html
8. [x] gap 2 in between "launch loop Lofstrom dynamic structure stream supported"
   - Dynamic structures carry loads far above the static strength of their material; Lofstrom's 1985 iron rotor runs at 14 km/s, held down by about twice its weight. https://engrxiv.org/preprint/download/6639/10868/9202 · https://www.nextbigfuture.com/2012/10/server-sky-concept-could-put-millions.html
9. [k] B6 "superconducting levitated ring rotor Earnshaw stability eddy losses high speed" (other groups)
   - Earnshaw: no stable levitation with static fields alone; diamagnets, superconductors and dynamics evade it. https://core.ac.uk/download/71164777.pdf · https://www.osti.gov/servlets/purl/632846
   - Spinning-top levitation without control. https://www.magneticbearings.org/app/uploads/publications/ismb5/ismb5_submission_83.pdf
   - A levitated superconducting current ring needed feedback and eddy-current damping (Cooper et al., 1970). https://scilit.com/publications/3964b2c304d2e605ace9862feea81fac
   - HTS flywheel rotation losses from eddy currents in field inhomogeneity (Physica C 483, 178, 2012). https://www.scribd.com/doc/229625328/1-s2-0-S0921453412002705-main
10. [x] anomaly "Earth flyby anomaly Anderson formula spacecraft"
    - Anderson et al., PRL 100, 091102 (2008): six flybys fitted by an empirical formula. https://link.aps.org/doi/10.1103/PhysRevLett.100.091102
    - Lense–Thirring is negligibly small. https://arxiv.org/pdf/0809.1888 · No velocity-independent force field reproduces the formula. https://ar5iv.arxiv.org/html/0903.0109 · Review: https://arxiv.org/pdf/1711.02875
11. [k] anomaly "Juno flyby anomaly absent tracking result" (other groups)
    - Iorio: absent at Galileo II and at Rosetta II and III; the formula predicted ~7 mm/s for Juno. https://arxiv.org/pdf/1412.7673
    - Juno 2013: absent or at threshold (Acedo et al.). https://ar5iv.labs.arxiv.org/html/1711.08893 · Pre-flyby prediction −6 to −8 mm/s: https://arxiv.org/pdf/1312.1139
12. [f] B6 "REBCO engineering current density 4.2 K 20 T tape kA/mm2 thin substrate"
    - Bruker tape (ARIES): J_e 600 A/mm² at 4.2 K, 20 T; a record of nearly 1,000 A/mm² (2019). https://acceleratingnews-archive.web.cern.ch/acceleratingnews-archive/node/154.html
    - STAR round wire: 586 A/mm² (SuST 32 10LT01, 2019). https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2019/12%20Newly%20Entered%20Pubs%20December%202019/2019%20cited/2019_Next%20generation%20highly%20flexible%20round.pdf
    - Houston thick-film R&D: J_e ~4,600 A/mm² in short samples; 40 m tapes above 4,000 A per 12 mm at 13 T. https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2025/01%20Newly%20Entered%20Pubs%20January%202025/2024%20cited/2024_40-meter-long%20REBCO%20tapes.pdf
    - Field along ab: I_c falls only ~22 % from self-field to 31.2 T in a 4 µm Hf-doped film. https://scite.ai/authors/mehdi-kochat-zlyd3

## Run-6 query log (11 Nov 2026, logged as each search returned)

Step 0: run 5 scored 14 of 14 green (no fixes). Canary6: 13 of 13 run-5 numbers re-derived from state v6 / part 3 inputs (12 within 1 %, one within its logged rounding). Query pre-check: max similarity to earlier runs 0.21, within run 0.27 (a kill query).

1. [f] B6 "Levitated Dipole Experiment floating coil levitation feedback vertical instability" (tag b6-ldx)
   - APEX-LD (IPP, arXiv 2511.07191, 2025): compact no-insulation REBCO floating coil, 7.5 cm radius, ~60 kA-turns persistent, B0 ~0.5 T; levitation over three hours with vertical stability sigma_z < 20 um by FPGA feedback on a lifting coil. https://arxiv.org/html/2511.07191v1
   - APEX record 3.5 h, limited by lifting-coil current; three laser rangefinders, PID on the L-coil current (APS DPP 2023). https://meetings.aps.org/Meeting/DPP23/Session/TP11.12
   - LDX: 560 kg superconducting coil in a 5 m chamber; first flight Feb 2007 (40 min) with digital feedback. https://archive.aps.org/dpp/2007/pp8/144 · "over 80 hours of flight time" (Garnier, FPA 2009) https://fire.pppl.gov/fpa09_LDX_garnier.pdf
   - LDX floating coil is vertically unstable and held by feedback; eddy currents measured with vertical jogs (APS DPP 2009). https://meetings-archive.aps.org/dpp/2009/up8/55/
   - IPP note (Saitoh et al. 2016): levitation force 2 pi r_F N_F I_F B_r; vertical motion stabilized by PID on the levitation-coil current. https://pure.mpg.de/pubman/item/item_2334697_5/component/file_2334719/IPP_17_52.pdf
2. [k] B6 "rotating damping whirl instability supercritical rotor magnetic bearing eddy current" (tag b6-whirl; rotordynamics groups, not levitated-dipole)
   - Genta et al. (Polito): non-rotating damping always stabilizes; damping in rotating parts destabilizes whirl in supercritical running (Dimentberg 1961; Lalanne & Ferraris 1990; Genta 1998); a stationary magnet over a rotating conducting disc can cause severe supercritical instability. https://iris.polito.it/bitstream/11583/1400976/2/583781.pdf
   - ISMB10 #78: forward whirl is permanently amplified above omega_lim = sqrt(k/m)(1 + c_nr/c_r). https://www.magneticbearings.org/app/uploads/publications/ismb10/ismb10_submission_78.pdf
   - Electrodynamic bearings go unstable from rotating damping; cure is stator-side (non-rotating) damping or active dampers. https://www.magneticbearings.org/app/uploads/publications/ismb16/ismb16_076.pdf · https://www.magneticbearings.org/publication/detail/ismb14_73/
   - Passive radial magnetic bearings: very low stiffness and damping, instability regions in the supercritical range unless damping added. https://www.magneticbearings.org/app/uploads/publications/ismb3/ismb3_submission_25.pdf
3. [f] B6 "REBCO critical current 40 T field parallel ab measurement tape 4.2 K" (tag rebco-je)
   - NHMFL torque magnetometry: Ic(B, theta) at 4.2 K for an R&D SuperPower 15 % BZO tape from 5 to 45 T, field in the ab plane and 60 deg off (Bradford et al., arXiv 2502.02706). https://nationalmaglab.org/media/giskvpml/july2025-dc-field-superconductor-testing.pdf
   - Little Big Coil: 45.5 T record in a 31.1 T background; LBC4 reached 44.0 T; screening-current stress is the obstacle above 40 T (PMC 11685629). https://pmc.ncbi.nlm.nih.gov/articles/PMC11685629
   - UNIGE 2025: non-copper Jc routinely above 2 kA/mm2 at 4.2 K, 19 T, field perpendicular. https://indico.cern.ch/event/1431972/contributions/6420066
   - Muon-collider tape: J_e above 2 kA/mm2 at 16 T (perpendicular), 4.2 K (arXiv 2504.21417). https://arxiv.org/pdf/2504.21417
   - Ic is highest with field in the ab plane; ab-plane tilt in commercial tapes (Lu et al., IEEE TAS 33, 6600504, 2023). https://par.nsf.gov/servlets/purl/10534122
4. [f] B6 "AC loss thin superconducting strip perpendicular field Brandt Indenbom" (tag ac-loss)
   - Brandt & Indenbom, PRB 48, 12893 (1993): thin strip width 2a, thickness d, field amplitude H0 perpendicular: P = 4 mu0 a^2 f Jc d H0 g(H0/Hc), Hc = Jc d / pi, g(x) = (2/x) ln cosh x - tanh x (Marchevsky, USPAS 2022). https://conferences.lbl.gov/event/979/contributions/5989/attachments/4086/3486/aclosses.pdf
   - Same formula in US 10,153,071 (per unit length; losses quadratic in strip width). https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10153071
   - Brandt, PRB 49, 9024 (1994), general thin-film formulation. https://ouci.dntb.gov.ua/works/4ELZvBN7
   - Fetch (under 3): PMC 11685629 blocked by a browser check; arxiv.org/abs/2502.02706 off the fetch allowlist (found again by search 13).
5. [f] K2 "coated conductor integrated thermal expansion 4 K measurement Hastelloy copper stabilizer" (tag rebco-cte)
   - No direct dilatometer measurement of a REBCO tape's free shrinkage found (informative absence). CEC-ICMC 2019 dilatometry of magnet materials 293-4 K, 1-2 % accuracy, no tape numbers. https://indico.cern.ch/event/760666/contributions/3391069/contribution.pdf
   - SuperPower SCS4050 surround-Cu tape: E 161 GPa at 5.7 K (141 at 298 K), 0.2 % proof 1045 MPa at 5.7 K (MT-21). https://snf.ieeecsc.org/files/ieeecsc/slides/MT-21_ST169.pdf  -> the 150 GPa tape modulus assumed in I.14/I.16 is within range.
   - Typical tape: 50 um Hastelloy, ~1 um REBCO, 20 um Cu per side, 4 mm wide. https://arxiv.org/pdf/2410.09915
6. [k] K2 "Toray M55J tensile strength modulus elongation" (tag fibre; maker data)
   - Toray M55J fibre: 4,020 MPa, 540 GPa, elongation 0.8 %, 1.91 g/cm3 (Toray TDS as hosted by Rock West). https://www.rockwestcomposites.com/on/demandware.static/-/Sites-rwc-master-catalog/default/dwfad691b5/downloads/Toray_M46J_TDS.pdf
   - Toray CMA M55J data sheet, unidirectional composite: modulus 338 GPa (49 Msi), tensile strain 0.61 %. https://www.toraycma.com/wp-content/uploads/M55J-Data-Sheet.pdf · M55J/cyanate UD laminate 1,896 MPa at 55 % Vf (Toray EX-1515 PDS). https://toraytac-staging.azurewebsites.net/media/57c4813d-ce39-4b11-a5f4-11c3aaeeeef4/14xkyg/TAC/Documents/Data_sheets/Thermoset/UD%20tapes%20and%20prepregs/EX-1515_Cyanate-Ester_PDS.pdf
   -> a loose band pre-strained 0.31-0.32 % keeps only 0.61 - 0.32 = 0.29 % for working strain, less than the tape's 0.63 %: the band, not the tape, sets the ceiling (run-4 error).
7. [f] K1 "Tsinghua Wei group superstrong nanotube fiber centimetre bundle" (tag cnt; data check)
   - No bundle data past a few cm beyond Bai et al. 2018 (informative absence). Physics Today: bundles several cm long, up to 15 tubes each; "about 43 GPa" on the engineering cross-section, against 80 GPa on the tubes' own area. https://physicstoday.aip.org/news/carbon-nanotubes-share-the-load · Tsinghua news (80 GPa). https://www.tsinghua.edu.cn/en/info/1245/5066.htm
   - Fetch nature.com/articles/s41565-018-0141-z: off the allowlist. Open input check for I.11: which area (and density) the 80 GPa uses.
8. [x] X1 "Exodus Propulsion Buhler thrust independent replication" (tag x1)
   - No published independent replication with an outside lab's own apparatus and uncertainty budget (Popular Mechanics, May 2026, as reported). https://okdiario.com/techy/en/?p=5485
   - Claims: 2,000+ vacuum tests, 5-10 mN, reverses with orientation, persists after power cut; APEC talks Jan-May 2026; seeking an in-orbit demo. https://www.pulse.bot/aerospace/news/exodus-propulsion-and-the-exodus-force-aka-electrostatic-pressure-force-f751b722-b207-434d-be9c-2deda6453224/ · https://www.thebrighterside.news/space/nasa-veteran-unveils-propellant-free-space-drive-that-could-redefine-exploration/ · https://geekchamp.com/?p=1064374
13. [f] B6 "Bradford Larbalestier torque magnetometry REBCO 45 T critical current flux jumps" (tag rebco-je)
   - Jaroszynski et al., arXiv 2502.02706 (Feb 2025): torque Ic(B, theta) to 45 T on 200+ samples; in the ab plane Ic decays exponentially with B; lengthwise Ic variation in edge-cut 12 mm tapes. https://arxiv.org/html/2502.02706v2
   - Fetch (2 parts): production SuperPower 15 % BZO tapes carry 700-2000 A at 30 T, 4.2 K, ab plane (width not stated); R&D sample Ic falls ~40 % from 5 to 30 T (B0 ~ 40 T). Flux jumps at 4.2 K always for REBCO 3.0-5.0 um thick, sporadic at 1.4-1.8 um, never at 1.12 um; more likely at high field; up to 7 K rise.
   -> the thick films behind B6's 4.6 kA/mm2 are the ones that flux-jump at 4.2 K during field sweeps.
9. [k] X1 "charged dielectric thruster sealed enclosure vacuum torsion balance null" (tag x1; other groups)
   - Exodus's own patent US 11,511,891 ("asymmetrical electrostatic pressure") cites Canning (2004): most asymmetric capacitors show null thrust without ion wind; no force in a vacuum bell jar. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11511891
   - Exodus test fixture: grounded ITO Faraday enclosure, thin dielectrics, a "walk-in" transient when charging and a relaxation after power-off attributed to charge retained in the dielectric (Medium interview). https://medium.com/predict/charles-buhler-and-exodus-technologies-on-propellantless-propulsion-1919cfd2b8d9
   - TU Dresden (Tajmar & Fiedler, JPC 2015): EMDrive "thrust" also in directions that should give none; balance returned to zero only slowly after power-off, as if charged: a known artefact signature. https://tu-dresden.de/die_tu_dresden/fakultaeten/fakultaet_maschinenwesen/ilr/rfs/forschung/folder.2007-08-21.5231434330/ag_raumfahrtantriebe/JPC - Direct Thrust Measurements of an EM Drive and Evaluation of Possible Side-Effects.pdf · https://www.scribd.com/document/273014789/6-2E2015-4083
   - Eagleworks 1.2 mN/kW (2016) with a null test article; later not reproduced (Dresden 2021, ledger 13). https://ntrs.nasa.gov/api/citations/20170000277/downloads/20170000277.pdf
10. [x] gap 8 in between "epitaxial compressive strain equivalent hydrostatic pressure nickelate film superconductivity" (tag strain-p)
   - Bilayer nickelate films: -2.01 % strain on SrLaAlO4 gives ambient-pressure superconductivity with onset near 40-42 K; in-plane compression expands c by Poisson, unlike hydrostatic pressure (arXiv 2608.01295; PARADIM / Nature 653, 76, 2026). https://arxiv.org/pdf/2608.01295 · https://www.paradim.org/node/924
   - Required strain nearly halved to -1.2 % on LaAlO3 (arXiv 2510.27613). https://synapsesocial.com/papers/6990113f2ccff479cfe57c50 · ~2 % strain, ARPES study (PRX, July 2026). https://journals.aps.org/prx/pdf/10.1103/4h5x-btvx
   - Trilayer La4Ni3O10: compressive strain is not a complete analogue of pressure; no superconductivity in films (arXiv 2606.20941). https://arxiv.org/pdf/2606.20941
11. [k] gap 8 in between "metal hydride epitaxial film lattice mismatch maximum strain GPa equivalent" (tag strain-p; hydride-film groups)
   - Clamped Nb-H films below ~6-8 nm stay elastic to about -10 GPa compressive stress; thicker films yield at -2 to -3 GPa (Pundt group). https://scite.ai/authors/magnus-hamm-Ea36RW · https://dspacecris7.sub.uni-goettingen.de/entities/publication/3332babb-c4f5-41c6-94c8-eb8416883a53 · Nb-Fe films -4.6 GPa (KIT). https://publikationen.bibliothek.kit.edu/1000139556/175182274
   - Epitaxial rare-earth hydride films exist (LaH2, 2025) but only low hydrides. https://pubs.rsc.org/en/content/articlelanding/2025/lf/d4lf00367e
   -> strain or clamping supplies <= ~10 GPa; superhydrides need 100-260 GPa: no strain route for hydrides.
12. [x] B6 in between "Inductrack passive electrodynamic levitation lift drag ratio speed stability" (tag inductrack)
   - Post, Inductrack: L/D = omega L / R = 2 pi v L / (lambda R); L/D 200:1 or more at speed; Earnshaw-stable levitation with no control above a transition speed of a few km/h; needs a moving Halbach array over passive circuits. https://typeset.io/pdf/the-inductrack-a-simpler-approach-to-magnetic-levitation-3rf5vuf4gz.pdf · https://mae.ufl.edu/nkim/Papers/conf37.pdf
   - Electrodynamic levitation still needs a minimum damping for stability (Galluzzi et al. 2026; Circosta et al., ISMB17). https://iris.polito.it/retrieve/handle/11583/2825845/365794 · https://www.magneticbearings.org/app/uploads/publications/ismb17/ismb17_005.pdf
