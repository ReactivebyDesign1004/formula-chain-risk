# Minimal reproduction: formula, worked example, N-agent table.
# Python 3.9 or later; numpy only.
import numpy as np
def p_high_stakes(p, q, c, g, n, N):
    """Chance of at least one high-stakes outcome in a chain of N agents,
    each taking n steps."""
    r = min(1.0, p * c)                # anomaly rate on contaminated input
    aC, sC = (1 - p) ** n, (1 - p * q) ** n   # clean: no anomaly / no harm
    aD, sD = (1 - r) ** n, (1 - r * q) ** n   # contaminated input
    M = np.array([[aC + (sC - aC) * (1 - g), aD + (sD - aD) * (1 - g)],
                  [(sC - aC) * g,            (sD - aD) * g]])
    return 1 - np.array([1, 1]) @ np.linalg.matrix_power(M, N) @ np.array([1, 0])
print("Worked example:", round(p_high_stakes(0.4, 0.5, 5, 1, 3, 2), 6))
print("Independent   :", round(1 - 0.8 ** 6, 6))
print("N-agent table (p=0.001, q=0.1, n=1000, g=1), percent:")
for N in (1, 2, 3, 5, 10):
    row = [float(round(100 * p_high_stakes(0.001, 0.1, c, 1, 1000, N), 2))
           for c in (1, 2, 5, 10)]
    print(N, row)
