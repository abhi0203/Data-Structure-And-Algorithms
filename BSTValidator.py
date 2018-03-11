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

	treeList.append(binTree.value)

	if binTree.rightChild:
		print_tree(binTree.rightChild, treeList)

	return treeList


#Create a Binary tree object.
# Code to create invalid binary tree 
'''
binTree= binary_tree()
treeList=[]
binTree= insert_treeData(binTree)
'''

'''
#This is the helper code to check if the tree is invalid.
#Here we create a wrong binary tree and then check if the code we wrote is caling this an invalid tree.
binTree= node(20)
binTree.leftChild= node(21)
binTree.rightChild= node(15)
treeList=[]
'''

treeList= print_tree(binTree, treeList)
#print(treeList)
if treeList==sorted(treeList):
	print("Binary Tree is Valid")
else:
	print("Binary Tree is Invalid")