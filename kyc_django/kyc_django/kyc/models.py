from django.db import models
from datetime import datetime, date


# Create your models here.
class Kyc_Info(models.Model):
    salutation = models.CharField(max_length=5)
    full_name = models.CharField(max_length=200)
    name_init = models.CharField(max_length=100)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile_pic/")
    # profile_vid = models.ImageField(null=True, blank=True, upload_to="images/profile_pic/")
    id_type = models.CharField(max_length=50)
    nics_no = models.CharField(max_length=50)
    date_of_birth = models.DateField('%Y-%m-%d')
    driv_lic = models.CharField(max_length=50, blank=True, null=True)
    driv_exp = models.CharField(max_length=20, blank=True, null=True)
    pass_no = models.CharField(max_length=50, blank=True, null=True)
    pass_exp = models.CharField(max_length=20, blank=True, null=True)
    birth_cernum = models.CharField(max_length=10, blank=True, null=True)
    post_id = models.CharField(max_length=10, blank=True, null=True)
    oafsc = models.CharField(max_length=10, blank=True, null=True)
    visa_copy = models.ImageField(null=True, blank=True, upload_to="images/visa_copy/")
    othe_identity_doc = models.ImageField(null=True, blank=True, upload_to="images/other_doc/")
    nationality = models.CharField(max_length=50)
    nationality_other = models.CharField(max_length=50, blank=True, null=True)
    type_of_visa = models.CharField(max_length=20,blank=True)
    visa_exp = models.CharField(max_length=20, blank=True, null=True)
    other_types = models.CharField(max_length=20,blank=True)
    other_exp = models.CharField(max_length=20, blank=True, null=True)
    foreign_addre = models.CharField(max_length=200, blank=True, null=True)
    vari_doc_type = models.CharField(max_length=200, blank=True, null=True)
    vari_doc = models.ImageField(null=True, blank=True, upload_to="images/vari_doc/")
    pep_person = models.CharField(max_length=200, blank=True, null=True)
    us_city = models.CharField(max_length=200, blank=True, null=True)

    # residential information
    resident_sri = models.CharField(max_length=10, blank=True, null=True)
    country_resident =models.CharField(blank=True, max_length=50)

    # current Address
    house_no = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    state_address = models.CharField(max_length=20, blank=True, null=True)

    # permenent Address
    house_no_per = models.CharField(max_length=20)
    street_per = models.CharField(max_length=20)
    city_per = models.CharField(max_length=20)
    postal_code_per = models.CharField(max_length=10, blank=True, null=True)
    
    # contact infromation
    mob_no = models.CharField(max_length=20)
    office_num = models.CharField(max_length=20, blank=True, null=True)
    home_num = models.CharField(max_length=20, blank=True, null=True)
    email_add = models.CharField(max_length=50, blank=True, null=True)
    email_add_temp = models.CharField(max_length=50, blank=True, null=True)

    
    




    """company_name = models.CharField(max_length=50)
    address_full = models.CharField(max_length=250)
    email_add = models.CharField(max_length=250)
    phone_num = models.CharField(max_length=12)
    long_text = models.TextField(max_length=255)"""


    def __str__(self):
        return self.full_name

class Kyc_Infotemp(models.Model):
    
    salutation_temp = models.CharField(max_length=5)
    full_name_temp = models.CharField(max_length=200)
    name_init_temp = models.CharField(max_length=100)
    profile_pic_temp = models.ImageField(null=True, blank=True, upload_to="images/")
    id_type_temp = models.CharField(max_length=50)
    nics_no_temp = models.CharField(max_length=50)
    date_of_birth_temp = models.DateField('%Y-%m-%d')
    driv_lic_temp = models.CharField(max_length=50, blank=True, null=True)
    driv_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    pass_no_temp = models.CharField(max_length=50, blank=True, null=True)
    pass_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    birth_cernum_temp = models.CharField(max_length=10, blank=True, null=True)
    post_id_temp = models.CharField(max_length=10, blank=True, null=True)
    oafsc_temp = models.CharField(max_length=10, blank=True, null=True)
    visa_copy_temp = models.ImageField(null=True, blank=True, upload_to="images/")
    othe_identity_doc_temp = models.ImageField(null=True, blank=True, upload_to="images/")
    nationality_temp = models.CharField(max_length=50)
    nationality_other_temp = models.CharField(max_length=50, blank=True, null=True)
    type_of_visa_temp = models.CharField(max_length=20,blank=True)
    visa_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    other_types_temp = models.CharField(max_length=20,blank=True)
    other_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    foreign_addre_temp = models.CharField(max_length=200, blank=True, null=True)
    vari_doc_type_temp = models.CharField(max_length=200, blank=True, null=True)
    vari_doc_temp = models.ImageField(null=True, blank=True, upload_to="images/")
    pep_person_temp = models.CharField(max_length=200, blank=True, null=True)
    us_city_temp = models.CharField(max_length=200, blank=True, null=True)

    # residential information
    resident_sri_temp = models.CharField(max_length=10, blank=True, null=True)
    country_resident_temp =models.CharField(blank=True, max_length=50)

    # current Address
    house_no_temp = models.CharField(max_length=20)
    street_temp = models.CharField(max_length=20)
    city_temp = models.CharField(max_length=20)
    postal_code_temp = models.CharField(max_length=10, blank=True, null=True)
    state_address_temp = models.CharField(max_length=20, blank=True, null=True)

    # permenent Address
    house_no_per_temp = models.CharField(max_length=20)
    street_per_temp = models.CharField(max_length=20)
    city_per_temp = models.CharField(max_length=20)
    postal_code_per_temp = models.CharField(max_length=10, blank=True, null=True)
    
    # contact infromation
    mob_no_temp = models.CharField(max_length=20)
    office_num_temp = models.CharField(max_length=20, blank=True, null=True)
    home_num_temp = models.CharField(max_length=20, blank=True, null=True)
    email_add_temp = models.CharField(max_length=50, blank=True, null=True)            #   -----------temp  email
    email_add_verification = models.CharField(max_length=50, blank=True, null=True)
    red_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    blue_flagadd_temp = models.CharField(max_length=5, blank=True, null=True)
    blue_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    

    class Meta:
        db_table = "Kyc_Infotemp"
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