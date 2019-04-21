""" command line way to access calculations and graph them """

# import all the functions that do the math
from calculations import (Arithmatic, Binary,
                          LeastChange, Exponential, Intvarients, Fibonacci,
                          Tribonacci, Pythagorean, Palindromic, Pi_digits,
                          Pi_Series, Primes, Geometric, TriangleNumbers,
                          fibcust)

# import the functions that do the graphing
from graphing import cmdlinegraph, setstyle, showgraph

# let user see the options
message = """
Options:
1. Prime Numbers (3,5,7,9...)
2. Fibonacci sequence (each number is sum of two previous ones, starting \
with 0 and 1) (0,1,1,2,3,5,8,13,21...)
3. Positive Integers (1,2,3,4,5...)
4. Round right triangle hypotheses (largest number in Pythagorean triplet) \
(a^2 + b^2 = c^2 where all are whole numbers)
5. Round right triangle smallest side (smallest number in Pythagorean \
triplet) (a^2 + b^2 = c^2 where all are whole numbers)
6. Round right triangle second largest side (middle number in Pythagorean \
triplet) (a^2 + b^2 = c^2 where all are whole numbers)
7. Square of numbers (n^2) (1,4,9,16...)
8. Cube of numbers (n^3) (1,8,27,64...)
9. Evens (divisible by 2) (2,4,6,8...)
10. Odds (Not divisible by 2) (1,3,5,7,9...)
11. Arithmetic Sequence (sequence going up by set amount each time) \
(1,6,11,16,21...)
12. Binary Sequence (2,4,8,16,32...)
13. Geometric Sequence (sequence multiplied by set amount each time) \
(3,9,27...)
14. Triangular Numbers (simplest two level dot triangle is one dot on top, \
two on bottom, simplest three level triangle is 1 on top , two in middle, \
three on bottom...) (1,3,6,10,15...)
15. Least number of coins that change in cents could be given by using coins \
up to the quarter in value(1,2,3,4,1...)
16. Tribonacci numbers (like Fibonacci but starts with 0,0,1 and next number \
is sum of last three numbers instead of last two) (0,0,1,1,2,4,7,13,24,44)
17. Palindromic numbers (numbers same backwards and forwards) \
(1,2,3,4,5,6,7,8,9,11,22,33...)
18. Digits of pi (goes from 1 to 9) (3,1,4,1,5...)
19. Value of pi without the decimal place (31415...) \
(3,31,314,3141,31415...)
20. Custom Fibonacci like sequence (each number is sum of \
two previous ones, starting number is chosen by user) (4,5,9,14...)
21. Custom exponential sequence (ex. n^5)

"""
# print the choices
print(message)


print("Enter the sequence you want")
print()
# get the inputs
theinput = input("sequence? (1-21)")
secinput = input(
    "How long go you need the sequence for (length of sequence)? ")
secinput = int(secinput)


# check what the inputs are,
# prompt for additional variables if necessary
# calculate it using calculation.py functions,
# then put list into result
# variable for printing
if (theinput == "arithmetic" or theinput == '11'):
    thirdinput = int(input("Starting number? "))
    fourthinput = int(input("Amount to increase each time? "))
    result = (Arithmatic(secinput, fourthinput, thirdinput))

# if the input matches do the calculation
# and put it into result variable
if (theinput == "binary" or theinput == '11'):
    result = (Binary(secinput))


# same for all below
# check what the inputs are,
# prompt for additional variables if necessary
# calculate it using calculation.py functions,
# then put list into result
# variable for printing

if (theinput == "change" or theinput == '15'):
    result = (LeastChange(secinput))

if (theinput == "exp" or theinput == '21'):
    thirdinput = int(input("Exponent ? (2 for squared, 3 for cubed ...) "))
    result = (Exponential(secinput, thirdinput))

if (theinput == "int" or theinput == '3'):
    result = (Intvarients(secinput)[0])


if (theinput == "even" or theinput == '9'):
    result = (Intvarients(secinput)[1])

if (theinput == "odds" or theinput == '10'):
    result = (Intvarients(secinput)[2])


if (theinput == "hyp" or theinput == '4'):
    result = (Pythagorean(secinput)[0])

if (theinput == "mid" or theinput == '6'):
    result = (Pythagorean(secinput)[1])

if (theinput == "sho" or theinput == '5'):
    result = (Pythagorean(secinput)[2])

if (theinput == "fib" or theinput == '2'):
    result = (Fibonacci(secinput))

if (theinput == "trib" or theinput == '16'):
    result = (Tribonacci(secinput))


if (theinput == "pal" or theinput == '17'):
    result = (Palindromic(secinput))

if (theinput == "pid" or theinput == '18'):
    result = (Pi_digits(secinput))

if (theinput == "pis" or theinput == '19'):
    result = (Pi_Series(secinput))

if (theinput == "primes" or theinput == '1'):
    result = (Primes(secinput))

if (theinput == "geo" or theinput == '12'):
    thirdinput = int(input("Starting number? "))
    result = (Geometric(secinput, thirdinput))

if (theinput == "tria" or theinput == '14'):
    result = (TriangleNumbers(secinput))

if (theinput == "squared" or theinput == '7'):
    result = (Exponential(secinput, 2))
if (theinput == "Cubed" or theinput == '8'):
    result = (Exponential(secinput, 3))


if (theinput == "fibcust" or theinput == '20'):
    thirdinput = int(input("Starting number? "))
    result = (fibcust(secinput, thirdinput))

# output result
print(result)

# see if user wants graph
graphinput = input("Do you want to see a graph of the series? y/n ")

# see if user wants graph
if ((graphinput == 'y') or (graphinput == 'yes') or (graphinput == 'ye')):
    # if so graph it using graphing.py
    # set the style
    setstyle()
    # we already have result so we just pass in
    # what will be the y values
    # no need to calcualate again
    cmdlinegraph(result)
    # show the graph
    showgraph()
