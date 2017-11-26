import random 

def creatArray():
	# r = 0
	x = int(input("Введите количество строк:"))
	y = int(input("Введите количество столбцов:"))
	array = []
	
	for i in range(x):
		array.append([])
		for j in range(y):
			array[i].append(random.randint(0,100))
			# r +=1
	print('\nMatrix:')
	for i in range(x):
		print(array[i])
	
	max_element = array[0][0] 
	for i in range(x):
		for j in range(y):
			if array[i][j] > max_element:
				max_element = array[i][j]
				max_str = i
	array[max_str].sort(reverse=True)
	print('\nResult matrix:')
	for i in range(x):
		print(array[i])
		
creatArray()