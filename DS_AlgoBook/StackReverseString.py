#This is the code to reverse a string.
# I am planning to use a stack. 
# Logic is, parse the string one character at a time and push it in the stack.
# The pop the stack and store it in another string.
# Return the final string
# Author: Abhiram
# Date: 27-March

class Stack:
	def __init__(self):
		self.items=[]

	def push(self, value):
		self.items.append(value)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def isempty(self):
		return self.items==[]

	def stackLength(self):
		return len(self.items)

def strReverse(testStr):
	s= Stack()
	revString=""
	for letter in testStr:
		s.push(letter)
	while not s.isempty():
		revString= revString+s.pop()

	return revString

print(strReverse("abhiram"))
