"""
This file is the main file where the final result will be handled.
"""

import argparse
from ReadFile import *
from ReadExpressions import *
from EvaluateExpressions import *

parser = argparse.ArgumentParser(description='Evaluate the arithmetic expressions.')
parser.add_argument('-i', '--input', type=str, help='Input file')
parser.add_argument('-dPN', '--digitsPerNode', type=int, help='Number of digits to divide by')
args = parser.parse_args()

def main():
    #enter input file and number of digits on command line
    input_file = args.input
    num_of_digits = args.digitsPerNode

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
    
    #print out the results
    for x in range(len(expressions)):
        print(expressions[x], '=', results[x], sep='')

    #END MAIN

#runs main program
if __name__ == "__main__":
    main()
