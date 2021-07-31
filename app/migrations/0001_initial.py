# Generated by Django 3.2.5 on 2021-07-31 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='allimg')),
                ('like', models.BooleanField(default=False)),
            ],
        ),
    ]