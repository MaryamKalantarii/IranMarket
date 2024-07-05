from rest_framework import viewsets
from .permission import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ...models import *
from .serializer import *
from .paginator import CustomePaginate

class ClothingView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    serializer_class = ClothingSerializer
    queryset = Product.objects.filter(status=True)
    search_fields = ['title','content1', 'content2','content3','content4','content5']
    ordering_fields = ['created_date']

class DijitalgoodsView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    serializer_class = Dijitalgoods_Serializer
    queryset = Product.objects.filter(status=True)
    search_fields = ['title','content1', 'content2','content3','content4','content5']
    ordering_fields = ['created_date']

class HomeappliancesView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    serializer_class = Homeappliances_Serializer
    queryset = Product.objects.filter(status=True)
    search_fields = ['title','content1', 'content2','content3','content4','content5']
    ordering_fields = ['created_date']

class BeautyView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    serializer_class = Beauty_Serializer
    queryset = Product.objects.filter(status=True)
    search_fields = ['title','content1', 'content2','content3','content4','content5']
    ordering_fields = ['created_date']

class AppliancesView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    serializer_class = Appliances_Serializer
    queryset = Product.objects.filter(status=True)
    search_fields = ['title','content1', 'content2','content3','content4','content5']
    ordering_fields = ['created_date']

class SupermarketView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    serializer_class = Supermarket_Serializer
    queryset = Product.objects.filter(status=True)
    search_fields = ['title','content1', 'content2','content3','content4','content5']
    ordering_fields = ['created_date']

class Child_and_babyView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    serializer_class = Child_and_babySerializer
    queryset = Product.objects.filter(status=True)
    search_fields = ['title','content1', 'content2','content3','content4','content5']
    ordering_fields = ['created_date']


class Category_DijitalgoodsView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = Category_Dijitalgoods_Serializer
    queryset = Category_Dijitalgoods.objects.all()

class Category_clothingView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = Category_clothing_Serializer
    queryset = Category_clothing.objects.all()

class Category_HomeappliancesView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = Category_Homeappliances_Serializer
    queryset = Category_Homeappliances.objects.all()

class Category_BeautyView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = Category_Beauty_Serializer
    queryset = Category_Beauty.objects.all()

class Category_AppliancesView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = Category_Appliances_Serializer
    queryset = Category_Appliances.objects.all()

class Category_SupermarketView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = Category_Supermarket_Serializer
    queryset = Category_Supermarket.objects.all()

class Category_Child_and_babyView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = Category_Child_and_baby_Serializer
    queryset = Category_Child_and_baby.objects.all()
