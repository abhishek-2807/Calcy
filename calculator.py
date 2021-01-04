from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

a=0


def verify():

    f = open(r"C:\Users\Home\PycharmProjects\Abhishek\test.txt", "r")
    data = f.read().split()

    user = e1.get()
    p = e2.get()

    e1.delete(0, END)
    e2.delete(0, END)

    if user in data and p in data:
            messagebox.showinfo("Login Successful", "Press OK to continue to App")
            ro.withdraw()
            root.deiconify()

    else:
        messagebox.showerror("Error","Username or password did not match")

def write(w):
    global a
    s = e.get()
    if s == "Enter Expression" or a == 1:
        e.delete(0,END)
        s=""
        a=0
    s = s + w
    e.delete(0,END)
    e.insert(0,s)


def clear():
    e.delete(0,END)

def final():
    global a
    try:
        s = str(eval(e.get()))
        e.delete(0,END)
        e.insert(0,s)
        a=1
    except:
        e.delete(0,END)
        e.insert(0,"E")
        a=1



def del_me():
    s = str(e.get())
    l = len(s)
    e.delete(0, END)
    for i in range(0,l-1):
        e.insert(END, str(s[i]))


if __name__ == "__main__":
    ro = Tk()
    root = Toplevel(ro)

    ro.configure(background="yellow")
    ro.title("Login Panel")
    ro.geometry("300x250")

    root.configure(background="yellow")
    root.title("Calculator")
    root.geometry("300x250")
    root.withdraw()

    my = Font(family="Helvetica", size=16, weight="bold", slant="italic")

    Label(ro, text="Please enter details below to log in").pack()
    Label(ro,text="",bg="yellow").pack()

    Label(ro,text="Username * ").pack()
    e1= Entry(ro)
    e1.pack()
    Label(ro,text="",bg="yellow").pack()
    Label(ro,text="Password * ").pack()
    e2=Entry(ro,show="*")
    e2.pack()
    Label(ro, text="",bg="yellow").pack()
    Button(ro, text="Login",width=10,height=1,command=verify).pack()
    Label(ro,text="",bg="yellow").pack()
    Label(ro, text="Presented by :-   Abhishek", font=my, fg="red").pack()

    e = Entry(root, width=400)
    e.grid(columnspan=4,ipady=8)
    e.insert(0, "Enter Expression")

    b1 = Button(root, text="1", fg="black", bg="green", command=lambda: write("1"), height=1, width=7)
    b1.place(x=10, y=40)
    b2 = Button(root, text="2", fg="black", bg="green", command=lambda: write("2"), height=1, width=7)
    b2.place(x=80, y=40)
    b3 = Button(root, text="3", fg="black", bg="green", command=lambda: write("3"), height=1, width=7)
    b3.place(x=150, y=40)
    b4 = Button(root, text="4", fg="black", bg="green", command=lambda: write("4"), height=1, width=7)
    b4.place(x=10, y=65)
    b5 = Button(root, text="5", fg="black", bg="green", command=lambda: write("5"), height=1, width=7)
    b5.place(x=80, y=65)
    b6 = Button(root, text="6", fg="black", bg="green", command=lambda: write("6"), height=1, width=7)
    b6.place(x=150, y=65)
    b7 = Button(root, text="7", fg="black", bg="green", command=lambda: write("7"), height=1, width=7)
    b7.place(x=10, y=90)
    b8 = Button(root, text="8", fg="black", bg="green", command=lambda: write("8"), height=1, width=7)
    b8.place(x=80, y=90)
    b9 = Button(root, text="9", fg="black", bg="green", command=lambda: write("9"), height=1, width=7)
    b9.place(x=150, y=90)
    b0 = Button(root, text="0", fg="black", bg="green", command=lambda: write("0"), height=1, width=7)
    b0.place(x=80, y=115)
    bp = Button(root, text="+", fg="black", bg="green", command=lambda: write("+"), height=1, width=7)
    bp.place(x=220, y=40)
    bv = Button(root, text="-", fg="black", bg="green", command=lambda: write("-"), height=1, width=7)
    bv.place(x=220, y=65)
    bm = Button(root, text="x", fg="black", bg="green", command=lambda: write("*"), height=1, width=7)
    bm.place(x=220, y=90)
    bn = Button(root, text="/", fg="black", bg="green", command=lambda: write("/"), height=1, width=7)
    bn.place(x=220, y=115)
    br = Button(root, text="Clear", fg="black", bg="green", command=clear, height=1, width=7)
    br.place(x=185, y=150)
    bd = Button(root, text=".", fg="black", bg="green", command=lambda: write("."), height=1, width=7)
    bd.place(x=10, y=115)
    bf = Button(root, text="=", fg="black", bg="green", command=final, height=1, width=7)
    bf.place(x=150, y=115)
    be = Button(root, text="Delete", fg="black", bg="green", command=del_me, height=1, width=7)
    be.place(x=45, y=150)

    l1 = Label(root, text="Presented by :-   Abhishek", font=my, fg="red")
    l1.place(x=10, y=200)

    root.mainloop()


