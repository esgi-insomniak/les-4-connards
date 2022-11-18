from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Books

def index(request):
    book_list = Books.objects.order_by('title')[:5]
    context = {
        'latest_question_list': book_list,
    }
    return render(request, 'books/index.html', context)

def detail(request, book_id):
    question = get_object_or_404(Books, pk=book_id)
    return render(request, 'books/detail.html', {'question': question})

def book_list(request):
    response = "List of BOOKS"
    return HttpResponse(response)