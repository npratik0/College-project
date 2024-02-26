from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import *
import sqlite3

# Function to retrieve data from the database
def get_users():
    connection = sqlite3.connect('user_registration.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()
    return users

# Function to add a new user to the database
def add_user_to_db(name, email, phone, gender, password):
    connection = sqlite3.connect('user_registration.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email, phone, gender, password) VALUES (?, ?, ?, ?, ?)",
                   (name, email, phone, gender, password))
    connection.commit()
    connection.close()

# Function to update user details in the database
def update_user_in_db(user_id, name, email, phone, gender, password):
    connection = sqlite3.connect('user_registration.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET name=?, email=?, phone=?, gender=?, password=? WHERE id=?",
                   (name, email, phone, gender, password, user_id))
    connection.commit()
    connection.close()

# Function to delete a user from the database
def delete_user_from_db(user_id):
    connection = sqlite3.connect('user_registration.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    connection.commit()
    connection.close()

# Function to display user details
def display_details():
    def search_user():
        query = search_entry.get()
        if query:
            filtered_users = [user for user in users if query.lower() in str(user).lower()]
            display_users(filtered_users)
        else:
            display_users(users)

    def display_users(users_list):
        for i in tree.get_children():
            tree.delete(i)
        for user in users_list:
            # Show all details including password
            tree.insert("", "end", text="User", values=user)

    details_window = Toplevel()
    details_window.title("User Details")

    search_frame = CTkFrame(details_window, width=800, height=50, bg_color="#f8f9fa", border_color="#adb5bd")
    search_frame.pack(side=TOP, fill=X)

    search_entry = Entry(search_frame, font=("Arial", 14))
    search_entry.pack(side=LEFT, padx=10, pady=10)

    search_button = CTkButton(search_frame, text="Search", command=search_user, font=("Arial", 14))
    search_button.pack(side=LEFT, padx=10, pady=10)

    tree_frame = CTkFrame(details_window, width=800, height=450, bg_color="#f8f9fa", border_color="#adb5bd")
    tree_frame.pack(side=TOP, fill=BOTH, expand=True)

    tree = ttk.Treeview(tree_frame)
    tree["columns"] = ("ID", "Name", "Email", "Phone", "Gender", "Password")
    tree.heading("#0", text="Type")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Email", text="Email")
    tree.heading("Phone", text="Phone")
    tree.heading("Gender", text="Gender")
    tree.heading("Password", text="Password")

    # Retrieve user details from the database
    users = get_users()
    display_users(users)

    tree.pack(expand=True, fill="both")

# Function for admin login
def admin_login():
    global username_entry, password_entry
    username = username_entry.get()
    password = password_entry.get()

    # Dummy admin credentials for demonstration
    if username == "admin" and password == "admin":
        login_success()
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Function to handle login success
def login_success():
    login_window.destroy()

    # Open the admin dashboard
    admin_dashboard()

# Function to add a new user
def add_user():
    global name_entry, email_entry, phone_entry, gender_var, password_entry
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    password = password_entry.get()

    if name and email and phone and gender and password:
        add_user_to_db(name, email, phone, gender, password)
        messagebox.showinfo("Success", "User added successfully")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

# Function to update user details
def update_user():
    global user_id_entry, name_entry, email_entry, phone_entry, gender_var, password_entry
    user_id = user_id_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    password = password_entry.get()

    if user_id and name and email and phone and gender and password:
        update_user_in_db(user_id, name, email, phone, gender, password)
        messagebox.showinfo("Success", "User updated successfully")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

# Function to delete user details
def delete_user():
    user_id = user_id_entry.get()
    if user_id:
        delete_user_from_db(user_id)
        messagebox.showinfo("Success", "User deleted successfully")
    else:
        messagebox.showerror("Error", "Please provide the User ID")

# Create the admin dashboard
def admin_dashboard():
    global user_id_entry, name_entry, email_entry, phone_entry, gender_var, password_entry
    dashboard_window = Tk()
    dashboard_window.title("Admin Dashboard")

    frame_mid = CTkFrame(dashboard_window, width=800, height=500, bg_color="#f8f9fa", border_color="#adb5bd")
    frame_mid.place(x=50, y=50)

    Label(frame_mid, text="User ID:", font=("Arial", 14)).place(x=50, y=50)
    user_id_entry = Entry(frame_mid, font=("Arial", 14))
    user_id_entry.place(x=200, y=50)

    Label(frame_mid, text="Name:", font=("Arial", 14)).place(x=50, y=100)
    name_entry = Entry(frame_mid, font=("Arial", 14))
    name_entry.place(x=200, y=100)

    Label(frame_mid, text="Email:", font=("Arial", 14)).place(x=50, y=150)
    email_entry = Entry(frame_mid, font=("Arial", 14))
    email_entry.place(x=200, y=150)

    Label(frame_mid, text="Phone:", font=("Arial", 14)).place(x=50, y=200)
    phone_entry = Entry(frame_mid, font=("Arial", 14))
    phone_entry.place(x=200, y=200)

    Label(frame_mid, text="Gender:", font=("Arial", 14)).place(x=50, y=250)
    gender_var = StringVar(frame_mid)
    gender_var.set("Male")
    Radiobutton(frame_mid, text="Male", variable=gender_var, value="Male", font=("Arial", 14)).place(x=200, y=250)
    Radiobutton(frame_mid, text="Female", variable=gender_var, value="Female", font=("Arial", 14)).place(x=300, y=250)

    Label(frame_mid, text="Password:", font=("Arial", 14)).place(x=50, y=300)
    password_entry = Entry(frame_mid, font=("Arial", 14), show="*")
    password_entry.place(x=200, y=300)

    add_button = CTkButton(frame_mid, text="Add User", command=add_user, font=("Arial", 14))
    add_button.place(x=50, y=350)

    update_button = CTkButton(frame_mid, text="Update User", command=update_user, font=("Arial", 14))
    update_button.place(x=200, y=350)

    delete_button = CTkButton(frame_mid, text="Delete User", command=delete_user, font=("Arial", 14))
    delete_button.place(x=350, y=350)

    display_button = CTkButton(frame_mid, text="Display Details", command=display_details, font=("Arial", 14))
    display_button.place(x=500, y=350)

    dashboard_window.geometry("900x600")
    dashboard_window.mainloop()

# Create the login window
login_window = Tk()
login_window.title("Admin Login")

frame_mid = CTkFrame(login_window, width=400, height=250, bg_color="#f8f9fa", border_color="#adb5bd")
frame_mid.place(x=100, y=50)

CTkLabel(frame_mid, text="Username:", font=("Arial", 14)).place(x=50, y=50)
username_entry = Entry(frame_mid, font=("Arial", 14))
username_entry.place(x=200, y=50)

CTkLabel(frame_mid, text="Password:", font=("Arial", 14)).place(x=50, y=100)
password_entry = Entry(frame_mid, show="*", font=("Arial", 14))
password_entry.place(x=200, y=100)

login_button = CTkButton(frame_mid, text="Login", command=admin_login, font=("Arial", 14))
login_button.place(x=150, y=150)

login_window.geometry("600x400")
login_window.mainloop()
