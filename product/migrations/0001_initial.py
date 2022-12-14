# Generated by Django 4.0.6 on 2022-11-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('discount', models.SmallIntegerField()),
                ('image', models.ImageField(upload_to='products')),
                ('color', models.ManyToManyField(related_name='products', to='product.color')),
                ('size', models.ManyToManyField(blank=True, null=True, related_name='products', to='product.size')),
            ],
        ),
    ]
