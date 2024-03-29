# Generated by Django 4.2.4 on 2024-02-14 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('product_image', models.ImageField(upload_to='products')),
                ('production_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField()),
                ('ratings', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapp.category')),
            ],
        ),
    ]
