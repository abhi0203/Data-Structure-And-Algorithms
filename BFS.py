# Author @Abhiram Pattarkine @abhtae

# Importing build in modules
import queue
#Importing the methods from BinaryTree module.
from BinaryTree import binary_tree
from BinaryTree import insert_treeData


# This is the function where we do BFS.

def breadth_first_search(binTree):
	# Create an queue object from Queue module we have imported.
	bfs_queue= queue.Queue()
	#Check if the tree is empty. 
	# If it is empty print tree is empty and return.
	# else put the root node of the tree in the queue and call the recursive function for BFS.
	if binTree.root== None:
		print("Tree is empty")
	else:
		bfs_queue.put(binTree.root)
		_breadth_first_search(bfs_queue)

# Recursive function for BFS.
def _breadth_first_search(bfs_queue):
	# Get the first node in the queue and then print its value.
	node=bfs_queue.get()
	print(node.value)
	# Check if the node we retrieved from the queue has any children. If it has then push them in the queue.
	if node.leftChild:
		bfs_queue.put(node.leftChild)
	if node.rightChild:
		bfs_queue.put(node.rightChild)
	# Now if the queue is not empty, then recursively call BFS method so that we can keep adding and printing new nodes. 
	# Else queue is empty, that means we have traversed the entire tree. So simply return.
	if not bfs_queue.empty():
		_breadth_first_search(bfs_queue)
	else:
		return



'''
#Commenting the helper code so that this method can be imported as module if required.
binTree = binary_tree()
#binTree=insert_treeData(binTree)
#binTree.print_tree()
binTree.insert_value(50)
binTree.insert_value(17)
binTree.insert_value(76)
binTree.insert_value(9)
binTree.insert_value(23)
binTree.insert_value(54)
binTree.insert_value(14)
binTree.insert_value(19)
binTree.insert_value(72)
binTree.insert_value(12)
binTree.insert_value(67)
binTree.insert_value(99)
print("result of inorder traversal")
binTree.print_tree()
print("result after BFS")
breadth_first_search(binTree)'''