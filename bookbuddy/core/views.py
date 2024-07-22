from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm, Completed
from .models import Book
from django.http import HttpResponse

@login_required
def base(request):
    user = request.user
    book = Book.objects.filter(user=user)
    return render(request, 'core/base.html', {
        'book':book,
        'user': user,
        })


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        
        if form.is_valid():
            category = form.cleaned_data.get('category')

            book = Book.objects.create(
                title = form.cleaned_data['title'],
                category = category,
                book_img = form.cleaned_data.get('book_img'),
                author = form.cleaned_data.get('author'),
                goal_date = form.cleaned_data.get('goal_date')
            )
            return redirect('core:home')
    else:
        form = BookForm()
    return render(request, 'core/add_book.html', {'form': form})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = Completed(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = Completed(instance=book)
    return render(request, 'core/book_detail.html', {
        'book':book,
        'form': form,
        })


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('core:home')
    else:
        return HttpResponse('Could not delete book')
    
    

