# This experiment is done in order to compare the time complexity of delete operation for List and Dictonary.
# We will perform del operation on various sizes of the lists and dictonaries.
# Author: Abhiram
# Date: 25-March

import random
import timeit

t1= timeit.Timer("del lst[j]","from __main__ import lst,j")
t2= timeit.Timer("del d[k]", "from __main__ import d,k")



for i in range(100000, 1000001, 100000):
	lst= list(range(i))
	j= random.randint(0,i-1)
	del_list= t1.timeit(number=1000)
	print("%d items in list took %f ms" % (i,del_list))

	d={l: None for l in range(i)}
	k= random.randint(0,i-1)
	del_dict= t2.timeit(number=1000)
	print("%d items in Dictonary took %f ms" %(i, del_dict))


# Ideally the del function on list should be O(n) and that on dict object should be O(1)
# The code is throwing the Key error. 
