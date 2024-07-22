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
    category = CategoryChoiceField(label="Category", required=True)
    goal_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), required=True)

    class Meta:
        model = models.Book
        fields = ['title', 'author', 'category', 'book_img', 'goal_date']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True


class Completed(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = ['completed']



