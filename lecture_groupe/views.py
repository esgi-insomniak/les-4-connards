from django.shortcuts import get_object_or_404, render

from .models import LectureGroupes

def index(request):
    book_list = LectureGroupes.objects.order_by('date')[:5]
    context = {
        'lecture_list': book_list,
    }
    return render(request, 'lecture/index.html', context)

def detail(request, lecture_groupe_id):
    question = get_object_or_404(LectureGroupes, pk=lecture_groupe_id)
    return render(request, 'lecture/detail.html', {'lecture': question})