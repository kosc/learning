# 1
# def p(x,y): 
# 	t = x%y
# 	++t # странный пример. учитывая, что такой операции как ++ в питоне нет.
# 	return t*x+y
# print(p(5,3))

# 2
# def func(level): 
# 	if level == 1:
# 		return 1
# 	else:
# 		return level+func(level-1)
# print(func(5)) # 15.

# # 3. принимает значение для количества элементов, елементы случайны от -1000 до 1000. 
# # Этот список сортируется следующим образом: отрицательные в порядке возрастания, затем 0, затем положительные в порядке убывания.
# from random import *
# elements = int(input('how many elements: '))
# result = []
# negative = []
# zero = []
# positive = []
# for i in range(elements):
# 	result.append(randint(-1000, 1000))
# print(result)
# max_index = len(result)
# max_index -= 1
# counter = 0
# while counter <= max_index:
# 	bar = result[counter]
# 	if bar<0:
# 		negative.append(bar)
# 		negative.sort()
# 	elif bar>0:
# 		positive.append(bar)
# 		positive.sort(reverse = True)
# 	else:
# 		zero.append(bar)
# 	counter += 1
# print(negative)
# print(positive)
# if zero:
# 	result = negative + zero + positive
# else:
# 	result = negative + positive
# print(result)

# 4 есть массив интов нечётной длины. заведомо известно, что в нем все элементы парные, кроме одного. ваша задача - найти этот элемент
# намекну - a XOR b XOR b === a
# 5 ну представьте себе куб, например, 1000x1000x1000 нужно сказать, какие именно сабкубики пересекает луч, определяемый единичным вектором
# from random import *
# while True:
#     try:
#         n=int(input("Enter the number of items in the list: \n"))
#         break
#     except Exeptions:
#         print("You entered an invalid value\n")
# lst =[]
# for i in range (n):
#     lst.append(randint(-1000,1000))
#     lst.sort()
# for i in range(n):
#     if lst[i]>-1 or i==n-1:
#         lst.insert(i,len(lst))
#         break
# print("Your list:{0}".format(lst))