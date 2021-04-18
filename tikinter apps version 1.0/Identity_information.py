#improting tkiner
import tkinter as tk

from tkinter import *
from tkinter import ttk,messagebox
#pip install pillow
from PIL import Image,ImageTk 
import mysql.connector
#pip istall pymysql
import pymysql
#==============================================================================================================================
# making connection to database
con=pymysql.connect(host="localhost",user="root",password="",database="kyc")
cur=con.cursor()



#===============================================================================================================================
#creating class call expences
class expences:
    def __init__(self,root):
        self.root=root
        self.root.title("Expence Window")
        self.root.geometry("1080x820+0+0")
        self.root.config(bg="white")
    
        #background image

        #self.bg=ImageTk.PhotoImage(file="background/3.jpg")
        #bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #background left image

        #self.left=ImageTk.PhotoImage(file="background/2.jpg")
        #left=Label(self.root,image=self.left).place(x=80,y=150,width=400,height=500)


#======================================================================================================================================
        #creating frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=50,y=50,width=1400,height=1400)

        #frame2=Frame(frame1,bg="brown")
        #frame2.place(x=370,y=70,width=400,height=200)



#====================================================================================================================================
        
        
        #customizing inside the frame
           
        #first title
        title=Label(frame1,text="Know your Customer(KYC) profile form – (Individual)",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=0,y=0)

        #second title
        title=Label(frame1,text="Section A – Identity Information",font=("times new roman",15,"bold"),bg="black",fg="white").place(x=0,y=50)

        #adding section A titles

        #row 1 -------->>>

        #Name with Initials
        Name_with_Initials=Label(frame1,text="Name with Initials",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=100)
        self.Name_with_Initials=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Name_with_Initials.place(x=200,y=100,width=500)

        #row 2------>>>

        #Name in Full
        Name_in_Full=Label(frame1,text="Name in Full",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=150)
        self.Name_in_Full=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Name_in_Full.place(x=200,y=150,width=500)

        #Identity Recognition
        ir=Label(frame1,text="Identity Recognition",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=200)


        clicked = StringVar()
        clicked.set("<--- Select Category --->")

        drop = OptionMenu(frame1, clicked ,"             NIC             ",
                                                "             Passport             ",
                                                "             Driving License             ")

        drop.place(x=200,y=200)
        drop.config(width = 27)

        #National ID
        NIC=Label(frame1,text="National ID",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=250)
        self.NIC=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.NIC.place(x=200,y=250,width=500)

        #Passport
        Passport=Label(frame1,text="Passport No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=300)
        self.Passport=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Passport.place(x=200,y=300,width=500)

        #Expiration Date
        Exp_pass=Label(frame1,text="Expiration Date",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=350)
        self.Exp_pass=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Exp_pass.place(x=200,y=350,width=500)

        #Driving License No.
        driving_license=Label(frame1,text="Driving License No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=400)
        self.driving_license=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.driving_license.place(x=200,y=400,width=500)

        #Expiration Date
        Exp_drive=Label(frame1,text="Expiration Date",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=450)
        self.Exp_drive=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Exp_drive.place(x=200,y=450,width=500)

        #Nationality
        Nationality=Label(frame1,text="Nationality",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=500)
        self.Nationality=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.Nationality.place(x=200,y=500,width=500)

        #Date od Birth
        DOB=Label(frame1,text="Date or Birth",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=550)
        self.DOB=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.DOB.place(x=200,y=550,width=500)
        
        #fingerprint values
        finger=Label(frame1,text="Fingerprint input",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=600)
        self.finger=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.finger.place(x=200,y=600,width=100)

        #face recongnition values
        face=Label(frame1,text="image input value",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=0,y=650)
        self.facer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.facer.place(x=200,y=650,width=100)

        #button inside the frame
        btn_evaluate=Button(frame1,text="Submit",font=("times new roman",20),bd=0,cursor="hand2",command=self.register_data).place(x=600,y=650)

#===================================================================================================================================

    
    def register_data(self):
        
        #define variable for taking input values==============================================================

        self.search_nic = self.NIC.get()
        self.search_fprint= self.finger.get()
        self.search_face = self.facer.get()
        self.search_name = self.Name_with_Initials.get()
        
        #selecting touples with different conditions==========================================================

        #self.finger_nic = "SELECT * FROM identity_information WHERE NIC = %s AND  finger_print1= %s"
        self.find_nic = "SELECT * FROM identity_information WHERE NIC = %s"
        self.find_finger = "SELECT * FROM identity_information WHERE finger_print1= %s"
        self.find_nic_finger = "SELECT * FROM identity_information WHERE NIC = %s AND finger_print1= %s"
        

        #search results and cursor towords the database table===================================================
        #self.name = (self.search_nic, self.search_fprint)

        self.name = (self.search_nic, )
        self.name1 = (self.search_fprint, )
        self.name2 = (self.search_nic, self.search_fprint)
        
        #defined cursors for each search list====================================================================
        self.result= cur.execute(self.find_nic, self.name)
        self.result= cur.fetchall()
        
        self.result1= cur.execute(self.find_finger, self.name1)
        self.result1= cur.fetchall()

        self.result2= cur.execute(self.find_nic_finger, self.name2)
        self.result2= cur.fetchall()

        print(self.result)
        print(self.result1)
        print(self.result2)
        

        #print(self.result[0][4])

        #if required fields are empty or not satisfied that is no kyc=============================================================
        if not self.result:
            self.result= "kyc not exist "
            print(self.result)
            #commiting code for the database=======================================================================================
            try:
                
                cur.execute("insert into identity_information (name_with_initials, name_in_full, NIC, passport , expiration_date_passport, driving_license, expiration_date_driving_license, nationality, DOB, face_recognition, finger_print1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.Name_with_Initials.get(),
                                self.Name_in_Full.get(),
                                self.NIC.get(),
                                self.Passport.get(),
                                self.Exp_pass.get(),
                                self.driving_license.get(),
                                self.Exp_drive.get(),
                                self.Nationality.get(),
                                self.DOB.get(),
                                self.facer.get(),
                                self.finger.get()

                                ))

                con.commit()
                con.close()
                messagebox.showinfo("sucess","register sucessful",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"error due to: {str(es)}",parent=self.root)

        #******************* in each and every face recogniton part the face_model needed to integrate***********

        #condition for  nic, fingerprint and face recognition=======================================================================


        elif((self.search_nic==self.result2[0][4] and self.search_fprint==self.result2[0][12]) and self.search_face<="0.25"):
            print("existing kyc main condtion")
            print("need to update")


        #condition for nic and face recognition part and then check with name========================================================


        elif(self.search_nic==self.result[0][4] and self.search_face<="0.25"):
            if(self.search_name==self.result[0][2]):
                print("existing kyc Nic and face and name update process")
                print("need to update")


        #condtion for nic and fingerprint and then check with name====================================================================

        elif(self.search_nic==self.result2[0][4] and self.search_fprint==self.result2[0][12]):
            if(self.search_name==self.result2[0][2]):
                print("existing kyc fingerprint and nic and name")
                print("need to update")

        #condtion fingerprint and face recognition then check with name===============================================================

        elif(self.search_fprint==self.result1[0][12] and self.search_face<="0.25"):
            if(self.search_name==self.result1[0][2]):
                print("existing kyc fingerprint and face and name")
                print("need to update")

        #condtion fingerprint and then check with name================================================================================

        elif(self.search_fprint==self.result1[0][12]):
            if(self.search_name==self.result1[0][2]):
                print("existing kyc fingerprint and name")
                print("need to update")

                try:
                    
                    cur.execute("insert into identity_information_clone (name_with_initials, name_in_full, NIC, passport , expiration_date_passport, driving_license, expiration_date_driving_license, nationality, DOB, face_recognition, finger_print1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (self.Name_with_Initials.get(),
                                    self.Name_in_Full.get(),
                                    self.NIC.get(),
                                    self.Passport.get(),
                                    self.Exp_pass.get(),
                                    self.driving_license.get(),
                                    self.Exp_drive.get(),
                                    self.Nationality.get(),
                                    self.DOB.get(),
                                    self.facer.get(),
                                    self.finger.get()

                                    ))

                    con.commit()
                    con.close()
                    messagebox.showinfo("sucess","register sucessful",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"error due to: {str(es)}",parent=self.root)

        #condtion for face recognition only and cross check===========================================================================

        elif(self.search_face<="0.25"):
            print("cross check face")

            try:
                    
                cur.execute("insert into identity_information_clone (name_with_initials, name_in_full, NIC, passport , expiration_date_passport, driving_license, expiration_date_driving_license, nationality, DOB, face_recognition, finger_print1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.Name_with_Initials.get(),
                                self.Name_in_Full.get(),
                                self.NIC.get(),
                                self.Passport.get(),
                                self.Exp_pass.get(),
                                self.driving_license.get(),
                                self.Exp_drive.get(),
                                self.Nationality.get(),
                                self.DOB.get(),
                                self.facer.get(),
                                self.finger.get()

                                ))

                con.commit()
                con.close()
                messagebox.showinfo("sucess","register sucessful",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"error due to: {str(es)}",parent=self.root)
        
        #condition for nic only and needed for cross checking and assistand guide options================================================

        elif(self.search_nic==self.result[0][4]):
            print("cross check nic")
            print("assistant guide")

            try:
                    
                cur.execute("insert into identity_information_clone (name_with_initials, name_in_full, NIC, passport , expiration_date_passport, driving_license, expiration_date_driving_license, nationality, DOB, face_recognition, finger_print1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.Name_with_Initials.get(),
                                self.Name_in_Full.get(),
                                self.NIC.get(),
                                self.Passport.get(),
                                self.Exp_pass.get(),
                                self.driving_license.get(),
                                self.Exp_drive.get(),
                                self.Nationality.get(),
                                self.DOB.get(),
                                self.facer.get(),
                                self.finger.get()

                                ))

                con.commit()
                con.close()
                messagebox.showinfo("sucess","register sucessful",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"error due to: {str(es)}",parent=self.root)
            
        #this is error handling if any conditon miss anything at alll :D=================================================
        else:

            try:
                
                cur.execute("insert into identity_information_clone (name_with_initials, name_in_full, NIC, passport , expiration_date_passport, driving_license, expiration_date_driving_license, nationality, DOB, face_recognition, finger_print1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.Name_with_Initials.get(),
                                self.Name_in_Full.get(),
                                self.NIC.get(),
                                self.Passport.get(),
                                self.Exp_pass.get(),
                                self.driving_license.get(),
                                self.Exp_drive.get(),
                                self.Nationality.get(),
                                self.DOB.get(),
                                self.facer.get(),
                                self.finger.get()

                                ))

                con.commit()
                con.close()
                messagebox.showinfo("sucess","register sucessful",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"error due to: {str(es)}",parent=self.root)

"""def clear():
    
    self.Name_with_Initials(0, END)
    self.Name_in_Full(0, END)
    self.NIC(0, END)
    self.Passport(0, END)
    self.Exp_pass(0, END)
    self.driving_license(0, END)
    self.Exp_drive(0, END)
    self.Nationality(0, END)
    self.DOB(0, END)
    self.facer(0, END)
    self.finge(0, END)"""



#=====================================================================================================================================

root=tk.Tk()
obj=expences(root)
root.mainloop()