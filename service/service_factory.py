from .models import *
from .exceptions import RecordExistsException


class ServiceFactory(object):
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
        items = [AccountInterest(**{'label': label, 'account': account}) for label in interests]
        AccountInterest.objects.bulk_create(items)

    @staticmethod
    def add_account_likes(account, likes):
        items = [{'liker': account.pk, 'likee': like['id'], 'ts': like['dt']} for like in likes]
        ServiceFactory.bulk_create_likes(items)

    @staticmethod
    def bulk_create_likes(likes):
        AccountSympathy.objects.bulk_create([AccountSympathy(**like) for like in likes])

    @staticmethod
    def add_account_subscribe(account, subscribe):
        subscribe_object = AccountSubscription(**subscribe)
        subscribe_object.account = account
        subscribe_object.save()
