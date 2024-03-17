from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
   path('', views.home, name='home'),
   path('register/', views.register, name='register'),
   path('login/', views.login, name='login'),
   path('logout', views.logout,name='logout'),
   path('works/', views.works, name='works'),
   path('about/', views.about, name='about'),
]
