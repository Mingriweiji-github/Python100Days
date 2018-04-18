#!/usr/bin/python

class Book:
	def __init__(self):
		self.chapter = [1,2,3]
		
	def __getitem__(self,n):
		return self.chapter[n]
		
b = Book()
#print(b[4])
for c in b:
	print(c)