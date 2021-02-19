#front-end
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as message
from votingdatabase import *
from register import *
from login import *
from result import *
class voting:
    def __init__(self):

        self.root1=Canvas(width=20,height=20)
        self.root1.grid(row=0,column=0,sticky=NW)
        image=ImageTk.PhotoImage(file="D:\\ß\\Python\\Project\\OVM\\voting1.png")
        self.root1.create_image(-120,-150,image=image,anchor=NW)
        
        l2=Label(self.root1,text='Choose within the following options to proceed...',font=("bold",20),bg="#1B6472",fg="white").grid(row=1,column=0)

        self.b1=Button(self.root1,text="REGISTER\n(if you're not a member)",font=("bold",10),bg="#1B6472",fg="white")
        self.b1.bind("<Button-1>",lambda event :self.reg(event))
        self.b1.grid(row=3,column=0,pady=20)
        self.b2=Button(self.root1,text="LOGIN\n(if you're already a member)",font=("bold",10),bg="#1B6472",fg="white")
        self.b2.bind("<Button-1>",lambda event :self.log(event))
        self.b2.grid(row=4,column=0)
        self.b3=Button(self.root1,text="RESULT",font=("bold",10),bg="#1B6472",fg="white")
        self.b3.bind("<Button-1>",lambda event :self.res(event))
        self.b3.grid(row=5,column=0,pady=20)

        self.root1.mainloop()
    def reg(self,event):
        self.root1.destroy()   
        register_ob=register()
    def log(self,event):
        self.root1.destroy()
        login_ob=login()
    def res(self,event):
        self.root1.destroy()
        result_ob=result()
ob=voting()
