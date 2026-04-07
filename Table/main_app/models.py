from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    role_id = models.CharField(max_length=255)

    def __str__(self):
        return self.username    

class Role(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    Role_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name