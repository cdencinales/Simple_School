from rest_framework import serializers
from journal.models import Journal


class JournalSerializer(serializers.ModelSerializer):
    model = Journal
    fields = ['header', 'body', 'user', 'time_stamp']
