# Below Code is to assess the time complexity of the list index access. 
# This is to check if the time complexity is of O(1)
# @ Author: Abhiram
# Date: 25-March

import timeit
import random

t1= timeit.Timer("lst[j]", "from __main__ import lst, j")

for i in range(100000, 2000001, 100000):
	lst= list(range(i))
	j= random.randint(0,i-1)
	acc_time= t1.timeit(number=1000)
	print("%d Size % f ms" % (i, acc_time))

