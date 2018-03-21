# This code is written to check if the given BST is AVL tree.
# A BST is considered as AVL tree if and only if the difference height of the left subtree and right subtree is 1.
# Also, the height of left and right subtree of any node should also be one.


class node:
	def __init__(self, value=None):
		self.value= value
		self.leftChild= None
		self.rightChild= None
		self.parent= None

class binaryTree:
	def __init__(self):
		self.root= None

	def insert_data(self, value):
		if self.root== None:
			self.root= node(value)
		else:
			self._insert_data(self.root, value)

	def _insert_data(self, current_node, value):
		if value< current_node.value:
			if current_node.leftChild==None:
				current_node.leftChild= node(value)
			else:
				self._insert_data(current_node.leftChild, value)
		elif value> current_node.value:
			if current_node.rightChild== None:
				current_node.rightChild= node(value)
			else:
				self._insert_data(current_node.rightChild, value)
		else:
			print("Value already present")

	def tree_height(self):
		if self.root== None:
			return 0
		else:
			return self._tree_height(self.root, 0)

	def _tree_height(self, current_node, current_height):
		if current_node==None:
			return current_height
		leftChildHeight= self._tree_height(current_node.leftChild, current_height+1)
		rightChildHeight= self._tree_height(current_node.rightChild, current_height+1)
		if abs(leftChildHeight- rightChildHeight)>1:
			print("This is not AVL tree")
		return max(leftChildHeight, rightChildHeight)


tree= binaryTree()
tree.insert_data(10)
tree.insert_data(8)
tree.insert_data(9)
tree.insert_data(7)
tree.insert_data(12)
tree.insert_data(11)
tree.insert_data(13)
print(tree.tree_height())
