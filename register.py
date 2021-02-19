#Register
try:
    from tkinter import *
    from PIL import Image,ImageTk
    from votingdatabase import *
    import tkinter.messagebox as message
    #from _Source import *
    import pyttsx3
    import sys
except:
    print("ERROR")
class register:
    def __init__(self):
        
        root=Canvas(width=20,height=20,bg="black")
        root.grid(row=0,column=0,sticky=NW)
        image=ImageTk.PhotoImage(file="D:\\ß\\Python\\Project\\OVM\\register.png")
        root.create_image(120,63,image=image,anchor=NW)
        
        
        self.b4=Button(root,text='Home',bg="black",fg="white")
        self.b4.bind("<Button-1>",lambda event :self.home(event))
        #self.b4.grid(row=0,column=1)
        
        lr0=Label(root,text='Registration Form',font=("bold",20),bg="black",fg="white").grid(row=1,column=0,pady=10,padx=125,columnspan=2)
        
        self.lr1=Label(root,text='Name :',bg="black",fg="white").grid(row=2,column=0,pady=5)
        self.er1=Entry(root)
        self.er1.grid(row=2,column=1,pady=5)

        self.lr2=Label(root,text='Age :',bg="black",fg="white").grid(row=3,column=0,pady=5)
        self.er2=Entry(root)
        self.er2.grid(row=3,column=1,pady=5)

        self.lr3=Label(root,text='Aadhar No. :',bg="black",fg="white").grid(row=4,column=0,pady=5)
        self.er3=Entry(root)
        self.er3.grid(row=4,column=1,pady=5)
        
        self.lr4=Label(root,text='Email :',bg="black",fg="white").grid(row=5,column=0,pady=5)
        self.er4=Entry(root)
        self.er4.grid(row=5,column=1,pady=5)

        self.lr5=Label(root,text='Password :',bg="black",fg="white").grid(row=6,column=0,pady=5)
        self.er5=Entry(root,show='*')
        self.er5.grid(row=6,column=1,pady=5)

        self.br1=Button(root,text='Submit',width=20,height=2,bg="black",fg="white",command=root.destroy)
        self.br1.bind("<Button-1>",lambda event :self.registered(event))
        self.br1.grid(row=7,column=0,columnspan=2,pady=5)
        root.mainloop();

    def registered(self,event):
        if(int(self.er2.get())<18):
            iKid=message.showinfo("OVM","Your age is not appropriate !")
        else:
            vodb=votingdb()
            vodb.setdetails(self.er1.get(),self.er2.get(),self.er3.get(),self.er4.get(),self.er5.get())
            vodb.close()
            try:
                engine = pyttsx3.init()
                engine.say("Successfully Registered")
                engine.runAndWait()
            except:
                print("Oops!",sys.exc_info()[0],"occured.")
                print("Next entry.")
                print()
                #iReg=message.showinfo("OVM", "Sucessfully Registered ")
    def home(self,event):
        _source_ob=voting(m)
        m.destroy()



