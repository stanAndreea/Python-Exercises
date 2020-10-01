#homework ex1
shop = [(x,y) for x in ['shirt',' scarf',' glove',' heat'] for y in ['S','M','L','XL','XXL']]*100
shop.pop()
shop.remove(('shirt', 'M'))
shop += [('shirt', 'M')]

#homework ex2 
tuplex = "h", 10, "o", "m", "e", "w", "o", "r", "k"
positivion = 1
tuplex = tuplex[ : positivion ] + tuplex[positivion+1 : ]
