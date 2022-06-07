from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=25)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f'{self.title}'

class Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=5, default='00000')
    phone = models.CharField(max_length=12, default="XXX-XXX-XXXX", null=True)
    email = models.EmailField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
