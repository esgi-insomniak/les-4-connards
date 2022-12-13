import json
from django.shortcuts import get_object_or_404, render

from .models import Books
from librairie.models import Librairie

def index(request):
    book_list = Books.objects.order_by('title')[:5]
    context = {
        'latest_question_list': book_list,
    }
    return render(request, 'books/index.html', context)

def detail(request, book_id):
    question = get_object_or_404(Books, pk=book_id)
    return render(request, 'books/detail.html', {'book': question})

def create_new_book(request):
    if request.user.is_superuser:
        librairie = Librairie.objects.all()
        if request.method == 'POST':
            book = Books(
                title = request.POST['title'],
                author = request.POST['author'],
                jaquette = request.POST['jaquette'],
                editeur = request.POST['editeur'],
                collection = request.POST['collection'],
                genre = request.POST['genre'],
                Librairie = Librairie.objects.get(pk=request.POST['librairie']),
                )
            book.save()
            return render(request, 'books/detail.html', {'book': book})
        else:
            return render(request, 'books/new.html', {'librairies': librairie})
    else:
        return render(request, 'books/index.html')

def edit_book(request, book_id):
    if request.user.is_superuser:
        book = Books.objects.get(pk=book_id)
        librairie = Librairie.objects.all()
        if request.method == 'POST':
            book = Books.objects.get(pk=book_id)
            book.title = request.POST.get('title')
            book.author = request.POST.get('author')
            book.jaquette = request.POST.get('jaquette')
            book.editeur = request.POST.get('editeur')
            book.collection = request.POST.get('collection')
            book.genre = request.POST.get('genre')
            book.Librairie = Librairie.objects.get(pk=request.POST.get('librairie'))
            book.save()
            return render(request, 'books/detail.html', {'book': book})
        else:
            print("ca passe pas")
            return render(request, 'books/update.html', {'book': book, 'librairies': librairie})
    else:
        return render(request, 'books/index.html')

def delete_book(request, book_id):
    if request.user.is_superuser:
        book = get_object_or_404(Books, pk=book_id)
        book.delete()
        return render(request, 'books/index.html')
    else:
        return render(request, 'books/index.html')

def search_book(request):
    if request.method == 'POST':
        search = request.POST.get('q')
        # return all objects that contain the search term in their title
        book = Books.objects.all().filter(title__icontains=search)
        return render(request, 'books/search.html', {'books': book, 'search': search})
    else:
        return render(request, 'books/index.html')