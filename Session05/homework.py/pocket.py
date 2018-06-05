backpack = ['xylophone', 'dagger', 'bedroll', 'bread loaf']
pouch = ['flint', 'twine', 'gemstone']
inventory = {
    'gold':500,
    'backpack':backpack,
    'pouch':pouch
}
print (inventory)
inventory['pocket']=['seashell', 'strange berry','lint']
print(inventory)
backpack.remove ('dagger')
print (inventory)
inventory['gold']+=50
print(inventory)