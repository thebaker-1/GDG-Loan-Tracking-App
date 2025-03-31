from rest_framework import serializers
from .models import loan_record

class LoanRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = loan_record
        fields = ['id', 'Name', 'Amount', 'Date', 'Reason']

