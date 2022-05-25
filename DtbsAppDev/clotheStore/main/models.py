from django.db import models


# Create your models here.
class callBack(models.Model):
    name_call = models.CharField('name_call', max_length=100)
    number = models.CharField('number', max_length=100)
    email_call = models.CharField('email_call', max_length=100)
    message = models.CharField('message', max_length=150)

    def __str__(self):
        return self.name_call
