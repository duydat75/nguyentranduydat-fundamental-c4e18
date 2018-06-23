from models.service import Service
import mlab


mlab.connect()

all_service = Service.objects()


### SEARCH BY ID
obj = all_service.get(id='5b2ba53ac0bfbc05f2fc9916')

### DELETE DOCUMENT
obj.delete()
