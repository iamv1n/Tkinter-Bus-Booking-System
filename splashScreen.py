from tkinter import *
from tkinter import ttk

root = Tk()
Style = ttk.Style()
root.title("BUS Booking System")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))


ImageFrame = ttk.Frame(
    root,
    width=width,
)
ImageFrame.grid(
    row=0,
    column=0,
    columnspan=9,
    rowspan=1,
    padx=0,
    pady=0,
)

ContentFrame = ttk.Frame(root, width=width)
ContentFrame.grid(row=1, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

BusImage = PhotoImage(file=".\\BusImage.png")
HeaderImage = Label(ImageFrame, image=BusImage, width=width)
HeaderImage.grid(
    row=0,
    column=0,
    columnspan=9,
    rowspan=1,
    #     padx=width // 2 - BusImage.width() // 2,
    ipady="40",
)

Heading = Label(
    ContentFrame,
    text="Online Bus Booking System",
    bg="LightSkyBlue1",
    fg="Red",
    font="Arial 30 bold",
    border=1,
    borderwidth=2,
    relief="solid",
    width=25,
)
Heading.grid(row=0, column=1, columnspan=9, rowspan=1, padx=0, ipady=20)

StudentInfoFrame = ttk.Frame(root, width=25)
StudentInfoFrame.grid(row=2, column=0, columnspan=9, rowspan=1, padx=0, pady=40)
# StudentInfoFrame.config()


StudentName = Label(
    StudentInfoFrame,
    text="Name : Vineet Anil Likhitkar",
    #     bg="LightSkyBlue1",
    fg="Blue",
    font="Arial 15 bold",
    width=50,
    # anchor="w",
)
StudentEnrollment = Label(
    StudentInfoFrame,
    text="Enrollment : 211B402",
    #     bg="LightSkyBlue1",
    fg="Blue",
    font="Arial 15 bold",
    width=50,
    # anchor="w",
)
StudentMobile = Label(
    StudentInfoFrame,
    text="Mobile : 9399946737",
    #     bg="LightSkyBlue1",
    fg="Blue",
    font="Arial 15 bold",
    width=50,
    # anchor="w",
)

StudentName.grid(row=0, column=0, columnspan=9, rowspan=1, padx=0, pady=10)
StudentEnrollment.grid(row=1, column=0, columnspan=9, rowspan=1, padx=0, pady=10)
StudentMobile.grid(row=2, column=0, columnspan=9, rowspan=1, padx=0, pady=10)


ProfName = Label(
    root,
    text="Submitted to : Dr. Mahesh Kumar",
    bg="LightSkyBlue1",
    fg="Red",
    font="Arial 25",
    width=32,
    wraplength=width,
)
ProfName.grid(row=10, column=0, columnspan=9, pady=10)

Footer = Label(root, text="Project Based Learning", fg="Red", font="Arial 15")
Footer.grid(row=11, column=0, columnspan=9, pady=0)


root.mainloop()
