"""
This file will contain the necessary functions to perform operations
on the arithmetic expressions.
"""

from math import *

#this function will take each element, find its place value, and add them
def add(op1, op2, res, nod, i):
	#takes element at 'i' and adds both from
	#each operand and multiplies by 10^(i * nod)
	#stores in results container and returns
	if i == len(op2)-1:
		_sum = (op1[i] + op2[i]) * (10 ** (i * nod))
		res.append(_sum)
	else:
		_sum = (op1[i] + op2[i]) * (10 ** (i * nod))
		res.append(_sum)
		add(op1, op2, res, nod, i+1)

	return res	

#this function will take each element, find its place value, and multiply them
#to the elements found in the second list
def multiply(op1, op2, res, nod, i, j):
	#variables for easier calculations
	i_place_value = 10 ** (i * nod)
	j_place_value = 10 ** (j * nod)

	#'i' is the first operand iterator
	if i == len(op1)-1:	
		_prod = (op1[i] * i_place_value) * (op2[j] * j_place_value)
		res.append(_prod)

	else:
		_prod = (op1[i] * i_place_value) * (op2[j] * j_place_value)
		res.append(_prod)
		multiply(op1, op2, res, nod, i+1, j)
