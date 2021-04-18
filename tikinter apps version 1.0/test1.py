#improting tkiner
import tkinter as tk

from tkinter import *
from tkinter import ttk,messagebox
#pip install pillow
from PIL import Image,ImageTk 

#pip istall pymysql
import pymysql

class expences:
    def __init__(self,root):
        root = Tk()
        root.title('Learn to code')
        root.geometry("1800x1820")

        #create a main frame

        frame1 = Frame(root)
        frame1.pack(fill=BOTH, expand=1)

        second_frame = Frame(root)
        second_frame.pack(fill=BOTH, expand=1) 

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

        second_frame = Frame(my_canvas, bg = "white")


        #add that new frame to a window in the canvas

        my_canvas.create_window((0,0), window = second_frame, anchor="nw")

        #background image

        #second_frame.bg=Image.Tk.PhotoImage(file="background/2.jpg")
        #bg=Label(second_frame.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        for thing in range(100):
            Button(second_frame, text=f'Button {thing} Yo!!').grid(row=thing, column=2000, pady=10, padx=2000)

        #my_label = Label(second_frame, text="Know your Customer(KYC) profile form – (Individual)").grid(row=1, column=2500)


        #adding  title
        title=Label(second_frame,text="Know your Customer(KYC) profile form – (Individual)",font=("times new roman",20,"bold","underline"),bg="white",fg="black").place(x=400,y=30)

        #adding section A title
        title=Label(second_frame,text="Section A – Identity Information",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=250,y=300)
                
        #adding section A titles

        #row 1 -------->>>

        #Name with Initials
        Name_with_Initials=Label(second_frame,text="Name with Initials",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=340)
        second_frame.Name_with_Initials=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.Name_with_Initials.place(x=500,y=340,width=700)

        #row 2------>>>

        #Name in Full
        Name_in_Full=Label(second_frame,text="Name in Full",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=380)
        second_frame.Name_in_Full=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.Name_in_Full.place(x=500,y=380,width=700)

        #Identity Recognition
        ir=Label(second_frame,text="Identity Recognition",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=420)


        clicked = StringVar()
        clicked.set("<--- Select Category --->")

        drop = OptionMenu(second_frame, clicked ,"             NIC             ",
                                                "             Passport             ",
                                                "             Driving License             ")

        drop.place(x=500,y=420)
        drop.config(width = 27)


        #National ID
        NIC=Label(second_frame,text="National ID",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=500,y=460)
        second_frame.NIC=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.NIC.place(x=500,y=500,width=200)

        #Passport
        Passport=Label(second_frame,text="Passport No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=500,y=540)
        second_frame.Passport=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.Passport.place(x=500,y=580,width=200)

        #Expiration Date
        Exp_pass=Label(second_frame,text="Expiration Date",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=800,y=540)
        second_frame.Exp_pass=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.Exp_pass.place(x=800,y=580,width=200)

        #Driving License No.
        driving_license=Label(second_frame,text="Driving License No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=500,y=620)
        second_frame.driving_license=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.driving_license.place(x=500,y=660,width=200)

        #Expiration Date
        Exp_drive=Label(second_frame,text="Expiration Date",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=800,y=620)
        second_frame.Exp_drive=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.Exp_drive.place(x=800,y=660,width=200)

        #Nationality
        Nationality=Label(second_frame,text="Nationality",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=700)
        second_frame.Nationality=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.Nationality.place(x=500,y=700,width=200)

        #Date od Birth
        DOB=Label(second_frame,text="Date or Birth",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=740)
        second_frame.DOB=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.DOB.place(x=500,y=740,width=200)


        #adding section B title
        title=Label(second_frame,text="Section B – Contact Information",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=250,y=800)

        #House No.
        House_No=Label(second_frame,text="House No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=850)
        second_frame.House_No=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.House_No.place(x=500,y=850,width=350)

        #Street
        Street=Label(second_frame,text="Street",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=890)
        second_frame.Street=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.Street.place(x=500,y=890,width=350)

        #City
        City=Label(second_frame,text="City",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=930)
        second_frame.City=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.City.place(x=500,y=930,width=350)

        #Postal Code
        Postal_Code=Label(second_frame,text="Postal Code",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=970)
        second_frame.Postal_Code=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.Postal_Code.place(x=500,y=970,width=350)

        #Country
        country=Label(second_frame,text="Country",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=1010)
        second_frame.country=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.country.place(x=500,y=1010,width=350)

        #Mobile No.
        Mobile_No=Label(second_frame,text="Mobile No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=1050)
        second_frame.Mobile_No=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.Mobile_No.place(x=500,y=1050,width=350)

        #E-mail
        Email=Label(second_frame,text="E-mail",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=1090)
        second_frame.Email=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        second_frame.Email.place(x=500,y=1090,width=350)


        #Gender
        Gender=Label(second_frame,text="Have an account in bank ......?",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=1150)

        second_frame.var1 = IntVar()
        Checkbutton(second_frame, text="male", variable=second_frame.var1).place(x=550,y=1150)
        second_frame.var2 = IntVar()
        Checkbutton(second_frame, text="female", variable=second_frame.var2).place(x=650,y=1150)
















        btn_cal=Button(second_frame,text="Submit",font=("times new roman",20),bd=0,cursor="hand2",command=second_frame.insert_identity_data).place(x=250,y=1050)



        #other residance
        #other_residance=Label(second_frame,text="Are you a citizen/resident of any other country",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=590)

        #second_frame.var1 = IntVar()
        #Checkbutton(second_frame, text="Yes", variable=second_frame.var1,font=("times new roman",15,"bold")).place(x=500,y=590)
                
        #second_frame.var2 = IntVar()
        #Checkbutton(second_frame, text="No", variable=second_frame.var2,font=("times new roman",15,"bold")).place(x=600,y=590)


        #row 8------>>>

        #yes state
        #yes_state=Label(second_frame,text="If ‘Yes’ please state",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=630)
        #second_frame.yes_state=Entry(second_frame,font=("times new roman",15),bg="lightgray")
        #second_frame.yes_state.place(x=350,y=630,width=500) 




        #adding section C titles
        #title=Label(second_frame,text="Section C – Address Information (Residential/Permanent Address)",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=790)
        #row 1 ------>>>



        def insert_identity_data(second_frame):
                #print(self.var_hloans.get())

                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="kyc")
                    cur=con.cursor()
                    cur.executecur.execute("insert into details (name_with _initials, name_in_full, NIC, passport, driving_license, expiration_date_passport, expiration_date_driving_license, nationality, DOB) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (second_frame.Name_with_Initials.get(),
                                    second_frame.Name_in_Full.get(),
                                    second_frame.NIC.get(),
                                    second_frame.Passport.get(),
                                    second_frame.driving_license.get(),
                                    second_frame.Exp_pass.get(),
                                    second_frame.Exp_drive.get(),
                                    second_frame.Nationality.get(),
                                    second_frame.DOB.get()
                                    ))

                    con.commit()
                    con.close()
                    messagebox.showinfo("sucess","Inserted Successfully",parent=second_frame.root)
                except Exception as es:
                    messagebox.showerror("Error",f"error due to: {str(es)}",parent=second_frame.root)









        root.mainloop()