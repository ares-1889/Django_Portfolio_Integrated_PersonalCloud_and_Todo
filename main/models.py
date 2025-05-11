from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    pass

class Files(models.Model):
    file_name = models.CharField(max_length=100, )
    file_file = models.FileField(upload_to='files/')
    # image_file = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.file_name