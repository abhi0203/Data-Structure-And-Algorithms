# Below experiement is to understand the time complexity of the dict get and set operation.
# We run this experiment for varying size of items in a dictonary and check if there is impact on the timing of the dictonary.
# Author: Abhiram 
# Date 25-March
import random
import timeit

t1= timeit.Timer("d[k]","from __main__ import d,k")
t2= timeit.Timer("d[l]=1", "from __main__ import d,l")




for i in range(100000, 1000001, 100000):
	d={j:None for j in range(i)}
	k= random.randint(0, i-1)
	getTime= t1.timeit(number= 1000)
	print("%d items get in %f ms" % (i, getTime))

	l= random.randint(0, i-1)
	setTime= t2.timeit(number=1000)
	print("%d items set in %f ms" % (i, setTime))


# From the above experiment, we can conclude that even though the size of the dictonary increases,
# the time to get and set the dictobary remains more or less the same. Hence the time complexity is 
# of O(1)