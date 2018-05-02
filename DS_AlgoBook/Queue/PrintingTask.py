'''
This code is written in order to simulate if the given rate of the printer is optimal or not.
Here, we assume certain inputs like printer's printting rate, input tasks, no. of docs per rtask etc. along with no. of students and print commands they give.
It is also assumed that the lenght of the class is approximately 1 hour. So any printing task goes beyond an hour will not be acceptable.
'''
# Author: Abhiram
# Date: 02-May


import random
import time

'''
We create a class printer that represents a printer.
This class will have methods like isBusy, startTask, continueWork.
This class will have variables like, printRate, currentTask, timeLeft
'''
class Printer:
	def __init__(self, printRate):
		self.printRate= printRate
		self.currentTask= None
		self.timeLeft= 0

	def isBusy(self):
		if self.currentTask!=None:
			return True
		return False

	def startTask(self, nextTask):
		self.currentTask= nextTask
		self.timeLeft= nextTask.getPages()* 60/ self.printRate

	def continueWork(self):
		if self.currentTask!=None:
			self.timeLeft-=1
			if self.timeLeft<=0:
				self.currentTask= None

'''
We now create a class for a task object. 
This class will have variables like no_of_pages, queueTime (represents moment it was created an queuesd)
This class will have methods like getPages(), getWaitTime()
'''

class Task:
	def __init__(self, queueTime):
		self.no_of_Pages= random.randrange(1,21)
		self.queueTime= queueTime

	def getPages(self):
		return self.no_of_Pages

	def getQueueTime(self):
		return self.queueTime

	def getWaitTime(self, currentTime):
		return currentTime- self.queueTime

'''
Queue Class
'''

class Queue:
	def __init__(self):
		self.items=[]

	def enqueue(self, value):
		self.items.append(value)

	def dequeue(self):
		return self.items.pop(0)

	def isQueueEmpty(self):
		return self.items==[]

	def queueLength(self):
		return len(self.items)



def newPrintTask():
	if random.randrange(1,181)==180:
		return True
	return False


'''
This is the main method where we bring togather all the classes we created above.
Here we first create a task. Then we add it to queue.
We check if the printer is available and queue has data and then start the printing task.
Then we keep on decrementing the counter for printer so that we can say when the task is completed.
At the end, we print the average wait time for the printer.
'''


def simulatePrinting(classDuration, printRate):
	printer1= Printer(printRate)
	printerQueue= Queue()
	waitTime= []
	for currentTime in range(classDuration):
		if newPrintTask():
			task= Task(currentTime)
			printerQueue.enqueue(task)

		if (not printer1.isBusy()) and (not printerQueue.isQueueEmpty()):
			newTask= printerQueue.dequeue()
			waitTime.append(newTask.getWaitTime(currentTime))
			printer1.startTask(newTask)

		printer1.continueWork()
	print("Average Waiting time is %f sec and No. of tasks in Queue is %d"%(sum(waitTime)/len(waitTime), printerQueue.queueLength()))





for i in range(10):
	simulatePrinting(3600,1800)