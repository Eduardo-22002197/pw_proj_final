from typing import final
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import fields

# Create your models here.
class Contact(models.Model):
    name = models.CharField(null = False, max_length = 30)
    last_name = models.CharField(null = False, max_length = 30)
    phone = models.CharField(null = False, max_length = 12)
    email = models.EmailField(null = False, max_length = 100)
    date_birth = models.DateTimeField(null = False)

    def __str__(self):
        return self.name + ' | ' + self.last_name + ' | ' + self.email


class Comment(models.Model):
    complete_name = models.CharField(null = False, max_length = 60)
    rating_website = models.IntegerField(null = False, default = 0, validators = [MinValueValidator(0), MaxValueValidator(5)])
    final_comment = models.TextField(null = True, default = '', max_length = 400)

    def __str__(self):
        return self.complete_name + ' |'