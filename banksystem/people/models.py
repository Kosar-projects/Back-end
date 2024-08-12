from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validator_length(value):
    if len(str(value)) <10 or len(str(value))>10 :
        raise ValidationError("national id must be 10 digit")
 
class People(models.Model):
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=256)
    national_id=models.BigIntegerField(validators=[validator_length])


