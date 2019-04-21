"""all the graphing is done here"""

# matplotlib is graphing module, default included in python in most cases
import matplotlib.pyplot as plt


# from calculations.py import all the needed functions to get list of data
# to graph

from calculations import (Arithmatic, Binary,
                          LeastChange, Exponential, Intvarients, Fibonacci,
                          Tribonacci, Pythagorean, Palindromic, Pi_digits,
                          Pi_Series, Primes, Geometric, TriangleNumbers)


def setstyle():
    plt.style.use('fivethirtyeight')
    # my personal favorite style, despite commercial
    # sounding name it
    # is included in default matplotlib, not additional
    # download
    # if more than 6 graphed at a time don't use

# for more than 6 colors


def setstyle2():
    plt.style.use('classic')


# if we already have the data for y just graph it
# only used for command line interface
def cmdlinegraph(n):
    # just graph list n, already calculated
    # y axis is values in list
    y = n
    # x axix is (1,2,3...) for length of list
    x = list(range(len(y)))

    # remove o for line graph
    plt.plot(x, y, 'o', label="Graph")
    # include label and color in legend
    plt.legend()


# reusable function to graph using passed though
# function, only function and scale is needed to
# graph
def genericgraph(n, nn):

    # function n with scale nn
    # y axis is values in list returned from function
    y = n(nn)
    # x axix is (1,2,3...) for length of list
    x = list(range(len(y)))

    # remove o for line graph
    plt.plot(x, y, 'o', label=n.__name__)
    plt.legend()
    # include label and color in legend


# reusable function to graph using passed though
# function, function scale and one more variable
# is used to # graph
def genericgraph2(n, nn, nnn):

    # n function with two variables inputed
    y = n(nn, nnn)
    x = list(range(len(y)))

    # remove o for line graph
    plt.plot(x, y, 'o', label=n.__name__)
    plt.legend()


# function to allow exponent function to be reused
# for squares, cubes and higher exponents,
# nnn is value of exponent,
# for squares and cubed legend says squared
# and cubed instead of just Exponent 2 or 3
def expgraph(n, nn, nnn):

    # nnn is exponent, nn is scale, n is name of fucntion
    y = n(nn, nnn)
    x = list(range(len(y)))

    # remove o for line graph
    if (nnn == 2):
        plt.plot(x, y, 'o', label="Squares")
    if (nnn == 3):
        plt.plot(x, y, 'o', label="Cubes")
    if (nnn > 3):
        plt.plot(x, y, 'o', label=n.__name__ + " " + str(nnn))
    plt.legend()


# similar to previous graph functions, uses 3 variables
# to pass through passed through function variable
def genericgraph3(n, nn, nnn):

    y = n(nn, nnn, custom)
    x = list(range(len(y)))

    # remove o for line graph
    plt.plot(x, y, 'o', label=n.__name__)
    plt.legend()

# similar to previous graph functions, uses 4 variables
# to pass through passed through function variable


def genericgraph4(n, nn, nnn, custom):

    y = n(nn, nnn, custom)
    x = list(range(len(y)))

    # remove o for line graph
    plt.plot(x, y, 'o', label=n.__name__)
    plt.legend()

# similar to expgraph, uses nn as variable
# to graph evens, odds, and Integers
# intvariants returns Integers, evens and odds
# at same time, only one from triplet is needed for each graph


def intgraph(nn, nnn):

    y = Intvarients(nnn * 2)[nn]
    x = list(range(len(y)))

    # remove o for line graph
    # only plot up to scale
    if nn == 0:
        plt.plot(x[:nnn], y[:nnn], 'o', label='Integers')
    if nn == 1:
        plt.plot(x[:nnn], y[:nnn], 'o', label='Evens')
    if nn == 2:
        plt.plot(x[:nnn], y[:nnn], 'o', label='Odds')

    plt.legend()

# similar to intgraph, except for Pythagorean triplets


def trianglegraph(n, nn):

    y = Pythagorean(nn)[n]
    x = list(range(len(y)))

    # remove o for line graph
    if n == 0:
        plt.plot(x[:nn], y[:nn], 'o', label='Hypotenuse')
    if n == 1:
        plt.plot(x[:nn], y[:nn], 'o', label='Middle Side')
    if n == 2:
        plt.plot(x[:nn], y[:nn], 'o', label='Shortest Side')

    plt.legend()


# these are the functions actually called from gui and command line
def graph_arithmatic(scale, custom, custom2):
    genericgraph4(Arithmatic, scale, custom, custom2)


def graph_binary(scale):
    genericgraph(Binary, scale)


def graph_change(scale):
    genericgraph(LeastChange, scale)


def graph_exponential(scale, x):
    expgraph(Exponential, scale, x)


def graph_exponentialdef(scale):
    expgraph(Exponential, scale, 4)

# 0 is for Integers


def graph_Integers(scale):
    intgraph(0, scale)

# 1 is for evens


def graph_evens(scale):
    intgraph(1, scale)


def graph_odds(scale):
    intgraph(2, scale)


def graph_Fibonacci(scale):
    genericgraph(Fibonacci, scale)


def graph_Tribonacci(scale):
    genericgraph(Tribonacci, scale)

# 0 is for Hypotenuse


def graph_Hypotenuse(scale):
    trianglegraph(0, scale)


def graph_Middle(scale):
    trianglegraph(1, scale)


def graph_Shortest(scale):
    trianglegraph(2, scale)


def graph_Palindromic(scale):
    genericgraph(Palindromic, scale)


def graph_Primes(scale):
    genericgraph(Primes, scale)


def graph_TriangleNumbers(scale):
    genericgraph(TriangleNumbers, scale)


def graph_Geometric(scale):
    genericgraph2(Geometric, scale, 3)

# 2 for raising to power of 2


def graph_squared(scale):
    graph_exponential(scale, 2)

# 3 raising to power of 3


def graph_cubed(scale):
    graph_exponential(scale, 3)


def graph_piseries(scale):
    genericgraph(Pi_Series, scale)


def graph_pidigits(scale):
    genericgraph(Pi_digits, scale)


# show the graph
def showgraph():
    plt.show()

# clear the graph then close it


def closegraph():
    plt.cla()
    plt.close()


""" for testing purposes not used """
# scale = 10
# custom = 2
# custom2 = 2
# def graph():
#   plt.close()
#   setstyle()
#   graph_Hypotenuse(scale)
#   graph_Middle(scale)
#   graph_Shortest(scale)
#   graph_Geometric(scale)
#   graph_TriangleNumbers(scale)
#   graph_Palindromic(scale)
#   graph_Primes(scale)
#   graph_arithmatic(scale, custom, custom2)
#   graph_change(scale)
#   graph_exponential(scale, 2)
#   graph_squared(scale)
#   graph_cubed(scale)
#   graph_binary(scale)
#   graph_evens(scale)
#   graph_odds(scale)
#   graph_Integers(scale)
#   graph_Fibonacci(scale)
#   graph_Tribonacci(scale)
#   plt.show()
# graph()
