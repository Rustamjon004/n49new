from django.shortcuts import render
def profile(request):
    return render(request=request,
                  template_name='profile.html')
def contacts(request):
    return render(request=request,
                  template_name='contacts.html')
def products(request):
    return render(request=request,
                  template_name='products.html')
# Create your views here.
