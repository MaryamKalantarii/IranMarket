from rest_framework import viewsets
from ...models import *
from .serializer import *

class ProductsView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(status=True)



class CategoryView(viewsets.ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

   