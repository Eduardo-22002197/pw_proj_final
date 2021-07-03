from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.CharField(primary_key = True, null = False, max_length = 7)
    name = models.CharField(null = False, max_length = 60)
    phone = models.CharField(max_length = 9)
    email = models.EmailField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.contact_id + self.name[:30] + self.phone + self.email + self.created
