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
    pady=10,
)

Heading = Label(
    ContentFrame,
    text="Online Bus Booking System",
    font="Arial 30",
    bg="LightSkyBlue1",
    fg="Red",
    border=1,
    borderwidth=2,
    relief="solid",
    width=25,
)
Heading.grid(row=0, column=1, columnspan=9, rowspan=1, padx=0, pady=20)

SubHeading = Label(
    ContentFrame,
    text="Add New Bus Details",
    # bg="green2",
    fg="green",
    font="Arial 25",
)
SubHeading.grid(row=1, column=1, columnspan=9, rowspan=1, padx=0, pady=20)


################################################################################

# Add New Bus Details

NewBusDetailFrame = ttk.Frame(root, width=width)
NewBusDetailFrame.grid(row=2, column=0, columnspan=9, rowspan=1, padx=0, pady=60)

bus_id = IntVar()
bus_capacity = IntVar()
bus_type = StringVar()
bus_fare = IntVar()
bus_operator_id = IntVar()
bus_route_id = IntVar()

newbusdetails = [bus_id, bus_capacity, bus_fare, bus_operator_id, bus_route_id]

BusIDLabel = Label(
    NewBusDetailFrame,
    text="Bus ID",
    font="Arial 12 bold",
)
BusIDLabel.grid(row=0, column=0, columnspan=1, rowspan=1, padx=10, pady=10)
BusIDEntry = Entry(
    NewBusDetailFrame,
    font="Arial 12 bold",
    width=10,
    textvariable=bus_id,
)
BusIDEntry.grid(row=0, column=1, columnspan=1, rowspan=1, padx=10, pady=10)

BusCapacityLabel = Label(
    NewBusDetailFrame,
    text="Bus Capacity",
    font="Arial 12 bold",
)
BusCapacityLabel.grid(row=0, column=4, columnspan=1, rowspan=1, padx=10, pady=10)
BusCapacityEntry = Entry(
    NewBusDetailFrame,
    font="Arial 12 bold",
    width=10,
    textvariable=bus_capacity,
)
BusCapacityEntry.grid(row=0, column=5, columnspan=1, rowspan=1, padx=10, pady=10)

BusFareLabel = Label(
    NewBusDetailFrame,
    text="Bus Fare",
    font="Arial 12 bold",
)
BusFareLabel.grid(row=0, column=6, columnspan=1, rowspan=1, padx=10, pady=10)
BusFareEntry = Entry(
    NewBusDetailFrame,
    font="Arial 12 bold",
    width=10,
    textvariable=bus_fare,
)
BusFareEntry.grid(row=0, column=7, columnspan=1, rowspan=1, padx=10, pady=10)

BusOperatorIDLabel = Label(
    NewBusDetailFrame,
    text="Bus Operator ID",
    font="Arial 12 bold",
)
BusOperatorIDLabel.grid(row=0, column=8, columnspan=1, rowspan=1, padx=10, pady=10)
BusOperatorIDEntry = Entry(
    NewBusDetailFrame,
    font="Arial 12 bold",
    width=10,
    textvariable=bus_operator_id,
)
BusOperatorIDEntry.grid(row=0, column=9, columnspan=1, rowspan=1, padx=10, pady=10)

BusRouteIDLabel = Label(
    NewBusDetailFrame,
    text="Bus Route ID",
    font="Arial 12 bold",
)
BusRouteIDLabel.grid(row=0, column=10, columnspan=1, rowspan=1, padx=10, pady=10)
BusRouteIDEntry = Entry(
    NewBusDetailFrame,
    font="Arial 12 bold",
    width=10,
    textvariable=bus_route_id,
)
BusRouteIDEntry.grid(row=0, column=11, columnspan=1, rowspan=1, padx=10, pady=10)


ButtonFrame = ttk.Frame(root, width=width)
ButtonFrame.grid(row=3, column=0, columnspan=9, rowspan=1, padx=0, pady=0)


AddBusButton = Button(
    ButtonFrame,
    text="Add Bus",
    font="Arial 12 bold",
    bg="green2",
    fg="Red",
    border=1,
    borderwidth=2,
    relief="solid",
    command=addnewbus,
    width=10,
)
AddBusButton.grid(row=1, column=0, columnspan=1, rowspan=1, padx=10, pady=30)

EditBusButton = Button(
    ButtonFrame,
    text="Edit Bus",
    font="Arial 12 bold",
    bg="green2",
    fg="Red",
    border=1,
    borderwidth=2,
    relief="solid",
    command=editnewbus,
    width=10,
)
EditBusButton.grid(row=1, column=1, columnspan=1, rowspan=1, padx=10, pady=30)

HomeButton = Button(
    ButtonFrame,
    text="Home",
    font="Arial 12 bold",
    bg="green2",
    fg="Red",
    border=1,
    borderwidth=2,
    relief="solid",
    command=gohome,
    width=10,
)
HomeButton.grid(row=1, column=2, columnspan=1, rowspan=1, padx=10, pady=30)


root.mainloop()
