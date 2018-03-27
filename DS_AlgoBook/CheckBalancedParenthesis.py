# This is the code written to check if the string of parenthesis is balanced or not.
# We are using stack to check that. For a opening brace we push on the stack and for closing one we pop.
# If stack is empty while popping then we return False or if the stack has values at the end of string, then also we retrun False.
# Otherwise we return True if the stack is empty and string is finished.
# Author: Abhirams
# Date: 27-March

from StackReverseString import Stack


def isBalancedParen(brace_string):
	s= Stack()
	for char in brace_string:
		if char=="(":
			s.push(char)
		else:
			if char==")" and s.isempty():
				return False
			else:
				s.pop()

	# Check if the stack is empty at the end of character string.
	if s.isempty():
		return True
	else:
		return False

'''
print(isBalancedParen("()()()"))
print(isBalancedParen("(()()(()))"))
print(isBalancedParen("((()"))
print(isBalancedParen("())()()"))
print(isBalancedParen("()"))
print(isBalancedParen(")("))'''