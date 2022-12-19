from django.urls import path, include
from . import views

urlpatterns = [
    path('shop/', views.get_all_shops, name='shops')
]