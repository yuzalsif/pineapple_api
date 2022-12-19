from django.urls import path, include
from . import views

urlpatterns = [
    path('shop/', views.get_all_shops, name='shops'),
    path('shop/<int:id>', views.get_shop_detail, name='shops_details')
]