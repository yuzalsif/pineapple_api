from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView

from .models import *
from .serializers import *

class ShopListCreate(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

