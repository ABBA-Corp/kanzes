# Generated by Django 4.1.7 on 2023-02-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_category_table_alter_faq_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to='news'),
        ),
        migrations.AlterField(
            model_name='ourwork',
            name='image',
            field=models.ImageField(blank=True, upload_to='our_work'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
    ]
