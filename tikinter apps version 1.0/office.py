#improting tkiner
import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import ttk,messagebox
#pip install pillow
from PIL import Image,ImageTk 

#pip istall pymysql
import pymysql

root = Tk()
root.title('Learn to code')
root.geometry("1600x900")
root.config(bg="silver")
#create a main frame

frame1 = Frame(root,bg="white")
frame1.pack(fill=BOTH, expand=1)
frame1.place(x=225,y=30,width=1100,height=775)
#create a canvas

my_canvas = Canvas(frame1)

#create another frama INSIDE thr canvas
second_frame = Frame(my_canvas)

#add that new frame to a window in the canvas
my_canvas.create_window((0,0), window = second_frame, anchor="nw")

#background image
frame1.bg=ImageTk.PhotoImage(file="background/4.jpg")
bg=Label(frame1,image=frame1.bg).place(x=0,y=0,relwidth=1,relheight=1)




#adding  title
title=Label(frame1,text="Know Your Customer(KYC) Profile Form – (Individual)",font=("times new roman",20,"bold","underline"),bg="lightblue",fg="black").place(x=225,y=10)

#adding  office use only title
title=Label(frame1,text="Office Use Only",font=("times new roman",15,"bold","italic"),bg="red",fg="white").place(x=60,y=60)

#date
date=Label(frame1,text="Date",font=("times new roman",15,"bold"),bg="khaki",fg="black").place(x=100,y=120)
frame1.date=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.date.place(x=220,y=120)

#account no.
account_no=Label(frame1,text="A/C No.",font=("times new roman",15,"bold"),bg="khaki",fg="black").place(x=100,y=180)
frame1.account_no=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.account_no.place(x=220,y=180)

#Branch No
Branch_No=Label(frame1,text="Branch No.",font=("times new roman",15,"bold"),bg="khaki",fg="black").place(x=100,y=240)
frame1.Branch_No=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.Branch_No.place(x=220,y=240)

#Officer’s S/No
account_no=Label(frame1,text="Officer’s S/No.",font=("times new roman",15,"bold"),bg="khaki",fg="black").place(x=600,y=120)
frame1.Officer_S_No=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.Officer_S_No.place(x=800,y=120)

#Manager’s INTL
Branch_No=Label(frame1,text="Manager’s INTL",font=("times new roman",15,"bold"),bg="khaki",fg="black").place(x=600,y=180)
frame1.Manager_INTL=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.Manager_INTL.place(x=800,y=180)

#Risk Category
rc=Label(frame1,text="Risk Category",font=("times new roman",15,"bold"),bg="khaki",fg="black").place(x=600,y=240)

clicked = StringVar()
clicked.set("<--- Select category --->")

drop = OptionMenu(root, clicked ,"                Low                ",
                                 "                Medium                ",
                                 "                High                ")
drop.pack()
drop.place(x=1024,y=270)
drop.config(width = 27)

#Officer Authorization
Office_Use=Label(frame1,text="Officer Authorization",font=("times new roman",15,"bold"),bg="lightgreen",fg="black").place(x=400,y=300) 

#Name of thw officer
Officer_Name=Label(frame1,text="Name of the Officer",font=("times new roman",15,"bold"),bg="skyblue",fg="black").place(x=250,y=350)
frame1.Officer_Name=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.Officer_Name.place(x=500,y=350,width=250)

#Signature
Signature=Label(frame1,text="Signature of the Officer",font=("times new roman",15,"bold"),bg="skyblue",fg="black").place(x=250,y=400)
frame1.Signature=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.Signature.place(x=500,y=400,width=250,height=40)

#date
date=Label(frame1,text="Date",font=("times new roman",15,"bold"),bg="skyblue",fg="black").place(x=250,y=450)
frame1.date=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.date.place(x=500,y=450,width=250)

#Manager Authorization
Office_Use=Label(frame1,text="Manager Authorization",font=("times new roman",15,"bold"),bg="cyan",fg="black").place(x=400,y=500) 

#Name of thw Manager
Manager_Name=Label(frame1,text="Name of the Manager",font=("times new roman",15,"bold"),bg="navajowhite",fg="black").place(x=250,y=550)
frame1.Manager_Name=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.Manager_Name.place(x=500,y=550,width=250)

#Signature
Signature=Label(frame1,text="Signature of the Manager",font=("times new roman",15,"bold"),bg="navajowhite",fg="black").place(x=250,y=600)
frame1.Signature=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.Signature.place(x=500,y=600,width=250,height=40)

#date
date=Label(frame1,text="Date",font=("times new roman",15,"bold"),bg="navajowhite",fg="black").place(x=250,y=650)
frame1.date=Entry(frame1,font=("times new roman",15),bg="lightgray")
frame1.date.place(x=500,y=650,width=250)

# create button 
button = Button(frame1, text='Submit', bg='#0052cc', fg='black') 
# apply font to the button label 
button['font'] = font.Font(family='Helvetica')  
# add button to gui window 
button.pack()
button.place(x=400,y=700,width=200,height=50) 

root.mainloop()