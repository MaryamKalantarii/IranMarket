from rest_framework import serializers
from product.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["image1", "image2", "image3","image4",
                    "title","content1","content2","content3",
                    "content4","content5","price","number" ,"off",
                    "warranty" ,"color" ,"category_clothing" ,"status","category_Dijitalgoods","category_Homeappliances", 
                    "category_Beauty","category_Appliances","category_Supermarket","category_Child_and_baby"]
        
    def to_representation(self,instance):
        rep = super().to_representation(instance)
        rep["category_clothing"] =  Category_clothing_Serializer(instance.Category_clothing,many=True).data
        rep["category_Dijitalgoods"] = Category_Dijitalgoods_Serializer(instance.Category_clothing,many=True).data
        rep["category_Homeappliances"] = Category_Homeappliances_Serializer(instance.Category_Homeappliances,many=True).data
        rep["category_Beauty"] = Category_Beauty_Serializer(instance.Category_Beauty,many=True).data
        rep["category_Appliances"] = Category_Appliances_Serializer(instance.Category_Appliances,many=True).data
        rep["category_Supermarket"] = Category_Supermarket_Serializer(instance.Category_Supermarket,many=True).data
        rep["category_Child_and_baby"] =  Category_Child_and_baby_Serializer(instance.Category_Supermarket,many=True).data
        request = self.context.get('request')
        kwargs = request.parser_context.get('kwargs')
        if kwargs.get('pk') is None:
            rep.pop('content')
            
        return rep
        


class Category_clothing_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category_clothing
        fields = ["id", "name"]

class Category_Dijitalgoods_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category_Dijitalgoods
        fields = ["id", "name"]

class Category_Homeappliances_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category_Homeappliances
        fields = ["id", "name"]

class Category_Beauty_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category_Beauty
        fields = ["id", "name"]

class Category_Appliances_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category_Appliances
        fields = ["id", "name"]

class Category_Supermarket_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category_Supermarket
        fields = ["id", "name"]

class Category_Child_and_baby_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category_Child_and_baby
        fields = ["id", "name"]