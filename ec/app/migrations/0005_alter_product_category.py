# Generated by Django 5.0.4 on 2024-05-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_payment_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ML', 'SAMSUNG'), ('CR', 'XIAOMI'), ('LS', 'APPLE'), ('MS', 'MOTOROLA'), ('PN', 'TECNO'), ('GH', 'REALME'), ('CZ', 'VIVO'), ('IC', 'HONOR')], max_length=2),
        ),
    ]