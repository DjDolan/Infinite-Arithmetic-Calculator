"""
This file will contain the necessary functions to evaluate the 
mathematical expressions written in the text files specified.
"""
# from ReadExpressions import *

# #this function will divide it into the left operand
# def left_operand(parsed_exp, left_exp):
# 	#base case
# 	#if its an operator return parse and exit loop
# 	if(is_operator(parsed_exp[0])):
# 		return left_exp
# 	else:
# 		left_exp.append(parsed_exp[0])
# 		parsed_exp.pop(0)
# 		left_operand(parsed_exp, left_exp)

# #this function will divide it into the right operand
# def right_operand(parsed_exp, right_exp):
# 	#base case
# 	#if it reaches the end of the list then append
# 	#the character to expression and exit loop
# 	if(len(parsed_exp) == 0):
# 		return right_exp
# 	else:
# 		right_exp.append(parsed_exp[0])
# 		parsed_exp.pop(0)
# 		right_operand(parsed_exp, right_exp)

# #This function will split the expression to left, right, and operator
# def split_expression(parsed_exp):
# 	#divide the expression into left, right, and op
	
# 	#temporary containers
# 	left_expression = []
# 	right_expression = []
# 	op = '!'

# 	#left expression
# 	left_operand(parsed_exp, left_expression)
	
# 	#operator
# 	op = parsed_exp[0]
# 	parsed_exp.pop(0)

# 	#right expression
# 	right_operand(parsed_exp, right_expression)

def split_expression(parsed_exp):

	operators = ['+', '-', '*', '/']

	set1 = set(parsed_exp)
	set2 = set(operators)

	if (set1 & set2):
		op_list = list(set1.intersection(set2))
		op = op_list[0]
	else:
		print("</Error>")

	print(smaller)
