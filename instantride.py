from tkinter import *
root=Tk()
root.title("Ride booking app")
root.geometry("800x700")


def home():
    root.destroy()
    import home

lbl=Label(root,text="Ride Booking App",font=("Arial Bold",40)).place(x=100,y=50)
lbl_1=Label(root,text="Instant Ride",font=("Arial",10)).place(x=10,y=150)

vehicle_label=Label(root,text="Select your vehicle type",font=("Arial",20)).place(x=100,y=220)


pickup_label=Label(root,text="Pickup location",font=("Arial",20)).place(x=100,y=360)
destination_label=Label(root,text="Destination",font=("Arial",20)).place(x=100,y=415)

pickup=Entry(root,width=60).place(x=300,y=365,height=35)
destination=Entry(root,width=60).place(x=300,y=420,height=35)

help_button=Button(root,text="Help",command="").place(x=5,y=650)
book_button=Button(root,text="Book",command="").place(x=760,y=650)
home_button=Button(root,text="Home",command=home).place(x=760,y=150)

root.mainloop()