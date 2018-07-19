from models.user import User
from models.lover import Lover
from datetime import datetime  
from datetime import timedelta  
from gmail import *
import mlab
mlab.connect()

all_lover = Lover.objects()
now = datetime.now()
for item in all_lover:
    if (now.month - item.date.month) == 0:
        if (now.day - item.date.day) == -1:
            email = item.user_id.email
            name = item.fullname
            gmail=GMail('nguyenduydat1027@gmail.com','dat12345678')
            html = "<p>Ng&agrave;y mai l&agrave; sinh nhật của&nbsp{{name}}</p>"
            html_content = html.replace("{{name}}", name)
            msg=Message('Nhắc nhở sinh nhật của người yêu',to=email, html=html_content)
            gmail.send(msg)
    
