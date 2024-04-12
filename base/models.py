from django.db import models

# Create your models here.
""" class DocumentScore(models.Model):
    document_types = {
        'IDENTITY': 'IDENTITY',
        'BANK_STATEMENT': 'BANK_STATEMENT',
    }

    score = models.FloatField()
    associated_user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50, choices=document_types) """

class DocumentScore(models.Model):

    document_id = models.BigAutoField(primary_key=True)
    score = models.FloatField()
    document_text = models.TextField(blank=True, null=True)


