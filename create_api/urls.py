from django.urls import path
from .views import greet_user, process_form, fetch_jokes


urlpatterns=[
    path('greet/', greet_user, name='greet_users'),
    path('process_form/', process_form , name='process_form'),
    path('fetch_jokes/', fetch_jokes, name='fetch_jokes'),
]

