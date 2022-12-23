from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:book_id>/', views.detail, name='detail'),
    path('new/', views.create_new_book, name='create_new_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('search/', views.search_book, name='search'),
]