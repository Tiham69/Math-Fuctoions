# area and diameter of quadrilateral
from math import sqrt

def main():

    type = ''
    print('Enter 4 side\'s of quadrilateral (cm or meter).')


    while (type != '0'):
        try:
            a, b, c, d = [float(input('Value of a: ')), float(input('Value of b: ')), int(input('Value of c: ')),
                          float(input('Value of d: '))]

            type = input('Enter area | diameter (0 to quit): ').lower().strip()

            if type != '0':
                unit = input('Enter Unit type (centimeter or meter): ').lower()

                if type in 'area':

                    if unit in 'meter':

                        area = quad_area(a, b, c, d)
                        print(f'The area of quadrilateral is {area: .2f}  meter.')

                    elif unit in 'centimeter':

                        area = quad_area(a, b, c, d)
                        print(f'The area of quadrilateral is {area: .2f} cm.')

                elif type in 'diameter':
                    if unit in 'meter':

                        dia = diameter(a, b, c, d)
                        print(f'The diameter of quadrilateral is {dia: .2f} meter.')

                    elif unit in 'centimeter':

                        dia = diameter(a, b, c, d)
                        print(f'The diameter of quadrilateral is {dia: .2f} centimeter.')
            elif type.strip() == '0':
                    print('Thank you for using the programme.')
                    break

        except ValueError:
            print('\nEnter Number for the length.\n')

def quad_area(a, b, c, d):

    s = (a + b + c + d) / 2

    sq_a = (s - a) * (s - b) * (s - c) * (s - d)

    return sqrt(sq_a)


def diameter(a, b, c, d):

    s2 = a + b + c + d

    return s2


if __name__ == '__main__':
    main()