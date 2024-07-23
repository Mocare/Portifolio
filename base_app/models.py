from django.db import models
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    birthday = models.DateField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.name

# Create your models here.
