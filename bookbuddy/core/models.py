from django.db import models
from accounts.models import CustomUser
from django.contrib.auth import get_user_model

# Create your models here.

def get_default_user():
    return get_user_model().objects.first()

class Book(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=get_default_user)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    book_img = models.ImageField(upload_to='books', blank=True, null=True)
    author = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    goal_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
