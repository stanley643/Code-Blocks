# Generated by Django 4.1.7 on 2023-02-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('short_id', models.CharField(max_length=10)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]