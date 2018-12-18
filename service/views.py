from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .service_factory import ServiceFactory
import json


def account_filter(request):
    return JsonResponse({}, safe=False)


def account_group(request):
    return HttpResponse('Account group endpoint')


def account_recommend(request, id):
    return HttpResponse('Account recommend endpoint: %s' % id)


def account_suggest(request, id):
    return HttpResponse('Account suggest endpoint: %s' % id)


@csrf_exempt
def account_create(request):
    body = json.loads(request.body.decode('utf-8'))

    interests = body.pop('interests', [])
    premium = body.pop('premium', [])
    likes = body.pop('likes', [])

    try:
        account = ServiceFactory.create_account(body)
        ServiceFactory.add_interests(account, interests)
        ServiceFactory.add_likes(account.pk, likes)
        ServiceFactory.add_subscribe(account, premium)
        return JsonResponse({}, safe=False, status=201)
    except Exception as e:
        print(e)
        return JsonResponse({}, safe=False, status=400)




def account_update(request, id):
    return HttpResponse('Account update endpoint: %s' % id)


def account_likes(request):
    return HttpResponse('Account likes endpoint')
