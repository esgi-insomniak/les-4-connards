from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

from .models import Librairie
from books.models import Books

def librairie(request):
    if request.method == 'POST':
        if request.POST['ville'] != '':
            librairie_list = Librairie.objects.filter(ville=request.POST['ville'])
            lieux = Librairie.objects.values_list('ville', flat=True).distinct()
            context = {
                'librairie_list': librairie_list,
                'lieux': lieux,
            }
        else:
            librairie_list = Librairie.objects.order_by('nom')[:5]
            lieux = Librairie.objects.values_list('ville', flat=True).distinct()
            context = {
                'librairie_list': librairie_list,
                'lieux': lieux,
            }
    else:
        librairie_list = Librairie.objects.order_by('nom')[:5]
        lieux = Librairie.objects.values_list('ville', flat=True).distinct()
        context = {
            'librairie_list': librairie_list,
            'lieux': lieux,
        }
    return render(request, 'librairie/index.html', context)

def librairie_detail(request, librairie_id):
    librairie = get_object_or_404(Librairie, pk=librairie_id)
    books = Books.objects.filter(Librairie=librairie.nom)
    return render(request, 'librairie/detail.html', {'librairie': librairie, 'books': books})

def create_new_librairie(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            librairie = Librairie(
                nom = request.POST['nom'],
                adresse = request.POST['adresse'],
                telephone = request.POST['telephone'],
                email = request.POST['email'],
            )
            librairie.save()
            if request.POST['password']:
                user = User.objects.create_user(
                    username=request.POST['nom'].replace(" ", "_").lower(),
                    password=request.POST['password'],
                    email=request.POST['email'],
                    is_staff=True,
                )
                user.save()
            return render(request, 'librairie/detail.html', {'librairie': librairie})
        else:
            return render(request, 'librairie/new.html')
    else:
        return render(request, 'librairie/index.html')

def edit_librairie(request, librairie_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            librairie = Librairie.objects.get(pk=librairie_id)
            librairie.nom = request.POST['nom'],
            librairie.adresse = request.POST['adresse'],
            librairie.telephone = request.POST['telephone'],
            librairie.email = request.POST['email'],
            librairie.save()
            return render(request, 'librairie/detail.html', {'librairie': librairie})
        else:
            return render(request, 'librairie/edit.html', {'librairie': librairie})
    else:
        return render(request, 'librairie/index.html')

def delete_librairie(request, librairie_id):
    if request.user.is_superuser:
        librairie = get_object_or_404(Lecture, pk=librairie_id)
        librairie.delete()
        return render(request, 'librairie/index.html')
    else:
        return render(request, 'librairie/index.html')