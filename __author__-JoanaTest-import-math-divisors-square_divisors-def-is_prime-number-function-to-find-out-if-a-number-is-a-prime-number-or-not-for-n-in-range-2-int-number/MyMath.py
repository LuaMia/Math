__author__ = 'LuaMia'
import math

divisors = []
square_divisors = []


def is_prime(number):
    # function to find out if a number is a prime-number or not
    for n in range(2,int(number/2)):
        if number % n == 0:
            return False
    return True


def find_divisors(number):
    # function to find all divisors of a given number, returns divisors in a list
    n = 1
    while n <= number:
        if number % n == 0:
            divisors.append(n)
            n += 1
        else:
            n += 1
    return divisors


def find_square_divisors(number):
    # function to find all square divisors of a given number, returns divisors in a list, needs find_divisors

    squares = find_divisors(number)
    for number in squares:
        if math.sqrt(number)%1 == 0:
            square_divisors.append(number)
    return square_divisors


def diophant(z, x_i, y_i):
    # function to solve the linear diophantine equitation for any given x,y and result(z)
    for x in range(1, int(z/x_i)):
        for y in range (1, int(z/y_i)):
            if x_i*x + y_i*y == z:
                print(x, y)


def find_gcd(number_one, number_two):
    # function to find all divisors which divide a and b, will only return the highest of them

    n = 1
    while n <= number_two:
        if number_one % n == 0 and number_two % n == 0:
            divisors.append(n)
            n += 1
        else:
            n += 1
    if number_two in divisors:
        return divisors[len(divisors)-2]
    else:
        return divisors[len(divisors)-1]


def distance_point_to_point(first_point, second_point):
    f_point = first_point.split(',')
    fp1 = float(f_point[0])
    fp2 = float(f_point[1])
    fp3 = float(f_point[2])
    s_point = second_point.split(',')
    sp1 = float(s_point[0])
    sp2 = float(s_point[1])
    sp3 = float(s_point[2])

    distance = math.sqrt((fp1-sp1)**2+(fp2-sp2)**2+(fp3-sp3)**2)
    return distance


def scalar_product(vector_a, vector_b):
    vector_a_l = vector_a.split(',')
    a1 = float(vector_a_l[0])
    a2 = float(vector_a_l[1])
    if len(vector_a_l) == 3:
        a3 = float(vector_a_l[2])
    else:
        a3 = 0

    vector_b_l = vector_b.split(',')
    b1 = float(vector_b_l[0])
    b2 = float(vector_b_l[1])
    if len(vector_b_l) == 3:
        b3 = float(vector_b_l[2])
    else:
        b3 = 0

    scalar = a1*b1 + a2*b2 + a3*b3
    return scalar

