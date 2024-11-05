from django.urls import path
from . import views

urlpatterns = [
    path('', views.connect4_view, name='connect4'),
]