from django.urls import path

from . import views

urlpatterns = [
    path('', views.librairie, name='librairie'),
    path('detail/<int:librairie_id>/', views.librairie_detail, name='detail'),
    path('new/', views.create_new_librairie, name='new'),
    path('edit/<int:librairie_id>/', views.edit_librairie, name='edit'),
    path('delete/<int:librairie_id>/', views.delete_librairie, name='delete'),
]