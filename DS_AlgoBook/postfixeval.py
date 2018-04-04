'''
This is the code written to evaluate a postfix expression.
Here we again sue the stack data structure. 
However, instead of pushing the operator, we push the operand.
The reason we use stack is we keep parsing the operands till we enocunter an operator.
Once we enocunter the operator, we know for sure that it has to used on last 2 operands. So in this case stack becoms the choice
of data structure.
'''
# Author Abhiram:
# Date: 04-April


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


def postfix_eval(expression):
	s= Stack()
	for char in expression:
		if char in "0123456789":
			s.push(int(char))
		else:
			op2= s.pop()
			op1= s.pop()
			result= doOperation(char, op1, op2)
			s.push(result)

	return s.pop()

def doOperation(oper, op1, op2):
	if oper== "*":
		return op1* op2
	elif oper== "/":
		return op1/ op2
	elif oper== "+":
		return op1+op2
	else:
		return op1- op2


# Helper code
print(postfix_eval("12+3*45*6/+"))


