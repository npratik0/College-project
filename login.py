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



# Custom frame with styling on the right side

frame_mid = CTkFrame(root, width=500, height=500, bg_color="white", border_color="black")
frame_mid.place(x=750, y=100)


login_label = Label(frame_mid, text="Log in", font=("Helvetica", 32), fg="#f8f5fa",bg="#7933ab")
login_label.place(x=200, y=50)

# Username Label
username_label = Label(frame_mid, text="Username:", font=("Helvetica", 14), fg="#495057", bg="#f8f9fa")
username_label.place(x=10, y=150)

# Username Entry
username_entry = Entry(frame_mid, font=("Helvetica", 14), bg="#e9ecef")
username_entry.place(x=200, y=150)

# Password Label
password_label = Label(frame_mid, text="Password:", font=("Helvetica", 14), fg="#495057", bg="#f8f9fa")
password_label.place(x=10, y=180)

# Password Entry
password_entry = Entry(frame_mid, show="*", font=("Helvetica", 14), bg="#e9ecef")
password_entry.place(x=200, y=180)

# Login Button
login_button = Button(frame_mid, text="Log in", command=login, font=("Helvetica", 14), bg="#007bff", fg="#ffffff")
login_button.place(x=200, y=290)

# "Don't have an account?" Label
donthaveaccount_label = Label(frame_mid, text="Don't have an account?", font=("Helvetica", 12), fg="#495057", bg="#f8f9fa")
donthaveaccount_label.place(x=50, y=400)

# Register Button
register_button = Button(frame_mid, text="Register", command=register, font=("Helvetica", 12), bg="#28a745", fg="#ffffff")
register_button.place(x=300, y=400)


def admin_login():
    root.destroy()
    import admin

#Admin login 
admin_button = Button(frame_mid, text="Admin Log in", command=admin_login, font=("Helvetica", 14), bg="#007bff", fg="#ffffff")
admin_button.place(x=300, y=450)

root.mainloop()

