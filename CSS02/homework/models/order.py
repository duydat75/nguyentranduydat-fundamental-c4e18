from mongoengine import *
class Order(Document):
    service_id = StringField()
    service_name = StringField()
    user_id = StringField()
    user_name = StringField()
    is_accepted = BooleanField()
    time = StringField()