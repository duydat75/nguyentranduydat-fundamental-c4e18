import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient (mongo_uri)
db = client.get_default_database()
customers = db['customers']

wom = customers.find({"ref":"wom"}).count()
events = customers.find({"ref":"events"}).count()
ads = customers.find({"ref":"ads"}).count() 

labels = ['wom','events','ads']
values = [wom,events,ads]
explode = [0.02,0.02,0.02]
colors = ['blue','red','yellow']

print ('Customers are acquired from wom:' ,wom,
        '\nCustomers are acquired from events:' ,events,
        '\nCustomers are acquired from ads:',ads)

pyplot.title('Customers group by references')
pyplot.pie(values,
            labels=labels,
            explode=explode,
            colors=colors,
            autopct='%1.1f%%',
            shadow=True)
pyplot.axis ("equal")
pyplot.show()