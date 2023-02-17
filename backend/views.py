from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import *
from .models import *

class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticated]

class NewsCommentView(viewsets.ModelViewSet):
    queryset = NewsComment.objects.all()
    serializer_class = NewsCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class TopProductView(viewsets.ModelViewSet):
    queryset = Product.objects.filter(top = True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class SearchProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = SearchProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class OurWorkView(viewsets.ModelViewSet):
    queryset = OurWork.objects.all()
    serializer_class = OurWorkSerializer
    permission_classes = [permissions.IsAuthenticated]

class FAQView(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [permissions.IsAuthenticated]