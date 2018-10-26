"""
This file will contain the necessary functions to perform operations
on the arithmetic expressions.
"""

from math import *

def add(op1, op2, res, nod, i):
	#takes element at 'i' and adds both from
	#each operand and multiplies by 10^(i * nod)
	#stores in results container and returns
	if (i == len(op2)-1):
		_sum = (op1[i] + op2[i]) * (10 ** (i * nod))
		res.append(_sum)
	else:
		_sum = (op1[i] + op2[i]) * (10 ** (i * nod))
		res.append(_sum)
		add(op1, op2, res, nod, i+1)

	return res

def multiply(op1, op2):
	return op1 * op2

