from django.shortcuts import render, redirect
from .models import Kyc_Info, Kyc_Infotemp, Id_Info
from django.contrib import messages

from .forms import update_forms


# define method for calling pages
# -----------------------------------------------------------------------------------------------------------------------

def index(request):
    return render(request, 'kyc/index.html')


def account(request):
    return render(request, 'kyc/(2nd)AccEmp.html')


def personal(request):
    return render(request, 'kyc/(3rd)Declaration.html')


def office(request):
    return render(request, 'kyc/(4th)office.html')


# defining function to filter and display flagged records in update.html
def update(request):
    result = Kyc_Infotemp.objects.filter(blue_flagadd_temp=True)
    result2 = Kyc_Infotemp.objects.filter(blue_flag_temp=True)
    result3 = Kyc_Infotemp.objects.filter(red_flag_temp=True)

    # passing variables to the update.html using dictionary
    return render(request, "kyc/update.html", {"Kyc_Infotemp1": result, "Kyc_Infotemp2": result2,
                                               "Kyc_Infotemp3": result3})


# defining function to get records using id through the database nad display in editing
def edit_val(request, id):
    update_val = Kyc_Infotemp.objects.get(id=id)

    return render(request, "kyc/edit.html", {"Kyc_Infotemp": update_val})


# defining database update function when click on update button
def update_data(request, id):
    updates_data = Kyc_Infotemp.objects.get(id=id)
    form = update_forms(request.POST, instance=updates_data)
    #print(form.errors)

    #print(updates_data)
    
    print(form)

    if form.is_valid():
        form.save()
        messages.success(request, "record update sucessfully")
        return render(request, "kyc/edit.html", {"Kyc_Infotemp": updates_data})


# -----------------------------------------------------------------------------------------------------------------------


# defining method to call accounts page and applying values to the variables
def insertkyc1(request):
    # *************variables of second form********************
    global occu_state

    occu_state = request.POST["Occutation_Status"]
    print(occu_state)
    print(full_name)
    print(name_init)

    if Kyc_Info.objects.filter(nics_no=nics_no).exists():
        submit_kyc_temp = Kyc_Infotemp(full_name_temp=full_name, name_init_temp=name_init, id_type_temp=id_type,
                                       nics_no_temp=nics_no, driv_lic_temp=driv_lic,
                                       pass_no_temp=pass_no, nationality_temp=nationality,
                                       nationality_other_temp=nationality_other, house_no_temp=house_no,
                                       street_temp=street,
                                       city_temp=city, mob_no_temp=mob_no, office_num_temp=office_num,
                                       home_num_temp=home_num,
                                       email_add_temp=email_add,
                                       occu_state_temp=occu_state, date_of_birth_temp=date_of_birth,
                                       driv_exp_temp=driv_exp,
                                       blue_flagadd_temp=green_flag, blue_flag_temp=blue_flag)
        submit_kyc_temp.save()
        messages.success(request, 'saved look')
        return render(request, 'kyc/(2nd)AccEmp.html')

    else:

        if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name, birth_day=date_of_birth,
                                  house_num=house_no,
                                  street_add=street, city_ref=city).exists():

            submit_kyc = Kyc_Info(full_name=full_name, name_init=name_init, id_type=id_type, nics_no=nics_no,
                                  driv_lic=driv_lic,
                                  pass_no=pass_no, nationality=nationality,
                                  nationality_other=nationality_other, house_no=house_no, street=street,
                                  city=city, mob_no=mob_no, office_num=office_num, home_num=home_num,
                                  email_add=email_add,
                                  occu_state=occu_state, date_of_birth=date_of_birth, driv_exp=driv_exp)
            submit_kyc.save()
            messages.success(request, 'Successfully saved')

            return render(request, 'kyc/(2nd)AccEmp.html')
        else:

            submit_kyc_temp = Kyc_Infotemp(full_name_temp=full_name, name_init_temp=name_init, id_type_temp=id_type,
                                           nics_no_temp=nics_no, driv_lic_temp=driv_lic,
                                           pass_no_temp=pass_no, nationality_temp=nationality,
                                           nationality_other_temp=nationality_other, house_no_temp=house_no,
                                           street_temp=street,
                                           city_temp=city, mob_no_temp=mob_no, office_num_temp=office_num,
                                           home_num_temp=home_num,
                                           email_add_temp=email_add,
                                           occu_state_temp=occu_state, date_of_birth_temp=date_of_birth,
                                           driv_exp_temp=driv_exp, red_flag_temp=red_flag,
                                           blue_flagadd_temp=green_flag, blue_flag_temp=blue_flag)
            submit_kyc_temp.save()
            messages.success(request, 'saved look')
            return render(request, 'kyc/(2nd)AccEmp.html')


def insertkyc(request):

    print("successfully completed")

    # definging global variables
    # -----------------------------------------------------------------------------------------------------------------------

    # ***************** variables of personal information first form ***************

    global full_name, name_init, id_type, nics_no, driv_lic, driv_exp, pass_no, pass_exp, nationality
    global nationality_other, date_of_birth

    # global full_name_temp, name_init_temp, date_of_birth_temp

    # variables of residential details
    global house_no, street, city

    # variables of contact information
    global mob_no, office_num, home_num, email_add

    # variable for flags
    global green_flag, blue_flag, red_flag
    green_flag = False
    blue_flag = False
    red_flag = False

    # calling variables for form inputs in personal detail section
    full_name = request.POST["fullname"]
    name_init = request.POST["nwi"]
    id_type = request.POST["ID_type"]
    nics_no = request.POST["NIC"]
    driv_lic = request.POST["driving_license"]
    driv_exp = request.POST["drive_exp"]
    pass_no = request.POST["passport"]
    pass_exp = request.POST["passport_exp"]
    nationality = request.POST["Nationality"]
    nationality_other = request.POST["Nationality_other"]
    date_of_birth = request.POST["birthday"]

    # calling variables for form inputs in residential detail section
    house_no = request.POST["house_number"]
    street = request.POST["street"]
    city = request.POST["city"]

    # calling variables for form inputs in contact detail section
    mob_no = request.POST["mobile_number"]
    office_num = request.POST["office_number"]
    home_num = request.POST["home_number"]
    email_add = request.POST["email"]

    # checking is there ID exists in Identity information database
    if Id_Info.objects.filter(nic_no=nics_no).exists():

        # if exists id number proceed to next step
        messages.success(request, 'NIC validated successfully')

        # check whether there are existing kyc in the database to the given id number
        if Kyc_Info.objects.filter(nics_no=nics_no).exists():

            # if true for existing kyc
            # messages.success(request, 'existing kyc')

            # check whether the full name is similar to id info database
            if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name).exists():

                # return to next page
                # return render(request, 'kyc/(2nd)AccEmp.html')

                # give an message if name is true
                # messages.success(request, 'existing kyc, name true')

                # check if birthday is true according to id info database
                if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name, birth_day=date_of_birth).exists():

                    # giving a message if dob is true
                    # messages.success(request, 'existing kyc, name true,dob ture')

                    if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name, birth_day=date_of_birth,
                                              house_num=house_no,
                                              street_add=street, city_ref=city).exists():

                        messages.success(request, 'existing kyc, name true, dob ture, address true')

                        green_flag = 'True'
                        print(green_flag)
                        return render(request, 'kyc/(2nd)AccEmp.html')

                    else:

                        messages.warning(request, 'existing kyc, name true,dob true, address false attach proof '
                                                  'document')

                        blue_flag = 'True'
                        return render(request, 'kyc/(2nd)AccEmp.html')



                # if date of birth is false
                else:
                    # give an error message
                    messages.warning(request, 'existing kyc, name true,dob false')
                    return render(request, 'kyc/index.html')
            else:
                # give an message if name is false
                messages.warning(request, 'existing kyc, name false')
                return render(request, 'kyc/index.html')

        else:

            print(full_name)
            print(name_init)
            print(id_type)
            print(nics_no)
            print(date_of_birth)
            print(driv_exp)

            # check whether the full name is similar to id info database
            if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name).exists():

                # return to next page
                # return render(request, 'kyc/(2nd)AccEmp.html')

                # give an message if name is true
                # messages.success(request, 'no kyc, name true')

                # check if birthday is true according to id info database
                if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name, birth_day=date_of_birth).exists():

                    # giving a message if dob is true
                    # messages.success(request, 'no kyc, name true,dob ture')

                    if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name, birth_day=date_of_birth,
                                              house_num=house_no,
                                              street_add=street, city_ref=city).exists():

                        messages.success(request, 'no kyc, name true, dob ture, address true')
                        return render(request, 'kyc/(2nd)AccEmp.html')

                    else:

                        messages.warning(request, 'no kyc, name true,dob true, address false attach proof '
                                                  'document')

                        red_flag = True

                        return render(request, 'kyc/(2nd)AccEmp.html')



                # if date of birth is false
                else:
                    # give an error message
                    messages.warning(request, 'no kyc, name true,dob false')
                    return render(request, 'kyc/index.html')
            else:
                # give an message if name is false
                messages.warning(request, 'no kyc, name false')
                return render(request, 'kyc/index.html')

            # messages.success(request, 'Successfully submitted')
            # return to next page
            # return render(request, 'kyc/(2nd)AccEmp.html')
            # return render(request, 'kyc/index.html')

    # it there is no id number in id information system give error message
    else:

        messages.warning(request, 'Invalid NIC Number. please check again')
        return render(request, 'kyc/index.html')

    """if request.method=='POST':
        if request.POST.get('ID_type'):
            savekyc = Kyc_info()
            savekyc = request.POST.get('ID_type')
            savekyc.save()
            messages.success(request, 'successful')
            return render(request, 'kyc/index.html')

    else:
        return render(request, 'kyc/index.html')"""
