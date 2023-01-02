import json
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

from .models import Books
from librairie.models import Librairie
from .models import Loan

def index(request):
    book_list = Books.objects.order_by('title')[:5]
    context = {
        'latest_question_list': book_list,
    }
    return render(request, 'books/index.html', context)

def detail(request, book_id):
    question = get_object_or_404(Books, pk=book_id)
    librairie = Librairie.objects.get(nom=question.Librairie)
    return render(request, 'books/detail.html', {'book': question, 'librairie': librairie})

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

def loan_book(request, librairie_id):
    librairie = Librairie.objects.get(pk=librairie_id)
    if request.user.username == librairie.nom.replace(" ", "_").lower():
        user = User.objects.exclude(pk=request.user.pk)
        books = Books.objects.all().filter(Librairie=librairie.nom)
        if request.method == 'POST':
            book = Books.objects.get(pk=request.POST.get('livre'))
            book.borrowed_by = User.objects.get(pk=request.POST.get('utilisateur'))
            book.statut = True
            book.date_emprut = request.POST.get('date_emprut')
            book.date_retour = request.POST.get('date_retour')
            book.save()
            loan = Loan(
                date_retour = request.POST.get('date_retour'),
                borrowed_by = User.objects.get(pk=request.POST.get('utilisateur')),
                book = book,
                )
            loan.save()
            return render(request, 'books/loan.html', {'livres': books, 'librairie': librairie, 'utilisateurs': user})
        return render(request, 'books/loan.html', {'livres': books, 'librairie': librairie, 'utilisateurs': user})
    else:
        book_list = Books.objects.order_by('title')[:5]
        context = {
            'latest_question_list': book_list,
        }
        return render(request, 'books/index.html', context)