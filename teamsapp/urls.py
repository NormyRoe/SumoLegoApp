from django.urls import path

from . import views

urlpatterns = [
    path('', views.TheModelView, name='TheModelView'),
    path('/school/<str:ID>', views.RequestedSchool, name='RequestedSchool'),
    path('/<str:ID>', views.RequestedTeam, name='RequestedTeam'),
    ]

