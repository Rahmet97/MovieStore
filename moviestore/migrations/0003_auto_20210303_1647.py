# Generated by Django 3.1.7 on 2021-03-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviestore', '0002_auto_20210303_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='batafsil',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='reyting',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='upload_date',
            field=models.DateField(auto_now=True, verbose_name='Yuklangan sanasi'),
        ),
    ]