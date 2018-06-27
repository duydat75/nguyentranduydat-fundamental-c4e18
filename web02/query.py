from models.service import Service
import mlab


mlab.connect()

all_service = Service.objects()
first_service = all_service [0]

service = all_service.get(id='5b2ba803c0bfbc077255a97c')
#service = Service.objects().with_id(service)

# print (service.to_mongo())

if service is not None:
    # service.delete()
    # print ("deleted")
    print (service.yob)
    service.update(set__yob = 2001)
    service.reload()
    print (service.yob)
else:
    print ('Service not found')