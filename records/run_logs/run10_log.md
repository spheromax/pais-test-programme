# Run 10 search log (logged as each search returned)

Kinds: f forward, k kill, x exploration, r re-check, s source recovery. Searches 1–8 were run again after a context reset (same wording, same day); their results are logged once.

## Planned searches

1. [f, field-homog] "Iseult 11.7 tesla whole-body magnet field homogeneity ppm measured"
   - Boulant, Quettier et al., MAGMA 36, 175 (2023): NbTi, 11.72 T, 1,470 A, 1.8 K, 308 H, 338 MJ, 132 t; spec < 0.5 ppm peak to peak on a 22 cm sphere, stability 0.05 ppm/h. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10140097/
   - ISMRM 2022 abstract 0382: measured 0.88 ppm peak to peak (RMS 0.15 ppm) with passive and cryo shims only (Metrolab field camera). https://cds.ismrm.org/protected/22MProceedings/PDFfiles/0382.html
   - Prototype double-pancake model coil (IEEE TAS 19, 2253, 2009) shows the winding method can reach the bare-magnet spec. https://www.osti.gov/servlets/purl/1023595
2. [f, emissivity] "high emissivity black coating cryogenic 20 K hemispherical emissivity measurement"
   - Copp, Tuttle et al., Cryogenics 64, 240 (2014): Ball IR Black ε ≥ 0.95 from 30 to 300 K for all area densities. https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........289a54d33970ebd022373d55775543e9
   - Tuttle et al. (NASA GSFC): most black paints drop steeply below about 100 K. https://ntrs.nasa.gov/citations/20180000042
   - Acktar Fractal Black, TFAWS 2023 (5–300 K): 0.8–0.9 and flat at 40–300 K; falls significantly below about 50 K (coating partly transparent at long wavelengths); 30 µm is the useful thickness. https://tfaws.nasa.gov/wp-content/uploads/TFAWS23-CR-1-Presentation.pdf
3. [k, b6-graze] "oblique hypervelocity impact grazing angle ricochet debris sliding along plate"
   - Schonberg et al. (NASA MSFC, 1988–1999): ricochet debris; the most damaging ricochet particle is up to 40 % of the projectile diameter at 24–36 % of the impact speed (flat plates). https://core.ac.uk/works/24878686 ; model https://ntrs.nasa.gov/api/citations/19990116783/downloads/19990116783.pdf
   - SPH, 3–6 km/s Al on Al: at 30–45° the projectile slides and back-splashes. https://seejournal.cn/article/doi/10.12126/see.2021.06.002
   - Inclined-plate lattice shield redirects debris by repeated ricochet (arXiv 2512.16611, 2025). https://arxiv.org/pdf/2512.16611
   - No test of debris sliding along a curved, concave wall at ≥ 3 km/s found. Kill search: no kill.
4. [f, lgg] "two-stage light gas gun flat plate projectile orientation sabot facility 7 km/s"
   - SwRI large LGG: 38 mm launch tube, 22 m gun, top speed 7 km/s, 0.5 kg at 3 km/s, 1.4 kg at 2 km/s; launches fragments and flyer plates. https://Swri.org/sites/default/files/brochures/large-two-stage-light-gas.pdf
   - JHU HyFIRE 1–7 km/s, 2- and 4-piece sabots (https://hemi.jhu.edu/facilities/hyfire); Illinois HIT lab 3–5 mm at > 7 km/s (https://aerospace.illinois.edu/research/research-facilities/space-testing-equipment-services/hit-lab); TAMU 0.8–12.7 mm at 1.5–8 km/s (https://telacyjr.engr.tamu.edu/facility); LLNL 0.485 g at 7.77 km/s, 7.6 mm bore (DOI 10.2172/7047151).
5. [k, rebco-thick] "long-length thick REBCO tape critical current uniformity variability performance drop"
   - Jaroszynski et al., arXiv 2502.02706 (2025), torque magnetometry to 45 T: large lengthwise Ic variation in samples cut every 20 m (4.2 K, 30 T); flux jumps in samples with thick REBCO and thin stabilizer. https://arxiv.org/pdf/2502.02706
   - NHMFL (Jaroszynski, 2018): low c-axis pinning looks harmless at 77 K but halves low-temperature performance; production scatter fell from 5 % to 1–2 %. https://conferences.lbl.gov/event/133/contributions/287/attachments/117/921/JAROSZYNSKI_JAX.pdf
   - UH: 50 m thin-substrate tape, Ic uniformity 2.2 %, dropouts < 10 % (SuST 2020). https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2020/08%20Newly%20Entered%20Pubs%20August%202020/2020%20cited/2020_Progress%20in%20scale-up.pdf
   - US 12,256,649 (QC of tapes): the orientation of BaMO3 nanocolumns sets the low-temperature lift factor; doped tapes scatter widely at 30 K, 3 T. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12256649
6. [f, rebco-ic-T] "thick-film coated conductor lift factor versus temperature Houston tape 30 kelvin"
   - US 10,818,416 / US 11,488,746 (Selvamanickam): lift factor at 3 T, B∥c: 4.1 at 30 K, 4.64 at 25 K, 5.67 at 20 K for one film. https://patents.google.com/patent/US10818416
   - Senatore et al. (arXiv 1512.01930): Jc changes by e^(−ΔT/T*) and the lift depends only on B. https://arxiv.org/pdf/1512.01930
   - 40 m A-MOCVD tapes: > 4,000 A/12 mm at 4.2 K, 13 T; > 1,400 A/12 mm at 20 K, 20 T (already on file, run 9).
7. [f, k3c60-film] "alkali fulleride thin film ultrafast optical spectroscopy pump probe molecular beam epitaxy"
   - Adelinia et al., Struct. Dyn. 12, 024503 (2025): MBE K3C60 on sapphire, grains ~100 nm, broad transition; ultrafast voltmeter. https://qcmd.mpsd.mpg.de/wp-content/uploads/2025/03/Adelina-structural-dynamics-2025.pdf ; thesis https://ediss.sub.uni-hamburg.de/bitstream/ediss/11591/1/Adelinia2025_Ultrafast_transport_experiments_on_optically_driven_K3C60.pdf
   - Wang et al., arXiv 2301.06425: MBE films, Tc = 19 K, in coplanar THz waveguides. https://arxiv.org/pdf/2301.06425
   - Review of MBE AxC60 films on graphene/SiC (AAPPS Bull. 2021). https://link.springer.com/10.1007/s43673-021-00031-2
   - Same group as the claim. No independent group found.
8. [k, k3c60] "Rb3C60 photoexcitation metastable superconductivity mid-infrared pressure"
   - Nothing new: Budden et al. (Nat. Phys. 2021), Rowe et al. (Nat. Phys. 2023, 10 THz), pressure tuning (features vanish near 0.3 GPa), arXiv 2502.20276 (the field-expulsion search, ledger 35). No independent replication. https://ora.ox.ac.uk/objects/uuid:1f44f968-40da-4d18-9abb-20557cc296e5
9. [f, b7-fel] "FELIX laboratory intracavity FELICE user experiment solid state sample"
   - FELICE: 3–100 µm intracavity line; user stations are a molecular beam and an FTICR cell (gas phase); Rayleigh range 55 and 82 mm. https://wiki.felix.science.ru.nl/FELICE
   - First lasing (FEL 2007): 4-mirror 9 m resonator, 5 cm Rayleigh range; 10 µJ outcoupled ≈ 400 µJ intracavity per micropulse; limited access during operation. https://epaper.kek.jp/f07/TALKS/MOAAU04_TALK.PDF
   - No solid-state intracavity user experiment found. Hardware stays C.
10. [k, x1] "Exodus Buhler thruster third-party verification latest"
   - NextBigFuture (31 Mar 2026): no third-party test, no peer review; Buhler chose not to seek peer review first; patent WO2020159603A2. https://www.nextbigfuture.com/2026/03/exodus-propulsion-and-the-electrostatic-pressure-force.html
   - APEC profile (~Apr 2026): needs third-party validation. https://www.altpropulsion.com/people/charles-buhler/ ; APEC device page claims verification by "two outside groups" (unnamed) and a shift to battery-driven charge injection. https://www.altpropulsion.com/exodus/
   - chriswest.tech (~Jul 2026): not independently verified; a paper in preparation; 4,500+ tests claimed. https://www.chriswest.tech/article/wheres-my-hoverboard
   - No change.
11. [x, hf-grav] "high-frequency electromagnetic field gravity coupling experiment balance search"
   - Only the steady-field study (Tajmar, Kößling, Neunzig, Sci. Rep. 14, 2024; DOI 10.1038/s41598-024-70286-w). No high-frequency follow-up found. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11339412/
   - Bridge: Brack et al. (ETH, arXiv 2201.03420): dynamic gravitational coupling between resonating beams at 42 Hz; detector amplitude up to 10⁻¹¹ m, sub-pm resolution, 2.5×10⁻²⁰ J/s energy flow, d⁻⁴, 3 % agreement with theory. https://arxiv.org/abs/2201.03420v1
12. [x, grav-patents] "gravitational field generator patent electromagnetic granted 2023 2024 2025"
   - USPTO Gazette entry for US 12,417,870 B1 (Zhang; on file). https://patentsgazette.uspto.gov/week37/OG/html/1538-3/US12417870-20250916.html
   - CPC B64G1/417 listing (ipiq.io): US 2024/0063731 "Propulsion system, inertia attenuator and force field generator"; US 2024/0375795 "Electromagnetic propulsion device for generating unidirectional force"; US 2025/0132082 "Propulsion system using force field generating coils" (electrons accelerated in D-shaped housings, radiation propels); US 2025/0286480 "Magnetic field propulsion unit"; US 2025/0296708 "Tilt drive for electromagnetic force vectoring"; US 12,442,361 "Photon drive and photon turbine"; an HFGW generator (gas shell, microwave emitters, acoustic cavities). https://ipiq.io/patent_classifications/cpc_subgroups/74718 ; https://ipiq.io/patent_classifications/cpc_subgroups/74718?page=3+3
   - US 2025/0055389 "Voorhees Anti-Gravity Engine II": pulsing field "to decouple the Higgs field". https://ipiq.io/patents/6232272
   - A promotional site pairs the Zhang patent with Pais's; it gives no data. https://unifiedfieldtheory.vercel.app/en/comparison/navy-patents
13. [x, bridge] "SPARC toroidal field model coil 20 tesla stored energy quench test result"
   - Hartwig et al., IEEE TAS 34, 0600316 (2024): 20.1 T at 40.5 kA, 815 kN/m on the REBCO, 10,058 kg, 270 km of tape, 600 W at 20 K; an intentional open-circuit quench at 31.5 kA caused local damage. https://arxiv.org/pdf/2308.12301
   - LaBombard (SNF 57, 2024): 16 pancakes, 256 turns, 40 kA, 20 K, 110 MJ; not self-protecting. https://snf.ieeecsc.org/files/ieeecsc/2024-10/LaBombard%20abstract.pdf
14. [x, hfgw] "high-frequency gravitational wave detector MHz GHz upper limit superconducting cavity"
   - Fischer et al., CQG 42, 115015 (2025): first characterization of the MAGO SRF cavity (kHz–MHz). https://bib-pubdb1.desy.de/record/617735/files/Fischer_2025_Class._Quantum_Grav._42_115015.pdf
   - Kim et al., arXiv 2511.17817: re-analysis of CAPP-12T axion data; 90 % limit h0 ≈ 3.9×10⁻²¹ near 5.3 GHz. https://www.arxiv.org/pdf/2511.17817
   - Overview (Jan 2026): cavities reach h ~ 10⁻²¹ at 250–330 MHz and ~10⁻²⁰ at 2.5–3.4 GHz. https://api.emergentmind.com/topics/high-frequency-gravitational-waves ; SONAR (ERC, 10 kHz–100 MHz) https://cordis.europa.eu/project/id/101266094
15. [x, grav-patents-2] "Espacenet antigravity propulsion device patent electrostatic coil"
   - Older family: US 3,095,167 (charge a missile against Earth's charge), US 3,610,971 (motional electric field, "antigravitational phenomena"), US 2003/0209637 A1 (rotating electrostatic field, "spacetime curvature tension"; abandoned), US 3,120,363 (Electronatom lifter), US 3,071,705 (electrostatic fluid propulsion). https://patents.google.com/patent/US3095167A ; https://patents.google.com/patent/US3610971A ; https://patents.google.com/patent/US20030209637A1 ; https://patents.google.com/patent/US3120363 ; https://patents.google.com/patent/US3071705
   - The project's own file, US 2006/0145019 A1 (triangular spacecraft: line charges at the corners, plane wave from the hull), turned up as a hit; B64G1/409. https://users.libero.it/jmbalzan/ETH/US20060145019A1%20-%20Triangular%20spacecraft%20-%20Google%20Patents.pdf

## Follow-up lookups (added after the plan; reported separately for novelty)

16. [k, field-homog] "screening current induced field REBCO coil field error ppm non-axisymmetric harmonics measurement"
   - Bang et al., Sci. Rep. (Aug 2024): 9.4 T all-REBCO NMR magnet; over 100 ppm difference between designed and measured field; even harmonics from screening current, odd from tape thickness; sub-ppm "barely possible" with present design. https://pmc.ncbi.nlm.nih.gov/articles/PMC11333634 ; https://doaj.org/article/864d0103bd704f2a982d467962dd8a64
   - Simulation: screening-current field up to 0.8 T, 7.8 % at the centre of high-field REBCO coils (Shi & Liang, J. Supercond. Nov. Magn. 35(12), 2022). https://searchworks.jioinstitute.edu.in/articles/asx__160140430
   - Remedies: current overshoot and field shaking (Changwon). https://koreascience.kr/article/JAKO201810263411681.pdf
17. [s] TFAWS 2023 paper (fetch): Fractal Black 60–90 % between 15 and 300 K, dropping significantly below about 50 K; no numbers below 40 K in the text. https://tfaws.nasa.gov/wp-content/uploads/TFAWS23-CR-1-Paper.pdf
18. [s] arXiv 2201.03420 abstract (fetch): numbers for item 11's bridge.
