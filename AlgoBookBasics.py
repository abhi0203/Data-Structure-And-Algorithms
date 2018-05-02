def findMinOn(lst):
	if not lst:
		return None
	else:
		min=lst[0]
		for data in range(1, len(lst)):
			if min> lst[data]:
				min = lst[data]
			else:
				continue
		return min

def findMinOn2(lst):
	if not list:
		return None
	else:
		min=0
		for i in range(0, len(lst)):
			for j in range(0, len(lst)):
				if lst[i]< lst[j]:
					min= lst[i]
				else:
					min=lst[j]
		return min

print(findMinOn([1,122,21,43,34,23,54,23,23,54,221,546,676,21]))
print(findMinOn2([1,122,21,43,34,23,54,23,23,54,221,546,676,21]))