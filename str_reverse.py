import sys
import os
import random

def main():
    a = input('Enter a single word: ').upper()
    b = ''

    length = len(a)

    # print(length)

    for i in range(length-1, -1, -1):

        b += a[i]

    # print(a)
    # print(b)

    if a == b:
        print(f'{a} -- is Palindrome string -- {b}')

    else:
        print(f'{a} -- is not Palindrome string -- {b}')





if __name__ == '__main__':
    main()