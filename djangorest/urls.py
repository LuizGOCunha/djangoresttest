from django.urls import path
from . import views

urlpatterns = [
    path('', views.testresponse, name="all"),
    path('add/', views.testresponse_add, name="add")
]