from tkinter import*
base=Tk()
base.geometry("500*500")
base.title("registration form")
lb1=Label(base,text="enter name",width=10,font=("arial",12))
lb1.place(x=20,y=120)
en1=Entry(base)
en1.place(x=200,y=120)
lb3=Label(base,text="enter email",width=10,font=("arial",12))
lb3.place(x=19,y=160)
en3=Entry(base)
en3.place(x=200,y=160)
lb4=Label(base,text="contact number",width=15,font=("arial",12))
lb4.place(x=19,y=200)
en4=Entry(base)
en4.place(x=200,y=200)
lb5=Label(base,text="select gender",width=15,font=("arial",12))
lb5.place(x=5,y=240)
vars=IntVar()
Radiobutton(base,text="male",padx=5,variable=vars,value=1).place(x=180,y=240)
Radiobutton(base,text="female",padx=10,variable=vars,value=2).place(x=240,y=240)
Radiobutton(base,text="others",padx=15,variable=vars,value=3).place(x=310,y=240)
list_of_cntry=("united state","india","nepal","germany")
cv=StringVar()
drplist=OptionMenu(base,cv,*list_of_cntry)
drplist.config(width=15)
cv.set("united states")
lbs2=Label(base,text="select country",width=13,font=("arial",12))
lbs2.place(x=14,y=280)
drplist.place(X=200,y=275)
lb6=Label(base,text="enter password",width=13,font=("arial",12))
lb6.place(x=19,y=320)
en6=Entry(base,show="*")
en6.place(x=200,y=320)
lb7=Label(base,text="Re-Enterpassword",width=15,font=("arial",12))
lb7.place(x=21,y=360)
en7=Entry(base,show="*")
en7.place(x=200,y=360)
Button(base,text="register",width=10).place(x=200,y=400)
base.mainloop()
print("registeration form is created successfully...")