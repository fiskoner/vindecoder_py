# Generated by Django 3.0.8 on 2020-07-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vindecoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.RemoveField(
            model_name='car',
            name='year',
        ),
        migrations.AddField(
            model_name='car',
            name='wmi',
            field=models.CharField(db_column='wmi', default='', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='additionalCode',
            field=models.CharField(db_column='add_cod', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='additionalInfo',
            field=models.CharField(db_column='additional_info', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='bodyType',
            field=models.CharField(db_column='body_type', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(db_column='color', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='countryCode',
            field=models.CharField(db_column='country_code', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='countryName',
            field=models.CharField(db_column='country', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='engineCapacity',
            field=models.CharField(db_column='engine_capacity', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='engineKW',
            field=models.CharField(db_column='engine_kw', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.CharField(db_column='manufacturer', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='mark',
            field=models.CharField(db_column='mark', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='markOwner',
            field=models.CharField(db_column='mark_owner', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(db_column='model', default='', max_length=100),
        ),
        migrations.AlterModelTable(
            name='car',
            table='wmi_table',
        ),
    ]
