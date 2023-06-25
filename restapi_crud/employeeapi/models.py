from django.db import models

# Create your models here.
class employee(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=15)
