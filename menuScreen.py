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
    bg="LightSkyBlue1",
    fg="Red",
    font="Arial 30",
    border=1,
    borderwidth=2,
    relief="solid",
)
Heading.grid(row=0, column=1, columnspan=9, rowspan=1, padx=0, pady=20)

ButtonFrame = ttk.Frame(root, width=width)
ButtonFrame.grid(row=2, column=0, columnspan=9, rowspan=1, padx=0, pady=60)

Button(
    ButtonFrame,
    text="Seat Booking",
    bg="SpringGreen3",
    fg="Black",
    font="Arial 13 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    command=lambda: root.destroy(),
    width=20,
    height=2,
    activebackground="SpringGreen4",
    activeforeground="White",
).grid(row=0, column=1, columnspan=1, rowspan=1, padx=10, pady=20)
Button(
    ButtonFrame,
    text="Check Booked Seats",
    bg="SpringGreen3",
    fg="Black",
    font="Arial 13 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    command=lambda: root.destroy(),
    width=20,
    height=2,
    activeforeground="White",
    activebackground="SpringGreen4",
).grid(row=0, column=2, columnspan=1, rowspan=1, padx=10, pady=20)
Button(
    ButtonFrame,
    text="Add Bus Details",
    bg="SpringGreen3",
    fg="Black",
    font="Arial 13 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    command=errorwindow,
    width=20,
    height=2,
    activebackground="SpringGreen4",
    activeforeground="White",
).grid(row=0, column=3, columnspan=1, rowspan=1, padx=10, pady=20)

AdminLabel = Label(
    ButtonFrame,
    text="Admin Only",
    bg="LightSkyBlue1",
    fg="Red",
    font="Arial 10 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    highlightbackground="Red",
    highlightcolor="Red",
    highlightthickness=2,
    width=20,
    height=2,
)
AdminLabel.grid(row=1, column=3, columnspan=1, rowspan=1, padx=0, pady=10)


root.mainloop()
