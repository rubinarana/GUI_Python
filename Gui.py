#import tkinter

import tkinter as tk
from tkinter import ttk
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

#create button's action
def action():
    user_name = name_var.get()
    user_age = age_var.get()
    user_email = email_var.get()
    print(f'{user_name} is {user_age} years old,{user_email}')
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        subscribed = 'NO'
    else:
        subscribed = 'YES'
    print(user_gender,user_type,subscribed)

    with open ('file.txt','a') as f:
        f.write(f'{user_name},{user_age},{user_email},{user_gender},{user_type},{subscribed}\n')

#delete value of entry box after entry 
        name_entrybox.delete(0,tk.END)
        email_entrybox.delete(0,tk.END)
        age_entrybox.delete(0,tk.END)
#for colour after submit
        name_label.configure(foreground='#b388ff')
#for ttk we need to use style, so use tk
        submit_button.configure(foreground='#b388ff')        
        
submit_button = tk.Button(window, text = 'SUBMIT',command = action) #action function is called
submit_button.grid(row = 6,column = 0)

#pack and grid layout
window.mainloop()
