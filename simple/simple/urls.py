from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.api.urls', 'account_api')),
    path('api/account/', include('rest_framework.urls')),
    url(r'^about', TemplateView.as_view(template_name='simple/about.html')) 

]

#to enter the registration 'page' in the browser follow your ip plus the developer server port (normally 8000) followed by the path: /api/account/register
#example of the url: http://127.0.0.1:8000/api/account/register