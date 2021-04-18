from django.db import models
from datetime import datetime, date


# Create your models here.
class Kyc_Info(models.Model):
    full_name = models.CharField(max_length=200)
    name_init = models.CharField(max_length=100)
    id_type = models.CharField(max_length=50)
    nics_no = models.CharField(max_length=50)
    driv_lic = models.CharField(max_length=50, blank=True, null=True)
    driv_exp = models.CharField(max_length=20, blank=True, null=True)
    pass_no = models.CharField(max_length=50, blank=True, null=True)
    pass_exp = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=50)
    nationality_other = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField('%Y-%m-%d')
    house_no = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    #country = models.CharField(max_length=20)
    mob_no = models.CharField(max_length=20)
    office_num = models.CharField(max_length=20, blank=True, null=True)
    home_num = models.CharField(max_length=20, blank=True, null=True)
    email_add = models.CharField(max_length=50, blank=True, null=True)
    occu_state = models.CharField(max_length=50, blank=True, null=True)




    """company_name = models.CharField(max_length=50)
    address_full = models.CharField(max_length=250)
    email_add = models.CharField(max_length=250)
    phone_num = models.CharField(max_length=12)
    long_text = models.TextField(max_length=255)"""


    def __str__(self):
        return self.full_name

class Kyc_Infotemp(models.Model):
    full_name_temp = models.CharField(max_length=200)
    name_init_temp = models.CharField(max_length=100)
    id_type_temp = models.CharField(max_length=50)
    nics_no_temp = models.CharField(max_length=50)
    driv_lic_temp = models.CharField(max_length=50, blank=True, null=True)
    driv_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    pass_no_temp = models.CharField(max_length=50, blank=True, null=True)
    pass_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    nationality_temp = models.CharField(max_length=50)
    nationality_other_temp = models.CharField(max_length=50, blank=True, null=True)
    #date_of_birth_temp = models.DateField('%Y-%m-%d', blank=True, null=True)
    date_of_birth_temp = models.CharField(max_length=20)
    house_no_temp = models.CharField(max_length=20)
    street_temp = models.CharField(max_length=20)
    city_temp = models.CharField(max_length=20)
    #country_temp = models.CharField(max_length=20)
    mob_no_temp = models.CharField(max_length=20)
    office_num_temp = models.CharField(max_length=20, blank=True, null=True)
    home_num_temp = models.CharField(max_length=20, blank=True, null=True)
    email_add_temp = models.CharField(max_length=50, blank=True, null=True)
    occu_state_temp = models.CharField(max_length=50)
    red_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    blue_flagadd_temp = models.CharField(max_length=5, blank=True, null=True)
    blue_flag_temp = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = "details"
    #def __str__(self):
        #return self.full_name_temp

class Id_Info(models.Model):
    nic_no = models.CharField(max_length=50)
    name_full = models.CharField(max_length=100)
    birth_day = models.DateField('%Y-%m-%d')
    house_num = models.CharField(max_length=20)
    street_add = models.CharField(max_length=20)
    city_ref = models.CharField(max_length=20)

    def __str__(self):
        return self.name_full