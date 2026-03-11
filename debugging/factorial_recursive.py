#!/usr/bin/python3
import sys

'''
 * factorial - recursiev factorial function
 * @n: input
 * Return: factorial(n); 
'''
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)