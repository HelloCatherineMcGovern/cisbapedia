#Define URL Patterns for Cisba

from django.urls import path

from .import views

app_name = 'cisba'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
]

