from customerlibrary import CustomerLibs
from tkinter import *
from tkinter import messagebox
from loginbackend import login


class LoginGUI():
    def __init__(self,root):
        self.root=root
        self.root.title('LOGIN PAGE')
        self.root.geometry('500x300')
        self.root.resizable(width=0, height=0)

        frame=Frame(self.root, bg='black', height=60)
        frame.pack(side=TOP, fill=BOTH)

        titlelabel=Label(frame, text='LOGIN SYSTEM BANK', font=('Times New Roman',16,'bold'))
        titlelabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        usernamelabel=Label(self.root, text="Username:", font=('Times New Roman',14))
        usernamelabel.place(x=60,y=100)

        usernametext=Entry(self.root, font=('Times New Roman',14))
        usernametext.place(x=200, y=100)

        passwordlabel=Label(self.root, text="Password:", font=('Times New Roman',14))
        passwordlabel.place(x=60, y=150)

        passwordtext=Entry(self.root, font=('Times New Roman',14),show="*")
        passwordtext.place(x=200, y=150)

        def loginlogic():
            customerdata=CustomerLibs(username=usernametext.get(), password=passwordtext.get())
            result=login(customerdata)
            if result!=None:
                messagebox.showinfo("ACCOUNT PAGE","LOGIN SUCCESSFUL\n Welcome client {}".format(usernametext.get()))

            else:
                messagebox.showerror("Error","Incorrect email and password")



        loginbtn=Button(self.root, text="Login",command=loginlogic, font=('Times New Roman',14))
        loginbtn.place(x=200, y=200)



if __name__=='__main__':
    root=Tk()
    LoginGUI(root)
    root.mainloop()