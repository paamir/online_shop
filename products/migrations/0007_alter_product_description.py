# Generated by Django 4.2.5 on 2023-09-17 20:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_comment_modified_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='product description'),
        ),
    ]
