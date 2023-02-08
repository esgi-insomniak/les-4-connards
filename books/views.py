import json
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime
from django.core.mail import send_mail
from django.core.paginator import Paginator

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
    return render(request, 'books/detail.html', {'books': question, 'librairie': librairie})

def create_new_book(request):
    if request.user.is_superuser or request.user.is_staff:
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
            return render(request, 'books/detail.html', {'books': book})
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
            return render(request, 'books/detail.html', {'books': book})
        else:
            print("ca passe pas")
            return render(request, 'books/update.html', {'books': book, 'librairies': librairie})
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
    search_title = request.GET.get('title', '')
    search_author = request.GET.get('author', '')
    search_genre = request.GET.get('genre', '')
    #search_librairie = request.GET.get('librairie')
    search_dispo = request.GET.get('dispo')
    number_of_books_per_page = 20
    #get last 5 books
    books = Books.objects.all().filter(Q(title__contains=search_title) & Q(genre__contains=search_genre) & Q(author__contains=search_author))

    authors = Books.objects.values_list('author', flat=True).distinct()
    # author is like ['J.K. Rowling', 'J.R.R. Tolkien', 'Stephen King', 'Stephen King, J.R.R. Tolkien']
    authors = [author.split(',') for author in authors]
    # array unique and trim
    authors = list(set([item.strip() for sublist in authors for item in sublist]))[0:5]

    genres = Books.objects.values_list('genre', flat=True).distinct()
    # genre is like ['fantasy', 'science-fiction', 'thriller, fantasy, horror', 'horror']
    genres = [genre.split(',') for genre in genres]
    # array unique and trim
    genres = list(set([item.strip() for sublist in genres for item in sublist]))

    if search_dispo == 'on':
        books = books.filter(statut=False)

    ##Books filtered
    books = books.order_by('title')

    ##Pagination
    paginator = Paginator(books, number_of_books_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/search.html', {
        'books': page_obj,
        'search': search_title,
        'genres': genres,
        'authors': authors,
    })

def loan_book(request, librairie_id):
    librairie = Librairie.objects.get(pk=librairie_id)
    if request.user.username == librairie.nom.replace(" ", "_").lower() or request.user.is_superuser:
        user = User.objects.exclude(pk=request.user.pk)
        books = Books.objects.all().filter(Librairie=librairie.nom)
        if request.method == 'POST':
            book = Books.objects.get(pk=request.POST.get('livre'))
            book.borrowed_by = User.objects.get(pk=request.POST.get('utilisateur'))
            book.statut = True
            book.date_emprut = datetime.now()
            book.date_retour = request.POST.get('date_retour')
            book.save()
            loan = Loan(
                date_retour = request.POST.get('date_retour'),
                borrowed_by = User.objects.get(pk=request.POST.get('utilisateur')),
                book = book,
                Librairie = librairie,
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

def loan_list(request, librairie_id):
    librairie = Librairie.objects.get(pk=librairie_id)
    if request.user.username == librairie.nom.replace(" ", "_").lower() or request.user.is_superuser:
        loan = Loan.objects.all().filter(Librairie=librairie)
        now = datetime.now()
        return render(request, 'books/loan_list.html', {'loans': loan, 'now': now})
    else:
        book_list = Books.objects.order_by('title')[:5]
        context = {
            'latest_question_list': book_list,
        }
        return render(request, 'books/index.html', context)

def return_book(request, loan_id):
    loan = Loan.objects.get(pk=loan_id)
    book = Books.objects.get(pk=loan.book.pk)
    book.borrowed_by = None
    book.statut = False
    book.date_emprut = None
    book.date_retour = None
    book.save()
    loan.delete()
    librairie_id = Librairie.objects.get(nom=book.Librairie).pk
    return redirect('loan_list', librairie_id=librairie_id)

def renew_book(request, loan_id):
    loan = Loan.objects.get(pk=loan_id)
    if request.method == 'POST':
        book = Books.objects.get(pk=loan.book.pk)
        book.date_retour = request.POST.get('date_retour')
        book.save()
        loan.date_retour = request.POST.get('date_retour')
        loan.save()
        librairie_id = Librairie.objects.get(nom=book.Librairie).pk
        return redirect('loan_list', librairie_id=librairie_id)
    librairie_id = Librairie.objects.get(nom=loan.Librairie).pk
    return render(request, 'books/renew.html', {'loan': loan, 'librairie_id': librairie_id})

def send_remember(request, loan_id):
    loan = Loan.objects.get(pk=loan_id)
    book = Books.objects.get(pk=loan.book.pk)
    user = User.objects.get(pk=loan.borrowed_by.pk)
    librairie = Librairie.objects.get(nom=book.Librairie)
    send_mail(
        'Rappel de retour de livre',
        'Bonjour ' + user.first_name + ' ' + user.last_name + ',\n\nVous devez rendre le livre ' + book.title + ' à la librairie ' + librairie.nom + ' avant le ' + loan.date_retour.strftime("%d/%m/%Y") + '.\n\nCordialement,\n\nL\'équipe de la librairie ' + librairie.nom,
        ')',
        [user.email],
        fail_silently=False,
    )
    return redirect('loan_list', librairie_id=librairie.pk)