# cd /d "D:/work/python/2017"
# str(123)							- перевод в строку
# int('123')						- перевод в целое число
# float(123)						- перевод в дробное
# bool('True')						- перевод в бул
# range(100)	#создать массив:	- диапазон 0 - 99
# list()		#list(range(100))	- перевод в строку
# https://pythonworld.ru/osnovy/vstroennye-funkcii.html

# test.index(x)						- возвращает индекс первого икса
# test.reverse()					- реверсирует массив
# test.count(x)						- считает, сколько иксов
# max(test)							- ищет максимальный элемент массива
# min(test)							- ищет минимальный элемент массива
# len(test)							- считает, сколько всего элементов
# test.append()						- добавляет элемент в конец массива
# test.insert(index, 'znachenie')	- довавляет элемент на выбранный индекс (оставльные двигаются)

# ##########whiles
# i = 5 
# while i<15:
# 	print(i)
# 	i +=1

# for i in 'Hello World':
# 	if i == 'o': continue			#break - exit
# 	print(i*2, end='')
# Слово else, примененное в цикле for или while, проверяет, был ли произведен выход из цикла инструкцией break, или же "естественным" образом. 
# else выполнится только в том случае, если выход из цикла произошел без помощи break.

# for i in 'Hello, World':
# 	if i == 'q':
# 		break
# else:
# 	print('\'q\' is not')

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
# 	[1,2,3] = 'black' - KeyError
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
# 	print(('{0:@^21}').format(input_str))
# else: 
# 	print(('{0:@^20}').format(input_str))

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

# ############################################################################## course nomder 2

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
# else:  					# оператор else в структуре for служит для исполнения кода, в случае если оператор break не сработал (если он, конечно, есть)
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
# print(i)					# переменная i существует после в.ыполнения цикла
# # item[START:STOP:STEP]

# a,b,c = 0,0,3				# так тоже можно
# print(a,b,c)

# a = 43,32,64,123.324
# b = [32.45,234,746,432,43]
# c = 123
# d = 86934086348
# e = 1387409237984632897563489529
# f = 13.24124515187095342
# g = 'HE:LWKeqwelri uewiovfdshgskl djfhgdflgh sl'
# h = None
# k = True
# l = False

# print(a.__sizeof__()) 			#28
# print(b.__sizeof__()) 			#40 		return size in bytes
# print(c.__sizeof__())
# print(d.__sizeof__())
# print(e.__sizeof__())
# print(f.__sizeof__())
# print(g.__sizeof__())
# print(h.__sizeof__())
# print(k.__sizeof__())
# print(l.__sizeof__())

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
# # # person.clear()
# # print(person)
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

# ###### functions 

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

# print(1/0) # ZeroDivision
# print(int('qwe')) #Value
# print('2'+1) # Type

# x = int(input())
# y = int(input())
# try:
# 	res = x/y
# except ZeroDivisionError: 
# 	res = 0 
# 	print('You can\'t division on 0')

# try:
# 	x = int(input())
# except ValueError: 
# 	print('You should enter a number')
# # print(x)									# x is not exist now

# try:
# 	x = int(input())
# except ValueError:
# 	print('It\'s not a number')
# 	x = 0
# try:
# 	y = int(input())
# except ValueError:
# 	print('It\'s not a number')
# 	y = 0
# else: 
# 	print('Your input is correct')
# finally:
# 	print('the input ends.')
# try: 
# 	res = x/y
# except ZeroDivisionError:
# 	print('0? again?')
# 	res = 0
# print(res)

# x, y = None, None								# максимально чистый код, которого мне удалось добиться
# while x is None or y is None or y == 0:
# 	try:
# 		x = int(input())
# 		y = int(input())
# 		res = x/y
# 	except ValueError:
# 		print('Your input is wrong. Try again')
# 		continue
# 	except ZeroDivisionError:
# 		print('Your Y is 0. Try again')
# 		continue
# 	else: 
# 		print('the input ends')
# 		print('answer - '+str(res))
# 		break
# print(x,y)

# f = open('text.txt')
# print(f.read())
# for line in f:
# 	print(line, end='')
# f.close()

# f = open('text.txt','w')
# f.write('testestsetsersetesrerewrwerwe rfd ')
# f.close()

# with open('test.txt', 'w', encoding='utf-8') as inFile:
# 	num = int(input())
# 	line = str('1 / ' + str(num) + ' = ' + str(1/num))
# 	print(line)
# 	inFile.write(line)

# # import math, time
# import random as r
# # try: 
# # 	import somemodule
# # except ImportError:
# # 	pass
# # import mymodule as m
# from mymodule import mult
# # print(math.e)
# # print(math.pi)
# # print(math.cos(3))
# # print(time.time())
# # print(os.getcwd())
# # print(r.random())
# # m.hi()
# # print(m.plus(15,43))
# print(mult(564,2))
# # print(m.mult(43,20))

# ############################################### OOP DAAAAAAAAAAAAAAAAAAAAAAAAA
# class Person:							# создаю класс 
# 	name = 'Default name'				# создаю в нём поле
# 	age = 10							# второе
# 										# 
# 	def __set(self, inp_name, inp_age):	# создаю в нём метод как функцию. в аргументах - обязятельно self, ибо это класс. 
# 		self.name = inp_name			# присваеваю к полю нейм то слово, что в аргументе
# 		self.age = inp_age				# и так же в возрастом
# 										# 
# vlad = Person()							# создаю объект класса 
# vlad._Person__set('Vladislav', 25)				# присваиваю значения к полям с помощью метода set
# print(vlad.name + ' ' + str(vlad.age))	# вывожу значения
# 										# 
# alex = Person()							# ну всё понятно... 
# alex._Person__set('Alex', 13)					# тоже самое.
# print(alex.name, alex.age)				# без конкатонации и преобразования тоже можно

# ######################### наследование, полиморфизм, инкапсуляция
# # наследование - создание класса, который в точности копирует все поля и методы класса
# class Student(Person):
# 	"""docstring for Student"""
# 	course = 1
# 										# def __init__(self, arg):
# 										# 	super(Student, self).__init__()
# 										# 	self.arg = arg
# igor = Student()
# igor._Person__set('Igor', 19)
# igor.course = 2
# print(igor.name, igor.course)

# #######################################Конструкторы

# class Person: 
# 	name = 'Dafault name'
# 	age = 18

# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def __set(self, name, age):
# 		self.name = name
# 		self.age = age

# class Student (Person):
# 	course = 1

# igor = Student()
# igor._Person__set('Igor', 19)
# igor.course = 2
# print(igor.course)

# vlad = Person()
# vlad._Person__set('Vlad', 25)
# print(vlad.name + ' ' + str(vlad.age))

# #######################################Декораторы

# def decorator(func):
# 	def wrapper():
# 		print('Hello, world 1')
# 		func()
# 		print('Hello, world 2')
# 	return wrapper

# def show():
# 	print('line')

# show()
# dec = decorator(show)
# dec()

# ----------------------------------------------------------------------------------------------------------------------------
# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword('big'))

# print(divmod(19, 3))				# тоже полезная штука.

# print(int(12.432))
# print(bin(123))
# print(oct(123))
# print(hex(123))
# print(int(0o173))

# print(0.2 + 0.2 + 0.2 + 0.2 + 0.2 + 0.2 + 0.2 + 0.2) 			# при 8 значениях ломается. показывает 0.7999. 1.59999.

# print(3**1000)

# int(123.123)		#same things
# round(123.123)	#same things

# x = 'Hello World'
# print(x)					# нельзя просто так взять и переписать символ в строке, нужно создавать новую.
# x = x[0:5] + ',' + x[6:]
# print(x)

# x = '598578950309845098'
# summ = 0
# for i in range(len(x)):
# 	summ += int(x[i])*(i+1) 
# print(summ)

# x = '{0}, {1}, {2}'.format('a','b','c')
# print(x)
# x = '{}, {}, {}'.format('a','b','c')
# print(x)
# x = '{0}, {1}, {2}'.format(*'abc')
# print(x)
# x = '{1}, {2}, {0}'.format('a','b','c')
# print(x)
# x = 'Coordinates: {latitude}, {longitude}'.format(latitude = '12.12', longitude = 'qwewqe')
# print(x)
# y = {'hello':'hi', 'first':'one'}
# x = 'Coordinates: {hello}, {first}'.format(**y)
# print(x)

# c = [x*3 for x in 'list']
# print(c)
# c = [x*3 for x in 'list' if x != 'i']
# print(c)
# c = [x+y for x in 'list' if x != 's' for y in 'qwerty' if y != 'r']

# quotes = {
#  "Moe": "A wise guy, huh?",
#  "Larry": "Ow!",
#  "Curly": "Nyuk nyuk!",
#  }
# stooge = "Curly"
# print(stooge, "says:", quotes[stooge])

# for countdown in 5, 4, 3, 2, 1, "hey!", 234:
#  print(countdown)

# import json
# from urllib.request import urlopen
# url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
# response = urlopen(url)
# contents = response.read()
# text = contents.decode('utf8')
# data = json.loads(text)
# for video in data['feed']['entry'][0:6]:
#  print(video['title']['$t'])

# import this

# while True:
# 	while True:
# 		try:
# 			a = float(input(':'))
# 			b = float(input(':'))
# 			break
# 		except ValueError:
# 			print('wrong input')
# 			# exit = input('Nadoelo? ')
# 			# if (exit == '1') or (exit == 'yes') or (exit == 'Yes'): break
# 			# else: continue
# 	oper = input('+, -, *, /, //, %, ^, div:')
# 	if oper == '+':
# 		c = a+b
# 	elif oper == '-':
# 		c = a-b
# 	elif oper == '*':
# 		c = a*b
# 	elif oper == '/':
# 		c = a/b
# 	elif oper == '//':
# 		c = a//b
# 	elif oper == '%':
# 		c = a%b
# 	elif oper == '^':
# 		c = a**b
# 	elif oper == 'div':
# 		print(divmod(a,b))
# 	else:
# 		print('wrong input')
# 	if oper != 'div':
# 		d = int(c)
# 		if d != c: 
# 			print(c)
# 		else: 
# 			print(d)
# 	exit = input('Exit? ')
# 	if (exit == '1') or (exit == 'yes') or (exit == 'Yes'): break
# 	else: continue

# x = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod'
# y = x.split()
# print(y[2])
# print(y)

# z = ' '.join(y)
# print(z)

# print(z.startswith('Lorem'))

# print(z.endswith('mod'))

# word = 'ip,'
# print(z.find(word))
# print(z.rfind(word))
# print(z.count(word))
# print(z.isalnum())

# ########################################### регистр

# setup = '**ut enim ad minim veniam, quis nostrud. exercitation ullamco************'
# z = setup.strip('***')
# print(z)
# z = z.capitalize()
# print(z)
# z = z.title()
# print(z)
# z = z.upper()
# print(z)
# z = z.lower()
# print(z)
# z = z.swapcase()
# print(z)
# z = z.center(70)
# print(z)
# z = z.rjust(95)
# print(z)

# x = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod'
# y = x.replace('si', '**')
# print(y)
# y = x.replace('si', '**', 1)
# print(y)

# x = list('cat')
# print(x)
# y = ('qe', 'asd', 'fjfjf')
# del y 						# tuple can be deleted
# x = list(y)
# print(x)
# x.append('llllllwerwerw')
# print(x)
# x = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet']
# y = ['consectetur', 'adipisicing', 'elit', 'sit', 'do', 'eiusmod']
# x.extend(y)
# print(x)
# x.insert(40, 'DOLOR')
# print(x)
# del x[-1]
# print(x)
# x.remove('sit')
# print(x)
# print(x.pop())
# print(x)
# print(x.index('sit'))

# print('sitw' in x)
# print(x.count('sit'))

# x.sort(reverse=True)
# print(x)

# first = ['qwe',';kl','ghj','fgh','try','zxc','asd']
# sec = ['qqq','www','eee','rrr','ttt','yyy']
# print(sec)
# sec = list(first)
# sec = first[:]
# sec = first.copy()
# print(sec)
# print(first)
# first = 'hello'
# print(sec)

# a = [1,2,3]
# b = a
# print(b)
# a[0] = 'surprise'
# print(b)
# b[0] = 'I hate surprises'
# print(a)


# n = int(input())			# числа фибаначи. 
# x, y = 0, 1
# while n > 0:
# 	print(x, end = '; ')
# 	x, y = y, x+y
# 	n -= 1
# print()

# max_num = int(input())
# x, y = 0, 1
# while x < max_num:
# 	print(x, end = '; ')
# 	x, y = y, x+y


# x = [1,2,4,5,6,7,8]
# print(x.reverse())
# print(x)

# x = [ ['a','A'], ['b','B'], ['c','C'] ]
# y = dict(x)
# print(y)


# x = {'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael', 'Chapman': 'Graham', 'Idle': 'Eric'}
# x['Gilliam'] = 'Terry'
# print(x)
# print('Cleese' in x)
# print('John' in x)
# print(x.get('Cleese'))
# print(x.items())
# keys = list(x.keys())
# values = list(x.values())
# print(keys)
# print(values)
# x = set(x)
# print(x)

# drinks = {
# 	'martini': {'vodka', 'vermouth'},
# 	'black russian': {'vodka', 'kahlua'},
# 	'white russian': {'cream', 'kahlua', 'vodka'},
# 	'manhattan': {'rye', 'vermouth', 'bitters'},
# 	'screwdriver': {'orange juice', 'vodka'}
# }
# for x, y in drinks.items():
# 	if 'vodka' in y and not ('vermouth' in y or 'cream' in y):
# 		print(x)
# print()
# for x, y in drinks.items():
# 	if ('orange juice' in y) or ('vermouth' in y):
# 		print(x)

# for x, y in drinks.items():
# 	if y & {'vermouth', 'orange juice'}:
# 		print(x)

# for x,y in drinks.items():
# 	if 'vodka' in y and not y & {'vermouth', 'cream'}:
# 		print(x)

# black = drinks['black russian']
# white = drinks['white russian']

# a = {1,2,3,4,10,11,12}
# b = {4,3,2,1.0,5,6,7,8}
# print(a & b)
# print(a.intersection(b))
# print(black & white)
# print()
# print(a | b)
# print(a.union(b))
# print(black | white)
# print()
# print(a - b)
# print(a.difference(b))
# print(b.difference(a))
# print(white - black)
# print()
# print(a ^ b)
# print(a.symmetric_difference(b))
# print(black ^ white)
# print()
# print(black <= white)
# print(black.issubset(white))
# print(white >= black)
# print(white.issuperset(black))


# marxes  = ['Groucho', 'Chico', 'Harpo']
# pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
# stooges = ['Moe', 'Curly', 'Larry']
# x = (marxes,pythons,stooges)
# print(x)
# x = [marxes,pythons,stooges]
# print(x)
# x_dict = {'Marxes' : marxes, 'Pythons' : pythons, 'Stooges' : stooges}
# print(x_dict)
# x = {
# 	(44.79, -93.14, 285) : 'My House',
# 	(38.89, -77.03, 13) : 'The wight house'
# }



# birth_year = 1998
# years = [i for i in range(birth_year, birth_year+6)]
# print(years)
# print('Тебе было 3 в ' + str(years[3]))
# print(years[-1])
# things = ['mozzarela','cinderella','salmonella']
# print(things[1].title())
# print(things)
# print(things[0].upper())
# print(things)
# things[0] = things[0].upper()
# print(things)
# x = things.index('salmonella')
# del things[x]
# print(things)

# surprise = ['Groucho', 'Chico', 'Harpo']
# surprise[-1] = surprise[-1].lower()
# surprise[-1] = surprise[-1].swapcase()
# print(surprise[-1])

# e2f = {'dog' : 'chien','cat' : 'chat','walrus' : 'morse'}
# print(e2f['walrus'])
# x = list(e2f.items())
# f2e = {}
# for i in x:
# 	print(i)
# 	f2e.update({i[1] : i[0]})
# print(f2e['chien'])

# y = set(e2f.keys())
# print(y)

# life = {
# 	'animal' : {
# 		'cat' : ['Henry', 'Grumpy', 'Lucy'],
# 		'octopi' : {},
# 		'emus' : {}
# 	},
# 	'plant' : {},
# 	'other' : {},
# }

# print(life.keys())
# print(life['animal'].keys())
# print(life['animal']['cat'])



# print('Hello\
# , World')
# long_word = 'qwertyuiopqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweqweq'\
# +'qweqweqweqweqweqwe[q]oqweqw]eq[w[[]]]]]]]]]]]]]]]]]]][[][w[[qw]e][qwe]\
# qweqwipoeqweiqwuepouqwpoieqwew'
# print(long_word)

# while True:
# 	stuff = input("String to capitalize [type q to quit]: ")
# 	if stuff == "q":
# 		break
# 	print(stuff.capitalize())

# while True:
# 	x = input()
# 	if x == 'q':
# 		break
# 	x = int(x)*int(x)
# 	if x%2:
# 		continue
# 	print(x)

# num = [1,2,3,4,5,7,8,9]
# position = 0
# while position < len(num):
# 	x = num[position]
# 	print(x)
# 	if x == 6:
# 		print('Found even number', x)
# 		break
# 	position += 1
# else: # break not called
# 	print('No even number found')

# lorem = {
# 	'ipsum' : 'dolor',
# 	'sit' : 'amet',
# 	'consectetur' : 'adipisicing',
# 	'elit' : 'sed',
# 	'do' : 'eiusmod',
# }
# for x in lorem: 		#can be also lorem.keys()
# 	print(x)
# for x in lorem.values():
# 	print(x)
# for x in lorem.items():
# 	print(x)
# for x, y in lorem.items():
# 	print('Hello', x, 'World', y)

# cheeses = []
# for x in cheeses:
# 	print('Cheese', x)
# 	break
# else: 
# 	print('here is no cheese')

# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['banana', 'orange', 'peach']
# drinks = ['coffee', 'tea', 'beer']
# desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
# 	print(day, fruit, drink, dessert)
# 	print(dessert) 				#pudding never works

# english= ['Monday', 'Tuesday', 'Wednesday']
# franch = ['Lundi', 'Mardi', 'Mercredi']

# x = zip(english, franch)
# print(x)
# x = list(x)
# print(x)
# x = dict(x)
# print(x)

# for x in range(0, 10, 2):
# 	print(x)
# lis = []
# for x in range(20, 10, -2):
# 	lis.append(x)
# print(lis)

# [выражение for элемент in итерабельный объект]

# lis = [x for x in range(20,10,-2)]
# print(lis)
# lis = [x**x for x in range(10,0,-1)]
# print(lis)
# lis = [x for x in range(0,30) if x%3==0]
# print(lis)
# lis = []
# for x in range(0,30):
# 	if x%3 == 0:
# 		lis.append(x)
# print(lis)

# cols = range(1,6)
# rows = range(1,4)
# # for col in cols:
# # 	for row in rows:
# # 		print(col, row)
# cells = [(col, row) for row in rows for col in cols]
# for x in cells:
# 	print(x)

# { выражение_ключа: выражение_значения for выражение in итерабельный объект }

# word = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do'
# dic = {x:word.count(x) for x in word}
# print(dic)

# word = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do'
# dic = {x:word.count(x) for x in set(word)}
# print(dic)

# { выражение for выражение in итерабельный объект}

# x = {x for x in range(50) if x%3==0}
# print(x)

# x = (x for x in range(10))
# print(x)
# # for t in x:
# # 	print(t)
# e = list(x)
# print(e)

# def menu(wine, entree, dessert = 'pudding'):
# 	return {'Wine':wine, 'entree':entree, 'dessert':dessert}
# print(menu('white', 'chicken', 'pie'))
# print(menu('first', 'second', 'third'))
# print(menu(entree = 'chicken', dessert = 'pie', wine = 'white'))

# def isbug(arg, x=[]):
# 	x.append(arg)
# 	return x
# print(isbug(15))
# print(isbug(21))
# print(isbug(42))

# def test(arg, x=None):
# 	if x is None:
# 		x = []
# 	x.append(arg)
# 	return x
# print(test(14))
# print(test('ew'))

# def test(*x):
# 	print('qweqwe', x)
# test()
# test('qwe', 12, True)

# def test(first, second, *args):
# 	'mmmm, documentation'
# 	print('First -', first)
# 	print('Second -', second)
# 	print('Other -', args)
# test('qwe', 'asd', 'dgdg', 'Hello')

# def print_kwords(**kwargs):
# 	'''MMMM LONG DOCUMENTATION'''
# 	print('Keywords:', kwargs)
# print_kwords(world='Hello')
# print_kwords(wine='merlot', entree='mutton', dessert='macaroon')
# help(print_kwords)
# print(print_kwords.__doc__)

# def sorokdwa():
# 	print(42)
# def runniga(func):
# 	func()
# runniga(sorokdwa)		# В Python круглые скобки означают «вызови эту функцию». 
# 				Если скобок нет, Python относится к функции как к любому другому объекту. 

# def plus(x,y):							# Внутри функции pluswithargs() аргумент plus, 
# 	print(x+y)							# представляющий собой имя функции, был присвоен 
# def pluswithargs(func, first, secind):	# параметру func, 13 — параметру first, а 15 — 
# 	func(first, secind)					# параметру secind. В итоге получается следующая 
# pluswithargs(plus, 13, 15)				# конструкция: plus(13,15)

# def summa(*args):
# 	return sum(args)
# def summ_with_args(func, *suuuma):
# 	return func(*suuuma)
# print(summ_with_args(summa, 1,2,3,4,5,6,7,8,9))

# def first(a,b):
# 	def second(c,d):
# 		print(c, 'c')
# 		print(d, 'd')
# 		return c + d
# 	return second(a,b)
# print(first(8,7))
# print(second(4,7))			# you can't

# def edit(text):
# 	def inner(hello):
# 		return 'Smili. Sweet. Sister. %s' % hello
# 	return inner(text)
# print(edit('CYKA BLYAT'))

# def edit2(text):
# 	def inner2():
# 		return 'Smile. Sweet. Sister. %s' % text
# 	return inner2
# # print(edit2('chiki briki i v damki')())
# a = edit2('chiki briki i v damki')
# # print(a())
# print(type(a))

# def editstory(words, func):
# 	for x in words: 
# 		print(func(x))
# stairs = ['thud','meow','thud','hiss']
# # qwe = ['qwe','qwe','asd','dfg']
# # def enliven(word):
# # 	return word.capitalize() + '!'
# # editstory(stairs, enliven)
# editstory(stairs, lambda word: word.capitalize() + '!')

# def f(x): return x**2
# print(f(8))
# g = lambda x:x**2
# print(g(8))

# def make_incrementor(n): return lambda x: x+n
# f = make_incrementor(2)
# g = make_incrementor(6)
# print(f(42),g(42))
# print(make_incrementor(6)(9))

# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# qwe = list(filter(lambda x: x%3==0, foo))
# print(filter(lambda x: x%3==0, foo))

# names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
# b_names = list(filter(lambda i: i.startswith('B'), names))
# print(b_names)

# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# print(list(map(lambda x: x * 2 + 10, foo)))
# print(foo)

# from functools import *
# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# print(reduce(lambda x, y: x + y, foo))

# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# def sqr(x):
# 	bar = []
# 	for i in x:
# 		bar.append(i**2)
# 	return bar
# print(sqr(foo))

# items = [1, 2, 3, 4, 5]
# def sqr(x): return x ** 2
# print(list(map(sqr, items)))

# def square(x):
# 	return (x**2)
# def cube(x):
# 	return (x**3)
# funcs = [square, cube]
# for r in range(5):
# 	value = list(map(lambda x: x(r), funcs))
# 	print(value)

# nums = range(50)
# qew = list(nums)
# print(nums)
# print(qew)
# if qew is nums:
# 	print('wqe')

# def sqr(x): return x**2
# print(list(map(sqr, [1, 2, 3])))

# В Python генератор — это объект, который предназначен для создания последовательностей

# def my_range(start = 1, end = 10, step = 1):
# 	number = start
# 	while number < end:
# 		yield number
# 		number += step
# print(my_range)
# ranger = my_range(1,5)
# for i in ranger:
# 	print(i)

# Декоратор — это функция, которая принимает одну функцию в качестве аргумента и возвращает другую функцию.

# def getTalk(type = 'shout'):
# 	def shout(word = 'Yes'):
# 		return word.capitalize() + '!'
# 	def whisper(word = 'Yes'):
# 		return word.lower() + '...'

# 	if type == 'shout':
# 		return shout
# 	else: 
# 		return whisper
# talk = getTalk()
# talksec = getTalk('not shout')
# print(talk)
# print(talk(('decor is easy')))
# print(talksec(('or not')))

# def capapcap(word = 'Yes'):
# 	print(word.capitalize() + '!')
# 	print()

# def dosomething(func):
# 	print('do something before you call the inner function, each you give me')
# 	func()

# dosomething(capapcap)

# def my_shine_new_decorator(a_func_to_decorate):
# 	def the_wrapper_around_the_original_func():
# 		print('Some code to do before main func')
# 		a_func_to_decorate()
# 		print('Some code to do after main func')
# 	return the_wrapper_around_the_original_func
# def a_stand_alone_func():
# 	print('It\'s just lonely function...')
# a_stand_alone_func = my_shine_new_decorator(a_stand_alone_func)
# a_stand_alone_func()
# print()
# @my_shine_new_decorator
# def another_stand_alone_func():
# 	print('Leave me alone!')
# another_stand_alone_func()

# def bread(func):
# 	def wrapper():
# 		print('</------\>')
# 		func()
# 		print('<\______/>')
# 	return wrapper
# def ingredients(func):
# 	def wrapper():
# 		print('##tomato##')
# 		func()
# 		print('~~salad~~')
# 	return wrapper
# @bread
# @ingredients
# def sandwich(food = '---ham---'):
# 	print(food)
# sandwich()
# print()
# # sandwich = bread(ingredients(sandwich))
# # sandwich()


# def document_it(func):
# 	def new_function(*args, **kwargs):
# 		print('Name func -', func.__name__)
# 		print('arguments -', args)
# 		print('dictionary-', kwargs)
# 		result = func(*args, **kwargs)
# 		print('result    -', result)
# 		return result
# 	return new_function

# def squer_it(func):
# 	def new_function(*args, **kwargs):
# 		result = func(*args, **kwargs) ** 2
# 		return result
# 	return new_function

# @document_it
# @squer_it
# def addnum(a,b):
# 	return a+b
# # cooleraddnum = document_it(addnum)
# # cooleraddnum(12,15)
# print(addnum(12,15))


# animal = 'Cat'
# def func():
# 	global animal
# 	animal = 'Fox'
# 	print(id(animal))
# 	print(animal)
# func()
# print(id(animal))

# def localvar():
# 	animal = 'cat'
# 	lis = ['qwe','asd',123]
# 	dick = {'Hi':'Hello', 'So':'Have you'}
# 	print(locals())
# print(globals(), end='\n\n')
# localvar()

# def somefunc():
# 	'''Some documantation
# 	on this func'''
# 	print('name: ' + somefunc.__name__)
# 	print('doc: ' + somefunc.__doc__)
# somefunc()

# lis = ['so','how','are','you']
# position = 5
# try:
# 	print(lis[position])
# except IndexError:
# 	print('position not between 0 and', len(lis)-1, 'now', position)
# except: 
# 	print('Oh, god! Something is wrong!')

# short_list = ['qwe','asd','zxc',123,4.1415]
# while True:
# 	position = input('Position? q = quit: ')
# 	if position == 'q': 
# 		break
# 	try: 
# 		position = int(position)
# 		print(short_list[position])
# 	except IndexError as ind:
# 		print('Wrong index:', position)
# 	except Exception as other:
# 		print('Something else broked:', other)

# class UppercaseException(Exception):
# 	pass
# words = ['eeenie', 'meenie', 'miny', 'MO']
# for i in words:
# 	if i.isupper():
# 		raise UppercaseException(i)

# 						guess_me = 0
# while guess_me != 7:
# 	guess_me = int(input('Number: '))
# 	if guess_me > 7: 
# 		print('Too high')
# 	elif guess_me < 7:
# 		print('Too low')
# 	else: 
# 		print('Ok')
# 		break
# start = 1
# while guess_me > start:
# 	print(start)
# 	if guess_me == start:
# 		print('Found')
# 		break
# 	elif start > guess_me:
# 		print('start too high')
# 		# start -+ 1 
# 		# continue
# 		break
# 	else: 
# 		print('start too low')
# # 	start += 1
# x = [3,2,1,0]
# for i in x:
# 	print(i)

# x = [i for i in range(10) if i%2!=0]
# print(x)

# squares = {x:x**2 for x in range(10)}
# print(squares)

# odd = {i for i in range(10) if i%2==0}
# print(odd)

# for thing in ('Got %s' % number for number in range(10)):
# 	print(thing)

# def test(func):
# 	def inner(*args, **kwargs):
# 		print('Start')
# 		result = func(*args, **kwargs)
# 		print('end')
# 		return result
# 	return inner
# @test
# def greeting():
# 	print('So have you heard?')
# greeting()

# nums = [55,44,33,22,11]
# if all(i > 5 for i in nums):
# 	print('все числа больше 5')
# if any(i % 2 == 0 for i in nums):
# 	print('тут есть чётные числа. ')
# for i in enumerate(nums):
# 	print(i)

# from random import choice as my_func
# x = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipisicing', 'elit', 'do', 'eiusmod']
# randomchoice = my_func(x)
# print(randomchoice)

# from weater import daily, weekli
# print('Daily weater:', daily.forecast())
# print('Weekly weater:')
# for i, j in enumerate(weekli.forecast(), 1):
# 	print(i, j)

# # , 'Palin': 'Michael', 'Chapman': 'Graham', 'Idle': 'Eric'
# x = {'Cleese': 'John', 'Jones': 'Terry'}
# print(x.get('Jones', 'NOT FOUND'))
# y = x.setdefault('Pelin','Hello!')
# print(x)
# z = x.setdefault('Cleese', 'sometext')
# print(z)

# from collections import defaultdict
# hmm = defaultdict(int)
# # hmm = {'Cleese': 'John', 'Jones': 'Terry' : None, 'Palin' : None, 'Chapman' : None, 'Idle': 'Eric'}
# hmm['Hydrogen'] = 1
# hmm['Lead']
# print(hmm)

# from collections import defaultdict
# def perce():
# 	return 'не тревожь читающих драконов'
# x = defaultdict(perce)
# x['first'] = 'one'
# x['second'] = 'two'
# print(x['notnotnot'])

# from collections import defaultdict
# food_counter = defaultdict(int)
# for food in ['чаёк','сосисочки','чаёк','кофе','кофе','кофе','молоко','кофе','яблоко','яблоко']:
# 	food_counter[food] += 1
# for one, count in food_counter.items():
# 	print(one, count)

# dict_counter = {}
# for food in ['чаёк','сосисочки','чаёк','кофе','кофе','кофе','молоко','кофе','яблоко','яблоко']:
# 	if not food in dict_counter:
# 		dict_counter[food] = 0
# 	dict_counter[food] += 1
# for food, count in dict_counter.items():
# 	print(food, count)

# x,y,z = ( input() for _ in range(3) )
# print(x,y,z)

# from collections import Counter
# breakfast = ['чаёк','сосисочки','чаёк','кофе','кофе','кофе','молоко','кофе','яблоко','яблоко']
# breakfast_counter = Counter(breakfast)
# print(breakfast_counter)
# print(breakfast_counter.most_common(2))			# two elements
# lunch = ['кофе','кофе','кофе','молоко','яблоко','яблоко']
# lunch_counter = Counter(lunch)
# print(lunch_counter)
# print(breakfast_counter + lunch_counter)
# print(breakfast_counter - lunch_counter)
# print(breakfast_counter & lunch_counter)
# print(breakfast_counter | lunch_counter)

# def polindrom(word):					# закончил на 152 странице. скучно, пиздец. потом продолжу. 
# 	from collections import deque
# 	dq = deque(word)
# 	while len(dq) > 1:
# 		if dq.popleft() != dq.pop():
# 			return False
# 		return True
# print(polindrom('rar'))

# from pprint import pprint
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
# pprint(person)



# CLASSES

# class Person():
# 	def __init__(self, name):
# 		self.name = name

# hunter = Person('Elmer Fudd')
# print(hunter.name)

# class pickle():
# 	def mmm(self):
# 		print('I\'m pickle Rick!')
# class rick(pickle):
# 	def mmm(self):
# 		print('mmmm, pickle...')
# gimicar = pickle()
# gimiyogo = rick()
# gimicar.mmm()
# gimiyogo.mmm()

# class pickle():
# 	def mmm(self):
# 		print('I\'m pickle Rick!')
# class rick(pickle):
# 	def mmm(self):
# 		print('mmmm, pickle...')
# 	def change(self):
# 		print('sorry I can\'t go with you')
# gimicar = pickle()
# gimiyogo = rick()
# gimicar.mmm()
# gimiyogo.mmm()
# gimiyogo.change()
# ##### pickle.mmm(gimicar)

# class Person():
# 	def __init__(self, name):
# 		self.name = name
# class MDPerson(Person):
# 	def __init__(self, name):				# it calls перегрузка метода
# 		self.name = 'Doctor ' + name
# class JDPerson(Person):
# 	def __init__(self, name):				# it calls перегрузка метода
# 		self.name = name + ' advakat'
# first = Person('Olejka')
# second = MDPerson('House')
# third = JDPerson('Judie Holps')
# print(first.name)
# print(second.name)
# print(third.name)

# class EmailPerson(Person):
# 	def __init__(self, name, email):
# 		super().__init__(name)
# 		self.email = email
# user = EmailPerson('Bob Morlie', 'bob@gmail.com')
# print(user.name)
# print(user.email)


# class Duck():
# 	def __init__(self,input_name):
# 		self.hidden_name = input_name
# 	def get_name(self):
# 		print('inside the getter')
# 		return self.hidden_name
# 	def set_name(self, input_name):
# 		print('inside the setter')
# 		self.hidden_name = input_name
# 	name = property(get_name, set_name)

# x = Duck('NNAAMMEE')
# print(x.name())

# nums = [11,22,33,44,55]
# res = list(map(lambda x: x+5, nums))
# print(res)

# def countdown():
# 	i = 5
# 	while i>0:
# 		yield i
# 		i -= 1
# for i in countdown():
# 	print(i)
# print(i)

# def numbers(x):
# 	for i in range(x):
# 		if i%2 == 0:
# 			yield i
# print(list(numbers(11)))

# def decor(func):
# 	def wrap():
# 		print('_____________________________')
# 		func()
# 		print('-----------------------------')
# 	return wrap
# @decor
# def print_text():
# 	print('Hello, World!')
# # def print_text():
# # 	print('Hello, World!')
# # decorated = decor(print_text)
# print_text()
# # decorated()

# def factorial(x):
# 	if x == 1:
# 		return 1
# 	else: 
# 		return x*factorial(x-1)

# def is_even(x):
# 	if x == 0:
# 		return True
# 	else: 
# 		return is_odd(x-1)
# def is_odd(x):
# 	return not is_even(x)

# 	fib(3)								 + fib(2)
# 	fib(2) 				+ fib(1)		fib(1) + fib(0)
# 	fib(1) 	+ fib(0)

# a = {1,2,3,4,5,6,}
# b = {4,5,6,7,8,9,}

# print(a|b)
# print(a&b)
# print(a-b)
# print(b-a)
# print(a^b)

# from itertools import count
# for i in count(4, 2):
# 	print(i)
# 	if i > 20:
# 		break

# from itertools import cycle
# # for i in 'python':
# # 	print(i)
# step = 0
# for i in cycle('python'):
# 	print(i)
# 	if step == 20:
# 		break
# 	step += 1

# from itertools import accumulate, takewhile
# nums = list(accumulate(range(8)))			# accumulate([1,2,3,4,5]) -> [1,3,6,10,15]
# print(nums)
# print(list(takewhile(lambda x: x<=6, nums))) 	# takewhile отличается от filter наличием брейка. 

# реализуйте класс для сохранения рядкив и роботы с ними. каждый объект класса должен как-то

# from itertools import product, permutations
# letters = ('a', 'b')
# qwe = ['12','qq','ww',12,32]
# print(list(product(letters, qwe, range(2))))
# print(list(permutations(letters)))

# class Cat:
# 	def __init__(self, color, legs):		# __init__ вызывается, когда создаётся экземпляр. считается конструктором
# 		self.color = color
# 		self.legs = legs
# felix = Cat('ginder', 4)
# rover = Cat('dog-colored', 4)
# stumpy = Cat('brown', 3)
# for attribute, value in felix.__dict__.items():
#     print(attribute, value)

# class Animal:
# 	def __init__(self, name, color):
# 		self.name = name
# 		self.color = color
# class Cat(Animal):
# 	def purr(self):
# 		print('purr')
# class Dog(Animal):
# 	def bark(self):
# 		print('Woof!')
# fido = Dog('Fido','brown')
# print(fido.color)
# fido.bark()

# class Wolf:
# 	def __init__(self, name, color):
# 		self.name = name 
# 		self.color = color
# 	def bark(self):
# 		print('Grrr')
# class Dog(Wolf):
# 	def bark(self):
# 		print('Woof')
# husky = Dog('Max', 'black')
# husky.bark()

# class A:
# 	def one(self):
# 		print('AAAA')
# class B(A):
# 	def two(self):
# 		print('BBBBB')
# class C(B):
# 	def three(self):
# 		print('CCCC')
# c = C()
# c.one()
# c.two()
# c.three()

# class A:
# 	def spam(self):
# 		print(1)
# class B(A):
# 	def spam(self):
# 		print(2)
# 	def superspam(self):
# 		super().spam()
# B().spam()
# B().superspam()

# class Vector:
# 	def __init__(self,x,y):
# 		self.x = x
# 		self.y = y
# 	def __add__(self, other):				# add привязан к +, 
# 		return Vector(self.x + other.x, self.y + other.y)
# 	def __sub__(self,other):				# sub привязан к -. Возвращать они могут что угодно
# 		return Vector(self.x - other.x, self.y - other.y)
		# <  def __lt__(self):	lower than						# *  def __mul__(self): 
		# <= def __lt__(self):	lower equal						# /  def __truediv__(self):
		# == def __lt__(self):	equal							# // def __floordiv__(self):
		# != def __lt__(self):	not equal						# %  def __mod__(self):
		# >  def __lt__(self):	greater than					# ** def __pow__(self):
		# >= def __lt__(self):	greater equal					# &  def __and__(self):
																# ^  def __xor__(self):
																# |  def __or__(self):
# __len__  -  len();	__getitem__  -  для индексации;	__setitem__  -  для присваивания значения индексируемому элементу
# __delitem__  -  для удаления индексируемого элемента;	__iter__  -  для перебора объектов (в циклах for, например)
# __contains__  -  для in;	__call__;  __int__;  __str__; 

# firstvecx = int(input('firstvecx: '))
# firstvecy = int(input('firstvecy: '))
# seconvecx = int(input('seconvecx: '))
# seconvecy = int(input('seconvecy: '))
# firstvec = Vector(firstvecx, firstvecy)
# seconvec = Vector(seconvecx, seconvecy)
# plus  = firstvec + seconvec
# minus = firstvec - seconvec
# print(plus.x)
# print(plus.y)
# print(minus.x)
# print(minus.y)

# class Special:
# 	def __init__(self,cont):
# 		self.cont = cont
# 	def __truediv__(self, other):
# 		line = '='*len(other.cont)
# 		return '\n'.join([self.cont, line, other.cont])
# spam = Special('spam')
# hello = Special('Hello, World!')
# print(spam/hello)

# class Special:					# что вообще происходит в этом класса? 
# 	def __init__(self, cont):		# неплохо было бы понять, но сейчас это слишком сложно...
# 		self.cont = cont
# 	def __gt__(self,other):
# 		for index in range(len(other.cont)+1):
# 			result = other.cont[:index] + '>' + self.cont
# 			result += '>' + other.cont[index:]
# 			print(result)
# spam = Special('spam')
# eggs = Special('eggs')
# spam>eggs

# import random
# class VagueList:
# 	def __init__(self, cont):
# 		self.cont = cont
# 	def __getitem__(self, index):
# 		return self.cont[index + random.randint(-1,1)]
# 	def __len__(self):
# 		return random.randint(0, len(self.cont)*2)
# vague_list = VagueList(['q','w','e','r','t','y'])
# print(len(vague_list))
# print(len(vague_list))
# print(vague_list[2])
# print(vague_list[2])


#### class GameObject:
####     class_name = ""
####     desc = ""
####     objects = {}
####     def __init__(self, name):
####         self.name = name
####         GameObject.objects[self.class_name] = self
####     def get_desc(self):
####         return self.class_name + "\n" + self.desc
#### class Goblin(GameObject):
####     def __init__(self, name):
####         self.class_name = "goblin"
####         self.health = 3
####         self._desc = "A foul creature"
####         super().__init__(name)
####     @property
####     def desc(self):
####         if self.health >= 3:
####             return self._desc
####         elif self.health == 2:
####             health_line = "It has a wound on its knee."
####         elif self.health == 1:
####             health_line = "Its left arm has been cut off!"
####         elif self.health <= 0:
####             health_line = "It is dead."
####         return self._desc + "\n" + health_line
####     @desc.setter
####     def desc(self, value):
####         self._desc = value
#### goblin = Goblin("Gobbly")
#### def hit(noun):
####     if noun in GameObject.objects:
####         thing = GameObject.objects[noun]
####         if type(thing) == Goblin:
####             thing.health -= 1
####             if thing.health <= 0:
####                 msg = "You killed the goblin!"
####             else:
####                 msg = "You hit the {}".format(thing.class_name)
####     else:
####         msg = "There is no {} here.".format(noun)
####     return msg
#### def examine(noun):
####     if noun in GameObject.objects:
####         return GameObject.objects[noun].get_desc()
####     else:
####         return "There is no {} here.".format(noun)
#### def get_input():
####     command = input(": ").split()
####     verb_word = command[0]
####     if verb_word in verb_dict:
####         verb = verb_dict[verb_word]
####     else:
####         print("Unknown verb {}".format(verb_word))
####         return
####     if len(command) >= 2:
####         noun_word = command[1]
####         print(verb(noun_word))
####     else:
####         print(verb("nothing"))
#### def say(noun):
####     return 'You said "{}"'.format(noun)
#### verb_dict = {
####     "say": say,
####     "examine": examine,
####     "hit": hit
#### }
#### while True:
####     get_input()



# class Class1:         # Базовый класс для класса Class2
#     def f_func1(self):
#         print("Метод f_func1() класса Class1")
 
# class Class2(Class1): # Класс Class2 наследует класс Class1
#     def f_func2(self):
#         print("Метод f_func2() класса Class2")
 
# class Class3(Class1): # Класс Class3 наследует класс Class1
#     def f_func1(self):
#         print("Метод f_func1() класса Class3")
#     def f_func2(self):
#         print("Метод f_func2() класса Class3")
#     def f_func3(self):
#         print("Метод f_func3() класса Class3")
#     def f_func4(self):
#         print("Метод f_func4() класса Class3")
 
# class Class4(Class2, Class3): # Множественное наследование
#     def f_func4(self):
#         print("Метод f_func4() класса Class4")
# c1 = Class4()             # Создаем экземпляр класса Class4
# c1.f_func1()              # Выведет: Метод f_func1() класса Class1
# c1.f_func2()              # Выведет: Метод f_func2() класса Class2
# c1.f_func3()              # Выведет: Метод f_func3() класса Class3
# c1.f_func4()




