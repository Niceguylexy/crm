from django.db import models

# Create your models here.
class Record(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=125)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    