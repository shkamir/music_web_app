# Generated by Django 3.1.2 on 2020-10-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahang', '0003_auto_20201020_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('isRead', models.BooleanField()),
            ],
        ),
    ]
