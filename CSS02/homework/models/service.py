from mongoengine import *







class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    description = StringField()
    measurements = StringField()
    avatar = StringField()