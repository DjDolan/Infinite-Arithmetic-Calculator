"""
This file will contain the necessary functions to evaluate the 
mathematical expressions written in the text files specified.
"""

from ReadExpressions import *
from Operations import *

#this function makes the operands the same length by appending zeroes
def make_lists_same_length(op1, op2, i):
	#if they are not the same then keep appending '0'
	if i == len(op1): 
		return
	else:
		op2.append(0)
		make_lists_same_length(op1, op2, i+1)

#this function will divide it into the left operand
def left_operand(parsed_exp, left_exp):
	#base case
	#if its an operator return parse and exit loop
	if(is_operator(parsed_exp[0])):
		return left_exp
	else:
		left_exp.append(parsed_exp[0])
		parsed_exp.pop(0)
		left_operand(parsed_exp, left_exp)

#this function will divide it into the right operand
def right_operand(parsed_exp, right_exp):
	#base case
	#if it reaches the end of the list then append
	#the character to expression and exit loop
	if(len(parsed_exp) == 0):
		return right_exp
	else:
		right_exp.append(parsed_exp[0])
		parsed_exp.pop(0)
		right_operand(parsed_exp, right_exp)

#this function evaluates the expression by the operation
def evaluate(left, right, nod, op, results):
	#temporary containers
	res = []

	#find the shorter expression to evaluate properly
	#reverse the list for proper evaluation
	#map the lists to integers for evaluation
	if len(left) < len(right):
		operand1 = list(map(int, right[::-1]))
		operand2 = list(map(int, left[::-1]))
	else:
		operand1 = list(map(int, left[::-1]))
		operand2 = list(map(int, right[::-1]))

	#pass to make_list_same_length function
	make_lists_same_length(operand1, operand2, len(operand2))

	#operate on the operands with Operations.py
	if op == '+':
		#if operator is add then call the add function
		add(operand1, operand2, res, nod, 0)
		results.append(res)
	elif op == '*':
		#if operator is multiply call the multiply function
		print("Multiplying")

#This function will split the expression to left, right, and operator
def split_expression(parsed_exp, results, num_of_digits):
	#temporary containers
	left_expression = []
	right_expression = []
	op = '!'

	#left expression
	left_operand(parsed_exp, left_expression)
	
	#operator
	op = parsed_exp[0] #get operator
	parsed_exp.pop(0) #pop it from the expression

	#right expression
	right_operand(parsed_exp, right_expression)

	#pass to evaluation
	evaluate(left_expression, right_expression, num_of_digits, op, results)


