#result
from tkinter import *
from votingdatabase import *
from PIL import Image,ImageTk

class result:
    def __init__(self):
        inc_count=0
        cpi_count=0
        bjp_count=0
        bsp_count=0
        total=0
        ob=votingdb()
        self.res=ob.selectCounter()
        for self.party in self.res:
            if(self.party[0]=='inc'):
                inc_count+=1
            if(self.party[0]=='cpi'):
                cpi_count+=1
            if(self.party[0]=='bjp'):
                bjp_count+=1
            if(self.party[0]=='bsp'):
                bsp_count+=1
            total+=1
        print("inc",inc_count)
        print("cpi",cpi_count)
        print("bjp",bjp_count)
        print("bsp",bsp_count)
        
        root=Canvas(width=500,height=500,bg="black")
        root.grid(row=0,column=0,sticky=NW)
        image=ImageTk.PhotoImage(file="D:\\ß\\Python\\Project\\OVM\\result2.png")
        root.create_image(25,80,image=image,anchor=NW)

        l1=Label(root,text="RESULTS",font=("bold",60),bg="black",fg="white").grid(row=0,column=0,columnspan=4,pady=10,padx=10)

        l2=Label(root,text="PARTIES",font=("comic sans ms",25)).grid(row=1,column=0,pady=4,padx=10)

        l3=Label(root,text="INC",font=("comic sans ms",20)).grid(row=2,column=0,pady=4,padx=10)
        l4=Label(root,text="CPI",font=("comic sans ms",20)).grid(row=3,column=0,pady=4,padx=10)
        l5=Label(root,text="BJP",font=("comic sans ms",20)).grid(row=4,column=0,pady=4,padx=10)
        l6=Label(root,text="BSP",font=("comic sans ms",20)).grid(row=5,column=0,pady=4,padx=10)

        l7=Label(root,text="Votes",font=("comic sans ms",25)).grid(row=1,column=1,pady=4,padx=10)
        
        l8=Label(root,text=inc_count,font=("comic sans ms",20))
        l8.grid(row=2,column=1,pady=4,padx=10)
        l9=Label(root,text=cpi_count,font=("comic sans ms",20))
        l9.grid(row=3,column=1,pady=4,padx=10)
        l10=Label(root,text=bjp_count,font=("comic sans ms",20))
        l10.grid(row=4,column=1,pady=4,padx=10)
        l11=Label(root,text=bsp_count,font=("comic sans ms",20))
        l11.grid(row=5,column=1,pady=4,padx=10)

        l12=Label(root,text="Percentage\nof Votes",font=("comic sans ms",25)).grid(row=1,column=2,pady=4,padx=10)
        
        l13=Label(root,text="no.",font=("comic sans ms",20)).grid(row=2,column=2,pady=4,padx=10)
        l14=Label(root,text="no.",font=("comic sans ms",20)).grid(row=3,column=2,pady=4,padx=10)
        l15=Label(root,text="no.",font=("comic sans ms",20)).grid(row=4,column=2,pady=4,padx=10)
        l16=Label(root,text="no.",font=("comic sans ms",20)).grid(row=5,column=2,pady=4,padx=10)

        l17=Label(root,text="Total Votes : ",font=("comic sans ms",20)).grid(row=6,column=0,pady=10,padx=10,columnspan=2)
        l18=Label(root,text=total,font=("comic sans ms",20))
        l18.grid(row=6,column=1,pady=10,columnspan=2)

        if(inc_count>cpi_count):
            if(inc_count>bjp_count):
                if(inc_count>bsp_count):
                    win='INC WON !!'
                else:
                    win='BSP WON !!'
            else:
                if(bjp_count>bsp_count):
                    win='BJP WON !!'
                else:
                    win='BSP WON !!'
        else:
            if(cpi_count>bjp_count):
                if(cpi_count>bsp_count):
                    win='CPI WON !!'
                else:
                    win='BSP WON !!'
            else:
                if(bjp_count>bsp_count):
                    win='BJP WON !!'
                else:
                    win='BSP WON !!'

        l19=Label(root,text=win,font=("bold",50),bg="black",fg="white").grid(row=7,column=0,columnspan=4,pady=20,padx=20)
        
        
        root.mainloop()
