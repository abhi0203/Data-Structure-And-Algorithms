'''
# This is the code written to convert an infix string into postfix.
# We use the stack data structure here. 
# Everytime a operand comes, we send it to output.
# Everytime an operator comes, we compare the priority of the operator on the stack with the one that has just arrived. 
# If the priority is more, we can push the operator. 
If the priority is less then we pop the operator from the stack and append it to the outcome.
# The reason we use stack is, depending on priority, we have to reverse the sequence in which the operator has arrived.
'''
# Author: Abhiram
# Date 04-April

class Stack:
	def __init__(self):
		self.items=[]

	def push(self, value):
		self.items.append(value)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def is_empty(self):
		return self.items==[]


def infix_to_postfix(equation):
	s= Stack()
	outcome= []
	priority={}
	priority["*"]= 3
	priority["/"]= 3
	priority["+"]= 2
	priority["-"]= 2
	priority["("]= 1

	for char in equation:
		if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			outcome.append(char)
		elif char=="(":
			s.push(char)
		elif char==")":
			c= s.pop()
			while c!= "(":
				outcome.append(c)
				c= s.pop()
		else:
			while not s.is_empty() and priority[s.peek()]>= priority[char]:
				c=s.pop()
				outcome.append(c)
			s.push(char)

	while not s.is_empty():
		c= s.pop()
		outcome.append(c)

	return " ".join(outcome)

'''
print(infix_to_postfix("A+B"))
print(infix_to_postfix("A+B*C"))
print(infix_to_postfix("A*B+C"))
print(infix_to_postfix("(A+B)*C"))
print(infix_to_postfix("(A+B)*C+(D*E)/F"))
'''
