from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('courses/', views.courses, name = 'courses'),
    path('instructors/', views.instructors, name = 'instructors'),
    path('blog/', views.blog, name = 'blog'),
    path('contact/', views.contact, name = 'contact'),
]