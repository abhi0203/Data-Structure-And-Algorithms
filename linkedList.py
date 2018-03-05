import random

names=['Abhiram','Sara','Neha','Alka','Vikram','Leena','Uma','Om','Shweta','Rohit','Tanmay','Soham']
count=100
class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None


class linkedList:
	def __init__(self):
		self.head=node()

	def addData(self,data):
		newNode= node(data)
		current=self.head
		while current.next!=None:
			current=current.next
		current.next=newNode

	def listLength(self):
		current=self.head
		length=0
		while current.next!=None:
			length+=1
			current=current.next
		return length

	def listDisplay(self):
		listElement=[]
		current=self.head
		while current.next!=None:
			current=current.next
			listElement.append(current.data)
		return listElement

	def removeData(self,index):
		if index>self.listLength():
			print("Error in the Index. So I cannot delete")
			return None
		currentIndex=0
		currentNode=self.head
		last_node=currentNode
		while True:
			currentIndex+=1
			currentNode=currentNode.next
			if currentIndex==index:
				last_node.next=currentNode.next
				currentNode.next=None
				return True
			else:
				last_node=currentNode



a = linkedList()
for i in range(count):
	a.addData(random.choice(names))

print(a.listLength())
print(a.listDisplay())

a.removeData(6)
print(a.listDisplay())
