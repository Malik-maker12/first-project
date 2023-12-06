import tkinter as tk 
from tkinter import messagebox
def register():
    username=entry_username.get()
    username=entry_password.get()
    if not username or not entry_password:
        messagebox.showerror("error","please fill in all fields.")
    else:
            messagebox.showinfo("success","registration successful")
window=tk.Tk()
window.title("registration form")
label_username=tk.Label(window,text="username:") 
label_username.grid(row=0,column=0,padx=10,pady=5)
entry_username=tk.Entry(window)
entry_username.grid(row=0,column=1,padx=10,pady=5)
label_password=tk.Label(window,text="password:")
label_password.grid(row=1,column=0,padx=10,pady=5) 
entry_password=tk.Entry(window,show="*") 
entry_password.grid(row=1,column=1,padx=10,pady=5)
register_button=tk.Button(window,text="register",command=register)
register_button.grid(row=2,column=0,columnspan=2,pady=10)
window.mainloop() 