from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('choose', views.choosebase, name='choose'),
    path('', views.homepage, name='homepage'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register/<str:base>/', views.register, name='register'),
    path('discover', views.discover, name="discover"),
    path('about', views.about, name="about"),
    path('blogs', views.blogs, name="blogs"),
    path('contact', views.contact, name="contact"),
]