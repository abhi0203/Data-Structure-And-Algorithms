# This code is written to find kth smallest element in the list in O(nlogn)
# Logic is we sort the list using list sort function and return the kth element.
# List sort fucntion is of complexity O(nlog n) and Index return is O(1)
# This code will only work if there are no duplicate elements in the list. If there are duplicate elements, then this code will not work
# Author: Abhiram
# Date 25-March

import random
import timeit

t1= timeit.Timer("test1", "from __main__ import test1, lst, j")
def test1():
	lst.sort()
	return lst[j]

for i in range(100000, 1000001, 100000):
	lst= [random.randint(0,i-1) for j in range(i)]
	j= random.randint(0,i-1)
	get_time= t1.timeit(number= 1000)
	print("%d items %s ms"% (i, get_time))





