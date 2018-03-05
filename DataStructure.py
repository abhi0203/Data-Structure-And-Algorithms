import random

names=['Abhiram','Neha','Sara','Alka','Vikram','Leena','Virag','Om','Uma','Sarang']
loopCount=500000

def data_creation():
	f=open('data.txt','w')
	for i in range(loopCount):
		current=random.choice(names)
		f.write(current+'\n')
	f.close()

def data_read_list():
	listCount=[]
	for data in names:
		listCount.append(0)
	with open('data.txt','r') as f:
		for line in f:
			line=line.strip()
			if line!='':
				listCount[names.index(line)]+=1
	print(listCount)

def data_read_dict():
	dictCount={}
	for data in names:
		dictCount[data]=0
	with open('data.txt','r') as f:
		for line in f:
			line=line.strip()
			if line!='':
				dictCount[line]+=1
	print(dictCount)






data_creation()
data_read_list()
data_read_dict()