from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Librairie

def librairie(request):
    librairie_list = Librairie.objects.order_by('nom')[:5]
    context = {
        'librairie_list': librairie_list,
    }
    return render(request, 'librairie/index.html', context)

def librairie_detail(request, librairie_id):
    librairie = get_object_or_404(Librairie, pk=librairie_id)
    return render(request, 'librairie/detail.html', {'librairie': librairie})