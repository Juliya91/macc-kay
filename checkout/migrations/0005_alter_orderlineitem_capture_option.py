# Generated by Django 4.0.1 on 2022-02-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='capture_option',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
