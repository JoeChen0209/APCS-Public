def K(a, n):
    if n >= 0:
        return (K(a, n-1)+a[n])
    else:
        return 0


def G(n):
    a = [5, 4, 3, 2, 1]
    return K(a, n)


print(G(3))
