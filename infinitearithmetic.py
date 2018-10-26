"""
This file is the main file where the final result will be handled.
"""

import getopt, sys
from ReadFile import *
from ReadExpressions import *
from EvaluateExpressions import *

def main():
    #enter input file and number of digits on command line
    input_file = "pycode.txt"
    num_of_digits = 2

    #create containers for expressions
    #must be using lists
    expressions = []            #list for expressions
    parsed_expressions = []     #list for parsed expressions
    results = []                #list for expression results

    #read the input file and append to expressions list
    read_file(input_file, expressions)

    #loop through expressions list to be read
    for exp in expressions:
        read_expression(exp[::-1], parsed_expressions, num_of_digits, 0)

    #evaluate each expression
    for parsed_exp in parsed_expressions:
        split_expression(parsed_exp, results, num_of_digits)
    
    for i in range(len(expressions)):
        print(expressions[i], '=', sum(results[i]), sep='')

    #END MAIN

#runs main program
if __name__ == "__main__":
    main()
