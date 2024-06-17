from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'api-v1'

router = DefaultRouter()
router.register('product',ProductsView , basename='products')
router.register('category',CategoryView , basename='category')
urlpatterns =router.urls
