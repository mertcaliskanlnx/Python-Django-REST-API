# Generated by Django 3.2.4 on 2021-11-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=254)),
                ('product_price', models.FloatField()),
                ('product_quantitiy', models.PositiveIntegerField()),
            ],
        ),
    ]
