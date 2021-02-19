#vote
from tkinter import *
import tkinter.messagebox as message
from PIL import Image,ImageTk
from votingdatabase import *
from login import *
class voteit:
    def __init__(self,aadharid):

        self.aadhar_id=aadharid
        
        root2=Canvas(width=20,height=20,bg="white")
        root2.grid(row=0,column=0,sticky=NW)
        image1=ImageTk.PhotoImage(file="D:\\ß\\Python\\Project\\OVM\\congress.png")
        image2=ImageTk.PhotoImage(file="D:\\ß\\Python\\Project\\OVM\\cpi2.png")
        image3=ImageTk.PhotoImage(file="D:\\ß\\Python\\Project\\OVM\\bjp.png")
        image4=ImageTk.PhotoImage(file="D:\\ß\\Python\\Project\\OVM\\bsp.png")

        imagebk=ImageTk.PhotoImage(file="D:\\ß\\Python\\Project\\OVM\\votevote3.png")
        root2.create_image(0,50,image=imagebk,anchor=NW)
        self.v=root2
        self.b5=Button(self.v,text='Back')
        self.b5.bind("<Button-1>",lambda event :self.back(event))
        self.b5.grid(row=0,column=0)
           
        l0=Label(self.v,text='Here are some democratic parties of your area...').grid(row=1,column=0,pady=10,padx=125,columnspan=2)
        l1=Label(self.v,text='V_O_T_E',font=("helvetica",30)).grid(row=2,column=0,pady=10,columnspan=2)
               
        self.b1=Button(self.v,image=image1,width=200,height=200,bg="#2C426B")
        self.b1.bind("<Button-1>",lambda event,party="inc" :self.vote_fun(event,party))
        self.b1.grid(row=3,column=0)

        l2=Label(self.v,text="INC",font=("bold",20)).grid(row=4,column=0)
        
        self.b2=Button(self.v,image=image2,width=200,height=200,bg="#2C426B")
        self.b2.bind("<Button-1>",lambda event,party="cpi" :self.vote_fun(event,party))
        self.b2.grid(row=3,column=1)

        l2=Label(self.v,text="CPI",font=("bold",20)).grid(row=4,column=1)
        
        self.b3=Button(self.v,image=image3,width=200,height=200,bg="#2C426B")
        self.b3.bind("<Button-1>",lambda event,party="bjp" :self.vote_fun(event,party))
        self.b3.grid(row=5,column=0)

        l2=Label(self.v,text="BJP",font=("bold",20)).grid(row=6,column=0)
        
        self.b4=Button(self.v,image=image4,width=200,height=200,bg="#2C426B")
        self.b4.bind("<Button-1>",lambda event,party="bsp" :self.vote_fun(event,party))
        self.b4.grid(row=5,column=1)

        l2=Label(self.v,text="BSP",font=("bold",20)).grid(row=6,column=1)

        self.v.mainloop()
    def back(self,event):
        self.v.destroy()
        login_obj=login()
    def vote_fun(self,event,party):  
        self.party=party
        db=votingdb()
        db.updateVote(self.aadhar_id,self.party)
        db.updateStatus(self.aadhar_id)
        print("voted",self.party)
        db.close()
        self.v.destroy()
        icomp=message.showinfo("OVM","Vote Registered :)")
   
