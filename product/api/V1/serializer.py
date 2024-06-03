from rest_framework import serializers
from product.models import Product,Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["image","image1", "image2", "image3",
                    "title","content","content2","content3",
                    "content4","content5","price","number" ,
                    "warranty" ,"color" ,"category" ,"status" ]
        
    def to_representation(self,instance):
        rep = super().to_representation(instance)
        rep["category"] = CategorySerializer(instance.category,many=True).data
        request = self.context.get('request')
        kwargs = request.parser_context.get('kwargs')
        if kwargs.get('pk') is None:
            rep.pop('content')
            
        return rep
        


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]