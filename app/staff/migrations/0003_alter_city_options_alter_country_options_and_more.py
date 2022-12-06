# Generated by Django 4.1.3 on 2022-12-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_continent_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name': 'Офис', 'verbose_name_plural': 'Офисы'},
        ),
        migrations.AlterModelOptions(
            name='persons',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Регион', 'verbose_name_plural': 'Регионы'},
        ),
        migrations.AlterField(
            model_name='city',
            name='title',
            field=models.CharField(max_length=500, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='continent',
            name='title',
            field=models.CharField(max_length=500, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='country',
            name='title',
            field=models.CharField(max_length=500, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='office',
            name='title',
            field=models.CharField(max_length=500, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='region',
            name='title',
            field=models.CharField(max_length=500, null=True, verbose_name='Название'),
        ),
    ]
