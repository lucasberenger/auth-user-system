from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
   path('', views.home, name='home'),
   path('register/', views.register, name='register'),
   path('login/', views.login, name='login'),
   path('logout', views.logout,name='logout'),
   path('userlist/', views.userlist, name='userlist'),
   path('changepassword/', views.changepassword, name='changepassword'),
]
