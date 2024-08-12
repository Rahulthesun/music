from django.urls import path
from . import views

urlpatterns = [
    path("" , views.music_form , name="music_form"),
    path("result/" , views.music_ml_model , name="result")
]