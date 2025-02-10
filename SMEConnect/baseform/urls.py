from django.urls import path
from . import views

urlpatterns = [
    path('investor', views.investor_view, name="investor"),
    path('startup', views.startup_view, name="startup"),
    path('investor_view', views.investorviewpage, name="investor_view"),
    path('startup_view', views.startupviewpage, name="startup_view"),
    path('startup_galleryview', views.startup_gallery, name="startup_galleryview"),
    path('dashboard', views.dashboard, name="dashboard"),
]