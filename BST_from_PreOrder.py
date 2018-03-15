#This utility is written to construct a Binary tree from Pre Order Traversal. Center --> Left --> Right
# @Author: Abhiram
# Date: 13-March

# I realized that this is same as inserting the normal data in the tree. 
# It will be interesting to see how we only construct Binary Tree from Pre order traversal and other traversal.
class node:
	def __init__(self, value=None):
		self.value= value
		self.leftChild= None
		self.rightChild= None
		self.parent= None

class binary_tree:
	
	def __init__(self):
		self.root= None

	def insert_data(self, value):
		if self.root== None:
			self.root= node(value)
		else:
			self._insert_data(self.root, value)

	def _insert_data(self, current_node, value):
		if current_node.value> value:
			if current_node.leftChild== None:
				current_node.leftChild= node(value)
			else:
				self._insert_data(current_node.leftChild, value)
		elif current_node.value< value:
			if current_node.rightChild== None:
				current_node.rightChild= node(value)
			else:
				self._insert_data(current_node.rightChild, value)
		else:
			print("Node already in tree")

	def print_preorder(self):
		if self.root== None:
			print("Nothing to print")
		else:
			self._print_preorder(self.root)

	def _print_preorder(self, current_node):
		print(current_node.value)

		if current_node.leftChild:
			self._print_preorder(current_node.leftChild)

		if current_node.rightChild:
			self._print_preorder(current_node.rightChild)


	def print_inorder(self):
		if self.root== None:
			print("Empty Tree")
		else:
			self._print_inorder(self.root)

	def _print_inorder(self, current_node):
		if current_node.leftChild:
			self._print_inorder(current_node.leftChild)

		print(current_node.value)

		if current_node.rightChild:
			self._print_inorder(current_node.rightChild)


bintree= binary_tree()
'''bintree.insert_data(23)
bintree.insert_data(5)
bintree.insert_data(2)
bintree.insert_data(54)
bintree.insert_data(40)
bintree.insert_data(21)
bintree.insert_data(27)
bintree.insert_data(13)
bintree.insert_data(7)'''

bintree.insert_data(23)
bintree.insert_data(5)
bintree.insert_data(2)
bintree.insert_data(21)
bintree.insert_data(13)
bintree.insert_data(7)
bintree.insert_data(54)
bintree.insert_data(40)
bintree.insert_data(27)


print("Printing Pre Order")
bintree.print_preorder()
print("Printing In Order")
bintree.print_inorder()


