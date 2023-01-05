from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_forum'),
    path('thread/<int:thread_id>/', views.thread, name='thread'),
    path('new/', views.new_thread, name='new_thread'),
]