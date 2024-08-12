import random
from faker import Faker
from account.models import Account 
from people.models import People 

# the dunctions below create random records for the database
def create_20t_record():
    fake = Faker()
    i=0
    people_data = []
    for i in range(0,20000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        national_id = (random.randint(1000000000, 9999999999))
        people_data.append(People(first_name=first_name, last_name=last_name, national_id=national_id))

    People.objects.bulk_create(people_data)
    k=0
    all_people = list(People.objects.all())
    bank_account_data = []
    for k in range(0,20000):
        owner = random.choice(all_people) 
        id_account = random.randint(1000, 999999)
        stock = random.randint(80000, 9999999999)
        bank_account_data.append(Account(owner=owner, id_account=id_account, stock=stock))
    print("done")
    Account.objects.bulk_create(bank_account_data)


def create_10m_record():
    fake = Faker()
    i=0
    people_data = []
    for i in range(0,1000000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        national_id = (random.randint(1000000000, 9999999999))
        people_data.append(People(first_name=first_name, last_name=last_name, national_id=national_id))

    People.objects.bulk_create(people_data)
    print("done")
    k=0
    all_people = list(People.objects.all())
    bank_account_data = []
    for k in range(0,1500000):
        owner = random.choice(all_people)
        id_account = random.randint(10000, 11100000)
        stock = random.randint(80000, 3000000)
        bank_account_data.append(Account(owner=owner, id_account=id_account, stock=stock))

    Account.objects.bulk_create(bank_account_data)
    print("done")
