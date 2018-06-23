from mongoengine import *

class Customer(Document):
    name = StringField()
    email = StringField()
    gender = IntField()
    job = StringField()
    phone = StringField()
    company = StringField()
    contracted = BooleanField()
    

