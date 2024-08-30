from django.shortcuts import render
def home(request):
    return render(request=request,
                  template_name='home.html')

def profile(request):
    return render(request=request,
                  template_name='profile.html')

def dashboard(request):
    return render(request=request,
                  template_name='dashboard.html')

def contacts(request):
    return render(request=request,
                  template_name='contacts.html')

def products(request):
    return render(request=request,
                  template_name='products.html')