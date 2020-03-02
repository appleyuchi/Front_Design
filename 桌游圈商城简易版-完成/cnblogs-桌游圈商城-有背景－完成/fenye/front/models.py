from django.db import models

class TableName(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=512, blank=True, null=True)
    pic_path = models.CharField(max_length=64, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'table_name'
