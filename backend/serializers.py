from rest_framework import serializers
from .models import *


class NewsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = News
        fields = '__all__'

class NewsCommentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = NewsComment
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = '__all__'

class SearchProductSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = ['id', 'name_uz', 'name_ru', 'name_en']

class OurWorkSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OurWork
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):    
    class Meta:
        model = FAQ
        fields = '__all__'