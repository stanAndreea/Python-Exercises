#homework ex1
shop = [(x,y) for x in ['shirt',' scarf',' glove',' heat'] for y in ['S','M','L','XL','XXL']]*100
shop.pop()
shop.remove(('shirt', 'M'))
shop += [('shirt', 'M')]
