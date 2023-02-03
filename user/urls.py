from django.urls import path
from . import views

urlpatterns = [
    path('', views.PortfolioAbout.set_language, name='aboutme'),
    path('en/', views.PortfolioAbout.main_en, name='en'),
    path('lt/', views.PortfolioAbout.main_lt, name='lt'),
]
