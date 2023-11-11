from django.urls import path

from . import views

urlpatterns = [ 
    # Create or clear and recreate a draw for the given competition.
    path('<str:competition_id>/create', views.CreateDrawForCompetition, name='CreateDrawForCompetition'),
    
    # Get the draw for the given competition. If draw does not exist, it will be automatically created.
    path('<str:competition_id>', views.GetDrawForCompetition, name='GetDrawForCompetition'),
]
