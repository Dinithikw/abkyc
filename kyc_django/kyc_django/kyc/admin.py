from django.contrib import admin
from .models import Kyc_Info, Kyc_Infotemp, Id_Info, Image
# Register your models here.

admin.site.register(Kyc_Info)
admin.site.register(Kyc_Infotemp)
admin.site.register(Id_Info)
admin.site.register(Image)