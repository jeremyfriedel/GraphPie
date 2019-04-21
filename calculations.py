""" general formula for nearly all functions
is make empty list, do calculation to get
next number in sequence, (usually addition, or multiplication)
add result to list, continue until list is long enough
to fit the size of the graph given by user, end infinite loop
and return list of the given size needed"""


# Arithmetic sequence, custom2 is starting number
# custom is amount added each time
# for ex. if 1 and 5 sequence is
# 1,6,11,16...
def Arithmatic(n, custom, custom2):
    arth = []
    tmp = custom2
    # infinite loop till list is long enough
    # for graph
    while(True):
        tmp = tmp + custom
        # add to list to be graphed
        arth.append(tmp)
        # once we have enough to fit scale loop
        # can exit
        if (len(arth) == n):
            break

    # return list
    return arth

# double each time from 2
# powers of 2
# 2,4,8,16,32...


def Binary(n):
    bina = []
    tmp = 1
    while(True):
        # double it each time
        tmp = tmp * 2
        # add to list to be graphed
        bina.append(tmp)
        # once list is long enough
        # end loop
        if (len(bina) == n):
            break

    # return list
    return bina

# from change assignment
# least number of coins to give change back
# does not include half-dollar or dollar coins


def LeastChange(n):
    least = []
    # count number of coins

    # start at largest value until below value of coin to find
    # most efficient method to give change

    for cash in range(0, n):
        counter = 0
        while (cash >= 25):   # quarters
            cash = cash - 25  # subtract to under 25
            counter = counter + 1

        while (cash >= 10):   # dimes
            cash = cash - 10  # subtract to under 10
            counter = counter + 1

        while (cash >= 5):   # nickels
            cash = cash - 5  # subtract to under 5
            counter = counter + 1

        while (cash > 0):    # pennies
            cash = cash - 1  # subtract till zero
            counter = counter + 1

        # add result to list
        least.append(counter)

    # return list
    return least

# raise to any exponent, used for squared, cubed
# and custom amount


def Exponential(n, nn):
    expo = []
    i = 0
    while(True):
        expo.append(i**nn)
        if (len(expo) == n):
            break
        i = i + 1

    return expo


# gives evens, odds, and integer as triplet,
# only one need for each so separated out by
# graph_Intvarients in graphing.py
def Intvarients(n):
    # just fills a list with all integers up to size of n
    # 1,2,3,4...
    intg = list(range(1, n))
    evens, odds = [], []
    # uses list of integers to find odds and evens
    for i in intg:
        # if its divisible by 2 its even
        if i % 2 == 0:
            evens.append(i)
        # if not its odd
        if i % 2 != 0:
            odds.append(i)

    # return everything, is separated out by other functions as needed
    return intg, evens, odds

# Fibonacci sequence
# number is sum of previous 2
# numbers, starts with 0,1
# 0,1,1,2,3,5...


def Fibonacci(n):
    # starting numbers
    fibn = [0, 1]
    a, b = 0, 1
    while(True):
        # a = b
        # b = a + b
        a, b = b, a + b
        fibn.append(b)
        # once list is long enough
        # end loop
        if (len(fibn) == n):
            break

    return fibn
# like Fibonacci sequence
# number is sum of previous 3
# numbers, instead of previous 2
# starts with 0,0,1
# 0,0,1,1,2,4,7,13,24


def Tribonacci(n):
    trib = [0, 0, 1]
    a, b, c = 0, 0, 1
    while(True):
        # a = b
        # b = c
        # c = a + b + c
        a, b, c = trib[-2], trib[-1], a + b + c
        trib.append(c)
        # once list is long enough
        # end loop
        if (len(trib) == n):
            break

    return trib

# Geometric Sequence (sequence multiplied by set amount each time)
# (3,9,27...)


def Geometric(n, custom):
    geom = [custom]
    tmp = custom
    while(True):
        tmp = tmp * custom
        # add to list of results
        geom.append(tmp)
        # once list is long enough
        # end loop
        if (len(geom) == n):
            break

    return geom

# Pythagorean triplets (a^2 + b^2 = c^2 where all are whole numbers)
# all are returned, other functions separate them as needed


def Pythagorean(n):
    # use sets to prevent duplicates
    hypotenuse = set()
    middle = set()
    shortest = set()

    # 230 is size needed to get first 100 of
    # the smallest side in triangle
    # i for a , ii  for b
    for i in range(1, 230):
        for ii in range(1, 230):
            # instead of looping for c
            # just calculate what it would need to be
            iii = (i**2) + (ii**2)
            # sqrt do determine necessary value of c
            # given a and b
            sqrt = (iii**.5)
            # if its whole add it,
            # if not loop to next value
            if (sqrt % 1 == 0):
                sqrt = int(sqrt)
                if (len(shortest) == n):
                    break
                    # break out of loop if we have enough already of
                    # shortest side length is slowest growing so if
                    # shortest list is long enough
                    # middle and hypotenuse are already long enough
                # sanity check, should always return true
                if(((i**2) + (ii**2)) == (iii)):
                    hypotenuse.add(sqrt)
                    # determine which value is middle and which is shortest
                    if (ii >= i):
                        middle.add(ii)
                        shortest.add(i)
                    else:
                        middle.add(i)
                        shortest.add(ii)

    # convert completed sets into lists
    hypotenuse = list(hypotenuse)
    middle = list(middle)
    shortest = list(shortest)

    # sort them into correct order, smallest to largest
    hypotenuse.sort()
    middle.sort()
    shortest.sort()

    # return lists up to needed length
    return hypotenuse[:n], middle[:n], shortest[:n]


# Palindromic numbers (numbers same backwards and forwards)
# (1,2,3,4,5,6,7,8,9,11,22,33...)
def Palindromic(n):
    i = 0
    pals = []
    while (True):
        i = i + 1
        # convert to string to reverse it
        strnum = str(i)
        # [::-1] is syntax for string backwards
        # if backwards and forwards are the same
        # then its a palindrome
        if (strnum[::-1] == strnum):
            pals.append(i)
        # break loop if we filled list up to required
        # length
        if (len(pals) == n):
            break

    return pals


# function contains and returns pi as a string, calculating pi
# mathematically is possible, but requires additional
# python libraries to do efficiently, and is only used by two options
# so string from website is used, math.pi is not long enough
# for this use case (math.pi only has 17 digits) string is from
# from http://www-groups.dcs.st-and.ac.uk/history/HistTopics/1000_places.html
# no decimal point cause not used by either function that uses it
def pistring():
    pie = "314159265358979323846264338327950288419716939937510\
58209749445923078164062862089986280348253421170679\
82148086513282306647093844609550582231725359408128\
48111745028410270193852110555964462294895493038196"
    return pie

# Digits of pi (goes from 1 to 9) (3,1,4,1,5...)
# uses pistring and finds digit at position
# on string


def Pi_digits(n):
    pie = pistring()

    digits = []

    for i in range(0, n):
        piedigit = pie[i]
        digits.append(int(piedigit))

    return digits
# Value of pi without the decimal place (31415...) (3,31,314,3141,31415...)
# uses pistring and concatenates up to  current position


def Pi_Series(n):
    pie = pistring()

    digits = []

    for i in range(1, n):
        piedigit = pie[0:i]
        digits.append(int(piedigit))

    return digits

# primes numbers in order
# Prime Numbers (numbers with only two factors (1,number))
# (3,5,7,9...)


def Primes(n):

    primes = []
    # just a large number
    # starting at 2 cause 2 first prime
    for i in range(2, 1000000):
        # variable to check if prime
        prime = True
        # factors can't be larger
        # than square root of number
        for factor in range(2, int(i**.5) + 1):
            # if perfect divisor
            # than it is a factor
            # and number can't be prime
            if (i % factor == 0):
                prime = False
                # don't need to check if there
                # are more factors
                # already know it's not prime
                break
        # if no factors besides 1 and n
        # then its prime
        if (prime):
            primes.append(i)

        # once list long enough
        # we can stop calculating
        if (len(primes) == n):
            break

    return primes
# Triangular Numbers (simplest two level dot \
# triangle is one dot on top, two on bottom, simplest \
# three level triangle is 1 on top , two in middle, three on bottom...) \
# (1,3,6,10,15...)
#
##
###
####
#####
######


def TriangleNumbers(n):
    # empty list for results
    tri = []
    tmp = 1
    total = 0
    while(True):
        # formula is just 1 + 2  + 3 ...
        # every interger up to n summed
        total = total + tmp
        tmp = tmp + 1
        tri.append(total)
        if (len(tri) == n):
            break

    return tri
# Custom Fibonacci like sequence (each number is sum of
# two previous ones, starting number is chosen by user) (4,5,9,14...)


def fibcust(n, custom):
    fibn = []
    a, b = custom, custom + 1
    fibn.append(b)
    while(True):
        a, b = b, a + b
        fibn.append(b)
        if (len(fibn) == n):
            break

    return fibn
