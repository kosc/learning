# cd /d "D:/work/python/2017"
# str(123)							- перевод в строку
# int('123')						- перевод в целое число
# float(123)						- перевод в дробное
# bool('True')						- перевод в бул
# range(100)	#создать массив:	- диапазон 0 - 99
# list()		#list(range(100))	- перевод в строку

# test.index(x)						- возвращает индекс первого икса
# test.reverse()					- реверсирует массив
# test.count(x)						- считает, сколько иксов
# max(test)							- ищет максимальный элемент массива
# min(test)							- ищет минимальный элемент массива
# len(test)							- считает, сколько всего элементов
# test.append()						- добавляет элемент в конец массива
# test.insert(index, 'znachenie')	- довавляет элемент на выбранный индекс (оставльные двигаются)

# test = list(range(2, 21, 2))
# i = 0 
# length = len(test) - 1
# while i <= length: 
# 	print(test[i])
# 	test[i] = str(test[i]) + '!'
# 	i+=1
# print(test)

# def max(x,y):
# 	'''Function description'''
# 	if x>y:
# 		print('X is biger')
# 		return x
# 	elif y>x:
# 		print('Y is biger')
# 		return y
# 	else:
# 		print('x==y')
# print(max.__doc__)

# import random
# print(random.randint(1,1000))
# for x in range(1,10):
# 	print(random.randint(1,1000))

# from math import pi #as My_Pi
# print(pi)

# import pyowm
# city = input('What do you want: ')
# owm = pyowm.OWM('9ba4beaa57dcfd11797b04f633831b4a')
# observation = owm.weather_at_place(city)
# w = observation.get_weather()
# temp = w.get_temperature('celsius')['temp']
# time = w.get_reception_time()
# it's not working correctly
# print('Time is money, friend! - ' + str(time))
# print('In the ' +  city + ' now: ' + str(int(temp)) + ' on the celsian')
# print('Also, it\'s ' + w.get_detailed_status())

# class HowdyHoError(Exception):
# 	'''docstring for HowdyHo'''
# 	print('HelloError')
# raise HowdyHoError

# def exc(x):
# 	assert x > 0, 'x should be biger then 0'
# 	print(x)
# test = int(input())
# exc(test)

# filename = input('What the file you want to open (there is only "text.txt"): ')
# file = open(filename, 'r')
# print(file.read())
# file.close()

# filename = input('You want to add new file? Enter the name first: ')
# file = open(filename, 'w')
# file.write(input())
# file.close()

# filename = input('Enter the name, what you want: ')
# text = input('What the text you want to put in the file: ')
# file = open(filename, 'w')
# file.write(text)
# file.close()

# file = open('text.txt', 'a')
# file.write(' I love you' * 10)
# file.close()

# firstfile = input('What the file you want to copy: ')
# secondfile = input('Choose the name of new file: ')
# if secondfile == '':
# 	secondfile = 'backup_' + firstfile
# filecopy = open(firstfile, 'rb')
# filepaste = open(secondfile, 'wb')
# filepaste.write(filecopy.read())
# filecopy.close()
# filepaste.close()

# file = open(input('Enter file name: '))
# strings = file.readlines()
# for x in strings: 
# 	print(x)
# file.close()

# with open(input('Enter file name: ')) as f:
# 	print(f.read())

# dictionary
# ages = {
# 	'Dave' : 24,
# 	'Mary' : 42,
# 	'Cris' : 93
# }
# print(ages['Dave'])

# primary = {
# 	'red' = [255,0,0],
# 	'green' = [0,255,0],
# 	'blue' = [0,0,255],
#	[1,2,3] = 'black' - KeyError
# }
# print(primary['red'])
# print(primary['yellow'])

# rab = {
# 	'Andry' : '+380123123123',
# 	'Artom' : '+380652394923',
# 	'DIMON' : '+380663857937'
# }
# if 'DIMON' in rab:
# 	print(rab['DIMON'])
# print(rab.get('dimon', 'not found'))

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = list1[2:5]
# print(list2)
# list3 = list1[:5]
# print(list3)
# list4 = list1[5:]
# print(list4)
# list5 = list1[::2]
# print(list5)
# underlist5 = list5[3:]
# print(underlist5)
# chot = range(0,101)[::2]
# for i in chot:
# 	print(i)
# list6 = list1[-4:-1]
# print(list6)
# list7 = list1[::-1]
# print(list7)
# list8 = list1[::-1][::-1]
# print(list8)
# list9 = list1[0:0]
# print(list9)

# cubes = [i**3 for i in range(5)]
# print(cubes)
# evens = [i**2 for i in range(10) if i**2%2==0]
# print(evens)
# x = [ i for i in range(21) if i%3 == 0]
# print(x)
# even = [i*2 for i in range(10**100)]
# a = [x*10 for x in range(5,10)]
# a = [i*10 for i in range(5,10)]
# print(a)

# name = 'Jessy'
# age = 30
# print('Hello, ' + name + '!\nYou are ' + str(age) + ' years old now!')
# print('Hello, %s!\nYou are %d years old now!' % (name, age))
# %s - str %d - int %f - float
# print('Hello, {}!\nYou are {} years old now!'.format(name,age))
# print('{0}{1}{0}'.
# 	format('habr','a'))
# print('Hello, {x}!\nYou are {y} years old now!'.format(x = name, y = age))
# human = {
# 	'name' : 'Jessy',
# 	'age'  : 30
# }
# print('Hello, {person[name]}!\nYou are {person[age]} years old now!'.format(person = human))
# input_str = 'Jessy'
# x = 10
# if len(input_str)%2:
# 	x +=1
# print(('{0:@^'+str(x)+'}').format(input_str))

# input_str = 'Jessy'
# if len(input_str)%2:
# 	print(('{0:@^11}').format(input_str))
# else: 
# 	print(('{0:@^10}').format(input_str))

# print(arr1)
# arr1 = [for i in range(arr)]
# arr = [10, 2123, 1234]
# print([sum(map(int, str(number))) for number in arr])

# fruits  = ['Lemon','Apple','Kiwi','Pineapple','Strawberry']
# members = 'James, Jonny, Jessie, Jack, John'
# join replace startswith endswith lower upper split min max abs sum
# print(', '.join(fruits))

# print('Hello, Petr!'.replace('Petr', 'Alex'))

# name = input('Enter your name: ')
# if name.startswith('A'):
# 	print('Alex, Aaaa, AAAAAAAAAAAAAAAAAAAAAA. ')

# name = input('Enter your name: ')
# if (name.lower().startswith('a')):
# 	print('Alex, Aaaa, AAAAAAAAAAAAAAAAAAAAAA. ')

# input_str = input('Entex text to lower: ')
# print(input_str.lower())

# word = 'Hello, Drudving' 
# if word.endswith('ing'):
# 	print('Hello, INGa!')
# else: 
# 	print('Hello.')

# input_str = input('Enter something: ')
# print(input_str.upper())

# print(members.split(', '))

# print(min([3,64,123,735,123,543,12413,124,123,-23423,123,0]))
# print(max([3,64,123,735,123,543,12413,124,123,-23423,123,0]))

# print(abs(12))
# print(abs(0))
# print(abs(-12))

# print(sum([3,64,123,735,123,543,12413,124,123,-2323,123,0]))

############################################################################### course nomder 2

# a = 10
# b = 20
# c = 30
# d = 'strinf'
# e = True
# print('Hello,','wolrd',a,b,c,d,e)				# через запятую может быть удобно перечислять

# name = int(input())
# x = 100 if name >100 else name 			
# print(x)

# while для обычных циклов
# for для прохождения по списку или массиву

# for j in 'Hello, world!':
# 	print(j*3, end = ' baka ')

# letter = str(input('На какой букве остановиться: '))
# while len(letter) > 1: 
# 	print('try again')
# 	letter = str(input('На какой букве остановиться: '))
# for j in 'Hello, world!':
# 	if j == letter: 
# 		print(' \'' + letter + '\' is there')
# 		break
# 	print(j*3, end = '')
# else:  						# оператор else в структуре for служит для исполнения кода, в случае если оператор break не сработал (если он, конечно, есть)
# 	print(' \'' + letter + '\' is not in there')

# a = [x + y for x in 'list' if x != 's' for y in 'soup' if y != 'u']
# print(a)

# l = []
# l.append(23)
# l.append(34) 						- edit elements to list
# a = [45,46]
# l.extend(a)						- edit list 'a' to list 'l'
# l.extend(range(20,40))			- edit list with 20,21...38,39 to list 'l'
# print(l)
# l.insert(4,99)					- edit '99' to index 4
# l.pop(3) # delete 46				- delete and return element with index '3', if index not selected - return and delete last element
# print(l)
# print(l.index(23))				- return number of inder when first meat '23'
# print(l.count(34))				- считает количество елементов '34'
# l.sort()							- sorting by low to high
# print(l)
# l.reverse()						- sorting bu high to low
# print(l)
# l.clear()							- delete all elements
# print(l)
# print(l[-1])						- return last element
# l.remove(99)						- delete first '99' in the list and if it's not exist, ejects ValeuError
# i = 0 
# while i < len(l):
# 	print(l[i])
# 	i+=1
# print(i)					# переменная i существует после выполнения цикла
# # item[START:STOP:STEP]

# a,b,c = 0,0,3				# так тоже можно
# print(a,b,c)

# a = 43,32,64,123.324
# b = [32.45,234,746,432,43]
# print(a.__sizeof__()) 			#28
# print(b.__sizeof__()) 			#40 		return size in bytes

# a = ('hello',)					# 1 way to declare a tuple
# print(a)						# it's already tuple, not variable

# a = tuple('Hello, World')		# tuplu of letters
# print(a)



# d = {'test' : 1, 'teset' : 2}			# 1 way to declare a dictionary

# d = dict (							# 2 way
# 	first = 'one',
# 	second = 'two')
# d['first'] = 1
# print(d)

# d = dict([							#3 way
# 	('first','one'), 
# 	('second','two')])
# print(d)

# d = dict.fromkeys(['q','w','e'])
# d = dict.fromkeys(['x','y','z'], (1, 2, 3))		# 4 way. all index have (1,2,3) as value
# print(d)

# d = {a : a**2 for a in range(7)}					# 5 way
# print(d)

# person = {											# 6 way
# 	'name' : {
# 		'last_name' : 'Ivanov',
# 		'first_name' : 'Ivan',
# 		'middle_name' : 'Ivanovich'},
# 	'address' : [
# 		's. Andruchki', 
# 		'st. Vasilkovska 23b', 
# 		'ap.12'],
# 	'phone' : {
# 		'home_phone' : '34-67-12',
# 		'mobile_phone' : '8-800-555-35-35',
# 		'mobile_phone2' : 'None'}
# }
# print(person)
# print(person['name']['first_name'])
# print(person['phone']['mobile_phone'])
# # person.clear()
# print(person)
# print(person.values())	#
# print(person.keys())	# возвращает ключи в словаре
# print(person.items())	# возвращает пары (ключ, значение)
# print(person.popitem())	# удаляет и возвращает пару (ключ, значение), если словарь пуст - бросает исключение KeyError
# print(person.popitem())	# если не указаны аргументы, удаляет первый ключ
# print(person.setdefault('phone', '0638070701'))	# возвращает значение ключа, но если его нет, не бросает 
# print(person.setdefault('study', '0638070701'))	# исключение, а создаёт ключ со значением default (или None)
# person.update([other])	# обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None.
# print(person.values())	# возвращает значение в словаре
# people = person.copy()	#
# print(people)

# a = set('Hello!')
# print(type(a))					# class <set>
# print(a)

# a = {'12' : 23}					# THIS is dictionary
# print(type(a))
# print(a)

# a = {'12', 23}					# THIS is set
# print(type(a))
# print(a)

# a = {i**2 for i in range(20)}	# SET
# print(type(a))
# print(a)

# a = {}							# DICTIONARY
# print(type(a))
# print(a)

# a = {1}							# SET
# print(type(a))
# print(a)

# a = set('zyxqwe')
# b = frozenset('hello, world')
# a.add(2)
# # b.add(3)
# print(type(a))
# print(a)
# print(type(b))
# print(b)

# a = ['J','o','r','a',' ','t','v','o','j','a',' ','m','a','m',' ','o','c','h','e','n',' ','k','r','a','s','i','v','a']
# print(set(a))

# a = {1,2,3,4,5,6,7,8,9}
# x = 15
# y = {12,53,234,62,5,234,90}
# print(len(a))
# print(x in a)
# print(a.isdisjoint(y))				# true if y and a абсолютно разные (нет ни 1 общего элемента)
# y = {1,2,3,4,5,6,7,8,9}					# y == a 		true
# y = {1,2,3,4,5,6,7,8}						# y == a 		false
# y = {9,8,7,6,5,4,3,2,1}					# y == a 		true
# print(y==a)

# a = {12,23,43,54,65}
# b = {52,72,25,63,234,74,2}
# a.update(b)
# print(type(a))
# print(a)								# {65, 2, 72, 234, 43, 12, 74, 52, 54, 23, 25, 63}

# a = {1,2,3,32,4,5,6,52}				# {32, 1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 52}
# b = {5,6,7,8,9,0}						# как это понимать? 
# a.update(b)
# print(type(a))
# print(a)

# a = {12,23,43,54,65,74,25,12}
# b = {52,72,25,63,234,74,2}
# a.intersection_update(b)
# print(a)
# a.difference_update(b)					# возвращает те числа из множества a, которых нет в множестве b
# a.symmetric_difference_update(b)			# возвращает те числа из множества a and b, которых нет в a and b одновременно
# a.add(99)									# only 1 element
# a.remove(12)								# nu ti ponyal. delete all 12's
# a.discard(12)								# delete, but not return errors.
# a.pop()									# delete random element
# a.clear()									# nu ti ponyal
# print(a)

####### functions 

# def func(x):
# 	def add(a):
# 		return x+a
# 	return add 
# print(func(100)(250))

# def exix():
# 	x = 15
# 	return x
# print(exix())
# print(x)								# x is not exist from outside the func

# def func(x,y,z=1):
# 	res = (x+y)*z
# 	return res
# print(func())

# def func(*args):						# tuple
# 	return args
# print(func(3,5,6,2,'12erd',True,67,2))

# def func(**args):						# dictionary
# 	return args
# print(func(a=12,b=32,c=90))

# add = lambda x,y : x*y
# print(add(5,6))

# print((lambda x,y : x%y) (19,3))

# fun = lambda *args : args 
# print(fun(123,432.43,True,'Helo',[43,53,76,90]))

