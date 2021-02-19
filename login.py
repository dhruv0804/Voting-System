#login
from tkinter import *
from votingdatabase import *
from PIL import Image,ImageTk
import tkinter.messagebox as message
if __name__=="login":
    from vote import *
class login:
    
    def __init__(self):
        self.root1=Canvas(width=20,height=20,bg="black")
        self.root1.grid(row=0,column=0,sticky=NW)
        image=ImageTk.PhotoImage(file="D:\\ß\\Python\\Project\\OVM\\login2.png")
        self.root1.create_image(70,90,image=image,anchor=NW)
        
        self.b4=Button(self.root1,text='Back')
        self.b4.grid(row=0,column=0)
        
        l0=Label(self.root1,text='LOGIN',font=("helvetica",30),bg="black",fg="white").grid(row=1,column=0,pady=50,padx=125,columnspan=2)

        ll1=Label(self.root1,text='Aadhar No. :',bg="black",fg="white").grid(row=2,column=0,pady=5)
        self.el1=Entry(self.root1)
        self.el1.grid(row=2,column=1,pady=5)

        ll2=Label(self.root1,text='Password :',bg="black",fg="white").grid(row=4,column=0,pady=5)
        self.el2=Entry(self.root1,show='*')
        self.el2.grid(row=4,column=1,pady=5)

        b1=Button(self.root1,text='Submit',bg="black",fg="white")
        b1.bind("<Button-1>",lambda event:self.vote(event))
        b1.grid(row=5,column=0,columnspan=2,pady=10)
        self.root1.mainloop()        
    def vote(self,event):
        vodb2=votingdb()
        self.res=vodb2.showdetails(self.el1.get(),self.el2.get())
        vodb2.close()

        if(self.res==1):
            a=self.el1.get()
            self.root1.destroy()
            voteit_ob=voteit(a)
    
