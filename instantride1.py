from tkinter import *
from tkinter import messagebox
import random
import sqlite3

def home():
    root.destroy()
    import home

def book_ride():
    pickup_location = pickup.get()
    destination_location = destination.get()

    # Check if pickup and destination are entered
    if not pickup_location or not destination_location:
        messagebox.showerror("Error", "Please enter both pickup and destination locations.")
        return

    # Check if a vehicle type is selected
    if not vehicle_var.get():
        messagebox.showerror("Error", "Please select a vehicle type.")
        return

    vehicle_type = vehicle_var.get()
    distance = random.randint(1, 15)
    fare = distance * fare_rate[vehicle_type]

    # Connect to the SQLite database
    connection = sqlite3.connect('user_registration.db')
    cursor = connection.cursor()

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

    display_fare_window(pickup_location, destination_location, distance, fare, vehicle_type)

    # Clear entry fields
    pickup.delete(0, END)
    destination.delete(0, END)

    # Optionally, provide user feedback
    messagebox.showinfo("Success", "Ride booked successfully!")

def create_rides():
    connection = sqlite3.connect('rides.db')
    cursor = connection.cursor()

    # Create a rides table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rides (
            ride_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            pickup_location TEXT NOT NULL,
            destination_location TEXT NOT NULL,
            distance INTEGER,
            fare INTEGER,
            vehicle_type TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

def display_fare_window(pickup_location, destination_location, distance, fare, vehicle_type):
    fare_window = Toplevel()
    fare_window.title("Fare Information")
    fare_window.geometry("400x200")

    Label(fare_window, text="Pickup Location:", font=("Arial", 12)).pack()
    Label(fare_window, text=pickup_location, font=("Arial", 12)).pack()

    Label(fare_window, text="Destination:", font=("Arial", 12)).pack()
    Label(fare_window, text=destination_location, font=("Arial", 12)).pack()

    Label(fare_window, text="Distance (km):", font=("Arial", 12)).pack()
    Label(fare_window, text=distance, font=("Arial", 12)).pack()

    Label(fare_window, text="Vehicle Type:", font=("Arial", 12)).pack()
    Label(fare_window, text=vehicle_type, font=("Arial", 12)).pack()

    Label(fare_window, text="Fare:", font=("Arial", 12)).pack()
    Label(fare_window, text=f"{fare} NRP", font=("Arial", 12)).pack()

root = Tk()
root.title("Ride booking System")
root.geometry("800x700")


root.configure(bg="light blue")  # Change background color to white

lbl = Label(root, text="Ride Booking System", font=("Arial Bold", 40),bg="lightblue") 
lbl.place(x=100, y=50)
lbl_1 = Label(root, text="Instant Ride", font=("Arial", 15),bg="lightblue")  
lbl_1.place(x=10, y=150)

vehicle_label = Label(root, text="Select your vehicle type", font=("Arial", 20),bg="lightblue") 
vehicle_label.place(x=100, y=220)

# Create a variable to store the selected vehicle type
vehicle_var = StringVar()
# Create an OptionMenu widget to select between bike and car
vehicle_option_menu = OptionMenu(root, vehicle_var, "", "Bike", "Car")
vehicle_option_menu.config(width=10)
vehicle_option_menu.place(x=450, y=220)

pickup_label = Label(root, text="Pickup location", font=("Arial", 20),bg="lightblue")  
pickup_label.place(x=100, y=360)
destination_label = Label(root, text="Destination", font=("Arial", 20),bg="lightblue")
destination_label.place(x=100, y=415)

pickup = Entry(root, width=40)
pickup.place(x=300, y=365, height=35)

destination = Entry(root, width=40)
destination.place(x=300, y=420, height=35)

help_button = Button(root, text="Help", command=lambda: print("Help"), bg="#007bff", fg="white", font=("Arial", 20))  # Change button color to blue and text color to white
help_button.place(x=5, y=650)

# Define fare rates for bike and car
fare_rate = {"Bike": 100, "Car": 200}

book_button = Button(root, text="Book", command=book_ride, bg="#007bff", fg="white", font=("Arial", 20))  # Change button color to blue and text color to white
book_button.place(x=400, y=500)

home_button = Button(root, text="Home", command=home, bg="#007bff", fg="white", font=("Arial", 20))  # Change button color to blue and text color to white
home_button.place(x=700, y=150)

root.mainloop()
