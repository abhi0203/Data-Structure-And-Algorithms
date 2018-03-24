import time
from random import randrange

def findMinON2(lst):
	minNum= lst[0]
	for i in lst:
		isMinValue= True
		for j in lst:
			if i>j:
				isMinValue= False
		if isMinValue:
			minNum= i
	return minNum

def findMinOn(lst):
	minNum= lst[0]
	for data in lst:
		if minNum > data:
			minNum= data
	return minNum


print(findMinOn([21,121,221,324,54,65,6,76,3,21,234,54,4556,56,676,3,2,323,21331]))
print(findMinON2([21,121,221,324,54,65,6,76,3,21,234,54,4556,56,676,3,2,323,21331]))

print("Order of n^2")
for i in range(1000, 11000, 1000):
	lst=[randrange(100000) for j in range(i)]
	start= time.time()
	print(findMinON2(lst))
	end = time.time()
	print("List Length %d ProcessingTime %f" % (len(lst), end-start))

print("Order of n")
for i in range(1000, 11000, 1000):
	lst=[randrange(100000) for j in range(i)]
	start= time.time()
	print(findMinOn(lst))
	end = time.time()
	print("List Length %d ProcessingTime %f" % (len(lst), end-start))

