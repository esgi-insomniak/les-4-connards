from django.shortcuts import get_object_or_404, render

from .models import Lecture
from books.models import Books
from librairie.models import Librairie

def index(request):
    lecture = Lecture.objects.order_by('date')[:5]
    context = {
        'lecture_list': lecture,
    }
    return render(request, 'lecture/index.html', context)

def detail(request, lecture_groupe_id):
    question = get_object_or_404(Lecture, pk=lecture_groupe_id)
    return render(request, 'lecture/detail.html', {'lecture': question})

def create_new_lecture(request):
    if request.user.is_superuser:
        books = Books.objects.all()
        librairie = Librairie.objects.all()
        if request.method == 'POST':
            lecture = Lecture(
                lieux = request.POST['lieux'],
                date = request.POST['date'],
                heure = request.POST['heure'],
                Books = Books.objects.get(pk=request.POST['livre']),
                Librairie = Librairie.objects.get(pk=request.POST['librairie']),
                )
            lecture.save()
            return render(request, 'lecture/detail.html', {'lecture': lecture})
        else:
            return render(request, 'lecture/new.html', {'books': books, 'librairies': librairie})
    else:
        return render(request, 'lecture/index.html')

def edit_lecture(request, lecture_groupe_id):
    if request.user.is_superuser:
        lecture = Lecture.objects.get(pk=lecture_groupe_id)
        books = Books.objects.all()
        librairie = Librairie.objects.all()
        if request.method == 'POST':
            lecture = Lecture.objects.get(pk=lecture_groupe_id)
            lecture.lieux = request.POST.get('lieux')
            lecture.date = request.POST.get('date')
            lecture.heure = request.POST.get('heure')
            lecture.Books = Books.objects.get(pk=request.POST['livre']),
            lecture.Librairie = Librairie.objects.get(pk=request.POST['librairie']),
            lecture.save()
            return render(request, 'lecture/detail.html', {'lecture': lecture})
        else:
            return render(request, 'lecture/edit.html', {'lecture': lecture, 'books': books, 'librairies': librairie})
    else:
        return render(request, 'lecture/index.html')

def delete_lecture(request, lecture_groupe_id):
    if request.user.is_superuser:
        lecture = get_object_or_404(Lecture, pk=lecture_groupe_id)
        lecture.delete()
        return render(request, 'lecture/index.html')
    else:
        return render(request, 'lecture/index.html')