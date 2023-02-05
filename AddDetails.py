from tkinter import *
from tkinter import ttk

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
    pady=10,
)

Heading = Label(
    ContentFrame,
    text="Online Bus Booking System",
    bg="LightSkyBlue1",
    fg="Red",
    font="Arial 30",
    border=1,
    borderwidth=2,
    relief="solid",
)
Heading.grid(row=0, column=1, columnspan=9, rowspan=1, padx=0, pady=20)

SubHeading = Label(
    ContentFrame,
    text="Add New Details to Database",
    # bg="LightSkyBlue1",
    fg="green",
    font="Arial 25",
)
SubHeading.grid(row=1, column=1, columnspan=9, rowspan=1, padx=0, pady=20)

ButtonFrame = ttk.Frame(root, width=width)
ButtonFrame.grid(row=2, column=0, columnspan=9, rowspan=1, padx=0, pady=60)

NewOperator = Button(
    ButtonFrame,
    text="New Operartor",
    bg="SpringGreen3",
    fg="Black",
    font="Arial 15 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    command=lambda: root.destroy(),
    width=20,
    height=2,
    activebackground="SpringGreen4",
    activeforeground="White",
)
NewOperator.grid(row=0, column=1, columnspan=1, rowspan=1, padx=10, pady=20)
NewBusbtn = Button(
    ButtonFrame,
    text="New Bus",
    bg="SpringGreen3",
    fg="Black",
    font="Arial 15 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    command=lambda: root.destroy(),
    width=20,
    height=2,
    activeforeground="White",
    activebackground="SpringGreen4",
)
NewBusbtn.grid(row=0, column=2, columnspan=1, rowspan=1, padx=10, pady=20)
NewRoutebtn = Button(
    ButtonFrame,
    text="New Route",
    bg="SpringGreen3",
    fg="Black",
    font="Arial 15 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    # command=errorwindow,
    width=20,
    height=2,
    activebackground="SpringGreen4",
    activeforeground="White",
)
NewRoutebtn.grid(row=0, column=3, columnspan=1, rowspan=1, padx=10, pady=20)

NewRunbtn = Button(
    ButtonFrame,
    text="New Run",
    bg="SpringGreen3",
    fg="Black",
    font="Arial 15 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    # command=errorwindow,
    width=20,
    height=2,
    activebackground="SpringGreen4",
    activeforeground="White",
)
NewRunbtn.grid(row=0, column=4, columnspan=1, rowspan=1, padx=10, pady=20)


root.mainloop()
