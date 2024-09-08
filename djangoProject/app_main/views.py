from django.shortcuts import render
from .models import Post
def home(request):
    posts = Post.objects.all()
    return render(request=request,
                  template_name='home.html',
                context={'posts':posts})
def dashboard(request):
    return render(request=request,
                  template_name='dashboard.html')

# Create your views here.
