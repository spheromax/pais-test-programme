"""Loop health test: is the Pais gap loop degrading?  Scores each run on measurable signals.
Usage: add the new run to RUNS (each query as (text, topic tag, kind f|k|x|r), kills, leads kept, gaps changed, errors caught,
hits, circularity, source domains used, canary result, prompt sizes old/new, repeated queries that found a new fact,
queries whose main source was already cited), then: python3 pais_loop_health.py <run number>.
Kinds: f forward, k kill, x exploration, r planned re-check, s source-recovery (a search redone because its result was not written down).
Thresholds were fixed in run 3 before any run was scored; change them only with a logged reason.
Signal 14 (rework: searches redone inside one run) was added in run 4 because the repeat signal compares only with EARLIER runs and
missed run 4's three source-recovery searches; its thresholds (green <= 0.07, red > 0.15) were set before it was computed."""
import json, re, sys
STOP = set('a an the of in on at to for and or with by from vs via is are be as into over under up 2021 2022 2023 2024 2025 2026 2018 2019 2020 '
           'results result new latest record records'.split())
def toks(q):
    return {t for t in re.findall(r'[a-z0-9]+', q.lower()) if t not in STOP and len(t) > 1}
def jac(a, b):
    return len(a & b) / max(1, len(a | b))

RUNS = {
 1: dict(queries=[
   ('Navy tested Pais effect experiments results funding War Zone FOIA', 'pais-test', 'x'),
   ('Tajmar 2021 EMDrive high-accuracy thrust measurements false positive thermal', 'emdrive', 'x'),
   ('DART momentum enhancement factor beta 3.6 Dimorphos Nature 2023', 'dart', 'f'),
   ('all-superconducting magnet world record tesla 2025', 'magnet', 'f'),
   ('ambient pressure superconducting transition temperature record 151 K Hg-1223 pressure quench', 'hg1223', 'f'),
   ('carbon nanotube fiber tensile strength record GPa 2025', 'cnt', 'f'),
   ('LUXE E-320 FACET-II strong-field QED Schwinger critical field electron laser collision results 2025', 'sfqed', 'f'),
   ('metastable photo-induced superconductivity K3C60 nanoseconds Budden 2021 resonant enhancement 10 THz Rowe 2023', 'k3c60', 'f'),
   ('1200 tesla indoor magnetic field record electromagnetic flux compression Takeyama 2018', 'pulsed-magnet', 'f'),
   ('hydride superconductor highest Tc 2025 La-Sc-H room temperature high pressure', 'hydride', 'f'),
   ('composite flywheel rotor maximum tip speed m/s carbon fiber record spin test', 'flywheel', 'f'),
   ('microfluidic cooling heat flux 1.7 kW/cm2 Nature 2020 van Erp co-designing electronics', 'cooling', 'f'),
   ('supertetragonal BiFeO3 giant polarization 150 uC/cm2', 'ferroelectric', 'f'),
   ('10 THz source high power GaN quantum cascade laser Reststrahlen band 5-12 THz gap', 'thz-source', 'f')],
   kills=0, leads_kept=6, progress=7, errors_caught=[], repeat_errors=0, hit=(14, 14), circular=0.0,
   domains=['twz.com', 'fis.tu-dresden.de', 'pdf.arxiv.org', 'refubium.fu-berlin.de', 'energy.mit.edu', 'english.iop.cas.cn',
            'nationalmaglab.org', 'issp.u-tokyo.ac.jp', 'physicsworld.com', 'arxiv.org', 'science.gov', 'english.imech.ac.cn',
            'data.zhenzhi.com', 'lasphys.com', 'scholar.gist.ac.kr', 'phys.org', 'ora.ox.ac.uk', 'infoscience.epfl.ch', 'eta.lbl.gov'],
   canary=None, prompt_chars=None),
 2: dict(queries=[
   ('photo-induced superconductivity K3C60 2025 2026 new results lifetime repetition rate', 'k3c60', 'f'),
   ('Dodge optical saturation spurious evidence photoinduced superconductivity K3C60', 'k3c60', 'k'),
   ('Budden 2021 metastable photo-induced superconductivity K3C60 fluence mJ/cm2 temperature 100 K nanosecond pulses', 'k3c60', 'f'),
   ('Fava 2024 Nature magnetic field expulsion optically driven YBa2Cu3O6.48', 'ybco-driven', 'f'),
   ('FELBE free-electron laser 13 MHz continuous pulse train mid-infrared 30 um average power', 'fel', 'f'),
   ('GaN terahertz quantum cascade laser lasing 2025 frequency room temperature', 'thz-source', 'f'),
   ('LaSc2H24 room-temperature superconductivity independent confirmation Meissner 2026', 'hydride', 'k'),
   ('pressure quench protocol hydride superconductor retained at ambient pressure attempt', 'pqp', 'f'),
   ('nickelate superconductor ambient pressure Tc record 2026 La3Ni2O7 thin film', 'nickelate', 'f'),
   ('Mg2IrH6 predicted ambient pressure superconductor synthesis attempt result', 'hydride', 'f'),
   ('light-induced Meissner effect K3C60 room temperature 10 THz drive 2025', 'k3c60', 'f'),
   ('Mach effect thruster Tajmar 2021 thrust artifact vibration null result', 'mach-effect', 'x')],
   kills=3, leads_kept=6, progress=3, errors_caught=['area-flux-vs-local-heat'], repeat_errors=0, hit=(12, 12), circular=0.05,
   domains=['nature.com', 'physicsworld.com', 'arxiv.org', 'pdf.arxiv.org', 'cui-advanced.uni-hamburg.de', 'fels-of-europe.eu',
            'biomedicaloptics.spiedigitallibrary.org', 'eurekalert.org', 'escholarship.org', 'ipiq.io', 'jpralves.net'],
   canary=None, prompt_chars=None),
 3: dict(queries=[
   ('carbon nanotube fiber strength decreases with gauge length size effect meter scale', 'cnt', 'k'),
   ('carbon nanotube reinforced REBCO superconducting coil high field magnet', 'cnt-rebco', 'x'),
   ('virial theorem minimum mass superconducting magnet structure stored energy strength density Moon 1982', 'virial', 'x'),
   ('highest frequency electrically generated coherent acoustic phonons terahertz saser record', 'saser', 'x'),
   ('K3C60 10 THz resonance 41 meV mode origin photo-induced superconductivity mechanism Rowe', 'k3c60', 'k'),
   ('optical pumping light-enhanced superconductivity Hg1223 mercury cuprate', 'hg1223-drive', 'x'),
   ('carbon nanotube composite flywheel rotor spin burst test rim speed', 'flywheel', 'f'),
   ('REBCO tape critical stress strain limit irreversible degradation 77 K Hastelloy substrate MPa', 'rebco-stress', 'f'),
   ('high average power terahertz free electron laser 10 THz 30 micron repetition rate MHz superconducting accelerator', 'fel', 'f'),
   ('light-induced superconductivity YBa2Cu3O6+x doping dependence underdoped optimally doped enhancement vanishes', 'ybco-driven', 'k'),
   ('FACET-II E-320 strong-field QED experiment results nonlinear Compton', 'sfqed', 'f'),
   ('torsion thrust balance nanonewton resolution thermal noise propellantless thruster test', 'thrust-balance', 'f'),
   ('spinning superconductor gravitational anomaly Tajmar Podkletnov replication null result', 'sc-anomaly', 'x'),
   ('CMUT capacitive micromachined ultrasonic transducer DC bias voltage gap height electric field membrane displacement MHz', 'cmut', 'x')],
   kills=4, leads_kept=4, progress=5, errors_caught=['cm-strength-at-metre-scale', 'pressure-called-hoop-stress'],
   repeat_errors=0, hit=(14, 14), circular=0.08,
   domains=['ustc.edu.cn', 'scholars.cityu.edu.hk', 'agris.fao.org', 'ar5iv.arxiv.org', 'patents.google.com', 'escholarship.org',
            'typeset.io', 'snf.ieeecsc.org', 'manuscript.isc.ac', 'ioa.org.uk', 'core.ac.uk', 'arxiv.org', 'nature.com',
            'cui-advanced.uni-hamburg.de', 'pmc.ncbi.nlm.nih.gov', 'qcmd.mpsd.mpg.de', 'saemobilus.sae.org', 'energy.gov',
            'jstage.jst.go.jp', 'indico.eli-laser.eu', 'lasphys.com', 'fis.tu-dresden.de', 'iafastro.directory',
            'faculty.eng.ufl.edu', 'ar5iv.labs.arxiv.org', 'research.ece.ncsu.edu'],
   canary='pass', prompt_chars=(5159, 5430),
   repeat_new_fact={1: True, 5: False, 7: True, 11: True}, recycled_sources=2),
 # run 4: wording of queries 1-12 reconstructed after a context reset (the exact strings and their sources were held only in
 # working context); kind 's' = source-recovery search caused by that loss. Domains: the 4 post-reset searches plus arXiv (E-320).
 4: dict(queries=[
   ('ultralong carbon nanotube bundle tensile strength gauge length Weibull', 'cnt', 'f'),
   ('Weibull shape parameter carbon nanotube yarn multiple gauge lengths', 'cnt', 'k'),
   ('carbon nanotube yarn composite ring NOL hoop test', 'cnt-composite', 'f'),
   ('REBCO carbon fiber overband high-modulus reinforcement coil', 'rebco-band', 'f'),
   ('REBCO compressive strain irreversible limit pre-compression critical current', 'rebco-stress', 'k'),
   ('terahertz split-ring resonator field enhancement superconductor film', 'thz-meta', 'x'),
   ('terahertz metamaterial gap heating damage threshold', 'thz-meta', 'k'),
   ('E-320 positrons nonlinear Breit-Wheeler arXiv 2026', 'sfqed', 'r'),
   ('Biefeld-Brown effect vacuum thrust null', 'ehd', 'x'),
   ('Tate Cooper pair mass anomaly London moment niobium', 'tate', 'x'),
   ('thermal contraction Hastelloy REBCO carbon fiber 4 K', 'cte', 'k'),
   ('specific strength commercial fibres Zylon Dyneema T1100G', 'fibre', 'x'),
   ('Tate Cooper pair mass anomaly explanation', 'tate', 'k'),
   ('carbon nanotube yarn tensile strength N/tex gauge length 2020', 'cnt', 's'),
   ('REBCO coil co-wound Hastelloy strain reduction screening current stress', 'rebco-band', 's'),
   ('terahertz metamaterial gap field enhancement damage threshold MV/cm', 'thz-meta', 's')],
   kills=5, leads_kept=4, progress=3,
   errors_caught=['overband-cte-ignored', 'enhancement-credited-as-F2', 'sources-not-logged-at-search'],
   repeat_errors=0, hit=(16, 16), circular=0.07,
   domains=['arxiv.org', 'x-mol.com', 'digitallibrarynasampe.org', 'pmc.ncbi.nlm.nih.gov', 'jstage.jst.go.jp', 'mdpi.com',
            'aminer.org', 'par.nsf.gov', 'public.magnet.fsu.edu', 'iopscience.iop.org', 'link.aps.org', 'core.ac.uk',
            'epj-conferences.org'],
   canary='pass', prompt_chars=(5430, 5984),
   repeat_new_fact={1: False, 4: True, 5: True, 13: True, 14: True, 16: True}, recycled_sources=2),
 # run 5: every search logged with its sources as it returned (run5_log.md -> claude/pais_search_log.md). Query wording pre-checked
 # against all earlier queries (max Jaccard 0.17 across runs, 0.22 within the run).
 5: dict(queries=[
   ('half-meter ultralong carbon nanotubes growth Schulz-Flory catalyst', 'cnt-sf', 'f'),
   ('Pugno nanoscale Weibull statistics nanotube defects', 'cnt-stat', 'k'),
   ('REBCO pancake cooldown measured hoop strain gauges stainless cowind', 'rebco-cold', 'f'),
   ('REBCO delamination c-axis tensile strength epoxy impregnated coil cooldown', 'rebco-delam', 'k'),
   ('PIPD M5 rigid-rod polymer filament tenacity', 'fibre', 'x'),
   ('graphene oxide wet-spun filament highest GPa', 'fibre', 'x'),
   ('Toray newest carbon fiber grade strongest MPa announced', 'fibre', 'f'),
   ('launch loop Lofstrom dynamic structure stream supported', 'dynamic', 'x'),
   ('superconducting levitated ring rotor Earnshaw stability eddy losses high speed', 'levitation', 'k'),
   ('Earth flyby anomaly Anderson formula spacecraft', 'flyby', 'x'),
   ('Juno flyby anomaly absent tracking result', 'flyby', 'k'),
   ('REBCO engineering current density 4.2 K 20 T tape kA/mm2 thin substrate', 'rebco-je', 'f')],
   kills=4, leads_kept=3, progress=2,
   errors_caught=['stale-record-from-table', 'rim-speed-wall-overstated', 'lost-source-input-reused'],
   repeat_errors=0, hit=(12, 12), circular=0.08,
   domains=['qianggroup.com', 'core.ac.uk', 'pmc.ncbi.nlm.nih.gov', 'acris.aalto.fi', 'arxiv.org', 'pugno.dicam.unitn.it',
            'public.magnet.fsu.edu', 'indico.cern.ch', 'typeset.io', 'katalog.lib.cas.cz', 'manuscript.isc.ac',
            'vufind-test.katalog.k.utb.cz', 'image-ppubs.uspto.gov', 'data.epo.org', 'taylorandfrancis.com', 'bohrium.dp.tech',
            'nature.com', 'pubs.rsc.org', 'toraytac.com', 'texdata.com', 'engrxiv.org', 'toughsf.blogspot.com', 'nextbigfuture.com',
            'osti.gov', 'magneticbearings.org', 'scilit.com', 'scribd.com', 'link.aps.org', 'ar5iv.arxiv.org', 'ar5iv.labs.arxiv.org',
            'acceleratingnews-archive.web.cern.ch', 'scite.ai'],
   canary='pass', prompt_chars=(5984, 6433), repeat_new_fact={}, recycled_sources=1),
 # run 6: logged in run6_log.md as each search returned; query 13 (torque magnetometry) ran in the second batch, so it sits 9th here.
 6: dict(queries=[
   ('Levitated Dipole Experiment floating coil levitation feedback vertical instability', 'b6-ldx', 'f'),
   ('rotating damping whirl instability supercritical rotor magnetic bearing eddy current', 'b6-whirl', 'k'),
   ('REBCO critical current 40 T field parallel ab measurement tape 4.2 K', 'rebco-je', 'f'),
   ('AC loss thin superconducting strip perpendicular field Brandt Indenbom', 'ac-loss', 'f'),
   ('coated conductor integrated thermal expansion 4 K measurement Hastelloy copper stabilizer', 'rebco-cte', 'f'),
   ('Toray M55J tensile strength modulus elongation', 'fibre', 'k'),
   ('Tsinghua Wei group superstrong nanotube fiber centimetre bundle', 'cnt', 'f'),
   ('Exodus Propulsion Buhler thrust independent replication', 'x1', 'x'),
   ('Bradford Larbalestier torque magnetometry REBCO 45 T critical current flux jumps', 'rebco-je', 'f'),
   ('charged dielectric thruster sealed enclosure vacuum torsion balance null', 'x1', 'k'),
   ('epitaxial compressive strain equivalent hydrostatic pressure nickelate film superconductivity', 'strain-p', 'x'),
   ('metal hydride epitaxial film lattice mismatch maximum strain GPa equivalent', 'strain-p', 'k'),
   ('Inductrack passive electrodynamic levitation lift drag ratio speed stability', 'inductrack', 'x')],
   kills=4, leads_kept=4, progress=2,
   errors_caught=['band-prestrain-not-subtracted-from-failure-strain'],
   repeat_errors=0, hit=(13, 13), circular=0.08,
   domains=['arxiv.org', 'meetings.aps.org', 'archive.aps.org', 'fire.pppl.gov', 'meetings-archive.aps.org', 'pure.mpg.de',
            'iris.polito.it', 'magneticbearings.org', 'nationalmaglab.org', 'pmc.ncbi.nlm.nih.gov', 'indico.cern.ch', 'par.nsf.gov',
            'conferences.lbl.gov', 'image-ppubs.uspto.gov', 'ouci.dntb.gov.ua', 'snf.ieeecsc.org', 'rockwestcomposites.com',
            'toraycma.com', 'toraytac-staging.azurewebsites.net', 'physicstoday.aip.org', 'tsinghua.edu.cn', 'okdiario.com',
            'pulse.bot', 'thebrighterside.news', 'geekchamp.com', 'medium.com', 'tu-dresden.de', 'scribd.com', 'ntrs.nasa.gov',
            'paradim.org', 'synapsesocial.com', 'journals.aps.org', 'scite.ai', 'dspacecris7.sub.uni-goettingen.de',
            'publikationen.bibliothek.kit.edu', 'pubs.rsc.org', 'typeset.io', 'mae.ufl.edu'],
   canary='pass', prompt_chars=(6433, 6871), repeat_new_fact={}, recycled_sources=1),
 # run 7: logged in run7_log.md as each search returned; query 9 was rephrased after the pre-check (0.33 vs run 6); query 17 is a
 # follow-up for V.9's numbers (FELICE), not a redo. Main sources already cited: APEX-LD (q1) and okdiario (q14).
 7: dict(queries=[
   ('LDX floating coil vertical position control system growth time bandwidth sensors', 'b6-ctrl', 'f'),
   ('Beams magnetically suspended rotor vacuum ultracentrifuge rotational speed burst', 'b6-prior', 'f'),
   ('electrostatically suspended gyroscope rotor suspension servo bandwidth spin speed', 'b6-prior', 'x'),
   ('dynamic resistance coated conductor DC transport current alternating perpendicular field threshold', 'ac-loss', 'k'),
   ('passive stabilization levitated superconducting ring persistent current loop null flux coil', 'b6-passive', 'x'),
   ('REBCO superconducting joint resistance persistent mode decay time', 'b6-passive', 'k'),
   ('bulk YBCO superconducting bearing stiffness N/mm flywheel levitation gap', 'smb', 'x'),
   ('superconducting magnetic bearing flux creep drift rotational loss rotor inhomogeneity', 'smb', 'k'),
   ('production coated conductor 30 tesla 4.2 K amperes per centimetre width SuperPower Faraday Fujikura', 'rebco-je', 'f'),
   ('Bai 2018 nanotube bundles 80 GPa cross-sectional area calculation method', 'cnt', 'k'),
   ('REBCO tape thermal contraction room temperature to 4 K measured strain gauge', 'rebco-cte', 'f'),
   ('stainless steel co-wound REBCO coil degradation thermal cycling delamination', 'k2', 'k'),
   ('intracavity sample free electron laser oscillator mid-infrared experiment', 'gap9-ic', 'x'),
   ('Exodus Propulsion electrostatic pressure force test outside laboratory', 'x1', 'k'),
   ('magnetic sail small magnetosphere ion gyroradius thrust kinetic regime', 'magsail', 'x'),
   ('mini-magnetospheric plasma propulsion M2P2 thrust overestimate criticism', 'magsail', 'k'),
   ('FELICE intracavity micropulse energy enhancement outcoupling FELIX 30 micron', 'gap9-ic', 'f')],
   kills=7, leads_kept=4, progress=2,
   errors_caught=['strength-paired-with-wrong-density'],
   repeat_errors=0, hit=(17, 17), circular=0.07,
   domains=['arxiv.org', 'dspace.mit.edu', 'pure.mpg.de', 'core.ac.uk', 'web.phys.virginia.edu', 'magneticbearings.org',
            'skoge.folk.ntnu.no', 'image-ppubs.uspto.gov', 'openaccess.wgtn.ac.nz', 'snf.ieeecsc.org', 'typeset.io', 'scite.ai',
            'infoscience.epfl.ch', 'manuscript.isc.ac', 'patents.google.com', 'patentimages.storage.googleapis.com', 'mdr.nims.go.jp',
            'aminer.org', 'indico.cern.ch', 'jspf.or.jp', 'pmc.ncbi.nlm.nih.gov', 'qk.sjtu.edu.cn', 'acnpsearch.tweb-dev.unibo.it',
            'bvbvf1.bib-bvb.de', 'conferences.lbl.gov', 'public.magnet.fsu.edu', 'indico.fnal.gov', 'media.springernature.com',
            'physicstoday.aip.org', 'pub.confit.atlas.jp', 'ptest.benchcouncil.org', 'jacow.org', 'okdiario.com', 'thebrighterside.news',
            'docs.google.com', 'jsst.jp', 'jstage.jst.go.jp', 'ntrs.nasa.gov', 'doc.surf', 'epaper.kek.jp'],
   canary='pass', prompt_chars=(6871, 7484), repeat_new_fact={}, recycled_sources=2),
 8: dict(queries=[
   ('closed-loop REBCO coil persistent mode quench current decay redistribution between turns', 'b6-quench', 'f'),
   ('LDX floating coil warm-up during levitation heat leak temperature rise hours', 'b6-thermal', 'f'),
   ('flywheel rotor burst containment housing energy absorbed per kilogram test', 'b6-contain', 'k'),
   ('inductively coupled parallel superconducting loops one loop quenches current transfer neighbours', 'b6-redund', 'x'),
   ('flywheel energy storage system specific energy Wh/kg including housing best demonstrated', 'b6-store', 'x'),
   ('counter-rotating flywheel pair vehicle gyroscopic torque cancellation manoeuvre', 'b6-gyro', 'x'),
   ('large warm bore 10 tesla superconducting magnet user facility 300 mm', 'b6-test', 'f'),
   ('FELIX free electron laser single-pass gain cavity round-trip loss mid-infrared', 'b7', 'f'),
   ('K3C60 film infrared optical conductivity absorption thickness 41 meV', 'k3c60-film', 'f'),
   ('photoexcited K3C60 superconductivity alternative explanation inhomogeneous conductivity critique', 'k3c60', 'k'),
   ('fulleride light-driven superconducting state reproduced different laboratory', 'k3c60', 'k'),
   ('manufacturer specification sheet second-generation HTS wire integral linear contraction from room temperature', 'rebco-cte', 'f'),
   ('screening current induced stress plastic deformation high-field insert coil damage mitigation', 'k2', 'k'),
   ('Buhler propellantless electrostatic thrust independent test after June 2026', 'x1', 'k'),
   ('electret trapped charge vacuum decay time force on grounded electrode after power removed', 'x1-electret', 'x'),
   ('cavity vacuum field changes superconducting transition temperature experiment fulleride Fabry-Perot', 'cavity-qed', 'x'),
   ('cavity-modified superconductivity claim null result vacuum fluctuations no Tc change', 'cavity-qed', 'k'),
   # 18-21: input lookups added after the 17-query plan because the maths needed sourced inputs (logged; novelty 0.49 without them)
   ('coated conductor transverse tensile delamination strength c-axis MPa anvil test', 'rebco-delam', 'f'),
   ('striated multifilament REBCO tape laser scribing number of filaments width', 'rebco-striate', 'f'),
   ('PTFE polyimide film volume resistivity datasheet ohm cm dielectric constant', 'dielectric', 'f'),
   ('Dyneema SK99 yarn breaking tenacity elongation at break specification sheet', 'fibre', 'f')],
   kills=6, leads_kept=4, progress=2,
   errors_caught=['safe-fraction-ignored-quench-coupling', 'test-speed-below-regime'],
   repeat_errors=0, hit=(21, 21), circular=0.05,
   domains=['bohrium.dp.tech', 'iopscience.iop.org', 'springerlink.bibliotecabuap.elogim.com', 'image-ppubs.uspto.gov', 'preprints.org', 'arxiv.org', 'manuscript.isc.ac', 'katalog.lib.cas.cz', 'collaborate.princeton.edu', 'osti.gov', 'jspf.or.jp', 'mdpi.com', 'doaj.org', 'core.ac.uk', 'ntrs.nasa.gov', 'corpora.tika.apache.org', 'indico.cern.ch', 'secwww.jhuapl.edu', 'vcef.engr.tamu.edu', 'patents.google.com', 'data.epo.org', 'agilent.com', 'nims.go.jp', 'epaper.kek.jp', 'fzd.de', 'jacow.org', 'accelconf.web.cern.ch', 'pmc.ncbi.nlm.nih.gov', 'dodge-research-group.github.io', 'archive.aps.org', 'phys.org', 'bridex.fujielectric.com', 'snf.ieeecsc.org', 'ui.adsabs.harvard.edu', 'public.magnet.fsu.edu', 'strathprints.strath.ac.uk', 'okdiario.com', 'geekchamp.com', 'webpronews.com', 'yahoo.com', 'nature.com', 'incompliancemag.com', 'library.oapen.org', 'arxivlens.com', 'interestingengineering.com', 'alphaxiv.org', 'ntt-research.com', 'nist.gov', 'conferences.lbl.gov', 'kb.osu.edu', 'peeref.com', 'professionalplastics.com', 'protolabs.com', 'cshyde.com', 'eriks.nl', 'pelicanrope.com', 'minifibers.com', 'careers.polyone.com'],
   canary='pass', prompt_chars=(7484, 8081), repeat_new_fact={}, recycled_sources=2),
 # run 9: logged in run9_log.md as each search returned; 16 planned + 1 exploration added mid-run (q17, LISA Pathfinder UV charge control,
 # a bridge for X1); 3 fetches (UT-CEM containment, LLNL vessel, '532 cited-by) not counted as queries. Side research not scored.
 # Planned-only domain novelty is computed separately in health9.py (Prompt C1 v9).
 9: dict(queries=[
   ('Faraday Factory tape in-field critical current 20 K 30 K data sheet', 'rebco-ic-T', 'f'),
   ('thick film REBCO production length 30 tesla engineering current density Houston advanced MOCVD', 'rebco-thick', 'f'),
   ('HTS wire critical current database Robinson Research Institute angular field temperature', 'hts-db', 'f'),
   ('momentum-supported structure stream break failure consequences energy release analysis', 'b6-dyn', 'k'),
   ('explosive containment vessel rated charge kg TNT vessel weight composite', 'b6-vessel', 'f'),
   ('virial theorem pressure vessel minimum mass gas energy containment bound', 'b6-virial', 'x'),
   ('rotatable containment liner flywheel torque transmitted housing reduction', 'b6-torque', 'x'),
   ('Whipple shield ballistic limit equation areal density 7 km/s aluminum projectile', 'b6-hvi', 'f'),
   ('K3C60 thin film MBE growth superconducting transition temperature encapsulation air', 'k3c60-film', 'f'),
   ('FELIX FEL-2 small-signal gain outcoupling hole losses 30 micron wavelength', 'b7-fel', 'f'),
   ('optically driven K3C60 2026 magnetic expulsion transport measurement independent group', 'k3c60', 'k'),
   ('30 micron difference frequency generation high average power watt laser source', 'b7-src', 'x'),
   ('asymmetric electrostatic pressure thruster replication attempt university vacuum chamber', 'x1', 'k'),
   ('micro-thrust balance electrostatic artifact charged dielectric residual charge neutralization ionizer', 'x1-ctrl', 'k'),
   ('patents citing US10144532 inertial mass reduction craft cited by', 'bridge', 'x'),
   ('integrated power and attitude control system flywheel spacecraft NASA counter-rotating', 'b6-ipacs', 'x'),
   ('LISA Pathfinder test mass charge management UV light discharge force noise', 'x1-uv', 'x')],
   kills=4, leads_kept=4, progress=2,
   errors_caught=['catcher-sized-by-absorbed-energy'],
   repeat_errors=0, hit=(16, 17), circular=0.06,
   domains=['indico.cern.ch', 'maglabweb.magnet.fsu.edu', 'eprints.soton.ac.uk', 'public.magnet.fsu.edu', 'indico.fnal.gov', 'figshare.com',
            'arxiv.org', 'ascelibrary.com', 'osti.gov', 'apps.dtic.mil', 'sandia.gov', 'image-ppubs.uspto.gov', 'scribd.com',
            'patents.google.com', 'core.ac.uk', 'saemobilus.sae.org', 'ntrs.nasa.gov', 'research.unipd.it', 'zenodo.org', 'link.springer.com',
            'accelconf.web.cern.ch', 'jacow.org', 'epaper.kek.jp', 'journals.aps.org', 'researchgate.net', 'tf.nist.gov', 'typeset.io',
            'bib-pubdb1.desy.de', 'altsci.net', 'altpropulsion.com', 'insights.greyb.com', 'link.aps.org', 'iris.unitn.it'],
   canary='pass', prompt_chars=(8081, 8534), repeat_new_fact={}, recycled_sources=2),
 10: dict(queries=[
   ('Iseult 11.7 tesla whole-body magnet field homogeneity ppm measured', 'field-homog', 'f'),
   ('high emissivity black coating cryogenic 20 K hemispherical emissivity measurement', 'emissivity', 'f'),
   ('oblique hypervelocity impact grazing angle ricochet debris sliding along plate', 'b6-graze', 'k'),
   ('two-stage light gas gun flat plate projectile orientation sabot facility 7 km/s', 'lgg', 'f'),
   ('long-length thick REBCO tape critical current uniformity variability performance drop', 'rebco-thick', 'k'),
   ('thick-film coated conductor lift factor versus temperature Houston tape 30 kelvin', 'rebco-ic-T', 'f'),
   ('alkali fulleride thin film ultrafast optical spectroscopy pump probe molecular beam epitaxy', 'k3c60-film', 'f'),
   ('Rb3C60 photoexcitation metastable superconductivity mid-infrared pressure', 'k3c60', 'k'),
   ('FELIX laboratory intracavity FELICE user experiment solid state sample', 'b7-fel', 'f'),
   ('Exodus Buhler thruster third-party verification latest', 'x1', 'k'),
   ('high-frequency electromagnetic field gravity coupling experiment balance search', 'hf-grav', 'x'),
   ('gravitational field generator patent electromagnetic granted 2023 2024 2025', 'grav-patents', 'x'),
   ('SPARC toroidal field model coil 20 tesla stored energy quench test result', 'bridge', 'x'),
   ('high-frequency gravitational wave detector MHz GHz upper limit superconducting cavity', 'hfgw', 'x'),
   ('Espacenet antigravity propulsion device patent electrostatic coil', 'grav-patents-2', 'x'),
   ('screening current induced field REBCO coil field error ppm non-axisymmetric harmonics measurement', 'field-homog', 'k')],
   kills=5, leads_kept=4, progress=1,
   errors_caught=['gap-entry-formula-differs-from-I.30', 'sources-recycled-without-check'],
   repeat_errors=0, hit=(15, 16), circular=0.11,
   domains=['ncbi.nlm.nih.gov', 'cds.ismrm.org', 'osti.gov', 'katalog.lib.cas.cz', 'ntrs.nasa.gov', 'tfaws.nasa.gov', 'indico.cern.ch',
            'core.ac.uk', 'seejournal.cn', 'arxiv.org', 'Swri.org', 'hemi.jhu.edu', 'aerospace.illinois.edu', 'telacyjr.engr.tamu.edu',
            'conferences.lbl.gov', 'public.magnet.fsu.edu', 'image-ppubs.uspto.gov', 'patents.google.com', 'qcmd.mpsd.mpg.de',
            'ediss.sub.uni-hamburg.de', 'link.springer.com', 'ora.ox.ac.uk', 'wiki.felix.science.ru.nl', 'epaper.kek.jp',
            'nextbigfuture.com', 'altpropulsion.com', 'chriswest.tech', 'patentsgazette.uspto.gov', 'ipiq.io',
            'unifiedfieldtheory.vercel.app', 'snf.ieeecsc.org', 'bib-pubdb1.desy.de', 'cordis.europa.eu', 'api.emergentmind.com',
            'users.libero.it', 'pmc.ncbi.nlm.nih.gov', 'doaj.org', 'searchworks.jioinstitute.edu.in', 'koreascience.kr'],
   canary='pass', prompt_chars=(8536, 9105), repeat_new_fact={}, recycled_sources=3),
 # run 11: the last literature pass; 9 planned + 1 kill follow-up (q10, the REBCO skeleton cyclotron); the loop stopped by its rule after it.
 11: dict(queries=[
   ('toroidal field model coil REBCO measured field map error compared with design', 'field-homog', 'k'),
   ('coated conductor thick superconducting layer flux jump instability 20 K magnetization avalanche', 'rebco-fj', 'k'),
   ('hypervelocity gouging sled track slipper rail damage onset velocity', 'b6-graze', 'k'),
   ('photoinduced superconductivity fulleride confirmed by another group November 2026', 'k3c60', 'k'),
   ('Buhler electrostatic thrust peer reviewed journal paper published', 'x1', 'k'),
   ('superconducting cyclotron first harmonic field error gauss trim coil correction', 'cyclotron', 'x'),
   ('compact cyclotron coated-conductor coil orbit field uniformity measured', 'cyclotron', 'x'),
   ('dynamic gravitational field measurement electromagnetic source anomalous coupling resonant detector', 'hf-grav', 'x'),
   ('flywheel burst fragment light gas gun test containment liner tangential impact', 'bridge', 'x'),
   ('skeleton cyclotron REBCO coil system magnetic field accuracy measured screening current UBSC results', 'cyclotron', 'k')],
   kills=6, leads_kept=4, progress=0,
   errors_caught=['ppm-against-assumed-field'],
   repeat_errors=0, hit=(9, 10), circular=0.09,
   domains=['katalog.lib.cas.cz', 'imeko.info', 'um.edu.mt', 'searchworks.jioinstitute.edu.in', 'indico.cern.ch', 'arxiv.org',
            'sandia.gov', 'proquest.com', 'core.ac.uk', 'tdl-ir.tdl.org', 'iopscience.iop.org', 'researchgate.net', 'unknowncountry.com',
            'altsci.net', 'yahoo.com', 'thedebrief.org', 'accelconf.web.cern.ch', 'epaper.kek.jp', 'jacow.org', 'vufind-test.katalog.k.utb.cz',
            'research-collection.ethz.ch', 'meetings-archive.aps.org', 'osti.gov', 'image-ppubs.uspto.gov', 'ntrs.nasa.gov', 'peeref.com',
            'aminer.cn', 'mdr.nims.go.jp'],
   canary='pass', prompt_chars=(9105, 9392), repeat_new_fact={}, recycled_sources=2),
}

def score(runs, upto):
    rows = {}
    seen_q, seen_d, seen_err = [], set(), set()
    for r in sorted(runs):
        if r > upto: break
        R = runs[r]; qs = R['queries']
        sims = []
        for q, tag, kind in qs:
            t = toks(q); sims.append(max([jac(t, s) for s in seen_q] or [0]))
        repeat = sum(s >= 0.30 for s in sims) / len(qs)
        tags = [t for _, t, _ in qs]; top = max(set(tags), key=tags.count); conc = tags.count(top) / len(tags)
        explore = sum(k == 'x' for _, _, k in qs) / len(qs)
        kr = R['kills'] / max(1, R['leads_kept'])
        dn = [d for d in R['domains'] if d not in seen_d]; dnov = len(dn) / len(R['domains'])
        rep_err = sum(e in seen_err for e in R['errors_caught'])
        too_easy = R['hit'][0] == R['hit'][1] and R['progress'] <= 1
        rq = [i + 1 for i, s in enumerate(sims) if s >= 0.30]
        nf = R.get('repeat_new_fact')
        ry = (sum(bool(nf.get(i)) for i in rq) / len(rq) if rq else 1.0) if nf is not None else None
        rec = R['recycled_sources'] / len(qs) if R.get('recycled_sources') is not None else None
        pg = (R['prompt_chars'][1] / R['prompt_chars'][0] - 1) if R['prompt_chars'] else None
        # within-run rework (signal 14, added in run 4 after its scoring, pre-registered from run 5): searches redone inside one run,
        # i.e. source-recovery searches (kind 's') plus non-kill queries with Jaccard >= 0.30 to an earlier query of the same run
        wr = 0
        for i, (q, tag, kind) in enumerate(qs):
            if kind == 's': wr += 1; continue
            if kind == 'k': continue
            if any(jac(toks(q), toks(qs[j][0])) >= 0.30 for j in range(i)): wr += 1
        rows_rework = wr / len(qs)
        rows[r] = dict(rework=rows_rework, repeat_yield=ry, recycled=rec, repeated_queries=rq, prompt_growth=pg, repeat=repeat, max_sim=max(sims), top_topic=top, concentration=conc, explore=explore, kill_ratio=kr,
                       domain_novelty=dnov, progress=R['progress'], repeated_errors=rep_err, too_easy=too_easy,
                       circular=R['circular'], canary=R['canary'], prompt_chars=R['prompt_chars'],
                       sims=[round(s, 2) for s in sims])
        seen_q += [toks(q) for q, _, _ in qs]; seen_d |= set(R['domains']); seen_err |= set(R['errors_caught'])
    return rows

# thresholds: (green test, red test) -> light
def light(name, v):
    if v is None: return 'not run'
    T = {'repeat': (lambda x: x <= 0.25, lambda x: x > 0.40), 'concentration': (lambda x: x <= 0.30, lambda x: x > 0.50),
         'explore': (lambda x: 0.20 <= x <= 0.50, lambda x: x < 0.10 or x > 0.60), 'kill_ratio': (lambda x: x >= 1.0, lambda x: x < 0.5),
         'domain_novelty': (lambda x: x >= 0.50, lambda x: x < 0.30), 'progress': (lambda x: x >= 2, lambda x: x == 0),
         'repeated_errors': (lambda x: x == 0, lambda x: x >= 1), 'too_easy': (lambda x: not x, lambda x: False),
         'circular': (lambda x: x <= 0.10, lambda x: x > 0.25), 'canary': (lambda x: x == 'pass', lambda x: x == 'fail'),
         'prompt_growth': (lambda x: x <= 0.30, lambda x: x > 0.60),
         'repeat_yield': (lambda x: x >= 0.75, lambda x: x < 0.5), 'recycled': (lambda x: x <= 0.15, lambda x: x > 0.30),
         'rework': (lambda x: x <= 0.07, lambda x: x > 0.15)}
    g, r = T[name]
    return 'green' if g(v) else ('red' if r(v) else 'amber')

if __name__ == '__main__':
    upto = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    rows = score(RUNS, upto)
    out = {}
    for r, d in rows.items():
        out[r] = {k: (d[k], light(k, d[k])) for k in ('repeat', 'concentration', 'explore', 'kill_ratio', 'domain_novelty', 'progress',
                                                      'repeated_errors', 'too_easy', 'circular', 'canary', 'prompt_growth', 'repeat_yield', 'recycled',
                                                      'rework')}
        out[r]['repeated_queries'] = d['repeated_queries']; out[r]['top_topic'] = d['top_topic']; out[r]['max_sim'] = round(d['max_sim'], 2); out[r]['sims'] = d['sims']
        print(f'run {r}:', {k: (round(v[0], 2) if isinstance(v[0], float) else v[0], v[1]) for k, v in out[r].items() if isinstance(v, tuple)},
              '| top topic', d['top_topic'], '| max sim', round(d['max_sim'], 2))
        print('   per-query max similarity to earlier queries:', d['sims'])
    import os
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'loop_health.json'), 'w'), indent=1)
