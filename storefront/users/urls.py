from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>', views.userProfile, name="user-profile"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('create_skill/', views.createSkill, name='create-skill'),
    path('edit-skill/<str:pk>/', views.editSkill, name='edit-skill'),
    path('delete/<str:pk>/', views.deleteSkill, name='delete-skill'),

    
]