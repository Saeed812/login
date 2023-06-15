
import tkinter as tk
from tkinter import messagebox

def show_login_page():
    
    
    login_window = tk.Toplevel(display)
    login_window.title("Login")
    login_window.geometry("400x400")
    
    username_label = tk.Label(login_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    login_button = tk.Button(login_window, text="Login",width="15",height="1")
    login_button.pack()
    


display = tk.Tk()
display.title("Button Example")
display.geometry("400x400")

btn_1 = tk.Button(display, text="click me (; )", command=show_login_page,width="20",height="2")
btn_1.pack()
btn_1.place(y="100" ,x="120")


def on_enter(e):
    btn_1['background'] = 'blue'

def on_leave(e):
    btn_1['background'] = 'white'
    
btn_1.bind("<Enter>", on_enter)
btn_1.bind("<Leave>", on_leave)

def Close():
   
    display.destroy() 

btn_2 = tk.Button(text="Quit!",width="20",height="2",foreground="black",command=Close)

btn_2.pack()

btn_2.place(y="160", x="120")


def on_enter(e):
    btn_2['background'] = '#ff2424'

def on_leave(e):
  
    btn_2['background'] = 'white'   

btn_2.bind("<Enter>", on_enter)

btn_2.bind("<Leave>", on_leave)



display.mainloop()
 
