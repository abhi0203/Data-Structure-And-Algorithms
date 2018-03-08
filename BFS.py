from BinaryTree import binary_tree
from BinaryTree import insert_treeData
import queue

# This is the function where we do BFS.

def breadth_first_search(binTree):
	# Create an queue object from Queue module we have imported.
	bfs_queue= queue.Queue()
	if binTree.root== None:
		print("Tree is empty")
	else:
		bfs_queue.put(binTree.root)
		_breadth_first_search(bfs_queue)

def _breadth_first_search(bfs_queue):
	node=bfs_queue.get()
	print(node.value)
	if node.leftChild:
		bfs_queue.put(node.leftChild)
	if node.rightChild:
		bfs_queue.put(node.rightChild)
	if not bfs_queue.empty():
		_breadth_first_search(bfs_queue)
	else:
		return


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
breadth_first_search(binTree)



