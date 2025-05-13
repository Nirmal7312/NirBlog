from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('add/', views.add,name="add"),
    path('adding/', views.adding,name="adding"),
    path('post/<int:pid>', views.post,name="post"),
    path('delete/<int:did>', views.delete,name="delete"),
    path('edit/<int:did>', views.edit,name="edit"),
    path('editing/<int:did>', views.editing,name="editing"),
]