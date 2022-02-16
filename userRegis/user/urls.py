from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history_user, name='history'),
]