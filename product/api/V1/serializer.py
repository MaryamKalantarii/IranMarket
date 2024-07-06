from rest_framework import serializers
from product.models import *



class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ["title","content1","content2","content3","content4","content5",
                    "image1", "image2", "image3","image4",
                    "more_details","category_clothing","category_color",
                    "price","number" ,"off","size","status","amazing_offer"
                   ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category_clothing'] = Category_clothing_Serializer(instance.category_clothing,many=True).data
        rep['category_color'] = Category_color_Serializer(instance.category_color,many=True).data
        request = self.context.get('request')
        # kwargs = request.parser_context.get('kwargs')
        # if kwargs.get('pk') is not None and None:
        #     rep.pop('content')
        return rep


class Dijitalgoods_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dijitalgoods
        fields = ["title","content1","content2","content3","content4","content5",
                    "image1", "image2", "image3","image4",
                    "more_details","category_Dijitalgoods","category_color","category_brand",
                    "price","number" ,"off","warranty" ,"status","amazing_offer" 
                    ]
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category_Dijitalgoods'] = Category_Dijitalgoods_Serializer(instance.category_Dijitalgoods,many=True).data
        rep['category_color'] = Category_color_Serializer(instance.category_color,many=True).data
        rep['category_brand'] = Category_brand_Serializer(instance.category_brand,many=True).data
        request = self.context.get('request')
        return rep
        



class Homeappliances_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Homeappliances
        fields = ["title","content1","content2","content3","content4","content5",
                    "image1", "image2", "image3","image4",
                    "more_details","category_Homeappliances","category_color","category_brand",
                    "price","number" ,"off","status","amazing_offer" 
                    ]
    def to_representation(self,instance):
        rep = super().to_representation(instance)
        rep["category_Homeappliances"] = Category_Homeappliances_Serializer(instance.category_Homeappliances,many=True).data
        rep["category_color"] = Category_color_Serializer(instance.category_color,many=True).data
        rep["category_brand"] = Category_brand_Serializer(instance.category_brand,many=True).data
        request = self.context.get('request')
        return rep
        



class Beauty_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Beauty
        fields = ["title","content1","content2","content3","content4","content5",
                    "image1", "image2", "image3","image4",
                    "more_details","category_Beauty", "category_color","category_brand", 
                    "price","number" ,"off","exception_date",
                    "status","amazing_offer" 
                    ]
    def to_representation(self,instance):
        rep = super().to_representation(instance)
        rep["category_Beauty"] = Category_Beauty_Serializer(instance.category_Beauty,many=True).data
        rep["category_color"] = Category_color_Serializer(instance.category_color,many=True).data
        rep["category_brand"] = Category_brand_Serializer(instance.category_brand,many=True).data
        request = self.context.get('request')
        return rep
        




class Appliances_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Appliances
        fields = ["title","content1","content2","content3","content4","content5",
                    "image1", "image2", "image3","image4",
                    "more_details","category_Appliances","category_color","category_brand",
                    "price","number","off","warranty","status"] 
    def to_representation(self,instance):
        rep = super().to_representation(instance)
        rep['category_Appliances'] = Category_Appliances_Serializer(instance.category_Appliances).data
        rep['category_color'] = Category_color_Serializer(instance.category_color,many=True).data
        rep['category_brand'] = Category_brand_Serializer(instance.category_brand,many=True).data
        request = self.context.get('request')
        return rep
        




class Supermarket_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Supermarket
        fields = ["title","content1","content2","content3","content4","content5",
                    "image1", "image2", "image3","image4",
                    "more_details","category_Supermarket","exception_date",
                    "price","number" ,"off","status" ]
    def to_representation(self,instance):

        rep = super().to_representation(instance)
        rep["category_Supermarket"] = Category_Supermarket_Serializer(instance.category_Supermarket,many=True).data
        request = self.context.get('request')
        return rep
        





class Child_and_babySerializer(serializers.ModelSerializer):
    class Meta:
        model = Child_and_baby
        fields = ["title","content1","content2","content3","content4","content5",
                    "image1", "image2", "image3","image4",
                    "more_details","category_Child_and_baby","category_color","size",
                    "price","number","off","status"
                    ]
    def to_representation(self,instance):
        rep = super().to_representation(instance)
        rep["category_Child_and_baby"] = Category_Child_and_baby_Serializer(instance.category_Child_and_baby,many=True).data
        rep["category_color"] = Category_color_Serializer(instance.category_color,many=True).data
        request = self.context.get('request')
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

class Category_brand_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category_brand
        fields = ['id', 'name','image']

class Category_color_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category_color
        fields = ["id", "name","image"]