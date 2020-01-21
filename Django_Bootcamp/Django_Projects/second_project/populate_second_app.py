import os
os.environ.setdefault('Django_Settings_Module','second_project.settings')

import django
django.setup()

import random
from second_app.models import UserInfo
from faker import Faker

fakegen = Faker()

def populate(N=3):

    for entry in range(N):
        fake_full = fakegen.name().split()
        fake_fn = fake_full[0]
        fake_ln = fake_full[1]
        fake_email = fakegen.email()

        user = UserInfo.objects.get_or_create(first_name=fake_fn,last_name=fake_ln,email=fake_email)[0]

if __name__ == '__main__':
    print("Populating Script!")
    populate(20);
    print("Population Complete.")
