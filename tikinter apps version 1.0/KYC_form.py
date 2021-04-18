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
        self.root.title("Expence Window")
        self.root.geometry("1080x820+0+0")
        self.root.config(bg="white")
    
        #background image

        self.bg=ImageTk.PhotoImage(file="background/3.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #background left image

        self.left=ImageTk.PhotoImage(file="background/2.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=150,width=400,height=500)


#======================================================================================================================================
        #creating frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=50,y=50,width=700,height=620)

        #frame2=Frame(frame1,bg="brown")
        #frame2.place(x=370,y=70,width=400,height=200)



#====================================================================================================================================
        
        
        #customizing inside the frame
           
        #adding Income title
        title=Label(frame1,text="KYC Profile form",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #name
        name=Label(frame1,text="Section A - Basic information of the individual includng of those with power Attorny",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=80)
        title=Label(frame1,text="Name in Full",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=130)
        self.txt_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_name.place(x=300,y=130,width=250)

        #address
        address=Label(frame1,text="Address of the customer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
        self.txt_address=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_address.place(x=300,y=180,width=250)

        #nature of business
        business=Label(frame1,text="Nature of Business (if any)",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=230)
        self.txt_business=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_business.place(x=300,y=230,width=250)

        #date of birth
        dob=Label(frame1,text="Date of birth",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=280)
        self.txt_dob=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_dob.place(x=300,y=280,width=250)

        #gender
        gender=Label(frame1,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=330)
        self.var1 = IntVar()
        Checkbutton(frame1, text="male", variable=self.var1).place(x=300,y=330)
        self.var2 = IntVar()
        Checkbutton(frame1, text="female", variable=self.var2).place(x=400,y=330)
        #self.txt_gender=Entry(frame1,font=("times new roman",15),bg="lightgray")
        #self.txt_gender.place(x=370,y=320,width=250)

        #marital status
        marital_status=Label(frame1,text="Marital Status",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=380)
        self.yes = IntVar()
        Checkbutton(frame1,text="married", variable=self.yes).place(x=300,y=380)
        self.no = IntVar()
        Checkbutton(frame1,text="not married", variable=self.no).place(x=400,y=380)
        #Education expences
        ex_education=Label(frame1,text="Education",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=360)
        self.txt_exeducation=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_exeducation.place(x=370,y=390,width=250)


        #button inside the frame
        btn_evaluate=Button(frame1,text="Evaluate",font=("times new roman",20),bd=0,cursor="hand2",command=self.register_data).place(x=250,y=450)

        #btn_cal=Button(frame1,text="calculate",font=("times new roman",20),bd=0,cursor="hand2",command=self.add_numbers).place(x=50,y=450)

        #button outside the frame
        #btn=Button(self.root,text="evaluate",font=("times new roman",20),bd=0,cursor="hand2").place(x=50,y=450)

        ex_total=Label(frame1,text="Total expenses",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=530)
        self.tot_ex=StringVar()
        result=Label(frame1, text="", textvariable=self.tot_ex, font=("times new roman",15,"bold")).place(x=370,y=530)


        rem_amount=Label(frame1,text="Remaining amount",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=570)
        self.tot_rem=StringVar()
        result=Label(frame1, text="", textvariable=self.tot_rem, font=("times new roman",15,"bold")).place(x=370,y=570)





#===================================================================================================================================
    
    #function for taking total expences and total remainings
    #def add_numbers(self):
       # res=int(self.txt_hloans.get())+int(self.txt_exauto.get())+int(self.txt_exhealth.get())+int(self.txt_food.get())+int(self.txt_exentertain.get())+int(self.txt_exeducation.get())
        #self.tot_ex.set(res)

       # rem=int(self.txt_tincome.get())-int(res)
        #self.tot_rem.set(rem)

    #function to check all are numbers
    def check_num(self):
        try:
            int(self.txt_tincome.get())
            messagebox.showinfo("Number","done",parent=self.root)
        except:
            messagebox.showerror("not number","please enter numer",parent=self.root)

    
    
    def register_data(self):
        #print(self.var_hloans.get())

        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="dapp")
            cur=con.cursor()
            cur.execute("insert into details (t_income,h_loans,ex_auto,ex_health,ex_food,ex_entertain,ex_education,tot_ex,tot_rem) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_tincome.get(),
                            self.txt_hloans.get(),
                            self.txt_exauto.get(),
                            self.txt_exhealth.get(),
                            self.txt_food.get(),
                            self.txt_exentertain.get(),
                            self.txt_exeducation.get(),
                            self.tot_ex.get(),
                            self.tot_rem.get()

                            ))

            con.commit()
            con.close()
            messagebox.showinfo("sucess","register sucessful",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"error due to: {str(es)}",parent=self.root)

        res=int(self.txt_hloans.get())+int(self.txt_exauto.get())+int(self.txt_exhealth.get())+int(self.txt_food.get())+int(self.txt_exentertain.get())+int(self.txt_exeducation.get())
        self.tot_ex.set(res)

        rem=int(self.txt_tincome.get())-int(res)
        self.tot_rem.set(rem)

#=====================================================================================================================================

root=tk.Tk()
obj=expences(root)
root.mainloop()