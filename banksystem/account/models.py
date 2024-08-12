from django.db import models

# Create your models here.
# the stock field can be with index and without it 
class Account(models.Model):
    owner=models.ForeignKey(to='people.People',on_delete=models.CASCADE,null=True)
    id_account=models.IntegerField()
    # stock=models.BigIntegerField(db_index=True)
    stock=models.BigIntegerField()