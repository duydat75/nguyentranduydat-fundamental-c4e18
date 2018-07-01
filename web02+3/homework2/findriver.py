
from models.river import River
import mlab1

mlab1.connect()

rivers = River.objects(continent = "Africa")
print ("All river in Africa")
for item in rivers:
    print(item.name)
    
print("-" * 20)
print ("All river in S.America with length less than 1000km")
short_river = River.objects(continent ="S. America",length__lt = 1000)
for item in short_river:
    print(item.name,':',item.length)
    

