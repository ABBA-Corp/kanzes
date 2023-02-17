from django.db import models

class News(models.Model):
	name_uz = models.CharField(max_length = 1000, blank = True)
	name_ru = models.CharField(max_length = 1000, blank = True)
	name_en = models.CharField(max_length = 1000, blank = True)
	description_uz = models.CharField(max_length = 10000, blank = True)
	description_ru = models.CharField(max_length = 10000, blank = True)
	description_en = models.CharField(max_length = 10000, blank = True)
	image = models.ImageField(upload_to = 'news', blank = True)
	date = models.CharField(max_length = 100, blank = True)

class NewsComment(models.Model):
	news_id = models.ForeignKey('News', on_delete = models.CASCADE, blank = True)
	author_uz = models.CharField(max_length = 1000, blank = True)
	author_ru = models.CharField(max_length = 1000, blank = True)
	author_en = models.CharField(max_length = 1000, blank = True)
	description_uz = models.CharField(max_length = 10000, blank = True)
	description_ru = models.CharField(max_length = 10000, blank = True)
	description_en = models.CharField(max_length = 10000, blank = True)
	date = models.CharField(max_length = 100, blank = True)

class Category(models.Model):
	name_uz = models.CharField(max_length = 1000, blank = True)
	name_ru = models.CharField(max_length = 1000, blank = True)
	name_en = models.CharField(max_length = 1000, blank = True)
	description_uz = models.CharField(max_length = 10000, blank = True)
	description_ru = models.CharField(max_length = 10000, blank = True)
	description_en = models.CharField(max_length = 10000, blank = True)
	image = models.ImageField(upload_to = 'category', blank = True)

class Product(models.Model):
	category_id = models.ForeignKey('Category', on_delete = models.CASCADE, blank = True)
	price = models.CharField(max_length = 100, blank = True)
	size = models.CharField(max_length = 100, blank = True)
	top = models.BooleanField(blank = True)
	name_uz = models.CharField(max_length = 1000, blank = True)
	name_ru = models.CharField(max_length = 1000, blank = True)
	name_en = models.CharField(max_length = 1000, blank = True)
	description_uz = models.CharField(max_length = 10000, blank = True)
	description_ru = models.CharField(max_length = 10000, blank = True)
	description_en = models.CharField(max_length = 10000, blank = True)
	image = models.ImageField(upload_to = 'product', blank = True)
	image1 = models.ImageField(upload_to = 'product', blank = True)
	image2 = models.ImageField(upload_to = 'product', blank = True)
	image3 = models.ImageField(upload_to = 'product', blank = True)
	color1 = models.CharField(max_length = 100, blank = True)
	color2 = models.CharField(max_length = 100, blank = True)
	color3 = models.CharField(max_length = 100, blank = True)
	color4 = models.CharField(max_length = 100, blank = True)
	title_uz = models.CharField(max_length = 1000, blank = True)
	title_ru = models.CharField(max_length = 1000, blank = True)
	title_en = models.CharField(max_length = 1000, blank = True)

class OurWork(models.Model):
	name_uz = models.CharField(max_length = 1000, blank = True)
	name_ru = models.CharField(max_length = 1000, blank = True)
	name_en = models.CharField(max_length = 1000, blank = True)
	description_uz = models.CharField(max_length = 10000, blank = True)
	description_ru = models.CharField(max_length = 10000, blank = True)
	description_en = models.CharField(max_length = 10000, blank = True)
	image = models.ImageField(upload_to = 'our_work', blank = True)

class FAQ(models.Model):
	question_uz = models.CharField(max_length = 1000, blank = True)
	question_ru = models.CharField(max_length = 1000, blank = True)
	question_en = models.CharField(max_length = 1000, blank = True)
	answer_uz = models.CharField(max_length = 10000, blank = True)
	answer_ru = models.CharField(max_length = 10000, blank = True)
	answer_en = models.CharField(max_length = 10000, blank = True)