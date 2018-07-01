from models.user import User
from models.order import Order
from models.service import Service
import mlab


mlab.connect()
order = Order.objects()
all_user = User.objects()
all_service = Service.objects()
for item in order:
    service = all_service.get(id = item.service_id).name
    user = all_user.get(id = item.user_id).fullname
    time = item.time
    print (service,time)

