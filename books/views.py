from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % book_id)

def book_list(request):
    response = "List of BOOKS"
    return HttpResponse(response)