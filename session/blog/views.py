from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

def blog(request):
    blog = Blog.objects.all()
    return HttpResponse(blog)