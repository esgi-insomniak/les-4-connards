from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:book_id>/', views.detail, name='detail'),
    path('books-list', views.book_list, name='list'),
]