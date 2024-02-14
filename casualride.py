from tkinter import *
root=Tk()
root.title("Ride Booking App")
root.geometry("800x700")

def home():
    root.destroy()
    import home



lbl_1=Label(root,text="Ride Boking App",font=("Arial Bold",40)).place(x=100,y=5)
lbl_2=Label(root,text="Chartered Ride",font=("Arial",15)).place(x=0,y=70)
lbl_pickuplocation=Label(root,text="Pickup Location",font=("Arial",15)).place(x=70,y=150)
lbl_destination=Label(root,text="Destination",font=("Arial",15)).place(x=70,y=180)

lbl_pickuplocation=Entry(root,width="40").place(x=250,y=155)
lbl_destination=Entry(root,width="40").place(x=250,y=185)


btn_home=Button(root,text="Home",font=("Arial",15),command=home).place(x=730,y=70)
btn_book=Button(root,text="Book",font=("Arial",20),command="").place(x=700,y=630)
btn_help=Button(root,text="Help",font=("Arial",20),command="").place(x=10,y=630)

root.mainloop()