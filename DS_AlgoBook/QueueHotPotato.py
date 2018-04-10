# This is the problem to represent a queue.
# Here we simulate passing a potato amoing kids and whoever has the potato looses.
# This is done using a queue since the potato traverse instriaght order. 
# Here the queue is simulated as circular queue. 

import random

class Queue:
	def __init__(self):
		self.items=[]

	def enqueue(self, value):
		self.items.insert(0, value)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items==[]


def hotPotato(names):
	q= Queue()
	for name in names:
		q.enqueue(name)

	while q.size()> 1:
		num= random.randint(5,15)
		for _ in range(num):
			q.enqueue(q.dequeue())
		q.dequeue()

	return q.dequeue()


print(hotPotato(['Abhiram', 'Neha', 'Sara', 'Alka','Sudhir']))



