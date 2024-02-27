from tkinter import *
from tkcalendar import DateEntry
root=Tk()
root.title("Ride Booking App")
root.geometry("800x700")
root.configure(bg="white")

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
    ride_details_window.configure(bg="white")

    lbl_pickuploc = Label(ride_details_window, text="Pickup Location: " + pickup_loc)
    lbl_pickuploc.pack()

    lbl_destination = Label(ride_details_window, text="Destination: " + destination)
    lbl_destination.pack()

    lbl_pickupdate = Label(ride_details_window, text="Pickup Date: " + pickup_date_value.strftime("%Y-%m-%d"))
    lbl_pickupdate.pack()

    lbl_returndate = Label(ride_details_window, text="Return Date: " + return_date_value.strftime("%Y-%m-%d"))
    lbl_returndate.pack()

    fare = calculate_fare(pickup_date_value, return_date_value)
    lbl_fare = Label(ride_details_window, text="Fare: NRP " + str(fare), bg="blue", fg="white")
    lbl_fare.pack()

btn_book = Button(root, text="Book", font=("Arial", 20), command=book_ride, bg="white", fg="blue")
btn_book.place(x=700, y=630)


lbl_1=Label(root,text="Ride Boking App",font=("Arial Bold",40)).place(x=100,y=5)
lbl_2=Label(root,text="Chartered Ride",font=("Arial",15)).place(x=0,y=70)
lbl_pickuplocation=Label(root,text="Pickup Location",font=("Arial",15)).place(x=70,y=150)
lbl_destination=Label(root,text="Destination",font=("Arial",15)).place(x=70,y=180)

lbl_pickuplocation=Entry(root,width="40").place(x=250,y=155)
lbl_destination=Entry(root,width="40").place(x=250,y=185)


btn_home=Button(root,text="Home",font=("Arial",15),command=home).place(x=730,y=70)
btn_book=Button(root,text="Book",font=("Arial",20),command="").place(x=700,y=630)
btn_help=Button(root,text="Help",font=("Arial",20),command="").place(x=10,y=630)

entry_pickuplocation = Entry(root, width="40")
entry_pickuplocation.place(x=250, y=155)

entry_destination = Entry(root, width="40")
entry_destination.place(x=250, y=185)

# Date selection widgets
lbl_pickupdate = Label(root, text="Pickup Date", font=("Arial", 15))
lbl_pickupdate.place(x=70, y=220)

pickup_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
pickup_date.place(x=250, y=225)

lbl_returndate = Label(root, text="Return Date", font=("Arial", 15))
lbl_returndate.place(x=70, y=250)

return_date = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
return_date.place(x=250, y=255)


root.mainloop()