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
    def update_account(pk, body=None):
        return Account.objects.filter(pk=pk).update(**body)

    @staticmethod
    def add_account_interests(account, interests):
        AccountInterest.objects.bulk_create([{'label': label, 'account': account} for label in interests])

    @staticmethod
    def add_account_likes(account, likes):
        items = [{'liker': account.id, 'likee': like['id'], 'ts': like['dt']} for like in likes]
        ServiceFactory.bulk_create_likes(items)

    @staticmethod
    def bulk_create_likes(likes):
        AccountSympathy.objects.bulk_create([AccountSympathy(**like) for like in likes])

    @staticmethod
    def add_like(data):
        like, created = AccountSympathy.objects.get_or_create(**data)
        return created

    @staticmethod
    def add_account_subscribe(account, subscribe):
        subscribe_object = AccountSubscription(**subscribe)
        subscribe_object.account = account
        subscribe_object.save()
