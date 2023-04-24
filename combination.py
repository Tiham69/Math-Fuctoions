def factorial(b):
    fac = 1

    for i in range(1, (b + 1)):
        fac *= i

    return fac

n, c, r =   int(input('Enter the value of n: ')),\
            input('Enter the combination symbol: '), \
            int(input('Enter the value of r: '))

if c in 'cC' and n > r:

     down = n-r

     combi = factorial(n) / (factorial(r) * factorial(down))

     print(combi)

elif c not in 'cC' and not (n > r):
    print('Enter a valid symbol and \'n larger than r\'')

elif c not in 'cC':
    print('Enter a valid symbol!!!')

elif not(n > r):
    print('n should be larger than r')