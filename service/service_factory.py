from abc import ABC
from .models import *
from .exceptions import RecordExistsException


class ServiceFactory(ABC):
    @staticmethod
    def create_account(body=None):
        account, created = Account.objects.get_or_create(**body)
        if created:
            return account
        raise RecordExistsException('account already exists')

    @staticmethod
    def add_interests(account, interests):
        for interest in interests:
            interest_object = AccountInterest(**interest)
            interest_object.account = account
            interest_object.save()

    @staticmethod
    def add_likes(account_id, likes):
        for like in likes:
            lk = AccountSympathy()
            lk.liker = account_id
            lk.likee = like['id']
            lk.ts = like['dt']
            lk.save()

    @staticmethod
    def add_subscribe(account, subscribe):
        subscribe_object = AccountSubscription(**subscribe)
        subscribe_object.account = account
        subscribe_object.save()
