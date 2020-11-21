from django.urls import path

from .views import *


urlpatterns = [
    path('v1/login', login, name='login'),
    path('v1/logout', Logout.as_view(), name='logout'),

    path('v1/registration', Registration.as_view(), name='registration'),
    path('v1/users_list', UserList.as_view(), name='users_list'),
]
