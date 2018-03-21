# This code is written to check if the given BST is AVL tree.
# A BST is considered as AVL tree if and only if the difference height of the left subtree and right subtree is 1.
# Also, the height of left and right subtree of any node should also be one.

# Adding 3 more variables ref to Parent, left height and right height. 
class node:
	def __init__(self, value=None):
		self.value= value
		self.leftChild= None
		self.rightChild= None
		self.parent= None
		self.leftChildHeight= 0
		self.rightChildHeight= 0

class binaryTree:
	def __init__(self):
		self.root= None

	def insert_data(self, value):
		if self.root== None:
			self.root= node(value)
		else:
			self._insert_data(self.root, value)

# Here the logic is while insertion itself, maintain the height of the node. So later on we can retrieve it.
	def _insert_data(self, current_node, value):
		if value< current_node.value:
			if current_node.leftChild==None:
				current_node.leftChildHeight+=1
				current_node.leftChild= node(value)
				current_node.leftChild.parent= current_node
				self._checkInsertionBalance(current_node.parent, current_node, current_node.leftChild)
			else:
				current_node.leftChildHeight+=1
				self._insert_data(current_node.leftChild, value)
		elif value> current_node.value:
			if current_node.rightChild== None:
				current_node.rightChildHeight+=1
				current_node.rightChild= node(value)
				current_node.rightChild.parent= current_node
				print("Inserting %s"% current_node.rightChild.value)
				self._checkInsertionBalance(current_node.parent, current_node, current_node.rightChild)
			else:
				current_node.rightChildHeight+=1
				self._insert_data(current_node.rightChild, value)
		else:
			print("Value already present")

	def print_tree(self):
		if self.root==None:
			print("Tree is empty")
		else:
			self._print_tree(self.root)

	def _print_tree(self, current_node):
		if current_node.leftChild:
			self._print_tree(current_node.leftChild)
		print(current_node.value)
		if current_node.rightChild:
			self._print_tree(current_node.rightChild)

	def print_postOrder_tree(self):
		if self.root==None:
			print("Tree is empty")
		else:
			self._print_postOrder_tree(self.root)

	def _print_postOrder_tree(self, current_node):
		if current_node.leftChild:
			self._print_postOrder_tree(current_node.leftChild)
		if current_node.rightChild:
			self._print_postOrder_tree(current_node.rightChild)
		print(current_node.value)


	def _checkInsertionBalance(self, parent_node, current_node, child_node):
		if parent_node==None:
			return
		if abs(parent_node.leftChildHeight-parent_node.rightChildHeight)>1:
			print("Parent Node %s" % parent_node.value)
			print("Current Node %s" % current_node.value)
			print("Child Node %s" % child_node.value)
			self._rebalance_tree(parent_node,current_node,child_node)
		#self._checkInsertionBalance(parent_node.parent, parent_node, current_node)

	def _rebalance_tree(self, parent_node, current_node, child_node):
		if parent_node.leftChild==current_node and current_node.leftChild==child_node:
			print("Needs right rotation")
			self._right_rotate(parent_node, current_node, child_node)
		elif parent_node.rightChild== current_node and current_node.rightChild== child_node:
			print("Need left rotation")
			self._left_rotate(parent_node, current_node, child_node)
		elif parent_node.leftChild== current_node and current_node.rightChild== child_node:
			print("Need Left --> Right rotation")
			self._left_rotate(parent_node, current_node, child_node)
			self._right_rotate(parent_node, current_node, child_node)
		elif parent_node.rightChild== current_node and current_node.leftChild== child_node:
			print("Need Right--> Left rotation")
			self._right_rotate(parent_node, current_node, child_node)
			self._left_rotate(parent_node, current_node, child_node)
		else:
			print("About to print exception")
			print(current_node.value)
			print(parent_node.value)
			print(child_node.value)
			raise Exception('_rebalance_node: z,y,x node configuration not recognized!')
	
	def _left_rotate(self, parent_node, current_node, child_node):
		parent_node.rightChildHeight-=1
		if parent_node.parent==None:
			self.root= current_node
		elif parent_node== parent_node.parent.leftChild:
			parent_node.parent.leftChild= current_node
		elif parent_node== parent_node.parent.rightChild:
			parent_node.parent.rightChild= current_node
		current_node.parent= parent_node.parent
		parent_node.parent= current_node
		parent_node.rightChild= current_node.leftChild
		current_node.leftChild= parent_node


	def _right_rotate(self, parent_node, current_node, child_node):
		parent_node.leftChildHeight-=1
		if parent_node.parent== None:
			self.root= current_node
		elif parent_node== parent_node.parent.leftChild:
			parent_node.parent.leftChild= current_node
		elif parent_node== parent_node.parent.rightChild:
			parent_node.parent.rightChild= current_node
		current_node.parent= parent_node.parent
		parent_node.parent= current_node
		parent_node.leftChild= current_node.rightChild
		current_node.rightChild= parent_node

	def tree_height(self):
		if self.root== None:
			return 0
		else:
			return self._tree_height(self.root, 0)



tree= binaryTree()
tree.insert_data(10)
tree.insert_data(11)
tree.insert_data(9)
tree.insert_data(8)
tree.insert_data(7)
print("In Order Traversal")
tree.print_tree()
print("Post Order traversal")
tree.print_postOrder_tree()

