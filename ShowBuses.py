from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("BUS Booking System")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))


ImageFrame = ttk.Frame(root, width=width)
ImageFrame.grid(row=0, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

ContentFrame = ttk.Frame(root, width=width)
ContentFrame.grid(row=1, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

BusImage = PhotoImage(file=".\\BusImage.png")
HeaderImage = Label(ImageFrame, image=BusImage)
HeaderImage.grid(
    row=0,
    column=0,
    columnspan=9,
    rowspan=1,
    padx=width // 2 - BusImage.width() // 2,
    pady=1,
)

Heading = Label(
    ContentFrame,
    text="Online Bus Booking System",
    bg="LightSkyBlue1",
    fg="Red",
    font="Arial 25",
    border=1,
    borderwidth=2,
    relief="solid",
    width=35,
)
Heading.grid(row=0, column=1, columnspan=9, rowspan=1, padx=0, pady=10)


SubHeading = Label(
    ContentFrame,
    text="Enter Journey Details",
    bg="lightgreen",
    fg="darkgreen",
    font="Arial 15",
    border=1,
    borderwidth=2,
    relief="solid",
    width=25,
)
SubHeading.grid(row=1, column=1, columnspan=9, rowspan=1, padx=0, pady=5)


###################################################################################

"""  Bus Details Frame  """


BusDetailsFrame = ttk.Frame(root, width=width)
BusDetailsFrame.grid(row=3, column=0, columnspan=9, rowspan=1, padx=0, pady=1)


def btnshowbus():

    details = ["Raipur", "Bhopal", "2020-03-15"]

    # busdetails = showbus(details)

    busdetails = [
        ("Kamla", "AC Sleeper", "23", "30", "500"),
        ("Rayeen", "AC 2x2", "2", "35", "1000"),
    ]

    Label(
        BusDetailsFrame, text="Select Bus", font="Arial 15 bold", foreground="green3"
    ).grid(row=0, column=0, padx=25, pady=(5, 2))
    Label(
        BusDetailsFrame, text="Operator", font="Arial 15 bold", foreground="green3"
    ).grid(row=0, column=1, padx=25, pady=(5, 2))
    Label(
        BusDetailsFrame, text="Bus Type", font="Arial 15 bold", foreground="green3"
    ).grid(row=0, column=2, padx=25, pady=(5, 2))
    Label(
        BusDetailsFrame,
        text="Available Seats",
        font="Arial 15 bold",
        foreground="green3",
    ).grid(row=0, column=3, padx=25, pady=(5, 2))
    Label(
        BusDetailsFrame, text="Capacity", font="Arial 15 bold", foreground="green3"
    ).grid(row=0, column=4, padx=25, pady=(5, 2))
    Label(BusDetailsFrame, text="Fare", font="Arial 15 bold", foreground="green3").grid(
        row=0, column=5, padx=25, pady=(5, 2)
    )

    ProceedBooking = Button(
        BusDetailsFrame,
        text=" Proceed to Book",
        font="Arial 15 bold",
        foreground="black",
        background="green",
        command=pass_details,
    )
    ProceedBooking.grid(row=0, column=6, rowspan=len(busdetails), padx=25)

    var = StringVar()

    for i in busdetails:
        rowno = busdetails.index(i) + 1
        Radiobutton(
            BusDetailsFrame,
            variable=var,
            value=i,
            bg="lightgreen",
            font="Arial 15 bold",
            foreground="green3",
        ).grid(row=rowno, column=0, padx=25, pady=(5, 2))
        for j in i:
            columnno = i.index(j) + 1

            Label(BusDetailsFrame, text=j, font="Arial").grid(
                row=rowno, column=columnno, padx=25, pady=(1, 1)
            )


""" Passenger Details Frame """

PassengerDetailsFrame = ttk.Frame(root, width=width)
PassengerDetailsFrame.grid(row=5, column=0, columnspan=9, rowspan=1, padx=0, pady=0)


def pass_details():
    # SubHeading = Label(
    #     root,
    #     text="Enter Journey Details",
    #     bg="lightgreen",
    #     fg="darkgreen",
    #     font="Arial 15",
    #     border=1,
    #     borderwidth=2,
    #     relief="solid",
    #     width=25,
    # )
    # SubHeading.grid(row=4, column=1, columnspan=9, rowspan=1, padx=0, pady=5)

    PassengerDetailsLabel = Label(
        PassengerDetailsFrame,
        text="Passenger Details",
        bg="lightgreen",
        fg="darkgreen",
        font="Arial 15",
        border=1,
        borderwidth=2,
        relief="solid",
        width=25,
    )
    PassengerDetailsLabel.grid(
        row=0, column=1, columnspan=10, rowspan=1, padx=0, pady=20
    )

    NameLabel = Label(PassengerDetailsFrame, text="Name", font="Arial 10")
    NameLabel.grid(row=1, column=0, padx=10, pady=(5, 2))
    NameEntry = Entry(PassengerDetailsFrame)
    NameEntry.grid(row=1, column=1, padx=10, pady=(5, 2))

    GenderLabel = Label(PassengerDetailsFrame, text="Gender", font="Arial 10")
    GenderLabel.grid(row=1, column=2, padx=10, pady=(5, 2))

    GenderButton = Menubutton(PassengerDetailsFrame, text="")
    GenderButton.grid(row=1, column=3, padx=10, pady=(5, 2))

    gender1 = IntVar()
    gender2 = IntVar()
    GenderButton.menu = Menu(GenderButton, tearoff=0)
    GenderButton["menu"] = GenderButton.menu
    GenderButton.menu.add_checkbutton(label="Male", variable=gender1)
    GenderButton.menu.add_checkbutton(label="Female", variable=gender2)

    SeatLabel = Label(
        PassengerDetailsFrame,
        text="No of Seats",
        font="Arial 10",
    )
    SeatLabel.grid(row=1, column=4, padx=10, pady=(5, 2))
    SeatEntry = Entry(PassengerDetailsFrame)
    SeatEntry.grid(row=1, column=5, padx=10, pady=(5, 2))

    MobileLabel = Label(
        PassengerDetailsFrame,
        text="Mobile No",
        font="Arial 10",
    )
    MobileLabel.grid(row=1, column=6, padx=10, pady=(5, 2))
    MobileEntry = Entry(PassengerDetailsFrame)
    MobileEntry.grid(row=1, column=7, padx=10, pady=(5, 2))

    AgeLabel = Label(PassengerDetailsFrame, text="Age", font="Arial 10")
    AgeLabel.grid(row=1, column=8, padx=10, pady=(5, 2))
    AgeEntry = Entry(PassengerDetailsFrame)
    AgeEntry.grid(row=1, column=9, padx=10, pady=(5, 2))


def btnbook():

    message = messagebox.askyesno(
        "askyesno", "Please confirm if you want to Book the ticket?"
    )

    if message == True:
        # bookticket(info)
        messagebox.showinfo("Ticket Booking", "Ticket Booked Successfully")
    else:
        messagebox.showinfo("Ticket Booking", "Ticket Booking Failed")


###################################################################################

""" Journey Details Frame """

QueryFrame = ttk.Frame(root, width=width)
QueryFrame.grid(row=2, column=0, columnspan=9, rowspan=1, padx=0, pady=1)

tocity = StringVar()
fromcity = StringVar()
journeydate = StringVar()

ToCityLabel = Label(QueryFrame, text="To", font="Arial 15")
ToCityLabel.grid(row=0, column=0, padx=(20, 5), pady=1)

ToCity = Entry(
    QueryFrame,
    textvariable=tocity,
    width=20,
)
ToCity.grid(row=0, column=1, padx=1, pady=1)

FromCityLabel = Label(QueryFrame, text="From", font="Arial 15")
FromCityLabel.grid(row=0, column=2, padx=(20, 1), pady=1)

FromCity = Entry(
    QueryFrame,
    textvariable=fromcity,
    width=20,
)
FromCity.grid(row=0, column=3, padx=1, pady=1)

JourneyDateLabel = Label(QueryFrame, text="Date", font="Arial 15")
JourneyDateLabel.grid(row=0, column=4, padx=(20, 1), pady=1)

JourneyDate = Entry(
    QueryFrame,
    textvariable=journeydate,
    width=20,
)
JourneyDate.grid(row=0, column=5, padx=1, pady=1)


ShowBusesbtn = Button(
    QueryFrame,
    text="Show Buses",
    bg="SpringGreen3",
    fg="Black",
    font="Arial 13 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    command=btnshowbus,
    width=15,
    height=2,
    activebackground="SpringGreen4",
    activeforeground="White",
)
ShowBusesbtn.grid(row=0, column=6, columnspan=1, rowspan=1, padx=(30, 10), pady=20)

HomeButtonImage = PhotoImage(file=".\\home.png")

Homebtn = Button(
    QueryFrame,
    image=HomeButtonImage,
    # bg="SpringGreen3",
    # fg="Black",
    # font="Arial 13 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    command=lambda: root.destroy(),
    # width=20,
    height=48,
    # activeforeground="White",
    # activebackground="SpringGreen4",
)
Homebtn.grid(row=0, column=7, columnspan=1, rowspan=1, padx=(20, 20), pady=20)


###################################################################################


root.mainloop()
