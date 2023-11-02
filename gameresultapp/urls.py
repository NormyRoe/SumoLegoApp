from django.urls import path

from . import views

urlpatterns = [
    path('/competition/<str:ID>', views.TheModelView, name='TheModelView'),
    path('/game/<str:ID>', views.SubmitScore, name='SubmitScore'),
    ]
