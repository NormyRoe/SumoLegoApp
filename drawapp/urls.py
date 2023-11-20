from django.urls import path

from . import views

urlpatterns = [ 
    # Create draw for the given competition.
    path('<int:competition_id>', views.CreateDrawForCompetition, name='CreateDrawForCompetition'),
]
