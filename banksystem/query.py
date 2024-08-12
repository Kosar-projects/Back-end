
from account.models import Account 
from people.models import People 
import os
from django.db.models import F
from django.db.models import Sum
from django.db.models import Q
import random
import time
# first we call the function in the create_database.py to create 20_000 record using bulk create

# query1
# this function print the owner of each account and the stock in the txt file
def info_print():
    file_path='query_1_output.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
    accounts=Account.objects.all()
    with open(file_path, 'w') as f:
        for account in accounts:
            the_owner=account.owner
            the_stock=account.stock
            f.write(f"Name: {the_owner.first_name} {the_owner.last_name}\n")
            f.write(f"Account Stock: {the_stock}\n\n")

# query2
# this function sort the accounts in descending order by their stock and then we choose first element
def print_max_stock():
    file_path='query_2_output.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
    max_Stock=Account.objects.order_by('-stock').first()
    with open(file_path, 'w') as f:
        f.write(f"Name: {max_Stock.owner.first_name} {max_Stock.owner.last_name}\n")
        f.write(f"Account Stock: {max_Stock.stock}\n\n")

# query3
# this function sort the accounts in ascending order by stock and return the first 5 element
def print_5_lowest_stock():
    lowest_stock=Account.objects.order_by('stock')[:5]
    file_path='query_3_output.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as f:
        for account in lowest_stock:
            f.write(f"Name:{account.owner.first_name} {account.owner.last_name}\n")
            f.write(f"Account Stock:{account.stock}\n\n")

# query4
# this function first randomely choode two accounts and then randomely choose value for transfering base on the source account
# then we drop the money from source account and add it to the target account
# we save all the info before and after transfer in txt file
def move_money_between_accounts():
    accounts=Account.objects.order_by('?')[:2]
    source_acc=accounts[0]
    target_acc=accounts[1]
    source_amount=source_acc.stock
    file_path='query_4_output.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as f:
        f.write(f'the source: {source_acc.owner.first_name} {source_acc.owner.last_name}\n')
        f.write(f'the amount before transfer: {source_acc.stock}\n')
        f.write(f'the target: {target_acc.owner.first_name} {target_acc.owner.last_name}\n')
        f.write(f'the amount before transfer: {target_acc.stock}\n\n')
        transfer_amount=random.randint(8000,source_amount)
        f.write (f'the amount of transfer: {transfer_amount}\n\n')
        source_acc.stock-=transfer_amount
        source_acc.save()
        target_acc.stock+=transfer_amount
        target_acc.save()
        f.write(f'the source: {source_acc.owner.first_name} {source_acc.owner.last_name}\n')
        f.write(f'the amount after transfer: {source_acc.stock}\n')
        f.write(f'the target: {target_acc.owner.first_name} {target_acc.owner.last_name}\n')
        f.write(f'the amount after transfer: {target_acc.stock}\n\n')

# query5
# this function find the accounts that their id is greater than their stock
def account_id_greater_stock():
    the_choosen_ones=Account.objects.filter(id_account__gt=F('stock'))
    file_path='query_5_output.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as f:
        for account in the_choosen_ones:
            f.write(f"Name:{account.owner.first_name} {account.owner.last_name}\n")
            f.write(f"Account Stock:{account.stock} and Account id: {account.id_account}\n\n")

# query6
# this function first reach the owner of each account and then find the national id of the owner
# then it chooses the ones that the national id is greater than stock
def id_greater_than_stock():
    the_choosen_ones=Account.objects.filter(owner__national_id__gt=F('stock'))
    file_path='query_6_output.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as f:
        for account in the_choosen_ones:
            f.write(f"Name:{account.owner.first_name} {account.owner.last_name}\n")
            f.write(f"Account Stock:{account.stock} and Account owner national_id: {account.owner.national_id}\n\n")


# from here the number of the records raise to 1_million people and 1_500_000 accounts
# since I use the virtual machine i couldnt afford generating 10_million record

# query7_1
# in this function we dont have index and use the query to find the accounts that have more than 2 million or less than 1 million
def without_index_stock_limitation():
    file_path='query_7_without_index_output.txt'
    start_time=time.time()
    accounts=Account.objects.filter(
        Q(stock__gt=2000000) | Q(stock__lt=1000000)
    )
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as f:
        for account in accounts:
            f.write(f"Name:{account.owner.first_name} {account.owner.last_name}\n")
        end_time=time.time()
        passed_time=end_time-start_time
        f.write (f'the taken time: {passed_time}')
        print(passed_time)


# query7_2
# in this function we add the index so we apply the same query to see the time difference
def with_index_stock_limitation():
    start_time=time.time()
    accounts=Account.objects.filter(
        Q(stock__gt=2000000) | Q(stock__lt=1000000)
    )
    file_path='query_7_with_index_output.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as f:
        for account in accounts:
            f.write(f"Name:{account.owner.first_name} {account.owner.last_name}\n")
        end_time=time.time()
        passed_time=end_time-start_time
        f.write (f'the taken time: {passed_time}')
        print(passed_time)
#both functions print the taken time at the end of txt file
# the time differnece : 3.1547

# query8
# in this function we calculate the total stock for each person 
def all_money_among_accounts():
    file_path='query_8_output.txt'
    total_stock_per_person=Account.objects.values('owner__first_name','owner__last_name').annotate(total_stock=Sum('stock'))
    with open(file_path, 'w') as f:
        for account in total_stock_per_person:
            f.write(f"Name: {account['owner__first_name']} {account['owner__last_name']}\n")
            f.write(f"total_Stock: {account['total_stock']}\n\n")