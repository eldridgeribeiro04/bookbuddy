from typing import Any, Sequence
from django import forms
from . import models

class CategoryChoiceField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = forms.TextInput(attrs={'class':'form-control'})
        self.choices = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery']

    def clean(self, value):
        value = value.strip()
        if value:
            return value
        else:
            raise forms.ValidationError("This field is required")    

class BookForm(forms.ModelForm):
    category = CategoryChoiceField(label="Category")
    goal_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = models.Book
        fields = ['title', 'author', 'category', 'book_img', 'goal_date']


class Completed(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = ['completed']
