# Generated by Django 2.2.10 on 2021-05-16 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kyc', '0003_remove_historicalkyc_info_blue_flag_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalkyc_info',
            name='blue_flagadd_temp',
        ),
        migrations.RemoveField(
            model_name='historicalkyc_info',
            name='red_flag_temp',
        ),
    ]