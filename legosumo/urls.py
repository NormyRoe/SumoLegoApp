"""legosumo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', include('loginapp.urls')),
    path('competitions', include('competitionsapp.urls')),
    path('divisions', include('divisionsapp.urls')),
    path('fields', include('fieldsapp.urls')),
    path('schools', include('schoolsapp.urls')),
    path('teams', include('teamsapp.urls')),
    path('users', include('usersapp.urls')),
    path('checkin/<str:ID>', include('checkinapp.urls')),
    path('gameresult', include('gameresultapp.urls')),
    path('draw/', include('drawapp.urls')),
]
