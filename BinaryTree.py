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

	#Function to define the height of the tree.
	# Here we traverse from root node with a count of the level. 
	# Then we each travel to left and right node counting the number of levels in recursive manner. 
	# Once we reach the None value for a node, we return the call.

	def find_height(self):
		if self.root!= None:
			return self._find_height(self.root, 0)

	# this is the recursive function. This is where we find the height.
	# This function takes 2 arguments. 1) Current Node 2) Current height
	def _find_height(self, current_node, current_height):
		# First we check if the root node is empty. If it is just return the current value i.e 0
		if current_node==None:
			return current_height
		
		# If the root is not none, that means there is atleast one element in the tree. 
		# So the logic we implement is, for each node, we calculate the height for it left and right tree and then add it to the one in the overall tree. 
		# Here we move to left till we find none.
		left_height= self._find_height(current_node.leftChild,current_height+1)

		# Same thing we do for the right nodes. So for rach node, we get the height for the right node as well. 
		# That way we cover all the nodes.

		right_height= self._find_height(current_node.rightChild,current_height+1)

		#Once we find the height of both the nodes, we just find the max and return it.
		# So we go to deepest node and find the height. At one point, we reach the root node, and return the height of its left or right child.

		return max(left_height, right_height)

	# This is the dunction to search if a value exists in the binary tree. 
	# Here we will define the private function as well.
	def find_element(self, value):
		# First we check if the tree is empty by checking root node. If it is not, then we call private function.
		# When we call the provate function then we send current node and the value to be searched to the private function.
		if self.root== None:
			print("Tree is empty.")
		else:
			return self._find_element(self.root, value)

	def _find_element(self, current_node, value):
		# Check if the value equal to value of current node. If it is then return true. If it is less than current, then traverse to left. 
		# If it is greater, traverse right. If at any point we encounter None in the child node, return false.

		if current_node.value == value:
			return True
		elif value < current_node.value and current_node.leftChild:
			return self._find_element(current_node.leftChild, value)
		elif value > current_node.value and current_node.rightChild:
			return self._find_element(current_node.rightChild, value)
		return False


def insert_treeData(root):
	no_of_nodes=2000
	max_int=20000
	for _ in range(no_of_nodes):
		num= random.randint(0,max_int)
		root.insert_value(num)
	return root


root_node= binary_tree()
root_node= insert_treeData(root_node)
'''root_node.insert_value(5)
root_node.insert_value(4)
root_node.insert_value(6)'''

root_node.print_tree()

print(root_node.find_height())

print(root_node.find_element(2121))
print(root_node.find_element(21))
print(root_node.find_element(232))
print(root_node.find_element(12323))
print(root_node.find_element(3434))
print(root_node.find_element(1122))
print(root_node.find_element(2233))
print(root_node.find_element(6545))
print(root_node.find_element(2121))
print(root_node.find_element(5467))
print(root_node.find_element(11232))
print(root_node.find_element(7657))
print(root_node.find_element(789))
print(root_node.find_element(987))
print(root_node.find_element(54))
print(root_node.find_element(87))




