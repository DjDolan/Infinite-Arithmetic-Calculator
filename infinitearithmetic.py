"""
This file is the main file where the final result will be handled.
"""

import getopt, sys
from ReadFile import *
from ReadExpressions import *

def main():
    #create containers for expressions
    #must be using lists
    expressions = []            #list for expressions
    parsed_expressions = []     #list for parsed expressions

    read_file("pycode.txt", expressions)

    #loop through expressions list to be read
    for exp in expressions:
        read_expression(exp, parsed_expressions)

    #END MAIN

#runs main program
if __name__ == "__main__":
    main();