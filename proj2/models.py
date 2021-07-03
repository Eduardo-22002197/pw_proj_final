from django.db import models
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(null = False, max_length = 30)
    last_name = models.CharField(null = False, max_length = 30)
    phone = models.CharField(null = False, max_length = 12)
    email = models.EmailField(null = False, max_length = 100)
    date_birth = models.DateField(null = False)

    def __str__(self):
        return self.name + ' | ' + self.last_name + ' | ' + self.email