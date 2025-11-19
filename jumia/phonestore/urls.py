from django.urls import path
from phonestore import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('services/', views.services, name='services'),
    path('product/', views.product, name='product'),
    path('contact/', views.contacts, name='contacts'),
    path('gallery/', views.gallery, name='gallery'),
]