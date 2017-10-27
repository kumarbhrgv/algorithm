import numpy as np
def pi(n, batch=1000):
    t = 0
    print(range(n // batch))
    for i in range(n // batch):
        p = np.random.rand(batch, 2)
        p = (p * p).sum(axis=1)
        t += (p <= 1).sum()
    return 4 * t / n

print(pi(10 ** 8))