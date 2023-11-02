from django.urls import path

from . import views

urlpatterns = [
    path('', views.TheModelView, name='TheModelView'),
    path('/<str:ID>', views.SpecificUser, name='SpecificUser'),
    ]

