from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_book'),
    path('detail/<int:book_id>/', views.detail, name='detail'),
    path('new/', views.create_new_book, name='create_new_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('search/', views.search_book, name='search'),
    path('loan/<int:librairie_id>/', views.loan_book, name='loan_book'),
    path('loan/list/<int:librairie_id>/', views.loan_list, name='loan_list'),
    path('loan/return/<int:loan_id>/', views.return_book, name='loan_return'),
    path('loan/renew/<int:loan_id>/', views.renew_book, name='loan_renew'),
    path('loan/remember/<int:loan_id>/', views.send_remember, name='loan_remembers'),
]