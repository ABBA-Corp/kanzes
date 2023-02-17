from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('news', NewsView, basename='news')
router.register('news_comment', NewsCommentView, basename='news_comment')
router.register('category', CategoryView, basename='category')
router.register('product', ProductView, basename='product')
router.register('top_product', TopProductView, basename='top_product')
router.register('search_product', SearchProductView, basename='search_product')
router.register('our_work', OurWorkView, basename='our_work')
router.register('FAQ', FAQView, basename='FAQ')

urlpatterns = [
    path('', include(router.urls)),
]