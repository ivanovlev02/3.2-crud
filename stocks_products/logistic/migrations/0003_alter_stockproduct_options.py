# Generated by Django 5.0.7 on 2024-07-29 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_alter_product_options_alter_stock_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockproduct',
            options={'ordering': ['stock'], 'verbose_name': 'склад', 'verbose_name_plural': 'Остатки складов'},
        ),
    ]