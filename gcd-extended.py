def gcd(x, y):
    u0, v0 = 1, 0
    u1, v1 = 0, 1
    while y:
        q = x // y
        x, y = y, x % y
    return x, u0, v0

print(gcd(2*3*7*9*11, 6*12*13))
