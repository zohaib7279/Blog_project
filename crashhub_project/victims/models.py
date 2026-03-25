from django.db import models

# Create your models here.
class Victim(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    incident = models.TextField()
    created_by = models.ForeignKey("Users.User", on_delete=models.CASCADE)