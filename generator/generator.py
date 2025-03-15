import random

from data.data import Person
from faker import Faker

faker_ua = Faker("uk_UA")

def generated_person():
    yield Person(
        full_name= faker_ua.first_name() + " " + faker_ua.last_name(),
        first_name= faker_ua.first_name(),
        last_name= faker_ua.last_name(),
        age= random.randint(10,80),
        salary= random.randint(1000, 5000),
        department= faker_ua.job(),
        email= faker_ua.email(),
        current_address= faker_ua.address(),
        permanent_address= faker_ua.address(),
    )
