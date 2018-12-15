from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=100, unique=True)
    fname = models.CharField(max_length=50, default=None)
    sname = models.CharField(max_length=50, default=None)
    phone = models.CharField(max_length=16, default=None)
    sex = models.CharField(max_length=1)
    birth = models.BigIntegerField(default=0)
    country = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    joined = models.BigIntegerField(default=0)
    status = models.CharField(max_length=20)


class Subscription(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    start = models.BigIntegerField()
    finish = models.BigIntegerField()


class Sympathy(models.Model):
    liker = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sympathy_liker_account')
    likee = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sympathy_likee_account')
    ts = models.BigIntegerField()


class Interest(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
