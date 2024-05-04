from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    book_img = models.ImageField(upload_to='books', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    goal_date = models.DateField()

    def __str__(self):
        return self.title
