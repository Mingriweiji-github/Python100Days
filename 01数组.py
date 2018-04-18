#!/usr/bin/python
#array = [1,2,3,4,5,6]
#small = []
#
#for n in array:
#	if n < 4:
#		small.append(n * 2)
#
#print(small)

arr = [1,2,3,4,5,6]
small = [n * 2 for n in arr if n < 4]

signs = ['+','-']
numbers = [1,2]

ascis = ['{sign}{number}'.format(sign = sign, number = number)for sign in signs for number in numbers]
		
