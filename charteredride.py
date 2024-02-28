from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

def home():
    root.destroy()
    import home  

def calculate_fare(pickup_date, return_date):
    # Calculate the number of days between pickup and return dates
    days = (return_date - pickup_date).days
    fare = days * 1000  # Fare rate NRP1000 per day
    return fare

def book_ride():
    pickup_loc = entry_pickuplocation.get()
    destination = entry_destination.get()
    pickup_date_value = pickup_date.get_date()
    return_date_value = return_date.get_date()

    # Create a new window to display ride details and fare
    ride_details_window = Toplevel(root)
    ride_details_window.title("Ride Details")
    ride_details_window.geometry("400x200")

    lbl_pickuploc = Label(ride_details_window, text="Pickup Location: " + pickup_loc)
    lbl_pickuploc.pack()

    lbl_destination = Label(ride_details_window, text="Destination: " + destination)
    lbl_destination.pack()

    lbl_pickupdate = Label(ride_details_window, text="Pickup Date: " + pickup_date_value.strftime("%Y-%m-%d"))
    lbl_pickupdate.pack()

    lbl_returndate = Label(ride_details_window, text="Return Date: " + return_date_value.strftime("%Y-%m-%d"))
    lbl_returndate.pack()

    fare = calculate_fare(pickup_date_value, return_date_value)
    lbl_fare = Label(ride_details_window, text="Fare: NRP " + str(fare))
    lbl_fare.pack()

root = Tk()
root.title("Ride Booking System")
root.geometry("800x700")
root.configure(bg="lightblue")  # Set background color

# Entry and DateEntry widgets
entry_pickuplocation = Entry(root, width=40)
entry_pickuplocation.place(x=250, y=155)

entry_destination = Entry(root, width=40)
entry_destination.place(x=250, y=185)

pickup_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
pickup_date.place(x=250, y=225)

return_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
return_date.place(x=250, y=255)

# Labels
lbl_1 = Label(root, text="Ride Booking System", font=("Arial Bold", 40), bg="lightblue")
lbl_1.place(x=100, y=5)

lbl_2 = Label(root, text="Chartered Ride", font=("Arial", 15), bg="lightblue")
lbl_2.place(x=0, y=70)

lbl_pickuplocation = Label(root, text="Pickup Location", font=("Arial", 15), bg="lightblue")
lbl_pickuplocation.place(x=70, y=150)

lbl_destination = Label(root, text="Destination", font=("Arial", 15), bg="lightblue")
lbl_destination.place(x=70, y=180)

lbl_pickupdate = Label(root, text="Pickup Date", font=("Arial", 15), bg="lightblue")
lbl_pickupdate.place(x=70, y=220)

lbl_returndate = Label(root, text="Return Date", font=("Arial", 15), bg="lightblue")
lbl_returndate.place(x=70, y=250)

# Buttons
btn_home = ttk.Button(root, text="Home", command=home, width=15)
btn_home.place(x=680, y=70)

btn_book = ttk.Button(root, text="Book", command=book_ride, width=30)
btn_book.place(x=400, y=500, anchor=CENTER)

btn_help = ttk.Button(root, text="Help")
btn_help.place(x=10, y=630)

root.mainloop()
