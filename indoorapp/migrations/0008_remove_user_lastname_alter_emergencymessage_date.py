# Generated by Django 4.1.7 on 2023-04-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indoorapp', '0007_alter_shop_x_axis_alter_shop_y_axis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='emergencymessage',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
