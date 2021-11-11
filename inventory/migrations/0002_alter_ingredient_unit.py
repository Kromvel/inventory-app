# Generated by Django 3.2.7 on 2021-09-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('kg', 'кг'), ('tbsp', 'гр'), ('other', 'другое')], default='other', max_length=5),
        ),
    ]