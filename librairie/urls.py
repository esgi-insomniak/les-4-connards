from django.urls import path

from . import views

urlpatterns = [
    path('', views.librairie, name='librairie'),
    path('detail/<int:librairie_id>/', views.librairie_detail, name='detail'),
]