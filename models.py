# models.py
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure = models.DecimalField(max_digits=5, decimal_places=2)
    cholesterol_levels = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f'{self.user.username} logged in at {self.login_time}'
