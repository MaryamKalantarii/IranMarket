from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'api-v1'

router = DefaultRouter()
router.register('product',ProductsView , basename='products')
# router.register('Category_Dijitalgoods',Category_DijitalgoodsView , basename='Category_Dijitalgoods')
# router.register('Category_clothing',Category_clothingView , basename='Category_clothing')
# router.register('Category_Homeappliances',Category_HomeappliancesView , basename='Category_Homeappliances')
# router.register('Category_Beauty',Category_BeautyView , basename='Category_Homeappliances')
# router.register('Category_Appliances',Category_AppliancesView , basename='Category_Appliances')
# router.register('Category_Supermarket',Category_SupermarketView , basename='Category_Supermarket')
# router.register('Category_Child_and_baby',Category_Child_and_babyView , basename='Category_Child_and_baby')
urlpatterns =router.urls
