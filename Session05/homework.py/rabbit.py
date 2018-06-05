adult_pair = 1
kid_pair = 0
for i in range (10):
    total = kid_pair + adult_pair
    kid_pair = adult_pair
    adult_pair = total
    print ("Month",i,":",total,"pair(s) of rabbit")