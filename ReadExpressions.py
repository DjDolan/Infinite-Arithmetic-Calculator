"""
This file will contain the necessary functions for parsing the expressions.
"""

#parser for separating expressions
def parser(exp, parse_list, tmp_str, i):
    #base case
    #the iterator reaches the end of the expressions list
    if(i == len(exp)):
        print(exp[i])
    else:
        print(exp[i])
        parser(exp, parse_list, tmp_str, i+1)

#reads the expression from main file
def read_expression(exp, parse_list, i):
    iterator = 0 #iterator variable for recursive looping
    temp_string = "" #temporary string for evaluation

    # base case
    # the iterator reaches the end of the expressions list
    if (i == len(exp)):
        print(exp[i])
    else:
        print(exp[i])
        parser(exp, parse_list, tmp_str, i + 1)