from django.shortcuts import render
def home(request):
    return render(request=request,
                  template_name='home.html')
def dashboard(request):
    return render(request=request,
                  template_name='dashboard.html')

# Create your views here.
