from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

@api_view()
def get_all_shops(request):
    queryset = Shop.objects.all()
    serializer = ShopSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def get_shop_detail(request, id):
    shop = get_object_or_404(Shop, pk=id)
    serializer = ShopSerializer(shop)
    return Response(serializer.data)
