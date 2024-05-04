from typing import Any, Sequence
from django import forms
from . import models

class CategoryChoiceField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = forms.TextInput(attrs={'class':'form-control'})
        self.choices = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery']

    def clean(self, value):
        if value not in self.choices:
            return value
        return super().clean(value)
    

class BookForm(forms.ModelForm):
    category = CategoryChoiceField()

    class Meta:
        model = models.Book
        fields = ['title', 'author', 'category', 'book_img', 'goal_date']
