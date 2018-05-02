import timeit

def test1():
	l=[]
	for i in range(1000):
		l=l+[i]

def test2():
	l=[]
	for i in range(1000):
		l.append(i)

def test3():
	l=[i for i in range(1000)]

def test4():
	l=[range(1000)]


t1= timeit.Timer("test1()", "from __main__ import test1")
print("Concat ", t1.timeit(number=1000), "ms")
t2= timeit.Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "ms" )
t3= timeit.Timer("test3()", "from __main__ import test3")
print("Comprehension ", t3.timeit(number=1000), "ms")
t4= timeit.Timer("test4()", "from __main__ import test4")
print("List ", t4.timeit(number=1000), "ms")