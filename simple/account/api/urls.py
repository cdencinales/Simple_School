from django.urls import path, include
from account.api.views import(
    registration_view,
)
from rest_framework import routers
from account.api.views import *


app_name = 'account'
#(note for dan) consider moving the router from within api/urls.py to its own file within the api app.
router = routers.DefaultRouter()
router.register('', AccountViewSet)

urlpatterns = [
    path('register', registration_view, name='register'),
]

#to enter the registration 'page' in the browser follow your ip plus the developer server port (normally 8000) followed by the path: /api/account/register
#example of the url: http://127.0.0.1:8000/api/account/register