'''
2494 задача


def f(n, k):
    if n < k:
        return f(n + 1, k) + f(n * 2, k) + f(n * 3, k)
    elif n == k:
        return 1
    else:
        return 0


print(f(1, 18))

3097


def f(n, k):
    if n < k:
        return f(n + 1, k) + (f(n * 1.5, k) if not n % 2 else 0)
    elif n == k:
        return 1
    else:
        return 0


print(f(2, 22))

3066


def f(n, k):
    if n < k:
        return f(n + 2, k) + f(n + 3, k) + f(2 * n - 1, k)
    elif n == k:
        return 1
    else:
        return 0


print(f(2, 11))


3095


def f(n, k):
    if n < k:
        return f(n + 1, k) + f(2 * n, k) + f(2 * n + 1, k) + f(10 * n, k)
    elif n == k:
        return 1
    else:
        return 0


print(f(1, 15))


2766


def f(n, k):
    if n > k:
        return f(n - 1, k) + f(n - 3, k) + f(n // 3, k)
    elif n == k:
        return 1
    else:
        return 0


print(f(22, 2))


2767


def f(n, k):
    if n > k:
        return f(n - 1, k) + f(n - 3, k) + (f(n % 4, k) if n > 4 else 0)
    elif n == k:
        return 1
    else:
        return 0


print(f(22, 2))


3102


def f(n, k):
    if n < k:
        return f(n + 1, k) + f(n + 10, k)
    elif n == k:
        return 1
    else:
        return 0


print(f(10, 33))


3103


def f(n, k):
    if n < k:
        return f(n + 1, k) + (f(n + 11, k) if n % 10 != 9 else f(n + 10, k))
    elif n == k:
        return 1
    else:
        return 0


print(f(26, 49))

445
2768
3611
447
446 на следующий
'''

'''def f(n, k):
    if n == 10 or n == 11:
        return 0

    if n < k:
        return f(n + 1, k) + f(n + 2, k) + f(n * 3, k)
    elif n == k:
        return 1
    else:
        return 0


# print(f(1, 8) * f(8, 28))


def f(n, k):
    if n > k:
        return f(n - 8, k) + f(n // 2, k)
    elif n == k:
        return 1
    else:
        return 0


# print(f(102, 43) * f(43, 5))


def f(n, k):
    if n < k:
        return f(n + 1, k) + f(n * 2, k)
    elif n == k:
        return 1
    else:
        return 0


# print(f(4, 22) + f(4, 11))'''

'''def f(n, k, i):
    if n == i:
        return 0
    if n < k:
        return f(n + 1, k, i) + f(n + 2, k, i)
    elif n == k:
        return 1
    else:
        return 0


print(f(17, 29, 23) * f(11, 17, 23) +
      f(23, 29, 17) * f(11, 23, 17) +
      f(17, 23, 0) * f(11, 17, 0) * f(23, 29, 0))


def f(n, k):
    if n < k:
        return f(n + 1, k) + f(n + 5, k)
    elif n == k:
        return 1
    else:
        return 0


n = 5
for k in range(6, 100):
    if f(n, k) == 34:
        print(k)'''


def f(n, k):
    if n < k:
        return f(n + 3, k) + f(n * 3, k)
    elif n == k:
        return 1
    else:
        return 0


n = 3
ln = 0
for k in range(4, 100, 2):
    if f(n, k) > 0:
        ln += 1
print(ln)