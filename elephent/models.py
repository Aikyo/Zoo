from django.db import models

# Create your models here.

class UserInfo(models.Model):

    user_type_choices = (
        (1,'普通用户'),
        (2,'supervisor')
    )

    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo',on_delete=True)
    token = models.CharField(max_length=64)



class Order(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    describe = models.CharField(max_length=100)


