# len() 
# x = [1,3,4,7,82,5]
# print(len(x))

# split() 
# x = 'qwe, asd, zxc'
# print(x.split())
# a,b,c = x.split()
# print(a,b,c)

# join() 
# x = ['qwe','asd','zxc']
# y = '*'
# print(y.join(x))

# x.startswith() 
# x = 'Hellom'
# print(x.startswith('Hel'))

# x.endswith() 
# x = 'Hellom'
# print(x.endswith('om'))

# x.find() 
# x = 'Hello, suka'
# print(x.find('s'))

# x.rfind() #The method rfind() returns the last index where the substring str is found, or -1 if no such index exists, optionally restricting the search to string[beg:end]
# x = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod'
# print(x.rfind('e', 0, len(x)))

# x.count() 
# x = [1,2,3,5,2,4,4,3,4,5,5,6,6,4,2,3,6,7,9,]
# print(x.count(4))

# x.isalnum() #chack only str
# x = '12334325245'
# print(x.isalnum())

# x.strip() 
# x = '**QWEQWEQWE*****'
# print(x.strip('*'))

# x.title() 
# x = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod'
# print(x.title())

# x.upper() 
# x = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod'
# print(x.upper())

# x.lower() 
# x = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod'
# print(x.lower())

# x.swapcase() 
# x = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod'
# print(x.swapcase())

# x.center() #return with spaces ( )
# x = 'sed do eiusmod'
# print(x.center(50))

# x.ljust() 
# x = 'sed do eiusmod'
# print(x.center(50))

# x.rjust() 
# x = 'sed do eiusmod'
# print(x.center(50))

# x.replace() 
# print('Hello, Petr!'.replace('Petr', 'Alex'))

# x.append() 
# x = [12,3,32,5]
# x.append(53)
# print(x)

# x.extend() 
# x = [12,3,32,5]
# x.extend([123,321,534,674,234])
# print(x)

# x.insert() 
# x = [12,3,32,5]
# x.insert(2, 53)
# print(x)

# x.remove() #can return error!!!
# x = [12,3,32,5]
# x.remove(3)
# print(x)

# x.pop() 
# x = [12,3,32,5]
# x.pop()
# print(x)

# x.index() 
# x = [12,3,32,5]
# print(x.index(3))

# f=sorted(s) #sorted doesn't change a list!
# x = [12,3,32,5]
# print(sorted(x))
# print(x)

# x.sort(reverse=True) 
# x = [12,3,32,5]
# x.sort(reverse=True)
# print(x)

# x.reverse()
# x = [1,2,4,5,6,7,8]
# print(x.reverse()) 		works even in print
# print(x)

# del something

# ferst = ('qe', 'asd', 'fjfjf')
# first = 'cat'
# s=list(first) 

# s=f[:] s=f.copy() 
# first = ['qwe',';kl','ghj','try','zxc','asd']
# sec = first.copy()

# x.__sizeof__()
# x = [32.45,234,746,432,43]
# print(x.__sizeof__())