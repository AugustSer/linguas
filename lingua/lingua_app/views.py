from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'lingua_app/index.html')


def courses(request):
    return render(request, 'lingua_app/courses.html')


def instructors(request):
    return render(request, 'lingua_app/instructors.html')


def blog(request):
    return render(request, 'lingua_app/blog.html')


def contact(request):
    return render(request, 'lingua_app/contact.html')