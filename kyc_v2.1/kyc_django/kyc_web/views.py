from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import KycInfo
from django.contrib import messages


# Create your views here.

def index(request):
    all_kyc = KycInfo.objects.all()
    return render(request, "kyc_web/index.html", {'kyc_name': all_kyc})


def addkyc(request):
    return HttpResponse("<h2> you can add kyc</h2>")


def add_kyc_submit(request):
    print("submitted successfully.")
    name_init = request.POST["first_name"]
    full_name = request.POST["last_name"]
    company_name = request.POST["company_name"]
    address_full = request.POST["address"]
    email_add = request.POST["email_add"]
    phone_num = request.POST["phone_num"]
    long_text = request.POST["details_area"]

    if KycInfo.objects.filter(email_add=email_add).exists():
        messages.warning(request, 'email already exists')
        return redirect('index')

    else:

        kyc_info = KycInfo(name_init=name_init, full_name=full_name, company_name=company_name,
                           address_full=address_full, email_add=email_add, phone_num=phone_num, long_text=long_text)
        kyc_info.save()
        messages.success(request, 'Successfully submitted')
        return redirect('index')
        all_kyc = KycInfo.objects.all()

    return render(request, "index.html", {'kyc_name': all_kyc})
    # return render(request, "kyc_web/index.html")
