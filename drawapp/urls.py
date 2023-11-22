from django.urls import path

from . import views

urlpatterns = [ 
    # Create draw for the given competition.
    path('', views.CreateDrawForCompetition, name='CreateDrawForCompetition'),
]
