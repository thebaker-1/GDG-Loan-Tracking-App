from django.db import models

# Create your models here.
class loan_record(models.Model):
    Name = models.Charfield(max_length=100)
    Amount = models.IntegerField()
    Date = models.DateField()
    Reason = models.CharField(max_length=100)
    
