from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('filter/', account_filter),
    path('group/', account_group),
    path('new/', account_create),
    path('<int:id>/recommend', account_recommend),
    path('<int:id>/suggest', account_suggest),
    path('<int:id>/', account_update),
    path('likes/', account_likes)
]
