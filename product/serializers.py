from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    size = serializers.StringRelatedField(many=True)
    color = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=True)
    class Meta:
        model =  models.Product
        fields = '__all__'
        
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  models.Size
        fields = '__all__'
        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model =  models.Color
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  models.Category
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(many=False)
    product = serializers.StringRelatedField(many=False)
    class Meta:
        model =  models.Review
        fields = '__all__'
