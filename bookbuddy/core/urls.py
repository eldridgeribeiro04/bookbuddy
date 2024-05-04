from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.base, name='home'),
    path("add_book/", views.add_book, name='add_book'),
    path("book_detail/<int:book_id>", views.book_detail, name='book_detail')
]