from django.db import models
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True) # by putting blank True we will not get error if we do not fill it
    phone = models.CharField(max_length= 20)
    email = models.CharField(max_length= 50)
    is_mvp =  models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now , blank= True)

    def __str__(self):
        return self.name