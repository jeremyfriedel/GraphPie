""" This programs uses matplotlib to graph various interger sequences
that are calculated in calculations.py, then graphed in graphing.py,
which can then be directed by the user using in the command line interface
of cmdline.py, or the graphical user interface in guifinal.py"""

from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
# without this code tkinter and matplotlib seem to
# have some sort of bug on os x
# where they use they same resource
# causing the program to crash, work around from
# https://github.com/MTG/sms-tools/issues/36
# matplotlib uses TkAgg instead of default os x
# back-end from tkinter
# this code avoids the bug


from appJar import gui
# wrapper around tkinter for cleaner syntax
# tkinter is default python GUI toolkit
# included in default python
# appjar is in pip3 and on github


# import all the functions that do the graphs
# from graphing.py
from graphing import (
    graph_change,
    showgraph,
    graph_arithmatic,
    graph_binary,
    graph_change,
    graph_evens,
    graph_odds,
    graph_Integers,
    graph_Fibonacci,
    graph_Tribonacci,
    graph_Hypotenuse,
    graph_Middle,
    graph_Shortest,
    graph_Palindromic,
    graph_Palindromic,
    graph_Primes,
    graph_TriangleNumbers,
    graph_Geometric,
    graph_squared,
    graph_cubed,
    graph_piseries,
    graph_pidigits,
    graph_exponentialdef,
    setstyle,
    setstyle2,
    closegraph)


# dictionary of all the options to be graphed,
# all set to false to be used to make the check-marks
# default unchecked. If they are checked false
# is changed to true in dictionary.

Choices = {
    "Arithmetic": False,
    "Binary": False,
    "Change": False,
    "Cubes": False,
    "Evens": False,
    "Exponential": False,
    "Fibonacci": False,
    "Geometric": False,
    "Hypotenuse": False,
    "Integers": False,
    "Middle Triangle": False,
    "Odds": False,
    "Palindromic": False,
    "Pi Digits": False,
    "Pi Series": False,
    "Primes": False,
    "Shortest Triangle": False,
    "Squares": False,
    "Triangle Numbers": False
}


def Welcome(props):

    # message in pop-up
    message = "Welcome to my final project! This is a program to graph \
various mathematical sequences onto a graph. You can graph only one \
sequence at a time, or graph them all at the same time, or anything in \
between. The sliding scale determines the range of the x axis. \
The graph button graphs all options current graphed, the help \
button descibes the graph options in more detail. Press the + button \
to view all options"

    # pop-up window if welcome button is pushed

    app.infoBox("Welcome", message, parent=None)


def helpb(props):

    # message in pop-up
    message = """
Options:
Arithmetic Sequence (sequence going up by set \
amount each time) (1,6,11,16,21...)
Binary Sequence (2,4,8,16,32...)
Least number of coins that change in cents could be \
given by using coins up to the quarter in value(1,2,3,4,1...)
Prime Numbers (numbers with only two factors (1,number)) (3,5,7,9...)
Fibonacci sequence (each number is sum of two previous ones, \
starting with 0 and 1) (0,1,1,2,3,5,8,13,21...)
Positive Integers (1,2,3,4,5...)
Round right triangle hypotheses (largest number in \
Pythagorean triplet) (a^2 + b^2 = c^2 where all are whole numbers)
Round right triangle smallest side (smallest number in \
Pythagorean triplet) (a^2 + b^2 = c^2 where all are whole numbers)
Round right triangle second largest side (middle number in \
Pythagorean triplet) (a^2 + b^2 = c^2 where all are whole numbers)
Square of numbers (n^2) (1,4,9,16...)
Cube of numbers (n^3) (1,8,27,64...)
Evens (divisible by 2) (2,4,6,8...)
Odds (Not divisible by 2) (1,3,5,7,9...)
Geometric Sequence (sequence multiplied by set amount each time) (3,9,27...)
Triangular Numbers (simplest two level dot \
triangle is one dot on top, two on bottom, simplest \
three level triangle is 1 on top , two in middle, three on bottom...) \
(1,3,6,10,15...)
Tribonacci numbers (like Fibonacci \
but starts with 0,0,1 and next number is \
sum of last three numbers instead of last two) (0,0,1,1,2,4,7,13,24,44)
Palindromic numbers (numbers same backwards and forwards) \
(1,2,3,4,5,6,7,8,9,11,22,33...)
Digits of pi (goes from 1 to 9) (3,1,4,1,5...)
Value of pi without the decimal place (31415...) (3,31,314,3141,31415...)
"""

# additional info about what each sequence is doing, pop-up window if
# choices button is pushed

    app.infoBox("Help", message, parent=None)

# function called every time graph button is pushed


def changed(props):
    raw = app.getAllProperties()
    # get the current dictionary of check-marks, see if checked or not

    scale = app.getScale("")
    # check where scale is, this will be length of x axis of graph

    selected = [key for key, checked in raw["Choices"].items() if checked]
    # returns all checked items, that are true in dictionary
    # selected is list of all checked options,
    # does not include unchecked items

    message = "Please select an options to graph"

    # pop-up window saying nothing checked to graphed
    if (len(selected) == 0):
        app.infoBox("None Selected", message, parent=None)
        return 0

    # closes the graph and clears it, to prevent multiple graph windows being
    # open
    closegraph()

    if (len(selected) <= 6):
        setstyle()
        # I like this style best but if
        # more than 6 checks it starts reusing colors,
        # so other style is used if more than 6 things checked
    if (len(selected) > 6):
        setstyle2()
        # other stlye, for more than 6 colors

    # all these calculations are done
    # in calculations.py and graphed in graphing.py
    # if string in list, graph that options and put into one graph
    if ('Arithmetic' in selected):
        graph_arithmatic(scale, 1, 5)
        # graphs arithmetic sequence,
        # calculations in Arithmetic function in calculation.py
        # graphing in graph_arithmatic function in graphing.py
    if ('Change' in selected):
        graph_change(scale)
        # graphs arithmetic sequence,
        # calculations in change function in calculation.py
        # graphing in graph_change graphing.py
    if ('Binary' in selected):
        graph_binary(scale)
        # graphs binary sequence,
        # calculations in Binary function in calculation.py
        # graphing in graph_binary graphing.py

        # similar for are other options below
        # calculations in (name) function in calculation.py
        # graphing in graph_(name) graphing.py
    if ('Cubes' in selected):
        graph_cubed(scale)
    if ('Squares' in selected):
        graph_squared(scale)
    if ('Evens' in selected):
        graph_evens(scale)
    if ('Odds' in selected):
        graph_odds(scale)
    if ('Integers' in selected):
        graph_Integers(scale)
    if ('Exponential' in selected):
        graph_exponentialdef(scale)
    if ('Fibonacci' in selected):
        graph_Fibonacci(scale)
    if ('Tribonacci' in selected):
        graph_Tribonacci(scale)
    if ('Hypotenuse' in selected):
        graph_Hypotenuse(scale)
    if ('Middle Triangle' in selected):
        graph_Middle(scale)
    if ('Shortest Triangle' in selected):
        graph_Shortest(scale)
    if ('Triangle Numbers' in selected):
        graph_TriangleNumbers(scale)
    if ('Palindromic' in selected):
        graph_Palindromic(scale)
    if ('Pi Digits' in selected):
        graph_pidigits(scale)
    if ('Pi Series' in selected):
        graph_piseries(scale)
    if ('Geometric' in selected):
        graph_Geometric(scale)
    if ('Primes' in selected):
        graph_Primes(scale)

    # shows the graph with all selected options

    showgraph()


# set app as name of new gui window
app = gui()
# background color
app.setBg("lightGreen")
# font size
# if text too large on your computer it is changeable
app.setFont(20)
# welcome button pop-up triggered if press
app.addButton("Welcome", Welcome)

# scale, for x axis length
app.addScale("")
# lets user see what scale value is currently on
app.showScaleValue("", show=True)
# min, max and default starting value of scale
app.setScaleRange("", 1, 100, curr=25)


# drop-down menu of graph options
app.startToggleFrame("Choices")
# using Choices dictionary creates check-mark boxes for all options,
# along with titles, all check-marks set to false at start
app.addProperties("Choices", Choices)

# commented out line below allows for
# auto changing/generating the graph
# every time user changes their options,
# without clicking button
# but I decide it was better to let user decide
# when to change their graph

# app.setPropertiesChangeFunction("Choices", changed)

# button to graph all options checked
app.addButton("Graph", changed)

# show help box with additional info about options
app.addButton("Help", helpb)

# closes the choices drop down check-box menu
app.stopToggleFrame()

# start the gui
app.go()
