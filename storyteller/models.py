from django.db import models


class Info(models.Model):
    bookname = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.IntegerField()
    price = models.IntegerField()


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

