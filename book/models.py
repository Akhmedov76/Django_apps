from django.db import models
from django.contrib.auth.models import User


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True)

    created = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class BookModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1)
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CommentsModel(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
