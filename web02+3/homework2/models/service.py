from mongoengine import *
import static






class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    description = StringField()
    measurements = StringField()
    avatar = FileField()