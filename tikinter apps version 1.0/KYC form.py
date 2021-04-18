#improting tkiner
import tkinter as tk

from tkinter import *

from tkinter import ttk,messagebox
#pip install pillow
from PIL import Image,ImageTk 

#pip istall pymysql
import pymysql


#===============================================================================================================================
#creating class call expences
class expences:
    def __init__(self,root):
        self.root=root
        self.root.title("KYC Window")
        self.root.geometry("2080x1820")
        self.root.config(bg="white")
    

        #background image

        self.bg=ImageTk.PhotoImage(file="background/2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #background left image

        #self.left=ImageTk.PhotoImage(file="background/3.jpg")
        #left=Label(self.root,image=self.left).place(x=80,y=150,width=400,height=500)


#======================================================================================================================================

        #creating frame
        frame1=Frame(root,bg="white")
        frame1.place(x=250,y=50,width=1000,height=2000)
      
#====================================================================================================================================
        
        
        #customizing inside the frame

        #adding  title
        title=Label(frame1,text="Know your Customer(KYC) profile form – (Individual)",font=("times new roman",20,"bold"),bg="white",fg="Black").place(x=150,y=30)

        #date
        date=Label(frame1,text="Date",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=96)
        self.date=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.date.place(x=780,y=100,width=200)

        #account no.
        account_no=Label(frame1,text="A/C No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=136)
        self.account_no=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.account_no.place(x=780,y=140,width=200)

         #Branch No
        Branch_No=Label(frame1,text="Branch No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=176)
        self.Branch_No=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Branch_No.place(x=780,y=180,width=200)

         #Officer’s S/No
        Officer_S_No=Label(frame1,text="Officer’s S/No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=216)
        self.Officer_S_No=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Officer_S_No.place(x=780,y=220,width=200)

         #Manager_ INTL
        Manager_INTL=Label(frame1,text="Manager’s INTL",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=256)
        self.Manager_INTL=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Manager_INTL.place(x=780,y=260,width=200)

       

        #adding section A title
        title=Label(frame1,text="Section A – Identity Information",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=310)
        
        #adding section A titles

        #row 1 -------->>>

        #Name with Initials
        Name_with_Initials=Label(frame1,text="Name with Initials",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=350)
        self.Name_with_Initials=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Name_with_Initials.place(x=350,y=350,width=250)

        #row 2------>>>

        #Initials Standard For
        Initials_Standard_For=Label(frame1,text="Initials Standard For",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=390)
        self.Initials_Standard_For=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Initials_Standard_For.place(x=350,y=390,width=250)     
        
        #row 3------>>>

        #Date of Birth
        DOB=Label(frame1,text="Date of Birth",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=430)
        self.DOB=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.DOB.place(x=350,y=430,width=250) 

        #row 4------>>>

        #Gender
        Gender=Label(frame1,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=470)
         
        #row 5------>>>

        #Marital Status
        Marital_Status=Label(frame1,text="Marital Status",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=510)
       
        #row 6------>>>

        #Nationality
        Nationality=Label(frame1,text="Nationality",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=550)
        self.Nationality=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Nationality.place(x=350,y=550,width=250)    
         
        #row 7------>>>

        #other residance
        other_residance=Label(frame1,text="Are you a citizen/resident of any other country",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=590)
         
        #row 8------>>>

        #yes state
        yes_state=Label(frame1,text="If ‘Yes’ please state",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=630)
        self.yes_state=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.yes_state.place(x=350,y=630,width=250)   
       
        #adding section B title
        title=Label(frame1,text="Section B – Proof of Identity (if you have)",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=670)
        
        #adding section B titles

        #row 1 -------->>>

        #National ID Card No.
        NIC=Label(frame1,text="National ID Card No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=710)
        self.NIC=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.NIC.place(x=350,y=710,width=250)

        #row 2------>>>

        #Passport No.
        Passport_No=Label(frame1,text="Passport No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=750)
        self.Passport_No=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Passport_No.place(x=350,y=750,width=250)     
        
        #Expiration
        Expiration=Label(frame1,text="Expiration Date",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=200,y=750)
        self.Expiration=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Expiration.place(x=350,y=750,width=250)

        #row 3------>>>

        #Driving License No.
        Driving_License_No=Label(frame1,text=" Driving License No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=750)
        self.Driving_License_No=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Driving_License_No.place(x=350,y=750,width=250) 

        #Expirations
        Expirations=Label(frame1,text="Expiration Date",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=200,y=750)
        self.Expirations=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Expirations.place(x=350,y=750,width=250)


        #adding section C titles
        title=Label(frame1,text="Section C – Address Information (Residential/Permanent Address)",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=790)
        #row 1 ------>>>

        #Address Line 01

        Address_Line_1=Label(frame1,text="Address_Line_1",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=840)
        self.Address_Line_1=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Address_Line_1.place(x=350,y=840,width=250)

        #row 2 ------>>>

        Address_Line_2=Label(frame1,text="Address_Line_2",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=880)
        self.Address_Line_2=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Address_Line_2.place(x=350,y=880,width=250)

        #row 3 ------>>>

        Address_Line_3=Label(frame1,text="Address_Line_3",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=920)
        self.Address_Line_3=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Address_Line_3.place(x=350,y=920,width=250)

        #row 4 ------>>>

        country=Label(frame1,text="Country",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=960)
        self.country=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.country.place(x=350,y=960,width=250)



        #adding section D titles
        title=Label(frame1,text="Section D – Contact Information",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=1000)
        #row 1 ------>>>

        #Home tel. No.

        Home_Tel=Label(frame1,text="Home Tel. No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=1040)
        self.Home_Tel=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Home_Tel.place(x=350,y=1040,width=250)

        #Mobile No.

        Mobile_No=Label(frame1,text="Mobile No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1040)
        self.Mobile_No=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Mobile_No.place(x=780,y=1040,width=200)

        #row 2 ------>>>

        #work place tel. No.

        Work_Tel=Label(frame1,text="Work Place Tel. No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=1080)
        self.Work_Tel=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Work_Tel.place(x=350,y=1080,width=250)

        #E-mail

        Email=Label(frame1,text="E-mail",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1080)
        self.Email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Email.place(x=780,y=1080,width=200)


        #adding section E titles
        title=Label(frame1,text="Section E – Employment Information",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=1120)
        #row 1 ------>>>
        
        
        #Employee Status
        date=Label(frame1,text="Date",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1140)
        



#SPACE TO ADD CHECK BOXES




        #occupation
        Occupation=Label(frame1,text="Occupation",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1250)
        self.Occupation=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Occupation.place(x=350,y=1250,width=200)

        #job title
        Job_Title=Label(frame1,text="Job Title",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1290)
        self.Job_Title=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Job_Title.place(x=350,y=1290,width=200)

        #Industry
        Industry=Label(frame1,text="Industry",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1330)
        self.Industry=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Industry.place(x=350,y=1330,width=200)

        #length of services
        Service_Length=Label(frame1,text="Length of Services",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1370)
        self.Service_Length=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Service_Length.place(x=350,y=1370,width=200)


        #adding section F titles
        title=Label(frame1,text="Section F – Purpose of Business Relationship",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=1400)
        
        #row 1 ------>>>
        
        #banking products
        Banking_Products=Label(frame1,text="Please indicate the banking products which relates to you",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1440)
        



        #SPACE TO ADD CHECK BOXES



      
        #adding section G titles
        title=Label(frame1,text="Section G – Customer Declaration and Certification",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=1460)
        
        #row 1 ------>>>
        
        #banking products
        Declaration=Label(frame1,text="I declare that the information furnished by me is true and correct and the company is entitled to verify the same either directly or through any third party agent. I also agree that if such declaration made by me are found to be incorrect, the company shall be entitled to terminate the account relationship. I confirm having read and understood the account rules and hereby agree to be bound by the terms and conditions and amendments governing the account(s) issued by the company from time to time.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1500) 


        #date
        date=Label(frame1,text="Date",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1540)
        self.date=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.date.place(x=350,y=1540,width=200)

        #Signature
        Signature=Label(frame1,text="Signature",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1580)
        self.Signature=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Signature.place(x=350,y=1580,width=200,height=20)



        #adding section H titles
        title=Label(frame1,text="Section H – For Office Use Only",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=1620)
        
        #row 1 ------>>>
        
        #Office Use
        Office_Use=Label(frame1,text="I checked the information that provide by the customer is correct.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1640) 


        #Name of thw officer
        Officer_Name=Label(frame1,text="Name of the Officer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=1680)
        self.Officer_Name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Officer_Name.place(x=400,y=1680,width=250)

        #Signature
        Signature=Label(frame1,text="Signature of the Officer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1720)
        self.Signature=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Signature.place(x=400,y=1720,width=200,height=20)

        #date
        date=Label(frame1,text="Date",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1760)
        self.date=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.date.place(x=400,y=1760,width=200)

        #Name of thw Manager
        Officer_Name=Label(frame1,text="Name of the Manager",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=1800)
        self.Officer_Name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Officer_Name.place(x=400,y=1800,width=250)

        #Signature
        Signature=Label(frame1,text="Signature of the Manager",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1840)
        self.Signature=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Signature.place(x=400,y=1840,width=200,height=20)

        #date
        date=Label(frame1,text="Date",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=600,y=1880)
        self.date=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.date.place(x=400,y=1880,width=200)
#=====================================================================================================================================

root=tk.Tk()
obj=expences(root)
root.mainloop()