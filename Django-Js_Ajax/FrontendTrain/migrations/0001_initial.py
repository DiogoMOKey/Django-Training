# Generated by Django 4.1.2 on 2022-12-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('release_on', models.DateField()),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
