from rest_framework import status, request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from journal.models import Journal
from account.models import Account
from journal.api.serializers import JournalSerializer

@api_view(['GET', ])
def api_detail_journal_view(request, slug):
    try:
        journal = journal.objects.get(slug=slug)
    except journal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = JournalSerializer(journal)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_update_journal_view(request, slug):
    try:
        journal = journal.objects.get(slug=slug)
    except journal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = JournalSerializer(journal, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_journal_view(request, slug):
    try:
        journal = journal.objects.get(slug=slug)
    except journal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        operation = journal.delete()
        data = {}
        if operation:
            data['succes'] = 'delete successful'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)

@api_view(['POST', ])
def api_create_journal_view(request):
    account = Account.objects.get(pk=1)
    journal = Journal(author=account)

    if request.method == 'POST':
        serializer = JournalSerializer(journal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
