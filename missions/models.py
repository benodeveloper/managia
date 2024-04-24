from django.db import models

# Create your models here.
class Mission(models.Model):
    reference = models.CharField(max_length=100)
    order_number = models.CharField(max_length=150)
    date = models.DateField()
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.reference
    
    