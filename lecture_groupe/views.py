from django.shortcuts import get_object_or_404, render

from .models import LectureGroupes
from books.models import Books
from librairie.models import Librairie

def index(request):
    book_list = LectureGroupes.objects.order_by('date')[:5]
    context = {
        'lecture_list': book_list,
    }
    return render(request, 'lecture/index.html', context)

def detail(request, lecture_groupe_id):
    question = get_object_or_404(LectureGroupes, pk=lecture_groupe_id)
    return render(request, 'lecture/detail.html', {'lecture': question})

def create_new_lecture(request):
    if request.user.is_superuser:
        books = Books.objects.all()
        librairie = Librairie.objects.all()
        if request.method == 'POST':
            lecture = LectureGroupes(
                lieux = request.POST['lieux'],
                date = request.POST['date'],
                heure = request.POST['heure'],
                livre = request.POST['livre'],
                participants = request.POST['participants'],
                librairie = request.POST['librairie'],
                )
            lecture.save()
            return render(request, 'lecture/detail.html', {'lecture': lecture})
        else:
            return render(request, 'lecture/new.html', {'books': books, 'librairies': librairie})
    else:
        return render(request, 'lecture/index.html')

def edit_lecture(request, lecture_groupe_id):
    if request.user.is_superuser:
        lecture = LectureGroupes.objects.get(pk=lecture_groupe_id)
        if request.method == 'POST':
            lecture = LectureGroupes.objects.get(pk=lecture_groupe_id)
            lecture.lieux = request.POST.get('lieux')
            lecture.date = request.POST.get('date')
            lecture.heure = request.POST.get('heure')
            lecture.livre = request.POST.get('livre')
            lecture.participants = request.POST.get('participants')
            lecture.librairie = request.POST.get('librairie')
            lecture.save()
            return render(request, 'lecture/detail.html', {'lecture': lecture})
        else:
            return render(request, 'lecture/edit.html', {'lecture': lecture})
    else:
        return render(request, 'lecture/index.html')

def delete_lecture(request, lecture_groupe_id):
    if request.user.is_superuser:
        lecture = get_object_or_404(LectureGroupes, pk=lecture_groupe_id)
        lecture.delete()
        return render(request, 'lecture/index.html')
    else:
        return render(request, 'lecture/index.html')