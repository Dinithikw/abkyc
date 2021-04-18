
#====================================imprting libraries==========================================================================
import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk 
import pymysql

#================================================================================================================================

#making connection

con=pymysql.connect(host="localhost",user="root",password="",database="kyc")
my_cursor=con.cursor()


#===================================================================================================================================

#creating main window---------------------------------------------------------------------------------------------------------------

root = Tk()
root.title('kyc form')
root.geometry("1366x720")

# Create A Main Frame----------------------------------------------------------------------------

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas--------------------------------------------------------------------------------

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas------------------------------------------------------------------

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas---------------------------------------------------------------------------
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

#define mouse event------------------------------------------------------------------------------

def _on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta
 / 100)), "units")

my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

# Create ANOTHER Frame INSIDE the Canvas
search_customers = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=search_customers, anchor="nw")

def update():
    """ updating values of sql database file """
    sql_command="""UPDATE customers SET first_name = %s, last_name = %s, address = %s WHERE user_id = %s """
    first_name = first_name_box2.get()
    last_name = last_name_box2.get()
    address = address_box2.get()

    id_value = id_box2.get()
    inputs =(first_name, last_name, address, id_value)
    my_cursor.execute(sql_command, inputs)
    mydb.commit()

    search_customers.destroy()

#define edit now functon--------------------------------------------------------------------------------------------------------------------------------
def edit_now(id,index):
    sql2 = "SELECT * FROM customers WHERE user_id = %s" 
    name2 = (id, )
    
    global result2
    result2= my_cursor.execute(sql2, name2)
    result2=my_cursor.fetchall()
    #print(result2)


    index +=1

    #lables------------------------------------------------------

    first_name_label=Label(search_customers, text="First Name", font=("times new roman",16)).grid(row=index+1, column=0, sticky=W, padx=10)
    last_name_label=Label(search_customers, text="last Name", font=("times new roman",16)).grid(row=index+2, column=0, sticky=W, padx=10)
    address_label=Label(search_customers, text="address", font=("times new roman",16)).grid(row=index+3, column=0, sticky=W, padx=10)
    id_lable= Label(search_customers,text="User ID").grid(row=index+4, column=0, sticky=W, padx=10)

    #boxes--------------------------------------------------------
        
    global first_name_box2
    first_name_box2 = Entry(search_customers)
    first_name_box2.grid(row=index+1, column=1, pady=10)
    first_name_box2.insert(0, result2[0][0])


    global last_name_box2
    last_name_box2 = Entry(search_customers)
    last_name_box2.grid(row=index+2, column=1, pady=5)
    last_name_box2.insert(0, result2[0][1])
        
    global address_box2
    address_box2 = Entry(search_customers)
    address_box2.grid(row=index+3, column=1, pady=5)
    address_box2.insert(0, result2[0][6])

       

    global id_box2
    id_box2 = Entry(search_customers)
    id_box2.grid(row=index+4, column=1, pady=5)
    id_box2.insert(0, result2[0][4])

    global save_record
    save_record = Button(search_customers,text="update", command=update)
    save_record.grid(row=index+5, column=1, pady=10)



def search_now():

    searched = search_box.get()
    find= search_box1.get()
    sql = "SELECT * FROM customers WHERE first_name = %s AND  last_name= %s"

    #sql1 = "SELECT * FROM customers WHERE last_name = %s"

    name = (searched, find)
    #name2= (find, )
    result= my_cursor.execute(sql, name)
    result=my_cursor.fetchall()

    #result1= my_cursor.execute(sql1, name2)
    #result1=my_cursor.fetchall()

    if not result:
        result= "record not found"
        searched_label = Label(search_customers, text=result)
        searched_label.grid(row=2, column=0)

    else:
        
        for index, x in enumerate(result):
            num =0
            index += 2
            id_reference = str(x[4])
            edit_button = Button(search_customers, text="Edit", command=lambda: edit_now(id_reference, index))
            edit_button.grid(row=index, column=num)
            for y in x:
                searched_label = Label(search_customers, text=y)
                searched_label.grid(row=index, column=num+1)
                num +=1
    csv_button = Button(search_customers, text="save to excel", command=lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)



search_box= Entry(search_customers)
search_box.grid(row=0, column=1, padx=10, pady=10)

search_box1= Entry(search_customers)
search_box1.grid(row=0, column=3, padx=10, pady=10)

search_box_label= Label(search_customers, text="search customer: ")
search_box_label.grid(row=0, column=0, padx=10, pady=10)
    

#entry box search button----------------------------------------------------------------------------- ------------------------------   
search_button= Button(search_customers, text="search customers", command=search_now)
search_button.grid(row=1, column=0, padx=10)

















#==================================================================================================================================


root.mainloop()