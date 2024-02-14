from tkinter import *

def register():
    # Code for registering a new user goes here
    root.destroy()
    import register

def login():
    root.destroy()
    import home

root = Tk()
root.title("Login Page")
from tkinter import *

def register():
    # Code for registering a new user goes here
    root.destroy()
    import register

def login():
    root.destroy()
    import home

root = Tk()
root.title("Login Page")

# Configure outer frame with white color
outer_frame = Frame(root, bg="white")
outer_frame.pack()

# Configure inner frame
inner_frame = Frame(outer_frame, bg="white")
inner_frame.pack(pady=20)

username_label = Label(inner_frame, text="Username:")
username_label.grid(row=0, column=0)
username_entry = Entry(inner_frame)
username_entry.grid(row=0, column=1)

password_label = Label(inner_frame, text="Password:")
password_label.grid(row=1, column=0)
password_entry = Entry(inner_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = Button(outer_frame, text="Log in", command=login)
login_button.pack(pady=10)

donthaveaccount_label = Label(outer_frame, text="Don't have an account?")
donthaveaccount_label.pack()

register_button = Button(outer_frame, text="Register", command=register)
register_button.pack(pady=10)

root.mainloop()

