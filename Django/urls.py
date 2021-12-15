from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('swish/callback', views.swish_callback, name='swish_callback'),
]

