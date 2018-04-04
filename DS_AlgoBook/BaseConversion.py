# This code is written to convert a given decimal number to specific base. It uses Stack as data strucutre to store the number.
# The method takes 2 arguments the number to be converted and the base to which this needs to be converted.
# Author: Abhiram
# Date: 01-April

class Stack:
	def __init__(self):
		self.items=[]

	def push(self, value):
		self.items.append(value)

	def pop(self):
		return self.items.pop()

	def isempty(self):
		return self.items ==[]

	def stackLength(self):
		return len(self.items)


def baseConversion(num, base):
	s= Stack()
	base_num=""
	if num==0:
		return num
	while num>0:
		value= num%base
		s.push(value)
		num= num//base
	while not s.isempty():
		base_num= base_num+str(s.pop())

	return base_num

# Helper code

#print(baseConversion(125,2))


