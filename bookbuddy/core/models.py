from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    book_img = models.ImageField(upload_to='books', blank=True, null=True)
    author = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    goal_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
