from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('check/<str:pk>', views.check, name="check"),
]