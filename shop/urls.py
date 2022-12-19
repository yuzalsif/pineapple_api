from django.urls import path, include
from . import views

urlpatterns = [
    path('shop/', views.ShopListCreate.as_view(), name='shops'),
]