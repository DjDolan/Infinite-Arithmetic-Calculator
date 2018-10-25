"""
This file is the main file where the final result will be handled.
"""

import getopt, sys
from ReadFile import *
from ReadExpressions import *

def main():

    numOfDigits = 2

    #create containers for expressions
    #must be using lists
    expressions = []            #list for expressions
    parsed_expressions = []     #list for parsed expressions

    read_file("pycode.txt", expressions)

    #loop through expressions list to be read
    for exp in expressions:
        read_expression(exp[::-1], parsed_expressions, numOfDigits, 0)

    #evaluate each expression
    for parsed_exp in parsed_expressions:
        print(parsed_exp)

    #END MAIN

#runs main program
if __name__ == "__main__":
    main()