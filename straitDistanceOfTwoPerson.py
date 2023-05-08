import os
import sys
import random
from math import sin, cos, sqrt, pi

a = 1

while(a != 0):
    try:
        a = int(input('Enter 0 to quit or 1 to start: '))
        if a == 0:
            break
            
        ang = int(input('Enter the angle(degree): '))
        speed_1 = int(input('Enter the first persons velocity(k/h): '))
        speed_2 = int(input('Enter the second persons velocity(k/h): '))
        hour = int(input('Enter both persons time(h): '))

        ac = speed_1 * hour
        ab = speed_2 * hour

        ang_bad = 180 - ang

        rad = pi / 180

        bd = ab * sin(ang_bad * rad)
        ad = ab * cos(ang_bad * rad)

        # print(sin((ang_bad * rad)))      # error handle
        # print(cos((ang_bad * rad)))

        cd = ac + ad

        bc = pow(cd, 2) + pow(bd, 2)

        f_bc = sqrt(bc)

        print(f'The strait distance between them is: {f_bc:.1f} km', end='\n\n')
    except ValueError:
        print('Enter only number\'')