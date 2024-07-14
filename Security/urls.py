from django.urls import path
from . import views

urlpatterns =[
	
	path('index/',views.index,name="index"),
	path('signup/', views.signup ,name="signup"), 
    path('', views.login ,name="login"), 
    path('logout/', views.logoutUser ,name="logout"), 
    path('home/', views.home ,name="home"), 
	
]