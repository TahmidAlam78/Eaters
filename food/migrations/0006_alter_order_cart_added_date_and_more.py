# Generated by Django 4.0.2 on 2022-05-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_alter_order_cart_added_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart_added_date',
            field=models.DateTimeField(default='NULL'),
        ),
        migrations.AlterField(
            model_name='order',
            name='checkout_date',
            field=models.DateTimeField(default='NULL'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_complete_date',
            field=models.DateTimeField(default='NULL'),
        ),
    ]
