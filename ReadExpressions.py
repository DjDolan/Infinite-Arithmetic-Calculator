"""
This file will contain the necessary functions for parsing the expressions.
"""

#function to check if character is an operator
def is_operator(c):
    if(c == '+' or c == '-' or c == '*' or c == '/'): return True
    else: return False

#parses the line for pushing to expressions list
def parse(exp, parsed_line, tmp_str, nod, i):
    
    #base case
    if(i == len(exp)-1):
        tmp_str += exp[i]
        parsed_line.append(tmp_str)

    #if operator then append temporary string
    #and append operator to parsed line
    elif(is_operator(exp[i])):
        parsed_line.append(tmp_str)
        parsed_line.append(exp[i])
        tmp_str = ""
        parse(exp, parsed_line, tmp_str, nod, i+1)

    # elif(len(tmp_str) == nod):
    #     parsed_line.append(tmp_str)
    #     tmp_str = ""
    #     parse(exp, parsed_line, tmp_str, nod, i+1)

    #else append any number and keep iterating
    #through the expression 
    else:
        tmp_str += exp[i]
        parse(exp, parsed_line, tmp_str, nod, i+1)

    return parsed_line

#reads the expression from main file and parses it
def read_expression(exp, parsed_list, nod, i):
    
    parsed_line = []
    temp_string = ""

    parsed_list.append(parse(exp, parsed_line, temp_string, nod, 0))





