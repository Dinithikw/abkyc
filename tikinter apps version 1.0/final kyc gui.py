#improting tkiner
import tkinter as tk

from tkinter import *
from tkinter import ttk,messagebox
#pip install pillow
from PIL import Image,ImageTk 

#pip istall pymysql
import pymysql


root = Tk()
root.title('Learn to code')
root.geometry("1800x1820")

#create a main frame

frame1 = Frame(root)
frame1.pack(fill=BOTH, expand=1)

#create a canvas

my_canvas = Canvas(frame1)
my_canvas.pack(side=LEFT, fill = BOTH, expand=1)

#add a scroll bar to the canvas

my_scrollbar = ttk.Scrollbar(frame1,orient = VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#configure the canvas

my_canvas.configure(yscrollcommand = my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

#create another frama INSIDE thr canvas

second_frame = Frame(my_canvas, bg = "lightsteelblue")


#add that new frame to a window in the canvas

my_canvas.create_window((0,0), window = second_frame, anchor="nw")

 #background image

#second_frame.bg=ImageTk.PhotoImage(file="background/3.jpg")
#bg=Label(second_frame,image=second_frame.bg).place(x=0,y=0,relwidth=1,relheight=1)


for thing in range(60):
    Button(second_frame, text=f'Button {thing} Yo!!').grid(row=thing, column=2000, pady=10, padx=2000)

#my_label = Label(second_frame, text="Know your Customer(KYC) profile form – (Individual)").grid(row=1, column=2500)


#adding  title
title=Label(second_frame,text="Know Your Customer(KYC) Profile Form – (Individual)",font=("times new roman",25,"bold","underline"),bg="lightsteelblue",fg="black").place(x=400,y=30)

#adding section A title
title=Label(second_frame,text="       Section A – Identity Information        ",font=("times new roman",20,"bold"),bg="mediumpurple",fg="white").place(x=250,y=290)
        
#adding section A titles


#Name with Initials
Name_with_Initials=Label(second_frame,text="Name with Initials",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=340)
second_frame.Name_with_Initials=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Name_with_Initials.place(x=500,y=340,width=800)


#Name in Full
Name_in_Full=Label(second_frame,text="Name in Full",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=380)
second_frame.Name_in_Full=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Name_in_Full.place(x=500,y=380,width=800)

#Identity Recognition
ir=Label(second_frame,text="Identity Recognition",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=420)


clicked = StringVar()
clicked.set("<--- Select Category --->")

drop = OptionMenu(second_frame, clicked ,"             NIC             ",
                                         "             Passport             ",
                                         "             Driving License             ")

drop.place(x=500,y=420)
drop.config(width = 27)

#National ID
NIC=Label(second_frame,text="National ID",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=500,y=470)
second_frame.NIC=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.NIC.place(x=500,y=500,width=200)

#Passport
Passport=Label(second_frame,text="Passport No.",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=500,y=550)
second_frame.Passport=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Passport.place(x=500,y=580,width=200)

#Expiration Date
Exp_pass=Label(second_frame,text="Expiration Date",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=800,y=550)
second_frame.Exp_pass=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Exp_pass.place(x=800,y=580,width=200)

#Driving License No.
driving_license=Label(second_frame,text="Driving License No.",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=500,y=630)
second_frame.driving_license=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.driving_license.place(x=500,y=660,width=200)

#Expiration Date
Exp_drive=Label(second_frame,text="Expiration Date",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=800,y=630)
second_frame.Exp_drive=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Exp_drive.place(x=800,y=660,width=200)

#Nationality
Nationality=Label(second_frame,text="Nationality",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=700)
second_frame.Nationality=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Nationality.place(x=500,y=700,width=200)

#Date od Birth
DOB=Label(second_frame,text="Date or Birth",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=740)
second_frame.DOB=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.DOB.place(x=500,y=740,width=200)


#adding section B title
title=Label(second_frame,text="Section B – Contact Information",font=("times new roman",20,"bold"),bg="mediumpurple",fg="white").place(x=250,y=800)

#House No.
House_No=Label(second_frame,text="House No.",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=850)
second_frame.House_No=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.House_No.place(x=500,y=850,width=350)

#Street
Street=Label(second_frame,text="Street",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=890)
second_frame.Street=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Street.place(x=500,y=890,width=350)

#City
City=Label(second_frame,text="City",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=930)
second_frame.City=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.City.place(x=500,y=930,width=350)

#Postal Code
Postal_Code=Label(second_frame,text="Postal Code",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=970)
second_frame.Postal_Code=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Postal_Code.place(x=500,y=970,width=350)

#Country
country=Label(second_frame,text="Country",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=1010)
second_frame.country=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.country.place(x=500,y=1010,width=350)

#Mobile No.
Mobile_No=Label(second_frame,text="Mobile No.",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=1050)
second_frame.Mobile_No=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Mobile_No.place(x=500,y=1050,width=350)

#E-mail
Email=Label(second_frame,text="E-mail",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=1090)
second_frame.Email=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Email.place(x=500,y=1090,width=350)


#Have an account in bank ......?
Account=Label(second_frame,text="Do you have an account in bank ......?",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=260,y=1160)

clicked = StringVar()
clicked.set("<--- Select Choice --->")

drop = OptionMenu(second_frame, clicked ,"             Yes             ",
                                         "             No             ")

drop.place(x=600,y=1160)
drop.config(width = 27)


#If Yes
If_Yes=Label(second_frame,text="If 'Yes', Please Select Your Account Type",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=450,y=1200)

second_frame.var1 = IntVar()
Checkbutton(second_frame, text="Fixed Deposite", variable=second_frame.var1, bg="lightsteelblue").place(x=400,y=1240)
second_frame.var2 = IntVar()
Checkbutton(second_frame, text="Mutual Fund Account", variable=second_frame.var2, bg="lightsteelblue").place(x=400,y=1280)
second_frame.var3 = IntVar()
Checkbutton(second_frame, text="Foreign Exchange", variable=second_frame.var3, bg="lightsteelblue").place(x=400,y=1320)
second_frame.var4 = IntVar()
Checkbutton(second_frame, text="Lease", variable=second_frame.var4, bg="lightsteelblue").place(x=650,y=1240)
second_frame.var5 = IntVar()
Checkbutton(second_frame, text="Vehicle Loan", variable=second_frame.var5, bg="lightsteelblue").place(x=650,y=1280)
second_frame.var6 = IntVar()
Checkbutton(second_frame, text="Mortage Loan", variable=second_frame.var6, bg="lightsteelblue").place(x=650,y=1320)
second_frame.var7 = IntVar()
Checkbutton(second_frame, text="Consumer Loans", variable=second_frame.var7, bg="lightsteelblue").place(x=850,y=1240)
second_frame.var8 = IntVar()
Checkbutton(second_frame, text="Commercial Loan", variable=second_frame.var8, bg="lightsteelblue").place(x=850,y=1280)
second_frame.var9 = IntVar()
Checkbutton(second_frame, text="Savings Account", variable=second_frame.var9, bg="lightsteelblue").place(x=850,y=1320)



#Purpose of the acoount
If_Yes=Label(second_frame,text="Purpose of the Account",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=650,y=1370)

second_frame.var1 = IntVar()
Checkbutton(second_frame, text="Business Transactions", variable=second_frame.var1, bg="lightsteelblue").place(x=500,y=1400)
second_frame.var2 = IntVar()
Checkbutton(second_frame, text="Mutual Fund Account", variable=second_frame.var2, bg="lightsteelblue").place(x=500,y=1440)
second_frame.var3 = IntVar()
Checkbutton(second_frame, text="Employeement/Professional Income", variable=second_frame.var3, bg="lightsteelblue").place(x=500,y=1480)
second_frame.var4 = IntVar()
Checkbutton(second_frame, text="Rare Transactions", variable=second_frame.var4, bg="lightsteelblue").place(x=500,y=1520)
second_frame.var5 = IntVar()
Checkbutton(second_frame, text="Upkeep of Family/Person", variable=second_frame.var5, bg="lightsteelblue").place(x=800,y=1400)
second_frame.var6 = IntVar()
Checkbutton(second_frame, text="Utility Bill Payment", variable=second_frame.var6, bg="lightsteelblue").place(x=800,y=1440)
second_frame.var7 = IntVar()
Checkbutton(second_frame, text="Savings", variable=second_frame.var7, bg="lightsteelblue").place(x=800,y=1480)
second_frame.var8 = IntVar()
Checkbutton(second_frame, text="Loan Repayment", variable=second_frame.var8, bg="lightsteelblue").place(x=800,y=1520)


#adding section C title
title=Label(second_frame,text="Section C – Employee Information",font=("times new roman",20,"bold"),bg="mediumpurple",fg="white").place(x=250,y=1560)


#Occupation Status
os=Label(second_frame,text="Occupation Status",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=250,y=1600)


clicked = StringVar()
clicked.set("<--- Select Category --->")

drop = OptionMenu(second_frame, clicked ,"             Salaried Worker             ",
                                         "             Retire             ",
                                         "             Self Employee             ",
                                         "             Un-Employeed             ",
                                         "             Student             ")

drop.place(x=500,y=1600)
drop.config(width = 27)



#Occupation
Occupation=Label(second_frame,text="Occupation",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=250,y=1650)
second_frame.Occupation=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Occupation.place(x=500,y=1650,width=800)



#Source of Income
If_Yes=Label(second_frame,text="Source of Income",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=350,y=1700)

second_frame.var1 = IntVar()
Checkbutton(second_frame, text="Sales and Business Turnover", variable=second_frame.var1, bg="lightsteelblue").place(x=400,y=1740)
second_frame.var2 = IntVar()
Checkbutton(second_frame, text="Family Remittances", variable=second_frame.var2, bg="lightsteelblue").place(x=400,y=1780)
second_frame.var3 = IntVar()
Checkbutton(second_frame, text="Commission Income", variable=second_frame.var3, bg="lightsteelblue").place(x=400,y=1820)
second_frame.var4 = IntVar()
Checkbutton(second_frame, text="Export Proceeds", variable=second_frame.var4, bg="lightsteelblue").place(x=400,y=1860)
second_frame.var5 = IntVar()
Checkbutton(second_frame, text="Contract Proceeds", variable=second_frame.var5, bg="lightsteelblue").place(x=800,y=1740)
second_frame.var6 = IntVar()
Checkbutton(second_frame, text="Donations/Charities(Local/Foreign)", variable=second_frame.var6, bg="lightsteelblue").place(x=800,y=1780)
second_frame.var7 = IntVar()
Checkbutton(second_frame, text="Salary/Profit Income", variable=second_frame.var7, bg="lightsteelblue").place(x=800,y=1820)
second_frame.var8 = IntVar()
Checkbutton(second_frame, text="Investment Proceeds", variable=second_frame.var8, bg="lightsteelblue").place(x=800,y=1860)
second_frame.var9 = IntVar()
Checkbutton(second_frame, text="Other", variable=second_frame.var9, bg="lightsteelblue").place(x=600,y=1900)

second_frame.Occupation=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Occupation.place(x=750,y=1900,width=200)



#Average Income
ai=Label(second_frame,text="Average Income",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=250,y=1950)


clicked = StringVar()
clicked.set("<--- Select Category --->")

drop = OptionMenu(second_frame, clicked ,"             Less than 100,000             ",
                                         "             100,001 - 500,000             ",
                                         "             500,001 - 1,000,000             ",
                                         "             Above 1,000,000             ")

drop.place(x=500,y=1950)
drop.config(width = 27)



#Mode of Transaction
MOT=Label(second_frame,text="Mode of Transaction",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=350,y=2000)

second_frame.var1 = IntVar()
Checkbutton(second_frame, text="Cash", variable=second_frame.var1, bg="lightsteelblue").place(x=400,y=2040)
second_frame.var2 = IntVar()
Checkbutton(second_frame, text="Cheque", variable=second_frame.var2, bg="lightsteelblue").place(x=400,y=2080)
second_frame.var3 = IntVar()
Checkbutton(second_frame, text="Standing Orders", variable=second_frame.var3, bg="lightsteelblue").place(x=400,y=2120)
second_frame.var4 = IntVar()
Checkbutton(second_frame, text="Slips/Wire Transfer/RTGS", variable=second_frame.var4, bg="lightsteelblue").place(x=800,y=2040)
second_frame.var5 = IntVar()
Checkbutton(second_frame, text="Foreign Remmitance", variable=second_frame.var5, bg="lightsteelblue").place(x=800,y=2080)
second_frame.var6 = IntVar()
Checkbutton(second_frame, text="POS Transaction", variable=second_frame.var6, bg="lightsteelblue").place(x=800,y=2120)
second_frame.var7 = IntVar()
Checkbutton(second_frame, text="Online Transaction", variable=second_frame.var7, bg="lightsteelblue").place(x=600,y=2160)
second_frame.var8 = IntVar()


#Operating Authority of the Account
ai=Label(second_frame,text="Operating Authority of the Account",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=250,y=2200)


clicked = StringVar()
clicked.set("<--- Select Category --->")

drop = OptionMenu(second_frame, clicked ,"             My Self             ",
                                         "             Our Selves             ",
                                         "             Guardian/Mother/Father             ",
                                         "             Others             ")

drop.place(x=500,y=2240)
drop.config(width = 27)

second_frame.Occupation=Entry(second_frame,font=("times new roman",15),bg="lavender")
second_frame.Occupation.place(x=750,y=2240,width=200)



#Available of Verification doc. Address
If_Yes=Label(second_frame,text="Available of Verification doc. Address",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=350,y=2290)

second_frame.var1 = IntVar()
Checkbutton(second_frame, text="NIC/Passport", variable=second_frame.var1, bg="lightsteelblue").place(x=400,y=2330)
second_frame.var2 = IntVar()
Checkbutton(second_frame, text="Utility Bill", variable=second_frame.var2, bg="lightsteelblue").place(x=400,y=2370)
second_frame.var3 = IntVar()
Checkbutton(second_frame, text="Valid Driving License", variable=second_frame.var3, bg="lightsteelblue").place(x=400,y=2410)
second_frame.var4 = IntVar()
Checkbutton(second_frame, text="Letter from Apublic Authority", variable=second_frame.var4, bg="lightsteelblue").place(x=400,y=2450)
second_frame.var5 = IntVar()
Checkbutton(second_frame, text="Income Tax Receipt/Assessment Notice", variable=second_frame.var5, bg="lightsteelblue").place(x=800,y=2330)
second_frame.var6 = IntVar()
Checkbutton(second_frame, text="Employment Contact", variable=second_frame.var6, bg="lightsteelblue").place(x=800,y=2370)
second_frame.var7 = IntVar()
Checkbutton(second_frame, text="Tenacy Agreement", variable=second_frame.var7, bg="lightsteelblue").place(x=800,y=2410)
second_frame.var8 = IntVar()
Checkbutton(second_frame, text="Grama Niladari", variable=second_frame.var8, bg="lightsteelblue").place(x=800,y=2450)


#PEP (Polotically Exposed Person)
PEP=Label(second_frame,text="Are You a Polotically Exposed Person..?",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=450,y=2520)

clicked = StringVar()
clicked.set("<--- Select Choice --->")

drop = OptionMenu(second_frame, clicked ,"                 Yes             ",
                                         "                 No             ")

drop.place(x=850,y=2520)
drop.config(width = 27)


#US Citizen
USC=Label(second_frame,text="Are You a Citizen of United States..?",font=("times new roman",15,"bold"),bg="lightsteelblue",fg="black").place(x=450,y=2570)

clicked = StringVar()
clicked.set("<--- Select Choice --->")

drop = OptionMenu(second_frame, clicked ,"                 Yes             ",
                                         "                 No             ")

drop.place(x=850,y=2570)
drop.config(width = 27)


#btn_cal=Button(second_frame,text="Submit",font=("times new roman",20),bd=0,cursor="hand2",command=second_frame.insert_identity_data).place(x=250,y=1050)



#def insert_identity_data(second_frame):
        #print(self.var_hloans.get())

    #    try:
     #       con=pymysql.connect(host="localhost",user="root",password="",database="kyc")
     #       cur=con.cursor()
      #      cur.execute("insert into details (name_with _initials, name_in_full, NIC, passport, driving_license, expiration_date_passport, expiration_date_driving_license, nationality, DOB) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
      #                      (second_frame.Name_with_Initials.get(),
       #                     second_frame.Name_in_Full.get(),
        #                    second_frame.NIC.get(),
        #                    second_frame.Passport.get(),
        #                    second_frame.driving_license.get(),
        #                    second_frame.Exp_pass.get(),
         #                   second_frame.Exp_drive.get(),
         #                   second_frame.Nationality.get(),
         #                   second_frame.DOB.get()
          #                  ))

     #       con.commit()
    #        con.close()
     #       messagebox.showinfo("sucess","Inserted Successfully",parent=second_frame.root)
    #    except Exception as es:
    #        messagebox.showerror("Error",f"error due to: {str(es)}",parent=second_frame.root)









root.mainloop()
