import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

window = tk.Tk()    #win ,window ,root
window.title('GUI')

#create labels
#ttk widget is better than tk
name_label = ttk.Label(window,text='Enter you name:')
name_label.grid(row = 0,column = 0,sticky = tk.W)

email_label = ttk.Label(window,text='Enter you email:')
email_label.grid(row = 1,column = 0,sticky = tk.W)

age_label = ttk.Label(window,text='Enter you age:')
age_label.grid(row = 2,column = 0,sticky = tk.W)

gender_label = ttk.Label(window,text='Select you gender:')
gender_label.grid(row=3, column=0, sticky = tk.W)

#create entry box
name_var = tk.StringVar() #constructor in tk class StringVar use to get string written in entry box and name_var is variable
name_entrybox = ttk.Entry(window,width = 17,textvariable = name_var)
name_entrybox.grid(row = 0,column = 1)
name_entrybox.focus()   #auto focus on name

email_var = tk.StringVar()
email_entrybox = ttk.Entry(window,width = 17,textvariable = email_var)
email_entrybox.grid(row = 1,column = 1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(window,width = 17,textvariable = age_var)
age_entrybox.grid(row = 2,column = 1)

#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(window,width = 14,textvariable = gender_var, state = 'readonly')
gender_combobox['values'] = ('Male','Female','Others')
gender_combobox.current(1)      #select current value from tuple
gender_combobox.grid(row = 3,column = 1)

#radio button
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(window,text = 'Student',value = 'Student',variable = usertype)
radiobtn1.grid(row = 4,column = 0)

radiobtn2 = ttk.Radiobutton(window,text = 'Teacher',value = 'Teacher',variable = usertype)
radiobtn2.grid(row = 4,column = 1)

#check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(window,text = 'check button', variable = 'checkbtn_var')
checkbtn.grid(row = 5,columnspan = 3) #merge and use 3 column 



#write to CSV file
def action():
    user_name = name_var.get()
    user_age = age_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'
    with open('file.csv','a',newline='') as f:  #no spacing
        dict_writer = DictWriter(f,fieldnames=['UserName','Age','Email','UserGender','UserType','Subscribed'])
        #to know file is empty or not
        if os.stat('file.csv').st_size == 0:   
            dict_writer.writeheader()
        dict_writer.writerow({
            'UserName' : user_name,
            'Age':      user_age,
            'Email':     user_email,
            'UserGender':user_gender,
            'UserType': user_type,
            'Subscribed':subscribed
        })
            
        name_entrybox.delete(0,tk.END)
        email_entrybox.delete(0,tk.END)
        age_entrybox.delete(0,tk.END)
#for colour after submit
        name_label.configure(foreground='#b388ff')
        submit_button.configure(foreground='#b388ff')
        
submit_button = tk.Button(window, text = 'SUBMIT',command = action) #action function is called
submit_button.grid(row = 6,column = 0)

window.mainloop()
