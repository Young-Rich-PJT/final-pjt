# Generated by Django 3.2.18 on 2023-05-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finlife', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agerecommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.CharField(max_length=255)),
                ('field_10', models.IntegerField(default=0)),
                ('field_20', models.IntegerField(default=0)),
                ('field_30', models.IntegerField(default=0)),
                ('field_40', models.IntegerField(default=0)),
                ('field_50', models.IntegerField(default=0)),
                ('field_60', models.IntegerField(default=0)),
                ('field_70', models.IntegerField(default=0)),
                ('field_80', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AssetRecommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.CharField(max_length=255)),
                ('field_1000', models.IntegerField(default=0)),
                ('field_2000', models.IntegerField(default=0)),
                ('field_3000', models.IntegerField(default=0)),
                ('field_4000', models.IntegerField(default=0)),
                ('field_5000', models.IntegerField(default=0)),
                ('field_6000', models.IntegerField(default=0)),
                ('field_7000', models.IntegerField(default=0)),
                ('field_8000', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SalaryRecommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.CharField(max_length=255)),
                ('field_100', models.IntegerField(default=0)),
                ('field_200', models.IntegerField(default=0)),
                ('field_300', models.IntegerField(default=0)),
                ('field_400', models.IntegerField(default=0)),
                ('field_500', models.IntegerField(default=0)),
                ('field_600', models.IntegerField(default=0)),
                ('field_700', models.IntegerField(default=0)),
                ('field_800', models.IntegerField(default=0)),
            ],
        ),
    ]
