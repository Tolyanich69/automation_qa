import random

from data.data import Person, Color, Date
from faker import Faker

faker_ua = Faker("uk_UA")
faker_en = Faker("En")

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
        mobile_number = faker_ua.msisdn(),
    )

def generated_file():
    path = rf"D:\pythonProject\automation_qa\file_test{random.randint(1,110)}.txt"
    file =open(path, "w+")
    file.write(f"Hello world {random.randint(1, 99)}")
    file.close()
    return file.name, path

def generated_color():
    yield Color(
        color_name = ["red", "Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )

def generated_date():
    yield Date(
        year = faker_en.year(),
        month = faker_en.month_name(),
        day = faker_en.day_of_month(),
        time = "12:00",
    )
