# Generated by Django 4.1.7 on 2023-03-22 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indoorapp', '0002_category_remove_notification_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='shop_id',
            field=models.ForeignKey(default=35, on_delete=django.db.models.deletion.CASCADE, to='indoorapp.shop'),
        ),
    ]
