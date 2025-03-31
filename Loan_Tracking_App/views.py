from rest_framework.viewsets import ModelViewSet
from .models import loan_record
from .serializer import LoanRecordSerializer

class LoanRecordViewSet(ModelViewSet):
    queryset = loan_record.objects.all()
    serializer_class = LoanRecordSerializer