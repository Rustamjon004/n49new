from django.urls import path
from .views import profile,products,contacts
urlpatterns = [

    path('profile/', profile),
    path('contacts/', contacts),
    path('products/', products),
]