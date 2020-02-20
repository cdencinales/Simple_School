from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.api.urls', 'account_api')),
]

#to enter the registration 'page' in the browser follow your ip plus the developer server port (normally 8000) followed by the path: /api/account/register
#example of the url: http://127.0.0.1:8000/api/account/register