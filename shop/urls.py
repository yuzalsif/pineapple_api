from django.urls import path, include
from . import views

urlpatterns = [
    path('shop/', views.ShopListCreate.as_view(), name='shops'),
    path('shop/<int:pk>', views.ShopRetrieveDeleteUpdate.as_view(), name='shop_detail'),
]