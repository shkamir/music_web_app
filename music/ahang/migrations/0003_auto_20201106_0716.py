# Generated by Django 3.1.2 on 2020-11-06 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ahang', '0002_auto_20201105_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdb',
            name='ahnag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ahang.ahang'),
        ),
    ]
