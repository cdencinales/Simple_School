from django.urls import path
from account.api.views import(

    registration_view,
)


app_name = 'account'

urlpatterns = [
    path('register', registration_view, name='register'),
]

#to enter the registration 'page' in the browser follow your ip plus the developer server port (normally 8000) followed by the path: /api/account/register
#example of the url: http://127.0.0.1:8000/api/account/register