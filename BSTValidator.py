'''
This is the code I am writing to validate Binary tree.
The logic I ma using is I am planning to print the given tree using inorder traversal. 
If the list is in sorted order, then we say that BST is valid. Else it is invalid.
There can be other ways to do this but I am using this technique.
@ Author : Abhiram
@ Date: 11-March
'''

#importing built in modules.


#importing custom module.
from BinaryTree import binary_tree
from BinaryTree import insert_treeData
from BinaryTree import node

# Override the print tree method to return a list.
def print_tree(binTree,treeList):
	if binTree.leftChild:
		print_tree(binTree.leftChild,treeList)

	# Check here only if the value we are appending to the list is greater than the last value in the list. 
	# If it is, then please add the value. 
	if treeList and treeList[-1]> binTree.value:
		return treeList, False

	treeList.append(binTree.value)

	if binTree.rightChild:
		print_tree(binTree.rightChild, treeList)

	return treeList, True


# This is one way to do the validation.
# Traverse the tree in inorder fashion and save it in th elist and once we traverse, sort the tree. 
# If original list and sorted list are the same, tree i valid. Else it is invalid.
def inorder_traversal_type():
	#Create a Binary tree object.
	# Code to create invalid binary tree 
	'''
	binTree= binary_tree()
	treeList=[]
	binTree= insert_treeData(binTree)
	'''
	
	
	#This is the helper code to check if the tree is invalid.
	#Here we create a wrong binary tree and then check if the code we wrote is caling this an invalid tree.
'''	binTree= node(20)
	binTree.leftChild= node(15)
	binTree.rightChild= node(21)
	treeList=[]'''
	
	treeList, Flag= print_tree(binTree, treeList)
	if Flag:
		print("Tree is Valid")
	else:
		print("Tree is invalid")

# In this way we find the max value from left subtree and minimum value from right subtree. 
# If the max value is less than center and min value is greater then center, we have a valid tree. Else invalid.
'''def min_max_Type():
	pass
if __name__=='main':
	inOrderTraversalType()'''
inorder_traversal_type()