from rest_framework import viewsets
from .permission import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ...models import *
from .serializer import *
from .paginator import CustomePaginate

class ProductsView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(status=True)
    search_fields = ['content', 'content2','content3','content4','content5','category__name']
    ordering_fields = ['created_date']



class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

   