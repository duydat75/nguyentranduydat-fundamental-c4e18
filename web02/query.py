from models.service import Service
import mlab


mlab.connect()

all_service = Service.objects()
first_service = all_service [0]



print (first_service.name)
