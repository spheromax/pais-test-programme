"""I.22 numerical check: best decay rate alpha(tau) achievable by delayed PD control of x'' = x - p x(t-tau) - d x'(t-tau) (gamma = 1).
Theory (D-subdivision): a stable (p, d) exists iff tau < sqrt(2). Uses the Chebyshev collocation in run7_math.py. Writes run7_delay.json."""
import json, math
import numpy as np
from scipy.optimize import minimize
import importlib.util
spec = importlib.util.spec_from_file_location('r7', '/home/claude/p3/sim/pais/run7_math.py')
src = open('/home/claude/p3/sim/pais/run7_math.py').read().split('delay_check = []')[0]
ns = {}; exec(src, ns)
rightmost = ns['rightmost']
res = []
for tau in (0.25, 0.5, 0.75, 1.0, 1.2, 1.3, 1.36, 1.40, 1.43, 1.47):
    best = (9, None)
    for p0 in (1.05, 1.2, 1.5, 2.0):
        for d0 in (0.3, 0.8, 1.5):
            r = minimize(lambda x: rightmost(x[0], x[1], tau, N=32), [p0, d0], method='Nelder-Mead',
                         options=dict(xatol=1e-5, fatol=1e-7, maxiter=600))
            if r.fun < best[0]: best = (r.fun, r.x.tolist())
    res.append(dict(tau=tau, alpha=-best[0], p=best[1][0], d=best[1][1]))
    print(f'tau {tau:.2f}: best rightmost {best[0]:+.5f} at p {best[1][0]:.4f}, d {best[1][1]:.4f}')
# boundary curve check: p(w) = (1+w^2) cos(w tau) leaves p = 1 to the right iff tau < sqrt 2
for tau in (1.3, 1.5):
    w = 0.05; print('tau', tau, 'p(0.05) - 1 =', (1 + w * w) * math.cos(w * tau) - 1)
json.dump(res, open('/home/claude/p3/sim/pais/run7_delay.json', 'w'), indent=1)
