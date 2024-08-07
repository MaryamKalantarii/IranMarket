from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'api-v1'

router = DefaultRouter()
router.register('clothing',ClothingView , basename='clothing')
router.register('dijitalgood',DijitalgoodsView , basename='dijitalgood')
router.register('homeappliance',HomeappliancesView , basename='homeappliance')
router.register('beauty',BeautyView , basename='beauty')
router.register('appliance',AppliancesView , basename='appliance')
router.register('supermarket',SupermarketView , basename='supermarket')
router.register('child',Child_and_babyView ,basename='child')



router.register('category_brand',Category_brandView , basename='category_brand')
router.register('category_Dijitalgoods',Category_DijitalgoodsView , basename='category_Dijitalgoods')
router.register('category_clothing',Category_clothingView , basename='category_clothing')
router.register('category_Homeappliances',Category_HomeappliancesView , basename='category_Homeappliances')
router.register('category_Beauty',Category_BeautyView , basename='category_Beauty')
router.register('category_Appliances',Category_AppliancesView , basename='category_Appliances')
router.register('category_Supermarket',Category_SupermarketView , basename='category_Supermarket')
router.register('category_Child_and_baby',Category_Child_and_babyView , basename='category_Child_and_baby')
urlpatterns =router.urls
