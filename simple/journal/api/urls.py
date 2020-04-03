from django.urls import path

from journal.api.views import (
    api_detail_journal_view,
    api_update_journal_view,
    api_delete_journal_view,
    api_create_journal_view,
)
app_name = 'journal'

urlpatterns = [
    path('<slug>/', api_detail_journal_view, name='detail'),
    path('<slug>/update/', api_update_journal_view, name='update'),
    path('<slug>/delete/', api_delete_journal_view, name='delete'),
    path('create/', api_create_journal_view, name='create'),
]