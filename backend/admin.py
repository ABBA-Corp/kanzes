from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
	pass 

class NewsCommentAdmin(admin.ModelAdmin):
	pass 

class CategoryAdmin(admin.ModelAdmin):
	pass 

class ProductAdmin(admin.ModelAdmin):
	pass 

class OurWorkAdmin(admin.ModelAdmin):
	pass 

class FAQAdmin(admin.ModelAdmin):
	pass 

admin.site.register(News, NewsAdmin)
admin.site.register(NewsComment, NewsCommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OurWork, OurWorkAdmin)
admin.site.register(FAQ, FAQAdmin)