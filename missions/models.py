from django.db import models

# Create your models here.
    
class Beneficiary(models.Model):
    first_name   = models.CharField(max_length=255)
    last_name    = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

class Mission(models.Model):
    reference    = models.CharField(max_length=100)
    order_number = models.CharField(max_length=150)
    date         = models.DateField()
    status       = models.CharField(max_length=100)
    beneficiary  = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.reference
    
    