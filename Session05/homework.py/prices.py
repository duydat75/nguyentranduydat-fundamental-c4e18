total = 0
prices = {
    'banana':4,
    'apple':2,
    'orange':1.5,
    'pear':3
}
stock = {
    'banana':6,
    'apple':0,
    'orange':32,
    'pear':15
}
for i in prices:
    print (i)
    print ("Price:", prices[i])
    print ("Stock:", stock[i])
    print ("-"*20)
for i in prices:
    total += prices[i]*stock[i] 
print ("Total:",total)


