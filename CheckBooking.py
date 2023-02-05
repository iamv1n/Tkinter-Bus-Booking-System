from tkinter import *
from tkinter import ttk

root = Tk()
root.title("BUS Booking System")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))


def errorwindow():
    errorbox = Toplevel(root)
    errorbox.title("Error")
    errorbox.geometry("300x100")
    errorbox.resizable(0, 0)
    errorbox.configure(bg="red")
    errorbox.iconbitmap("error.ico")
    errorbox.overrideredirect(1)
    errorbox.after(2000, lambda: errorbox.destroy())


ImageFrame = ttk.Frame(root, width=width)
ImageFrame.grid(row=0, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

HeadingFrame = ttk.Frame(root, width=width)
HeadingFrame.grid(row=1, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

BusImage = PhotoImage(file=".\\BusImage.png")
HeaderImage = Label(ImageFrame, image=BusImage)
HeaderImage.grid(
    row=0,
    column=0,
    columnspan=9,
    rowspan=1,
    padx=width // 2 - BusImage.width() // 2,
    pady=10,
)

Heading = Label(
    HeadingFrame,
    text="Online Bus Booking System",
    bg="LightSkyBlue1",
    fg="Red",
    font="Arial 30",
    border=1,
    borderwidth=2,
    relief="solid",
)
Heading.grid(row=0, column=0, columnspan=9, rowspan=1, padx=0, pady=(10, 5))

SubHeading = Label(
    HeadingFrame,
    text="Online Bus Booking System",
    bg="green2",
    fg="green4",
    font="Arial 20",
    border=1,
    borderwidth=2,
    relief="solid",
)
SubHeading.grid(row=1, column=0, columnspan=9, rowspan=1, padx=0, pady=(5, 5))

##########################################################################################

""" Check Booking Frame """

BookingFrame = ttk.Frame(root, width=width)
BookingFrame.grid(row=3, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

mobilenumber = StringVar()

MobileNumberLabel = Label(
    BookingFrame, text="Enter your Mobile Number:", font="Arial 12"
)
MobileNumberLabel.grid(row=0, column=0, columnspan=1, rowspan=1, padx=0, pady=0)


MobileNumberEntry = Entry(BookingFrame, textvariable=mobilenumber, width=20)
MobileNumberEntry.grid(row=0, column=1, columnspan=1, rowspan=1, padx=0, pady=0)
CheckBookingbtn = Button(
    BookingFrame,
    text="Check Booking",
    # bg="SpringGreen3",
    # fg="Black",
    font="Arial 12",
    border=1,
    borderwidth=2,
    relief="solid",
    command=lambda: root.destroy(),
    # width=15,
    # height=2,
    activebackground="SpringGreen4",
    activeforeground="White",
)
CheckBookingbtn.grid(row=0, column=3, columnspan=1, rowspan=1, padx=(30, 10), pady=20)


BookingDetailsFrame = Frame(
    root,
    width=width,
    border=1,
    borderwidth=2,
    relief="solid",
)
BookingDetailsFrame.grid(
    row=4, column=0, columnspan=9, rowspan=1, padx=(0, 0), pady=(10, 5), ipadx=50
)

seatnumber = "0"
passengername = "Vineet Likhitkar"
age = "20"
gender = "Male"
mobilenumber = "9462877456"
traveldate = "20/10/2020"
destinationpoint = "Pune"
boardingpoint = "Mumbai"
busnumber = "MH 12 1234"
busrefnumber = "556477"
busname = "VRL Travels"
busfare = "500"
busdeparturetime = "10:00 AM"
busarrivaltime = "12:00 PM"


PassengerNameLabel = Label(
    BookingDetailsFrame, text="Passenger: " + passengername, font="Arial 12"
)
PassengerNameLabel.grid(
    row=0, column=0, columnspan=1, rowspan=1, padx=(0, 30), pady=0, sticky=W
)

PassengerGenderLabel = Label(
    BookingDetailsFrame, text="Gender: " + gender, font="Arial 12"
)
PassengerGenderLabel.grid(
    row=0, column=1, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W
)

PassengerPhoneLabel = Label(
    BookingDetailsFrame, text="Phone: " + mobilenumber, font="Arial 12"
)
PassengerPhoneLabel.grid(
    row=0, column=2, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W
)


PassengerBookingrefLabel = Label(
    BookingDetailsFrame, text="Booking Ref: " + busrefnumber, font="Arial 12"
)
PassengerBookingrefLabel.grid(
    row=3, column=0, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W
)

PassengerBusNumberLabel = Label(
    BookingDetailsFrame, text="Bus Number: " + busnumber, font="Arial 12"
)
PassengerBusNumberLabel.grid(
    row=4, column=0, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W
)

PassengerBusNameLabel = Label(
    BookingDetailsFrame, text="Bus Name: " + busname, font="Arial 12"
)
PassengerBusNameLabel.grid(
    row=8, column=0, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W
)


PassengerAgeLabel = Label(BookingDetailsFrame, text="Age: ", font="Arial 12")
PassengerAgeLabel.grid(
    row=1, column=0, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W
)

PassengerSeat = Label(BookingDetailsFrame, text="Seat: " + seatnumber, font="Arial 12")
PassengerSeat.grid(row=2, column=0, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W)

PassengerFare = Label(BookingDetailsFrame, text="Fare: " + busfare, font="Arial 12")
PassengerFare.grid(row=1, column=1, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W)

TravelDateLabel = Label(
    BookingDetailsFrame, text="Travel Date: " + traveldate, font="Arial 12"
)
TravelDateLabel.grid(row=5, column=0, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W)

PassengerDestPointLabel = Label(
    BookingDetailsFrame, text="Destination: " + destinationpoint, font="Arial 12"
)
PassengerDestPointLabel.grid(
    row=6, column=0, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W
)

PassengerBoardingPoint = Label(
    BookingDetailsFrame, text="Boarding Point: " + boardingpoint, font="Arial 12"
)
PassengerBoardingPoint.grid(
    row=4, column=1, columnspan=1, rowspan=1, padx=0, pady=0, sticky=W
)

root.mainloop()
