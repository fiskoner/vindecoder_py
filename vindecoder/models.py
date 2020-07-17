from django.db import models

class Car(models.Model):
    mark = models.CharField(max_length=100, default='', db_column='mark')
    wmi = models.CharField(max_length=100, default='', db_column='wmi', primary_key=True)
    additionalCode = models.CharField(max_length=100, default='', db_column='add_cod')
    manufacturer = models.CharField(max_length=100, default='', db_column='manufacturer')
    markOwner = models.CharField(max_length=100, default='', db_column='mark_owner')
    countryCode = models.CharField(max_length=100, default='', db_column='country_code')
    countryName = models.CharField(max_length=100, default='', db_column='country')
    additionalInfo = models.CharField(max_length=100, default='', db_column='additional_info')
    bodyType = models.CharField(max_length=100, default='', db_column='body_type')
    model = models.CharField(max_length=100, default='', db_column='model')
    engineCapacity = models.CharField(max_length=100, default='', db_column='engine_capacity')
    engineKW = models.CharField(max_length=100, default='', db_column='engine_kw')
    color = models.CharField(max_length=100, default='', db_column='color')
    # year = models.CharField(max_length=100, default='', db_column='year')

    class Meta:
        db_table = 'wmi_table'
# Create your models here.