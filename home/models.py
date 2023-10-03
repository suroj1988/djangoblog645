from django.db import models

# Create your models here.
class Service(models.Model):
    logo = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=300)
    post = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    comment = models.TextField(blank=True)

    def __str__(self):
       return self.name

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    subject = models.TextField(blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name



