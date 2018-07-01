from models.service import Service
import mlab
from faker import Faker
from random import  randint, choice

mlab.connect()

fake = Faker()

for i in range (1):
    print ("Saving Service", i+1,"."*20)
    new_service = Service(
        name = fake.name(),
        yob = randint (1998,2002),
        gender = randint(0,1),
        height = randint(155,190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice ([True,False])
    )

    new_service.save()

# print (fake.profile())