# from tkinter import * 
# from customtkinter import *

# def register():
#     # Code for registering a new user goes here
#     root.destroy()
#     import register

# def login():
#     root.destroy()
#     import home

# root =Tk()
# root.title("Login Page")
# root.geometry("1200x750")


# frame_mid=CTkFrame(root,width=500,height=500, fg_color="#f56290", border_color="#0d0c0c").place(x=650,y=100)

# username_label =Label(root, text="Username:")
# username_label.place(x=700,y=200)
# username_entry =Entry(root)
# username_entry.place(x=800,y=200)

# password_label =Label(root, text="Password:")
# password_label.place(x=700,y=300)
# password_entry =Entry(root, show="*")
# password_entry.place(x=800,y=300)

# login_button =Button(root, text="Log in", command=login)
# login_button.place(x=800,y=400)

# donthaveaccount_label =Label(root, text="Don't have an account?")
# donthaveaccount_label.place(x=700,y=500)

# register_button =Button(root, text="Register", command=register)
# register_button.place(x=850,y=500)

# root.mainloop()



from tkinter import *
from customtkinter import *

from tkinter import messagebox
import sqlite3

def register():
    # Code for registering a new user goes here
    root.destroy()
    import register

def home():
    root.destroy()
    import home

def login():
    # Get the entered username and password
    entered_username = username_entry.get()
    entered_password = password_entry.get()

# Check if the username or password is empty
    if not entered_username or not entered_password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return
    
    # Connect to the SQLite database
    connection = sqlite3.connect('user_registration.db')
    cursor = connection.cursor()

    # Query to check if the entered credentials are valid
    cursor.execute("SELECT * FROM users WHERE name=? AND password=?", (entered_username, entered_password))
    user = cursor.fetchone()

    # Close the connection
    connection.close()

    if user:
        # If user exists, login is successful
        messagebox.showinfo("Success", "Login Successful!")
        home()
    else:
        # If user doesn't exist or credentials are incorrect, show an error message
        messagebox.showerror("Error", "Invalid username or password. Please try again.")


root = Tk()
root.title("Login Page")
root.geometry("1200x750")
root.resizable(FALSE,FALSE)

# Load and place an image on the left side
image_label = Label(root)
image_label.place(x=50, y=100)  # Adjust the position as needed
photo = PhotoImage(file="loginimage.png")  # Load the image
image_label.config(image=photo)
image_label.image = photo

login_label = Label(root, text="Log in", font=("Helvetica", 24), fg="#333333")
login_label.place(x=910, y=50)

# Custom frame with styling on the right side
frame_mid = CTkFrame(root, width=500, height=500, bg_color="#f8f9fa", border_color="#adb5bd")
frame_mid.place(x=700, y=100)

# Username Label
username_label = Label(frame_mid, text="Username:", font=("Helvetica", 14), fg="#495057", bg="#f8f9fa")
username_label.place(x=50, y=50)

# Username Entry
username_entry = Entry(frame_mid, font=("Helvetica", 14), bg="#e9ecef")
username_entry.place(x=200, y=50)

# Password Label
password_label = Label(frame_mid, text="Password:", font=("Helvetica", 14), fg="#495057", bg="#f8f9fa")
password_label.place(x=50, y=100)

# Password Entry
password_entry = Entry(frame_mid, show="*", font=("Helvetica", 14), bg="#e9ecef")
password_entry.place(x=200, y=100)

# Login Button
login_button = Button(frame_mid, text="Log in", command=login, font=("Helvetica", 14), bg="#007bff", fg="#ffffff")
login_button.place(x=270, y=150)

# "Don't have an account?" Label
donthaveaccount_label = Label(frame_mid, text="Don't have an account?", font=("Helvetica", 12), fg="#495057", bg="#f8f9fa")
donthaveaccount_label.place(x=50, y=250)

# Register Button
register_button = Button(frame_mid, text="Register", command=register, font=("Helvetica", 12), bg="#28a745", fg="#ffffff")
register_button.place(x=300, y=250)

root.mainloop()
