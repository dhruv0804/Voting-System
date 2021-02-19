import mysql.connector as s
import tkinter.messagebox as m
class votingdb():
    def __init__(self):
        self.con = s.connect(user='root',
                            password='VardaaN@123',
                            host='localhost',
                            database='votingdb')

        self.db = self.con.cursor()

    def setdetails(self,n,age,a,e,p):
        self.qu = 'insert into register(name,age,aadharno,email,password)values(%s,%s,%s,%s,%s)'
        self.val = (n,age,a,e,p)
        self.db.execute(self.qu, self.val)
    def showdetails(self,a,p):
        self.check=0
        self.qu = 'select * from register where aadharno=%s and password=%s'
        self.db.execute(self.qu,(a,p))
        self.rec=self.db.fetchall()
        for row in self.rec:
            if row[7]==0:
                success=m.showinfo("OVM","Login Successful")
                self.check=1
                break
            elif row[7]==1:
                    success=m.showerror("OVM","Already Voted !")
                    break
        else:
             success=m.showerror("OVM","Wrong Username or Password")
                   
                    
                    
        return self.check
    def updateVote(self,addharno,party):
        self.qu = 'update  register set party=%s where aadharno =%s'
        self.val = (party,addharno)
        self.db.execute(self.qu, self.val)

    def updateTotal(self):
        self.qu1='select total_votes from total'
        self.db.execute(self.qu1)
        self.res=self.db.fetchall()
        self.res+=1
        self.c=str(self.res)
        self.qu2 = 'update  total set total_votes=%s'
        self.val = (self.c,)
        self.db.execute(self.qu2,self.val)

    def updateStatus(self,addharno):
        self.st=1
        self.qu='update register set status=%s where aadharno =%s'
        self.val=(self.st,addharno)
        self.db.execute(self.qu,self.val)

    def selectCounter(self):
        self.q1='select party from register'
        self.db.execute(self.q1)
        self.res=self.db.fetchall()
        return self.res
        
    def close(self):
        self.con.commit()
        self.con.close()

