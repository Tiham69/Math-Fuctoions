print("s = ut + 1/2 at^2 Formula\n")

ts = float(input('Enter start time: '))
tf = float(input('Enter final time: '))
u = float(input('Enter start velocity: '))
v = float(input('Enter final velocity: '))

a = 0

t = tf - ts

if t > 0:
    a = (v - u)/abs(t)
else:
    pass

s = (u * t) + 0.5 * (a * pow(t, 2))

print(f'Your distance is {s} '
      f'm \nand acelaration is {a} m/s^2')