from django.contrib import admin

from .models import *

admin.site.register(Account)
admin.site.register(AccountSubscription)
admin.site.register(AccountSympathy)
admin.site.register(AccountInterest)

