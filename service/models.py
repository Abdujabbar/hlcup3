from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=100, unique=True)
    fname = models.CharField(max_length=50, blank=True)
    sname = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    sex = models.CharField(max_length=1)
    birth = models.BigIntegerField(default=0)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    joined = models.BigIntegerField(default=0)
    status = models.CharField(max_length=20)

    def __str__(self):
        return '%s - %s' % (self.id, (self.fname + ' ' + self.sname))


class AccountSubscription(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    start = models.BigIntegerField()
    finish = models.BigIntegerField()

    def __str__(self):
        return 'start: %s, finish: %s' % (self.start, self.finish)


class AccountSympathy(models.Model):
    liker = models.BigIntegerField()
    likee = models.BigIntegerField()
    ts = models.BigIntegerField()

    def __str__(self):
        return '%s - %s:%s' % (self.liker, self.likee, self.ts)


class AccountInterest(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)

    def __str__(self):
        return '%s: %s' % (self.account, self.label)
