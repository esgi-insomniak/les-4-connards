from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:lecture_groupe_id>/', views.detail, name='detail'),
    path('new/', views.create_new_lecture, name='create_new_lecture'),
    path('edit/<int:lecture_groupe_id>/', views.edit_lecture, name='edit_lecture'),
    path('delete/<int:lecture_groupe_id>/', views.delete_lecture, name='delete_lecture'),
    path('calendar/', views.calendar, name='calendar'),
    path('api/events/', views.api_events, name='api_events'),
]