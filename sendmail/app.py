from apscheduler.schedulers.blocking import BlockingScheduler
import mlab
from models.lover import Lover
from gmail import *
from datetime import datetime  
from datetime import timedelta  

mlab.connect()

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print("a")
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

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()