from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='SUni-home'),
    path('contact/', views.contact, name='SUni-contact'),
    path('about/', views.about, name='SUni-about'),
    path('login/', views.login, name='SUni-login'),
    path('signup/', views.signup, name='SUni-signup'),
]