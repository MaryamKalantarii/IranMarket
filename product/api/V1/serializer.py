from rest_framework import serializers
from ...models import *

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
        model = Product
        fields = ["image","image1", "image2", "image3",
                    "title","content","content2","content3",
                    "content4","content5","price","number" ,
                    "warranty" ,"color" ,"category" ,"status" ]



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]