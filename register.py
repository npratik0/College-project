# from tkinter import *
# from customtkinter import *
# import string
# import random

# def register():
#     # Get the user input
#     name = name_entry.get()
#     email = email_entry.get()
#     phone = phone_entry.get()
#     gender = gender_var.get()
#     password = password_entry.get()

#     # Generate the password strength
#     strength = 0
#     if len(password) >= 8:
#         strength += 1
#     if any(c.islower() for c in password):
#         strength += 1
#     if any(c.isupper() for c in password):
#         strength += 1
#     if any(c in string.digits for c in password):
#         strength += 1
#     if any(c in string.punctuation for c in password):
#         strength += 1

#     # Display the password strength
#     strength_label.config(text=f"Password strength: {strength}/5")

# def switch_to_login():
#     # Code to switch to the login page goes here
#     root.destroy()
#     import login

# def register():
#     # Code for displaying home
#     root.destroy()
#     import home

# root =Tk()
# root.title("Register Page")

# Label(root, text="Name:").grid(row=0, column=0)
# name_entry =Entry(root)
# name_entry.grid(row=0, column=1)

# Label(root, text="Email:").grid(row=1, column=0)
# email_entry =Entry(root)
# email_entry.grid(row=1, column=1)

# Label(root, text="Phone:").grid(row=2, column=0)
# phone_entry =Entry(root)
# phone_entry.grid(row=2, column=1)

# Label(root, text="Gender:").grid(row=3, column=0)
# gender_var =StringVar()
# gender_var.set("Male")
# Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1)
# Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=3, column=2)

# Label(root, text="Password:").grid(row=4, column=0)
# password_entry =Entry(root, show="*")
# password_entry.grid(row=4, column=1)

# Label(root, text="Password strength:").grid(row=5, column=0)
# strength_label =Label(root, text="")
# strength_label.grid(row=5, column=1)

# Button(root, text="Register", command=register).grid(row=6, column=1)
# Button(root, text="Already have an account?", command=switch_to_login).grid(row=7, column=0, columnspan=2)


# root.mainloop()



from tkinter import *
from customtkinter import *
import string
import sqlite3
from tkinter import messagebox


def register():
    # Get the user input
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    password = password_entry.get()
        # Check if required fields are empty
    if not name or not email or not phone or not gender or not password:
        messagebox.showerror("Error", "Please fill in all the required fields.")
        return
    # Generate the password strength
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c in string.digits for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    # Display the password strength
    strength_meter.place(x=300, y=310)
    strength_meter.config(text=f"Password strength: {strength}/5")

    # Connect to the SQLite database
    connection = sqlite3.connect('user_registration.db')
    cursor = connection.cursor()

    # Create a table for user registration if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            gender TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Insert user data into the table
    cursor.execute("INSERT INTO users (name, email, phone, gender, password) VALUES (?, ?, ?, ?, ?)",
                   (name, email, phone, gender, password))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

    messagebox.showinfo("Success", "Registration Successful!")

    switch_to_login()

def switch_to_login():
    # Code to switch to the login page goes here
    root.destroy()
    import login

def home():
    root.destroy()
    import home

root = Tk()
root.title("Register Page")
root.geometry("1200x750")

# Load and place an image on the left side
image_label = Label(root)
image_label.place(x=50, y=100)  # Adjust the position as needed
# Load your image here, for example:
photo = PhotoImage(file="registerimage.png")
# Resize the image slightly larger
photo = photo.subsample(1, 1)
image_label.config(image=photo)
image_label.image = photo

# Custom frame with styling on the right side
frame_mid = CTkFrame(root, width=500, height=500, bg_color="#f8f9fa", border_color="#adb5bd")
frame_mid.place(x=650, y=100)

# Register label
register_label = Label(root, text="Register", font=("Arial", 36, "bold"), fg="#333333")
register_label.place(x=750, y=10)

# Name
Label(frame_mid, text="Name:", font=("Arial", 16)).place(x=50, y=50)
name_entry = Entry(frame_mid, font=("Arial", 14))
name_entry.place(x=200, y=50)

# Email
Label(frame_mid, text="Email:", font=("Arial", 16)).place(x=50, y=100)
email_entry = Entry(frame_mid, font=("Arial", 14))
email_entry.place(x=200, y=100)

# Phone
Label(frame_mid, text="Phone:", font=("Arial", 16)).place(x=50, y=150)
phone_entry = Entry(frame_mid, font=("Arial", 14))
phone_entry.place(x=200, y=150)

# Gender
Label(frame_mid, text="Gender:", font=("Arial", 16)).place(x=50, y=200)
gender_var = StringVar()
gender_var.set("Male")
Radiobutton(frame_mid, text="Male", variable=gender_var, value="Male", font=("Arial", 14)).place(x=200, y=200)
Radiobutton(frame_mid, text="Female", variable=gender_var, value="Female", font=("Arial", 14)).place(x=300, y=200)

# Password
Label(frame_mid, text="Password:", font=("Arial", 16)).place(x=50, y=250)
password_entry = Entry(frame_mid, show="*", font=("Arial", 14))
password_entry.place(x=200, y=250)

# Password strength
Label(frame_mid, text="Password strength:", font=("Arial", 16)).place(x=50, y=300)
strength_meter = Label(frame_mid, text="", font=("Arial", 14))
strength_meter.place(x=300, y=300)

# Register Button
Button(frame_mid, text="Register", command=register, font=("Arial", 16)).place(x=200, y=370)

# Already have an account label
Label(frame_mid, text="Already have an account?", font=("Arial", 14)).place(x=150, y=420)

# Switch to Login Button
Button(frame_mid, text="Log in", command=switch_to_login, font=("Arial", 14)).place(x=400, y=420)

root.mainloop()
########prratik is don####