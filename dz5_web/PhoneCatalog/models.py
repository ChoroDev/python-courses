from django.db import models


class PhoneCatalog(models.Model):
    name = models.CharField(max_length = 255)
    reg_date = models.DateTimeField()
    address = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 30)