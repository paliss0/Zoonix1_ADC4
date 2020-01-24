"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import views

app_name = "main"
urlpatterns = [
	path('',views.homepage,name="homepage"),
	path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name="logout"),
    path('login/',views.user_login,name="login"),

    path('book/upload/',views.upload_book, name="upload"), 
    path ('book/, views.book_list', name = "book_list"),
    path('book/<int:pk>/', views.delete_book, name= "delete_book"),
    path('/update/<int:id>/', views.update_books),
    path('api/', views.api_data, name="api_data"),
    path ('api/<int:pk>/', views.api_update_data, name="api_update_data"),
]

    
