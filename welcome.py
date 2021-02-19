#WELCOME
from tkinter import *
import time
from PIL import Image, ImageTk
from _Source import *

class welcome:
    def __init__(self,root):

        l1=Label(root,text='Welcome\nto\nOnline Voting Portal !',font=("bold",30),bg='black',fg='white')
        l1.grid(row=0,column=0,pady=10,padx=40)
        l2=Label(root,text='Please wait...',font=("italic",20)).grid(row=1,column=0,pady=130)
        
m=Canvas(width=20,height=20,bg='black')
m.grid(row=0,column=0,sticky=NW)
image=ImageTk.PhotoImage(file="D:\\ß\\Python\\Project\\OVM\\Welcome.png")
m.create_image(93,155,image=image,anchor=NW)

ob=welcome(m)

obj=voting()
m.mainloop()

