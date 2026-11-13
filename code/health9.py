"""Run-9 health: all signals via loop_health.py, plus domain novelty for the 16 planned searches alone (Prompt C1 v9)."""
import importlib.util, json, copy
spec = importlib.util.spec_from_file_location('lh', '/home/claude/p3/sim/pais/loop_health.py'); lh = importlib.util.module_from_spec(spec); spec.loader.exec_module(lh)
rows = lh.score(lh.RUNS, 9)
r9 = rows[9]
keys = ('repeat', 'repeat_yield', 'recycled', 'concentration', 'explore', 'kill_ratio', 'domain_novelty', 'progress', 'repeated_errors',
        'too_easy', 'circular', 'canary', 'prompt_growth', 'rework')
lights = {k: lh.light(k, r9[k]) for k in keys}
seen = set()
for r in range(1, 9): seen |= set(lh.RUNS[r]['domains'])
planned_dom = [d for d in lh.RUNS[9]['domains'] if d not in ('link.aps.org', 'iris.unitn.it')]   # q17 (added) sources
new_all = [d for d in lh.RUNS[9]['domains'] if d not in seen]; new_pl = [d for d in planned_dom if d not in seen]
out = dict(values={k: r9[k] for k in keys}, lights=lights, sims=r9['sims'], max_sim=r9['max_sim'], top_topic=r9['top_topic'],
           novelty_all=(len(new_all), len(lh.RUNS[9]['domains'])), novelty_planned=(len(new_pl), len(planned_dom)), new_domains=new_all,
           explore_planned=sum(k == 'x' for _, _, k in lh.RUNS[9]['queries'][:16]) / 16)
json.dump(out, open('health9.json', 'w'), indent=1, default=str)
for k in keys: print(f'{k:16s} {str(round(r9[k], 3) if isinstance(r9[k], float) else r9[k]):>8s}  {lights[k]}')
print('novelty all', out['novelty_all'], round(out['novelty_all'][0] / out['novelty_all'][1], 3), '| planned', out['novelty_planned'], round(out['novelty_planned'][0] / out['novelty_planned'][1], 3))
print('new domains', new_all); print('explore planned', out['explore_planned'], 'max sim', out['max_sim'], 'top', out['top_topic'])
print('tally', {c: sum(v == c for v in lights.values()) for c in ('green', 'amber', 'red')})
