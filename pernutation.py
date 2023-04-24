def factorial(n):
    fac = 1

    for i in range(1, (n + 1)):
        fac *= i

    return fac


n, p, r = int(input('Enter the value of n: ')), \
    input('Enter a permutation symbol: '), \
    int(input('Enter the value of r: '))

if p in 'pP':

    down = n - r

    f = factorial(n) / factorial(down)

    print(f)

elif p not in 'Pp' and not (n > r):
    print('Enter a valid symbol and \'n larger than r\'')

elif p not in 'Pp':
    print('Enter a valid symbol!!!')

elif not(n > r):
    print('n should be larger than r')