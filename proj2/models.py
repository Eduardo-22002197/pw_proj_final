from typing import final
from django.db import models
from django.db.models import fields
from django.db.models.enums import Choices


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
    rating_website = models.IntegerField(null = False, default = 0)
    final_comment = models.TextField(null = True, default = '', max_length = 400)
    comment_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.complete_name + ' | ' + self.comment_date.strftime('%a, %d %b %Y')