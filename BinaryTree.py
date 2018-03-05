import random
#Define a class Node. This acts as the standard node

class node:
	#Define and init fucntion and assign the value, leftChild and rightChild.
	def __init__(self,value):
		self.value=value
		self.leftChild= None
		self.rightChild= None


#Define another class that take care of all the node operations.

class binary_tree:
	#define and init function. we only initiate the root value. This is initiated to None. 
	# So when the tree object is newly created the root is defined to None.
	def __init__(self):
		self.root= None

	# Define a funtion to insert a value into the tree.
	#It will take value as input and will add that value to the node.

	def insert_value(self,value):
		# Check if the root node is none. If it is then allocate this value to root node.
		# If root node is not none, we need to check where to fit the value.
		# This will be done by using a recursive function which compares the value to value of current node and then based on the outcome
		# attaches the value to left or right.

		if self.root==None:
			self.root= node(value)
		else:
			self._insert_value(value,self.root)

		#In the above method, the reason we call the _insert_value function with self obeject is because, self object represents the entire tree. 
		# Since we want to insert the data in the tree, we call it using self. Also we send the value of root here which acts as current node.


	# Define another fnction to insert the value actually. This is kind of private function and hence it starts with underscore.
	def _insert_value(self, value, curr_node):
		# Here we compare the values in current Node and given value. 
		# If the value is less and current node has no child, then we attach the new value to the left of current node by creating a new node. 
		# Else, we call recursive function in which we send the value and currentNode's left child. 
		if value < curr_node.value:
			if curr_node.leftChild== None:
				curr_node.leftChild= node(value)
			else:
				self._insert_value(value,curr_node.leftChild)
		elif value > curr_node.value:
			if curr_node.rightChild == None:
				curr_node.rightChild = node(value)
			else:
				self._insert_value(value, curr_node.rightChild)
		else:
			print("This value already exists.")


	# Define a finction to print the values of the binary tree. This is done using Inorder traversale where Left--> Center --> Right. 
	# So the tree is again printed in the sorted order.

	def print_tree(self):
		# Check if the root node exists. If it does then recursively implement inorder way.
		if self.root != None:
			self._print_tree(self.root)

	# This is a type of private function for the Inorder traversal.
	# Here we first move to the leftmost node, then print it and then move to the right most node.
	def _print_tree(self, curr_node):
		# Get the current node  and keep moving to left if left exists.
		if curr_node.leftChild:
			self._print_tree(curr_node.leftChild)

		print(curr_node.value)

		if curr_node.rightChild:
			self._print_tree(curr_node.rightChild)


def insert_treeData(root):
	no_of_nodes=200
	max_int=2000
	for _ in range(no_of_nodes):
		num= random.randint(0,max_int)
		root.insert_value(num)


root_node= binary_tree()
insert_treeData(root_node)

root_node.print_tree()


