import pymysql
import tkinter as tk

########################################################################

class LoginApp:
    def __init__(self):
        
        root=tk.Tk()
        root.title("Login Form")

        root.geometry("300x300")
        
        self.v2 = tk.StringVar()
        
        self.v4 = tk.StringVar()
        
        self.v6 = tk.StringVar()
        
        self.v7= tk.StringVar()

       
        label2=tk.Label(root,text="Email:").grid(row=1,column=0)
        entry2=tk.Entry(root,textvariable=self.v2).grid(row=1,column=1)

        label5=tk.Label(root,text="Password:").grid(row=4,column=0)
        entry5=tk.Entry(root,show="*",textvariable=self.v4).grid(row=4,column=1)

        label7=tk.Label(root,text=" ",textvariable=self.v6).grid(row=7,column=1)
        button1=tk.Button(root,text="Log in",fg='blue',command=lambda: self.validate(root)).grid(row=6,column=1)

        label7=tk.Label(root,text=" ",textvariable=self.v7).grid(row=8,column=1)
        #btn = tk.Button(root, text="New user?", command=lambda: self.openFrame(root)).grid(row=8,column=1)
        
    def validate(self,root):
        a2=str(self.v2.get())
        a5=str(self.v4.get())
        if a5=='':
             self.v6.set("password must be filled")
        else:
            conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='student management system')
            cur=conn.cursor()
            res=cur.execute("select * from `admin` where Email='"+a2+"' and Password='"+a5+"'")
            if res:
                root.destroy()
                prof=Profile()
            else:
                self.v6.set("Invalid email or password") 
        cur.close()
        conn.close()

    def openFrame(self,root):
        
        """   """
        root.destroy()
        app = MyApp()

    def onCloseOtherFrame(self,otherFrame):
        """"""
        otherFrame.destroy()
        app = LoginApp() 

app = LoginApp()


########################################################################


class MyApp:
    def __init__(self):

        root=tk.Tk()
        root.title("Registration Form")

        root.geometry("400x300")
        self.v1 = tk.StringVar()
        self.v2 = tk.StringVar()
        self.v3 = tk.StringVar()
        self.v4 = tk.StringVar()
        self.v5 = tk.StringVar()
        self.v6 = tk.StringVar()

        label1=tk.Label(root,text="Name:").grid(row=0,column=0)
        entry1=tk.Entry(root,textvariable=self.v1).grid(row=0,column=1)

        label2=tk.Label(root,text="Email:").grid(row=1,column=0)
        entry2=tk.Entry(root,textvariable=self.v2).grid(row=1,column=1)

        label3=tk.Label(root,text="Phone:").grid(row=2,column=0)
        entry3=tk.Entry(root,textvariable=self.v3).grid(row=2,column=1)

        self.g=tk.StringVar()

        label4=tk.Label(root,text="Gender:").grid(row=3,column=0)
        rb1=tk.Radiobutton(root,text="Male",variable=self.g,value="male").grid(row=3,column=1)
        rb2=tk.Radiobutton(root,text="Female",variable=self.g,value="female").grid(row=3,column=2)

        label5=tk.Label(root,text="Password:").grid(row=4,column=0)
        entry5=tk.Entry(root,show="*",textvariable=self.v4).grid(row=4,column=1)

        label6=tk.Label(root,text="Confirm password:").grid(row=5,column=0)

        entry6=tk.Entry(root,show="*",textvariable=self.v5).grid(row=5,column=1)

        button1=tk.Button(root,text="Submit",fg='blue',command=lambda: self.validate()).grid(row=6,column=1)


        label7=tk.Label(root,text=" ",textvariable=self.v6).grid(row=7,column=1)

 
        btn = tk.Button(root, text="Already Have an Account?",bg='yellow', command=lambda: self.openFrame(root)).grid(row=8,column=1)
    
    def validate(self):
        a1=str(self.v1.get())
        a2=str(self.v2.get())
        a3=str(self.v3.get())
        a4=str(self.g.get())
        a5=str(self.v4.get())
        a6=str(self.v5.get())
        if a5=='':
            self.v6.set("password must be filled")
        elif a5!=a6:
            self.v6.set("both password should be same")
        else:
            conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='student management system')
            cur=conn.cursor()
            res=cur.execute("select * from admin where Email='"+a2+"'")
            if res:
                self.v6.set("Email Already Exist")
            else:
                str1="INSERT INTO admin (`Name`, `Email`, `Phone`,`Gender`, `Password`) VALUES ('"+a1+"', '"+a2+"', '"+a3+"','"+a4+"', '"+a5+"')";
                try:
                    cur.execute(str1)
                    conn.commit()
                    self.v6.set("Inserted Sucessfully")
                except:
                    conn.rollback()
            cur.close()
            conn.close()

    def openFrame(self,root):
        """   """
        root.destroy()
        app = LoginApp()
   

########################################################################


class Profile:
   
    def __init__(self):
        
        root=tk.Tk()
        root.title("Profile Page")

        root.geometry("300x300")
        self.v1 = tk.StringVar()
        self.v2 = tk.StringVar()
        self.v3 = tk.StringVar()
        self.v4 = tk.StringVar()
        self.v5 = tk.StringVar()


        button1=tk.Button(root,text="Create New Admin",fg='indigo',command=lambda: self.create(root)).grid(row=1,column=2)
        label7=tk.Label(root,text=" ",textvariable=self.v1).grid(row=2,column=2)
        button1=tk.Button(root,text="Add New Student data",fg='green',command=lambda: self.add(root)).grid(row=3,column=2)
        label7=tk.Label(root,text=" ",textvariable=self.v2).grid(row=4,column=2)
        button1=tk.Button(root,text="View Record",fg='brown',command=lambda: self.view(root)).grid(row=5,column=2)
        label7=tk.Label(root,text=" ",textvariable=self.v3).grid(row=6,column=2)
        button1=tk.Button(root,text="Delete Record",fg='red',command=lambda: self.delete(root)).grid(row=7,column=2)
        label7=tk.Label(root,text=" ",textvariable=self.v4).grid(row=8,column=2)
        button1=tk.Button(root,text="Update Record",fg='purple',command=lambda: self.update(root)).grid(row=9,column=2)
        label7=tk.Label(root,text=" ",textvariable=self.v5).grid(row=10,column=2)
        button1=tk.Button(root,text="Logout",bg='yellow',command=lambda: self.validate(root)).grid(row=11,column=2)
 
    def create(self,root):
        
        """   """
        root.destroy()
        app = MyApp()

    def add(self,root):
        
        """   """
        root.destroy()
        add = AddNew()
        
    def view(self,root):
        
        """   """
        root.destroy()
        view = View()
        

    def delete(self,root):
        
        """   """
        root.destroy()
        delete=Delete()

    def update(self,root):
        
        """   """
        root.destroy()
        edit=Edit()

    def validate(self,root):
        
        """   """
        root.destroy()
        app = LoginApp()


    def onCloseOtherFrame(self,otherFrame):
        """"""
        otherFrame.destroy()
        prof=Profile()


########################################################################


class AddNew:
    def __init__(self):
        
        root=tk.Tk()
        root.title("Add New Student Data")

        root.geometry("400x300")
        self.v1 = tk.StringVar()
        self.v2 = tk.StringVar()
        self.v3 = tk.StringVar()
        self.v4 = tk.StringVar()
        self.v5 = tk.StringVar()
        
        label1=tk.Label(root,text="Name:").grid(row=0,column=0)
        entry1=tk.Entry(root,textvariable=self.v1).grid(row=0,column=1)

        label2=tk.Label(root,text="Roll no:").grid(row=1,column=0)
        entry2=tk.Entry(root,textvariable=self.v2).grid(row=1,column=1)

        label3=tk.Label(root,text="Department:").grid(row=2,column=0)
        entry3=tk.Entry(root,textvariable=self.v3).grid(row=2,column=1)

        label4=tk.Label(root,text="Marks:").grid(row=3,column=0)
        entry4=tk.Entry(root,textvariable=self.v4).grid(row=3,column=1)


        button1=tk.Button(root,text="Submit",fg='blue',command=lambda: self.validate()).grid(row=6,column=1)


        label7=tk.Label(root,text=" ",textvariable=self.v5).grid(row=7,column=1)

        btn = tk.Button(root, text="Return to Profile",bg='yellow', command=lambda: self.openFrame(root)).grid(row=8,column=1)

    def validate(self):
        a1=str(self.v1.get())
        a2=str(self.v2.get())
        a3=str(self.v3.get())
        a4=str(self.v4.get())
        a5=str(self.v5.get())
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='student management system')
        cur=conn.cursor()
        res=cur.execute("INSERT INTO `student database` (`Name`, `RollNo`, `Department`,`Marks`) VALUES ('"+a1+"', '"+a2+"', '"+a3+"','"+a4+"')")
        conn.commit()
        if res:
            self.v5.set("Inserted Sucessfully")
        else:
            self.v5.set("Failed")
        
        cur.close()
        conn.close()


    def openFrame(self,root):
        """   """
        root.destroy()
        prof=Profile()

########################################################################


class View:
    def __init__(self):
        
        root=tk.Tk()
        root.title("View Student Data")

        root.geometry("300x200")
        self.v1 = tk.StringVar()

        button1=tk.Button(root,text="View all Student Data",fg='blue',command=lambda: self.validate()).grid(row=1,column=1)
        label2=tk.Label(root,text=" ",textvariable=self.v1).grid(row=2,column=1)
 
        btn = tk.Button(root, text="Return to Profile",bg='yellow', command=lambda: self.openFrame(root)).grid(row=3,column=1)

    def validate(self):
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='student management system')

        cur=conn.cursor()

        res=cur.execute("SELECT * FROM `student database`")

        for r1 in cur:
            print(r1)

        cur.close()
        conn.close()

    def openFrame(self,root):
        """   """
        root.destroy()
        prof=Profile()


########################################################################


class Delete:
    def __init__(self):
        """Constructor"""
        root=tk.Tk()
        root.title("Delete Record")

        root.geometry("300x200")
        self.v1 = tk.StringVar()
        self.v2 = tk.StringVar()

        label1=tk.Label(root,text="Roll no:").grid(row=0,column=0)
        entry1=tk.Entry(root,textvariable=self.v1).grid(row=0,column=1)


        button1=tk.Button(root,text="Submit",fg='blue',command=lambda: self.validate()).grid(row=1,column=1)


        label2=tk.Label(root,text=" ",textvariable=self.v2).grid(row=2,column=1)

        btn = tk.Button(root, text="Return to Profile",bg='yellow', command=lambda: self.openFrame(root)).grid(row=8,column=1)
        
    def validate(self):
        a1=str(self.v1.get())
        a2=str(self.v2.get())

        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='student management system')
        cur=conn.cursor()
        res=cur.execute("delete from `student database` where RollNo='"+a1+"'")
        conn.commit()
        if res:
            self.v2.set("Deleted Sucessfully")
        else:
            self.v2.set("Failed. Incorrect Roll No.")
        
        cur.close()
        conn.close()


    def openFrame(self,root):
        """   """
        root.destroy()
        prof=Profile()


########################################################################


class Edit:
    def __init__(self):
        """Constructor"""
        root=tk.Tk()
        root.title("Update Record")

        root.geometry("300x300")
        self.v1 = tk.StringVar()
        self.v2 = tk.StringVar()
        self.v3 = tk.StringVar()
        self.v4 = tk.StringVar()
        self.v5 = tk.StringVar()
        
        label1=tk.Label(root,text="Name:").grid(row=0,column=0)
        entry1=tk.Entry(root,textvariable=self.v1).grid(row=0,column=1)

        label2=tk.Label(root,text="Roll no:").grid(row=1,column=0)
        entry2=tk.Entry(root,textvariable=self.v2).grid(row=1,column=1)

        label3=tk.Label(root,text="Department:").grid(row=2,column=0)
        entry3=tk.Entry(root,textvariable=self.v3).grid(row=2,column=1)

        label4=tk.Label(root,text="Marks:").grid(row=3,column=0)
        entry4=tk.Entry(root,textvariable=self.v4).grid(row=3,column=1)


        button1=tk.Button(root,text="Update",fg='blue',command=lambda: self.validate()).grid(row=6,column=1)


        label7=tk.Label(root,text=" ",textvariable=self.v5).grid(row=7,column=1)

        btn = tk.Button(root, text="Return to Profile",bg='yellow', command=lambda: self.openFrame(root)).grid(row=8,column=1)
 
    def validate(self):
        a1=str(self.v1.get())
        a2=str(self.v2.get())
        a3=str(self.v3.get())
        a4=str(self.v4.get())
        a5=str(self.v5.get())
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='student management system')
        cur=conn.cursor()
        res=cur.execute("update `student database` set Name='"+a1+"', Department='"+a3+"', Marks='"+a4+"' where Rollno='"+a2+"'")
        conn.commit()
        if res:
            self.v5.set("Updated Sucessfully")
        else:
            self.v5.set("Failed. Incorrect Roll No")
        
        cur.close()
        conn.close()


    def openFrame(self,root):
        """   """
        root.destroy()
        prof=Profile()


