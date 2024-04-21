from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#function for button sign-in
def signin():
    username=user.get()
    password=code.get()

    #dashboard window
    if username=='jmabalos' and password=='jm123':
        screen=Toplevel(root)
        screen.title("Dashboard")
        screen.geometry('1366x768')
        screen.config(bg="white")

        #header
        header = Frame(screen, bg='#009df4')
        header.place(x=300, y=0, width=1500, height=60)

        logout_text = Label(header, text="Logout", bg='#009df4', font=("", 20, "bold"), bd=0, fg='white')
        logout_text.place(x=1000, y=15)

        #sidebar
        sidebar = PhotoImage(file='images/background.png')
        sidebar_label = Label(screen, image=sidebar)
        sidebar_label.place(x=0, y=0, width=300, height=900)

        #profile
        logoImage = PhotoImage(file='images/profile.png')
        logo = Label(screen, image=logoImage)
        logo.place(x=46, y=0, width=200, height=195)

        #profile name
        name = Label(screen, text='DASHBOARD', font=("", 20, "bold"))
        name.place(x=55, y=200)

        #sales-graph
        graph_image = PhotoImage(file='images/sales-growth.png')
        graph = Label(screen, image=graph_image, bg='#ffffff')
        graph.place(x=320, y=70)

        #piechart
        piechart_image = PhotoImage(file='images/pie-graph.png')
        piechart = Label(screen, image=piechart_image, bg='#ffffff')
        piechart.place(x=870, y=70, height=350)

        #color frames
        bodyFrame2 = Frame(screen, bg='green')
        bodyFrame2.place(x=328, y=495, width=310, height=220)

        bodyFrame3 = Frame(screen, bg='#ffcb1f')
        bodyFrame3.place(x=680, y=495, width=310, height=220)

        bodyFrame4 = Frame(screen, bg='#e21f26')
        bodyFrame4.place(x=1030, y=495, width=310, height=220)

        screen.mainloop()

    elif username!='jmabalos' and password!='jm123':
        messagebox.showerror("Invalid", "invalid username and password")

    elif password!='jm123':
        messagebox.showerror("Invalid", "invalid password")

    elif username!='jmabalos':
        messagebox.showerror("Invalid", "invalid username")

#Image
img = PhotoImage(file='images/login.png')
Label(root,image=img,bg='white').place(x=50, y=50)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading = Label(frame,text='Sign in', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#function for username
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

#username
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#function for password
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
#password
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#button
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2', fg='#57a1f8')
sign_up.place(x=215,y=270)

root.mainloop()