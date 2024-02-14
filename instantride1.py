from tkinter import *
import random

def home():
    root.destroy()
    import home

def book_ride():
    pickup_location = pickup.get()
    destination_location = destination.get()
    vehicle_type = vehicle_var.get()
    distance = random.randint(1, 15)
    fare = distance * fare_rate[vehicle_type]
    display_fare_window(pickup_location, destination_location, distance, fare, vehicle_type)

def display_fare_window(pickup_location, destination_location, distance, fare, vehicle_type):
    fare_window =Toplevel()
    fare_window.title("Fare Information")
    fare_window.geometry("400x200")

    Label(fare_window, text="Pickup Location:").pack()
    Label(fare_window, text=pickup_location).pack()

    Label(fare_window, text="Destination:").pack()
    Label(fare_window, text=destination_location).pack()

    Label(fare_window, text="Distance (km):").pack()
    Label(fare_window, text=distance).pack()

    Label(fare_window, text="Vehicle Type:").pack()
    Label(fare_window, text=vehicle_type).pack()

    Label(fare_window, text="Fare:").pack()
    Label(fare_window, text=f"{fare} NRP").pack()

root =Tk()
root.title("Ride booking app")
root.geometry("800x700")

lbl =Label(root, text="Ride Booking App", font=("Arial Bold", 40)).place(x=100, y=50)
lbl_1 =Label(root, text="Instant Ride", font=("Arial", 10)).place(x=10, y=150)

vehicle_label = Label(root, text="Select your vehicle type", font=("Arial", 20)).place(x=100, y=220)

# Create a variable to store the selected vehicle type
vehicle_var = StringVar()
# Create an OptionMenu widget to select between bike and car
vehicle_option_menu = OptionMenu(root, vehicle_var, "Bike", "Car")
vehicle_option_menu.place(x=450, y=220)

pickup_label = Label(root, text="Pickup location", font=("Arial", 20)).place(x=100, y=360)
destination_label = Label(root, text="Destination", font=("Arial", 20)).place(x=100, y=415)

pickup = Entry(root, width=60)
pickup.place(x=300, y=365, height=35)

destination = Entry(root, width=60)
destination.place(x=300, y=420, height=35)

help_button = Button(root, text="Help", command=lambda: print("Help"))
help_button.place(x=5, y=650)

# Define fare rates for bike and car
fare_rate = {"Bike": 100, "Car": 200}

book_button = Button(root, text="Book", command=lambda: book_ride())
book_button.place(x=760, y=650)

home_button = Button(root, text="Home", command=home)
home_button.place(x=760, y=150)

root.mainloop()