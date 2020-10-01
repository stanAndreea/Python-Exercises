#homework ex1
shop = [(x,y) for x in ['shirt',' scarf',' glove',' heat'] for y in ['S','M','L','XL','XXL']]*100
shop.pop()
shop.remove(('shirt', 'M'))
shop += [('shirt', 'M')]

#homework ex2 
tuplex = "h", 10, "o", "m", "e", "w", "o", "r", "k"
positivion = 1
tuplex = tuplex[ : positivion ] + tuplex[positivion+1 : ]

#homework ex3 
listx = [(x, y) for x in [1,2,3] for y in [4,5,6]]
listx[-1] = 'last'


#homework ex4
slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']
stringList = [i for i in slist if isinstance(i, str)]


#homework ex5

