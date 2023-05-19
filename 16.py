'''def F(n):
    if n <= 3:
        return n
    elif 3 < n <= 32:
        return n // 4 + F(n - 3)
    elif n > 32:
        return 2 * F(n - 5)

print(F(100))


def F(n):
    if n == 1:
        return 1
    elif n > 1:
        if not n % 2:
            return n * n + F(n - 1)
        else:
            return F(n - 1) + 2 * F(n - 2)


print(F(23))'''
# № 2266

'''from functools import *


@lru_cache(None)
def F(n):
    if n < 10:
        return n
    elif n >= 10:
        return F(G(n))

@lru_cache(None)
def G(n):
    if n < 10:
        return n
    elif n >= 10:
        return n % 10 + G(n // 10)

print(G(12345678987654321))'''

def F(n):
    if n < 4:
        return n - 1
    elif n >= 4:
        if n % 3:
            return F(n - 2) + F(n - 3)
        else:
            return n + 2 * F(n - 1)


print(sum(list(map(int, str(F(25))))))