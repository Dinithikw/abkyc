from django.db import models


# Create your models here.
class KycInfo(models.Model):
    name_init = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=50)
    address_full = models.CharField(max_length=250)
    email_add = models.CharField(max_length=250)
    phone_num = models.CharField(max_length=12)
    long_text = models.TextField(max_length=255)

    def __str__(self):
        return self.name_init
