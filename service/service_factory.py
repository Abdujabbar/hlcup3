from .models import *
from .exceptions import RecordExistsException
from django.db import transaction

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
    def create_account_with_relationships(body):
        interests = body.pop('interests', [])
        premium = body.pop('premium', {})
        likes = body.pop('likes', [])

        with transaction.atomic():
            account = ServiceFactory.create_account(body)
            ServiceFactory.add_account_interests(account, interests)
            ServiceFactory.add_account_likes(account, likes)
            ServiceFactory.add_account_subscribe(account, premium)

    @staticmethod
    def add_account_interests(account, interests):
        if len(interests) > 0:
            items = [AccountInterest(**{'label': label, 'account': account}) for label in interests]
            AccountInterest.objects.bulk_create(items)

    @staticmethod
    def add_account_likes(account, likes):
        if len(likes) > 0:
            items = [{'liker': account.pk, 'likee': like['id'], 'ts': like['ts']} for like in likes]
            ServiceFactory.bulk_create_likes(items)

    @staticmethod
    def bulk_create_likes(likes):
        if len(likes) > 0:
            AccountSympathy.objects.bulk_create([AccountSympathy(**like) for like in likes])

    @staticmethod
    def add_account_subscribe(account, subscribe):
        if len(subscribe) > 0:
            subscribe_object = AccountSubscription(**subscribe)
            subscribe_object.account = account
            subscribe_object.save()
