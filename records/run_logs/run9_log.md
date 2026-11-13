# Run 9 search log (logged as each search returned)

Kinds: f forward, k kill, x exploration, r re-check, s source recovery. Side research (not scored) at the end.

## Planned searches

1. [f, rebco-ic-T] "Faraday Factory tape in-field critical current 20 K 30 K data sheet"
   - Senatore (Geneva), HiTAT slides, CERN indico: Ic/width 1094–1218 A/cm at 4.2 K, 19 T and 341–460 A/cm at 20 K, 19 T (B ⊥ tape); α = 0.75 above 10 T (4.2 K); Ic∥/Ic⊥ = 3.5–3.8; T* = 21–23 K below 40 K. https://indico.cern.ch/event/1220254/contributions/5270668/attachments/2607765/4504754/HiTAT-Senatore.pdf
   - Molodyk, "Production of 2G HTS tape at Faraday Factory Japan", ICMC 2024 (lift factor at 20 K, 20 T by lot). https://indico.cern.ch/event/1296489/contributions/5881530/attachments/2902968/5091645/Molodyk-Wed-Or12.pdf
   - NHMFL ASC 2024: Ic(B, T) of 4 mm tape 15–55 K in a 31 T magnet; 242 A at 20 K, 20 T (⊥, 20 % Zr). https://maglabweb.magnet.fsu.edu/media/kgwbyvp4/august-2024-asc-measuring-transport-dependencie-rebco-tapes.pdf
   - Southampton/CERN, four makers' Ic (TASC 2025). https://eprints.soton.ac.uk/500774/1/TASC.2025.3543797.pdf
2. [f, rebco-thick] "thick film REBCO production length 30 tesla engineering current density Houston advanced MOCVD"
   - Majkic et al., SuST 2020 letter: 4.0 µm film with 15 % Hf, Jc (B∥ab) 40.5 and 36.3 MA/cm² at 14 and 30 T; J_e estimate uses a 50 µm tape. https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2020/06%20Newly%20Entered%20Pubs%20June%202020/2020%20cited/2020_In-field%20critical%20current%20performance.pdf
   - Majkic et al., SuST 31, 10LT01 (2018): J_e > 5 kA/mm² at 4.2 K, 14 T (B∥c). https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2018/12%20Newly%20Entered%20Pubs%20December%202018/2018%20cited/2018_Engineering%20Current%20Density.pdf
   - "40-meter-long REBCO tapes with critical current over 4,000 A/12 mm", Superconductivity 9, 100081 (2024). https://public.magnet.fsu.edu/AToth/NSF%20publication%20access/2025/01%20Newly%20Entered%20Pubs%20January%202025/2024%20cited/2024_40-meter-long%20REBCO%20tapes.pdf
   - Selvamanickam, FNAL slides: 50 m A-MOCVD tape 3.5× typical commercial Ic at 4.2 K, 20 T; STAR wires > 2.5 kA at 4.2 K, 30 T. https://indico.fnal.gov/event/61772/attachments/172362/233757/selvamanickam%20venkat.pdf
3. [f, hts-db] "HTS wire critical current database Robinson Research Institute angular field temperature"
   - Wimbush & Strickland, IEEE TAS 27, 8000105 (2017); figshare collection, Ic(T, B ≤ 8 T, angle) 15–90 K. https://figshare.com/collections/A_high_temperature_superconducting_HTS_wire_critical_current_database/2861821
4. [k, b6-dyn] "momentum-supported structure stream break failure consequences energy release analysis"
   - No failure analysis of a dynamic (momentum-supported) structure found. Closest: Slepyan et al., transition (failure) wave in a supported beam, propagates when the energy release is positive. https://arxiv.org/pdf/1212.5492 ; energy-based progressive collapse (ASCE 2009). https://ascelibrary.com/doi/10.1061/41031%28341%29138
5. [f, b6-vessel] "explosive containment vessel rated charge kg TNT vessel weight composite"
   - LLNL composite vessel: 2 m diameter for 35 kg TNT; 1 m half-scale vessels tested to 150 % with 8.2 kg C-4. https://www.osti.gov/biblio/15014483
   - LANL M-9 HY-100 steel vessel, 10 kg TNT, weight limit 75 t. https://apps.dtic.mil/sti/pdfs/ADA525803.pdf ; proof test https://apps.dtic.mil/sti/pdfs/ADA499952.pdf
   - TDC detonation chamber: 88-ton steel, 40 lb TNT. https://www.osti.gov/servlets/purl/1641147
   - Sandia EDS V31: 11 kg TNT for 1092 shots. https://www.sandia.gov/research/publications/details/results-of-the-explosive-destruction-system-p3-vessel-qualification-2023-07-01/ ; V28 static rating 2800 psi https://www.osti.gov/servlets/purl/1600620
   - US 6,644,165 explosion containment vessel, 10 kg TNT. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6644165
6. [x, b6-virial] "virial theorem pressure vessel minimum mass gas energy containment bound"
   - Gas virial 2⟨E_kin⟩ = 3pV (arXiv physics/0305011). https://arxiv.org/pdf/physics/0305011
   - 3(γ − 1)E_i + Ω = 0; coefficient 2 for γ = 5/3 (Axion Astrophysics review). https://arxiv.org/pdf/2411.02492
   - Pressure-vessel minimum mass ∝ PVρ/σ (design note). https://www.scribd.com/document/249274159/Design-Parameters
   - No prior art found for a magnetic stator doubling as burst containment.
7. [x, b6-torque] "rotatable containment liner flywheel torque transmitted housing reduction"
   - US 6,889,577: liner released above a torque threshold, then rides on a fluid film. https://patents.google.com/patent/US6889577
   - US 11,143,277: free-spinning liner absorbs the burst rotor's angular momentum (0.5 in 4130 steel). https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11143277
   - UT-CEM rotatable composite containment (DARPA/DOT program): burst at ~40,000 rpm, rotor and liner spin down together in ~2 min. https://core.ac.uk/download/322358635.pdf ; SAE 2004-01-0005 https://saemobilus.sae.org/content/2004-01-0005/
8. [f, b6-hvi] "Whipple shield ballistic limit equation areal density 7 km/s aluminum projectile"
   - Modified Cour-Palais equation, C = 0.16, valid for V_n ≥ 7 km/s (NASA JSC memo). https://ntrs.nasa.gov/api/citations/19920010826/downloads/19920010826.pdf
   - Regimes: ballistic < 3 km/s, shatter 3–7 km/s, melt/vapour > 7 km/s (Padova 2024). https://research.unipd.it/retrieve/45663415-bcaa-43c6-9d9f-06e0aad98670/1-s2.0-S0094576524001280-main.pdf
   - Stuffed Whipple shields, 1.71 g/cm² total (Christiansen). https://zenodo.org/records/1258555/files/article.pdf
9. [f, k3c60-film] "K3C60 thin film MBE growth superconducting transition temperature encapsulation air"
   - MBE films avoid bulk air sensitivity and phase separation; in-plane C60 spacing 8.1 Å (AAPPS Bull. 2021 review). https://link.springer.com/article/10.1007/s43673-021-00031-2 ; https://www.arxiv.org/pdf/2202.05968
   - K3C60 films on bilayer graphene/SiC, nodeless gap (ARPES). https://arxiv.org/pdf/2304.13914
   - K3C60 on Si(111): 1–140 ML at ~2 ML/h, superconducting down to ≥ 25 ML; 0.35 mΩ cm at 100 K (Delft, PRB 2003). https://arxiv.org/pdf/cond-mat/0206221
   - Rb3C60 films 3–9 ML, T_c up to 23 K. https://export.arxiv.org/pdf/2102.07914
10. [f, b7-fel] "FELIX FEL-2 small-signal gain outcoupling hole losses 30 micron wavelength"
   - FHI mid-IR FEL: computed single-pass gain > 200 % for 1 ps bunches at 7–30 µm; 1 % mirror loss. https://accelconf.web.cern.ch/FEL2012/papers/moob01.pdf
   - ELBE U100: measured 10 % loss per pass at 30 µm with a 2 mm hole. https://accelconf.web.cern.ch/f07/PAPERS/MOPPH036.PDF ; design gain > 25 % over the range, losses ≤ 6 % without outcoupling https://epaper.kek.jp/f05/PAPERS/TUPP031.PDF
   - FELIX FEL-2 hole coupling study (van der Meer, FEL 2012). https://jacow.org/FEL2012/papers/WEPD40.pdf ; FELIX FEL-1 measured gain and losses near tuning gaps (FEL 2010) https://jacow.org/FEL2010/papers/TUOC4.pdf
11. [k, k3c60] "optically driven K3C60 2026 magnetic expulsion transport measurement independent group" (extended)
   - de Vecchi et al., "Upper limit on magnetic field expulsion in optically driven K3C60", Phys. Rev. Research 7, 043270 (Dec 2025): ~50 nT resolution, χ_v > −0.1; claimant's group. https://arxiv.org/abs/2502.20276 ; https://journals.aps.org/prresearch/abstract/10.1103/21g5-x5bj
   - Wang et al. (2023), "Superconducting nonlinear transport in optically driven high-temperature K3C60": thin films on photoconductive switches, granular superconducting-like response. https://www.researchgate.net/publication/375523521_Superconducting_nonlinear_transport_in_optically_driven_high-temperature_K3C60
   - No independent-group replication found.
12. [x, b7-src] "30 micron difference frequency generation high average power watt laser source"
   - Nothing near 30 µm at watt level: best DFG combs 6.7 W at 2.9 µm (NIST, Opt. Lett. 2020) https://tf.nist.gov/general/pdf/3085.pdf ; watt-scale intrapulse DFG in the fingerprint region (Gaida et al., LSA 2018) https://typeset.io/pdf/watt-scale-super-octave-mid-infrared-intrapulse-difference-1mff8409jd.pdf ; long-wave combs limited by crystal damage and multiphonon absorption https://bib-pubdb1.desy.de/record/434790/files/oe-28-2-1369.pdf
13. [k, x1] "asymmetric electrostatic pressure thruster replication attempt university vacuum chamber" (extended)
   - No outside replication. Latest coverage: altsci.net (about late Oct 2026), interview-based. https://www.altsci.net/charles-buhler-exodus-technologies-propellantless-propulsion/ ; >1500 test articles, ±20 µN, force persists while plates stay charged https://www.altpropulsion.com/propellantless-propulsion-vacuum-chamber-test/
   - US 11,511,891 (cites Talley 1991: vacuum force attributed to chamber interaction). https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11511891 ; US 2024/0011469 A1 https://patents.google.com/patent/US20240011469A1/en
14. [k, x1-ctrl] "micro-thrust balance electrostatic artifact charged dielectric residual charge neutralization ionizer"
   - Weighing practice: charge on a sample gives force errors; ionizers neutralize until a sensor reads neutral (US 12,523,519). https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12523519 ; residual potential and ion balance (US 7,973,292) https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7973292
   - Air ionizers need gas: in vacuum the control must be UV photoemission, an electron flood or a bake.
15. [x, bridge] "patents citing US10144532 inertial mass reduction craft cited by"
   - Status "Expired – Fee Related" confirmed; no citing patents surfaced. https://patents.google.com/patent/US10144532 ; Pais portfolio 7 patents, 6 families (GreyB) https://insights.greyb.com/?p=33581 ; AIAA 2017-5343 and 2019-0869 (HAUC, room-temperature superconducting system)
16. [x, b6-ipacs] "integrated power and attitude control system flywheel spacecraft NASA counter-rotating"
   - Roithmayr et al., NASA/TP-2003-212178 (IPACS with counter-rotating flywheels and CMGs). https://ntrs.nasa.gov/api/citations/20030014715/downloads/20030014715_V2.pdf
   - Roithmayr, ISS attitude motion with flywheel storage: contingency of one rotor stopping abruptly while the other spins. https://ntrs.nasa.gov/api/citations/20040086750/downloads/20040086750.pdf
   - US 6,113,033 combined flywheel storage and attitude control (counter-rotating pairs). https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6113033 ; CARES (1985) https://ntrs.nasa.gov/citations/19850005550 ; MagneMotion shaftless maglev flywheel (AAS 02-066) https://ntrs.nasa.gov/api/citations/20020034156/downloads/20020034156.pdf

## Follow-up lookups (added after the plan; reported separately for novelty)

17. [fetch, b6-torque] UT-CEM rotatable composite containment paper: burst at 39,500 rpm; torque into the housing never above 63,000 ft-lb (design predicted 400,000); spin-down 120 s; no masses or energy given. https://core.ac.uk/download/322358635.pdf
18. [fetch, b6-vessel] LLNL composite vessel record: 2 m diameter, 35 kg TNT; no mass given. https://www.osti.gov/biblio/15014483
19. [fetch, bridge] Google Patents, US 10,144,532 B2: cited by three later private filings: US 10,669,973 B2 (Currie, rotating RF resonant-cavity turbine, 2020), DE 11 2022 000 319 T5 (Martins, drive system and force-field generator, 2023), US 12,553,420 B2 (Orduthowski, vehicle propulsion unit, 2026); family citation US 10,135,366 (Pais). Legal events: fee reminder 2022-07-25, lapse effective 2022-12-04, recorded 2023-01-09/31. https://patents.google.com/patent/US10144532B2/en
20. [x, x1-uv] "LISA Pathfinder test mass charge management UV light discharge force noise" (added exploration: a bridge for X1's control)
   - Armano et al., PRL 118, 171101 (2017): charge-induced force on free-falling test masses measured; discharge by UV photoemission as on Gravity Probe B. https://link.aps.org/accepted/10.1103/PhysRevLett.118.171101
   - Armano et al., PRD 98, 062001 (2018): precision charge control with Hg lamps (254 nm). https://link.aps.org/accepted/10.1103/PhysRevD.98.062001
   - PRD 106, L101101 (2022): test-mass charge modulated sinusoidally by phasing UV pulses, to read stray potentials from the force. https://link.aps.org/accepted/10.1103/PhysRevD.106.L101101
   - Dal Bosco, PhD thesis (Trento): torsion-pendulum tests of the LISA UV-LED charge management system. https://iris.unitn.it/retrieve/ca664949-61b7-4859-b828-25284e6b5d86/PhD%20thesis%20-%20Davide%20Dal%20Bosco%20-%20corrected.pdf
   - UV discharge systems review (expected LPF charge up to ±2.35×10⁸ e). https://ar5iv.arxiv.org/html/1207.0394
