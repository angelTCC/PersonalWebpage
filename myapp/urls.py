from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Home'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog')
]