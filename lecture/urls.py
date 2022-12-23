from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:lecture_groupe_id>/', views.detail, name='detail'),
    path('new/', views.create_new_lecture, name='create_new_lecture'),
    path('edit/<int:lecture_groupe_id>/', views.edit_lecture, name='edit_lecture'),
    path('delete/<int:lecture_groupe_id>/', views.delete_lecture, name='delete_lecture'),
    path('events/', views.events, name='events'),
    path('participate/<int:lecture_groupe_id>/', views.participate_lecture, name='participate_lecture')
]