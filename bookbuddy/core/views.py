from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Book

# Create your views here.

@login_required
def base(request):
    return render(request, 'core/base.html')


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            if book.category not in ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery']:
                custom_category = request.POST.get('category')
                book.category = custom_category
            book.save()
            return redirect('core:book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'core/add_book.html', {'form': form})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'core/book_detail.html')