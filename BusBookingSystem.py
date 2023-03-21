from tkinter import *
from tkinter import ttk, messagebox

from datetime import datetime

import sqlite3

now = datetime.now()

connection = sqlite3.connect("busdatabase.db")
cursor = connection.cursor()


class BBS:

    ## Root Window ##
    def rootframe(self):
        root = Tk()
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
        StudentEnrollment.grid(
            row=1, column=0, columnspan=9, rowspan=1, padx=0, pady=10
        )
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

        def menu(e=1):
            root.destroy()
            self.menuframe()

        root.bind("<KeyPress>", menu)
        root.mainloop()

    ## Menu Window ##
    def menuframe(self):
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

        def callcheckbookingframe(e=1):
            root.destroy()
            self.checkbookingframe()

        def callseatbookingframe(e=1):
            root.destroy()
            self.seatbookingframe()

        def calladminframe(e=1):
            root.destroy()
            self.adminframe()

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
            command=callseatbookingframe,
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
            command=callcheckbookingframe,
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
            command=calladminframe,
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

    def checkbookingframe(self):
        root = Tk()
        root.title("BUS Booking System")

        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))

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

        mobilenumber = IntVar()

        MobileNumberLabel = Label(
            BookingFrame, text="Enter your Mobile Number:", font="Arial 12"
        )
        MobileNumberLabel.grid(row=0, column=0, columnspan=1, rowspan=1, padx=0, pady=0)

        MobileNumberEntry = Entry(BookingFrame, textvariable=mobilenumber, width=20)
        MobileNumberEntry.grid(row=0, column=1, columnspan=1, rowspan=1, padx=0, pady=0)

        Button()

        def checkbooking():
            mobilenumber = MobileNumberEntry.get()
            if mobilenumber == "":
                messagebox.showerror("Error", "Please Enter your Mobile Number")
            elif len(mobilenumber) != 10:
                messagebox.showerror("Error", "Please Enter a Valid Mobile Number")
            else:
                print("Phone okay")
                print(mobilenumber)

                try:
                    cursor.execute(
                        """select passengerinfo.name,seats,age,bookingid,run.date,
                        source,gender,operatorinfo.name,fare,destination
                        from bookinginfo,passengerinfo,run,businfo,routeinfo,operatorinfo
                        where bookinginfo.bookingid=passengerinfo.passengerid
                        and bookinginfo.buid=businfo.busid
                        and businfo.roid=routeinfo.routeid
                        and businfo.opid=operatorinfo.operatorid
                        and bookinginfo.buid=run.bus_id
                        and passengerinfo.phone=?""",
                        (mobilenumber,),
                    )
                    data = cursor.fetchall()
                    print(data)
                    if data == []:
                        messagebox.showerror("Error", "No Booking Found")

                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", "Please Enter a Valid Mobile Number")

                ticket = data[0]

                dettest = [
                    (
                        ticket[0],
                        str(ticket[1]),
                        str(ticket[2]),
                        str(ticket[3]),
                        ticket[4],
                        ticket[5],
                        ticket[6],
                        ticket[7],
                        str(ticket[8]),
                        ticket[9],
                    )
                ]
                showbooking(dettest, mobilenumber)
                # try:
                #     cursor.execute(
                #         "select * from booking where mobilenumber = ?", (mobilenumber,)
                #     )
                #     bookings = cursor.fetchall()
                #     print(bookings)
                #     if len(bookings) == 0:
                #         messagebox.showerror("Error", "No Booking Found")
                #     else:
                #         messagebox.showinfo("Success", "Booking Found")
                #         showbooking(bookings)
                # except Exception as e:
                #     messagebox.showerror("Error", f"Error due to: {str(e)}")

        def showbooking(b, mob):

            ticket = b[0]

            BookingDetailsFrame = Frame(
                root,
                width=width,
                border=1,
                borderwidth=2,
                relief="solid",
            )
            BookingDetailsFrame.grid(
                row=4,
                column=0,
                columnspan=9,
                rowspan=1,
                padx=(0, 0),
                pady=(10, 5),
                ipadx=50,
            )

            passengername = ticket[0]
            seatnumber = str(ticket[1])
            age = str(ticket[2])
            busrefnumber = str(ticket[3])
            traveldate = ticket[4]
            boardingpoint = ticket[5]
            gender = ticket[6]
            mobilenumber = mob
            busnumber = "MH 12 AB 1234"
            busname = ticket[7]
            busfare = str(int(ticket[8]) * int(ticket[1]))
            destinationpoint = ticket[9]

            # Name
            PassengerNameLabel = Label(
                BookingDetailsFrame,
                text="Passenger: " + passengername,
                font="Arial 12",
            )
            PassengerNameLabel.grid(
                row=0,
                column=0,
                columnspan=1,
                rowspan=1,
                padx=(0, 30),
                pady=(3, 3),
                sticky=W,
            )

            ##### Seat ##############
            PassengerSeat = Label(
                BookingDetailsFrame, text="Seat: " + seatnumber, font="Arial 12"
            )
            PassengerSeat.grid(
                row=1,
                column=0,
                columnspan=1,
                rowspan=1,
                padx=0,
                pady=(3, 3),
                sticky=W,
            )

            ##### Age ##############
            PassengerAgeLabel = Label(
                BookingDetailsFrame, text="Age: " + str(age), font="Arial 12"
            )
            PassengerAgeLabel.grid(
                row=2,
                column=0,
                columnspan=1,
                rowspan=1,
                padx=0,
                pady=(3, 3),
                sticky=W,
            )

            ##### Booking Ref ##############
            PassengerBookingrefLabel = Label(
                BookingDetailsFrame,
                text="Booking Ref: " + busrefnumber,
                font="Arial 12",
            )
            PassengerBookingrefLabel.grid(
                row=3,
                column=0,
                columnspan=1,
                rowspan=1,
                padx=0,
                pady=(3, 3),
                sticky=W,
            )

            ##### Travel Date ##############
            TravelDateLabel = Label(
                BookingDetailsFrame,
                text="Travel Date: " + traveldate,
                font="Arial 12",
            )
            TravelDateLabel.grid(
                row=4,
                column=0,
                columnspan=1,
                rowspan=1,
                padx=0,
                pady=(3, 3),
                sticky=W,
            )

            ##### Boarding Point ##############
            PassengerBoardingPoint = Label(
                BookingDetailsFrame,
                text="Boarding Point: " + boardingpoint,
                font="Arial 12",
            )
            PassengerBoardingPoint.grid(
                row=5,
                column=0,
                columnspan=1,
                rowspan=1,
                padx=0,
                pady=(3, 3),
                sticky=W,
            )

            ##### Gender ##############
            PassengerGenderLabel = Label(
                BookingDetailsFrame, text="Gender: " + gender, font="Arial 12"
            )
            PassengerGenderLabel.grid(
                row=0,
                column=1,
                columnspan=1,
                rowspan=1,
                padx=(10, 2),
                pady=(3, 3),
                sticky=W,
            )

            ##### Mobile Number ##############
            PassengerPhoneLabel = Label(
                BookingDetailsFrame, text="Phone: " + mobilenumber, font="Arial 12"
            )
            PassengerPhoneLabel.grid(
                row=1,
                column=1,
                columnspan=1,
                rowspan=1,
                padx=(10, 2),
                pady=(3, 3),
                sticky=W,
            )

            PassengerBusNumberLabel = Label(
                BookingDetailsFrame,
                text="Bus Number: " + busnumber,
                font="Arial 12",
            )
            PassengerBusNumberLabel.grid(
                row=2,
                column=1,
                columnspan=1,
                rowspan=1,
                padx=(10, 2),
                pady=(3, 3),
                sticky=W,
            )

            PassengerBusNameLabel = Label(
                BookingDetailsFrame, text="Bus Name: " + busname, font="Arial 12"
            )
            PassengerBusNameLabel.grid(
                row=3,
                column=1,
                columnspan=1,
                rowspan=1,
                padx=(10, 2),
                pady=(3, 3),
                sticky=W,
            )

            PassengerFare = Label(
                BookingDetailsFrame, text="Fare: " + busfare, font="Arial 12"
            )
            PassengerFare.grid(
                row=4,
                column=1,
                columnspan=1,
                rowspan=1,
                padx=(10, 2),
                pady=(3, 3),
                sticky=W,
            )

            PassengerDestPointLabel = Label(
                BookingDetailsFrame,
                text="Destination: " + destinationpoint,
                font="Arial 12",
            )
            PassengerDestPointLabel.grid(
                row=5,
                column=1,
                columnspan=1,
                rowspan=1,
                padx=(10, 2),
                pady=(3, 3),
                sticky=W,
            )

        CheckBookingbtn = Button(
            BookingFrame,
            text="Check Booking",
            # bg="SpringGreen3",
            # fg="Black",
            font="Arial 12",
            border=1,
            borderwidth=2,
            relief="solid",
            command=checkbooking,
            # width=15,
            # height=2,
            activebackground="SpringGreen4",
            activeforeground="White",
        )
        CheckBookingbtn.grid(
            row=0, column=3, columnspan=1, rowspan=1, padx=(30, 10), pady=20
        )

        root.mainloop()

    def seatbookingframe(self):
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

        # Finds Buses in Db
        def findbuses(details):
            print(details)

            try:
                cursor.execute(
                    "select name, bustype,seat_avail,capacity,fare,busid from businfo,run,routeinfo,operatorinfo where source=? and destination=? and date=? and routeid=roid and businfo.busid=run.bus_id and businfo.opid = operatorinfo.operatorid",
                    (
                        details[0],
                        details[1],
                        details[2],
                    ),
                )
                print()
                res = cursor.fetchall()
                # connection.commit()
                if res == 0:
                    messagebox.showerror("Error", "No buses found")
                # messagebox.showinfo(
                #     "Success", "Bus Details Added Successfully", parent=root
                # )
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=root)

            return res

        # Gets Bus Details from screen
        def getbusdetails():
            source = fromcity.get()
            destination = tocity.get()
            date = journeydate.get()
            return [source, destination, date]

        selectedbus = StringVar()
        selectedbus.set("0")

        # passes Selected Bus Details to Passenger Entry Frame
        def pass_selbus():
            bus = selectedbus.get()
            print(bus)
            passenger_details(bus)

            return bus

        # Displays All the Avaiolable Buses in Frame
        def btnshowbus():

            details = getbusdetails()
            busdetails = findbuses(details)

            if busdetails == []:
                messagebox.showerror("Error", "No buses found")
                return

            # busdetails = [
            #     ("Kamla", "AC Sleeper", "23", "30", "500"),
            #     ("Rayeen", "AC 2x2", "2", "35", "1000"),
            # ]

            Label(
                BusDetailsFrame,
                text="Select Bus",
                font="Arial 15 bold",
                foreground="green3",
            ).grid(row=0, column=0, padx=25, pady=(5, 2))
            Label(
                BusDetailsFrame,
                text="Operator",
                font="Arial 15 bold",
                foreground="green3",
            ).grid(row=0, column=1, padx=25, pady=(5, 2))
            Label(
                BusDetailsFrame,
                text="Bus Type",
                font="Arial 15 bold",
                foreground="green3",
            ).grid(row=0, column=2, padx=25, pady=(5, 2))
            Label(
                BusDetailsFrame,
                text="Available Seats",
                font="Arial 15 bold",
                foreground="green3",
            ).grid(row=0, column=3, padx=25, pady=(5, 2))
            Label(
                BusDetailsFrame,
                text="Capacity",
                font="Arial 15 bold",
                foreground="green3",
            ).grid(row=0, column=4, padx=25, pady=(5, 2))
            Label(
                BusDetailsFrame, text="Fare", font="Arial 15 bold", foreground="green3"
            ).grid(row=0, column=5, padx=25, pady=(5, 2))

            ProceedBooking = Button(
                BusDetailsFrame,
                text=" Proceed to Book",
                font="Arial 15 bold",
                foreground="black",
                background="green",
                command=pass_selbus,
            )
            ProceedBooking.grid(row=0, column=6, rowspan=1, columnspan=2, padx=25)

            for i in busdetails:
                rowno = busdetails.index(i) + 1
                Radiobutton(
                    BusDetailsFrame,
                    variable=selectedbus,
                    value=rowno - 1,
                    font="Arial 15 bold",
                    foreground="green3",
                ).grid(row=rowno, column=0, padx=25, pady=(5, 2))
                for j in range(len(i) - 1):
                    columnno = j + 1

                    Label(BusDetailsFrame, text=i[j], font="Arial").grid(
                        row=rowno, column=columnno, padx=25, pady=(1, 1)
                    )

        """ Passenger Details Frame """

        PassengerDetailsFrame = ttk.Frame(root, width=width)
        PassengerDetailsFrame.grid(
            row=5, column=0, columnspan=9, rowspan=1, padx=0, pady=0
        )

        passName = StringVar()
        passAge = StringVar()
        passGender = StringVar()
        passSeats = StringVar()
        passMobile = StringVar()

        def btnbook(passdet):
            message = messagebox.askyesno(
                "askyesno", "Please confirm if you want to Book the ticket?"
            )

            if message is True:
                print("Yes Book Ticket")
                # bookticket(info)
                details = getbusdetails()
                # if passdet[3] >  details[3]:
                #     messagebox.ERROR("Error","Seat not available")
                #     return
                # if(passdet[])
                try:
                    cursor.execute(
                        "INSERT INTO passengerinfo(name,phone,gender,age) VALUES (?,?,?,?)",
                        (
                            passdet[0],
                            passdet[4],
                            passdet[2],
                            passdet[1],
                        ),
                    )
                    res = ""
                    connection.commit()
                    print("Passenger details inserted")

                    bussel = int(selectedbus.get())
                    busdetails = findbuses(details)
                    bus = busdetails[bussel][5]

                    date = now.strftime("%d/%m/%Y")

                    print("date", date)

                    print("Bus ID", bus)
                    cursor.execute(
                        "Insert into bookinginfo(buid,date,seats) values(?,?,?)",
                        (bus, date, passdet[3]),
                    )

                    connection.commit()

                    # seat_av = cursor.fetchall()

                    # print(seat_av, "Seat avail")
                    # print(passdet[3])

                    # new_seat = int(seat_av[0][0]) - passdet[3]

                    # cursor.execute(
                    #     "Update run set seat_avail = ? where bus_id=?",
                    #     (new_seat, bus),
                    # )
                    # connection.commit()

                    # messagebox.showinfo(
                    #     "Success", "Passenger Details Added Successfully", parent=root
                    # )
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", " Please try again")

                messagebox.showinfo("Ticket Booking", "Ticket Booked Successfully")
                root.destroy()
                global pho
                pho = passdet[4]
                self.ticketconfirmationframe()

            else:
                messagebox.showinfo("Ticket Booking", "Ticket Booking Failed")

        def passdet():

            if len(passMobile.get()) != 10:
                messagebox.ERROR("Error", "Enter correct phone number")
                return
            passdet = [
                passName.get(),
                passAge.get(),
                passGender.get(),
                passSeats.get(),
                passMobile.get(),
            ]

            for i in passdet:
                if i == "":
                    messagebox.showerror("Error", "Please fill all the details")
                    return
                else:
                    btnbook(passdet)
                    return

        def passenger_details(bus):

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
            NameEntry = Entry(PassengerDetailsFrame, textvariable=passName)
            NameEntry.grid(row=1, column=1, padx=10, pady=(5, 2))

            GenderLabel = Label(PassengerDetailsFrame, text="Gender", font="Arial 10")
            GenderLabel.grid(row=1, column=2, padx=10, pady=(5, 2))

            GenderOptions = [
                "Male",
                "Female",
                "Other",
            ]
            GenderOptionBox = OptionMenu(
                PassengerDetailsFrame,
                passGender,
                *GenderOptions,
            )
            GenderOptionBox.grid(row=1, column=3, padx=10, pady=(5, 2))

            SeatLabel = Label(
                PassengerDetailsFrame,
                text="No of Seats",
                font="Arial 10",
            )
            SeatLabel.grid(row=1, column=4, padx=10, pady=(5, 2))
            SeatEntry = Entry(PassengerDetailsFrame, textvariable=passSeats)
            SeatEntry.grid(row=1, column=5, padx=10, pady=(5, 2))

            MobileLabel = Label(
                PassengerDetailsFrame,
                text="Mobile No",
                font="Arial 10",
            )
            MobileLabel.grid(row=1, column=6, padx=10, pady=(5, 2))
            MobileEntry = Entry(PassengerDetailsFrame, textvariable=passMobile)
            MobileEntry.grid(row=1, column=7, padx=10, pady=(5, 2))

            AgeLabel = Label(PassengerDetailsFrame, text="Age", font="Arial 10")
            AgeLabel.grid(row=1, column=8, padx=10, pady=(5, 2))
            AgeEntry = Entry(PassengerDetailsFrame, textvariable=passAge)
            AgeEntry.grid(row=1, column=9, padx=10, pady=(5, 2))

            ProceedBooking = Button(
                PassengerDetailsFrame,
                text=" Book Ticket",
                font="Arial 15 bold",
                foreground="black",
                background="green",
                command=passdet,
            )
            ProceedBooking.grid(row=2, column=9, padx=25, pady=(20, 10))

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
        ShowBusesbtn.grid(
            row=0, column=6, columnspan=1, rowspan=1, padx=(30, 10), pady=20
        )

        HomeButtonImage = PhotoImage(file=".\\home.png")

        def gohome():
            root.destroy()
            self.menuframe()

        Homebtn = Button(
            QueryFrame,
            image=HomeButtonImage,
            # bg="SpringGreen3",
            # fg="Black",
            # font="Arial 13 bold",
            border=1,
            borderwidth=2,
            relief="solid",
            command=gohome,
            # width=20,
            height=48,
            # activeforeground="White",
            # activebackground="SpringGreen4",
        )
        Homebtn.grid(row=0, column=7, columnspan=1, rowspan=1, padx=(20, 20), pady=20)

        ###################################################################################

        root.mainloop()

    def adminframe(self):
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

        def calladdnewbusframe():
            root.destroy()
            self.newbusframe()

        def calladdnewrouteframe():
            root.destroy()
            self.newrouteframe()

        def calladdnewoperatorframe():
            root.destroy()
            self.newoperatorframe()

        def calladdnewrunframe():
            root.destroy()
            self.newrunframe()

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
            command=calladdnewoperatorframe,
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
            command=calladdnewbusframe,
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
            command=calladdnewrouteframe,
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
            command=calladdnewrunframe,
            width=20,
            height=2,
            activebackground="SpringGreen4",
            activeforeground="White",
        )
        NewRunbtn.grid(row=0, column=4, columnspan=1, rowspan=1, padx=10, pady=20)

        root.mainloop()

    def newbusframe(self):
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
        NewBusDetailFrame.grid(
            row=2, column=0, columnspan=9, rowspan=1, padx=0, pady=60
        )

        bus_id = IntVar()
        # bus_name = ""
        bus_type = StringVar()
        bus_capacity = IntVar()
        bus_route_id = IntVar()
        bus_operator_id = IntVar()
        bus_fare = IntVar()

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

        BusTypeLabel = Label(
            NewBusDetailFrame,
            text="Bus Type",
            font="Arial 12 bold",
        )
        BusTypeLabel.grid(row=0, column=2, columnspan=1, rowspan=1, padx=10, pady=10)
        BusTypeOptions = [
            "AC 2x2",
            "Non-AC 2x2",
            "AC 2x3",
            "Non-AC 2x3 Sleeper",
            "AC Sleeper",
        ]
        BusTypeOptionBox = OptionMenu(
            NewBusDetailFrame,
            bus_type,
            *BusTypeOptions,
        )
        BusTypeOptionBox.grid(
            row=0, column=3, columnspan=1, rowspan=1, padx=10, pady=10
        )

        BusCapacityLabel.grid(
            row=0, column=4, columnspan=1, rowspan=1, padx=10, pady=10
        )
        BusCapacityEntry = Entry(
            NewBusDetailFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=bus_capacity,
        )
        BusCapacityEntry.grid(
            row=0, column=5, columnspan=1, rowspan=1, padx=10, pady=10
        )

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
        BusOperatorIDLabel.grid(
            row=0, column=8, columnspan=1, rowspan=1, padx=10, pady=10
        )
        BusOperatorIDEntry = Entry(
            NewBusDetailFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=bus_operator_id,
        )
        BusOperatorIDEntry.grid(
            row=0, column=9, columnspan=1, rowspan=1, padx=10, pady=10
        )

        BusRouteIDLabel = Label(
            NewBusDetailFrame,
            text="Bus Route ID",
            font="Arial 12 bold",
        )
        BusRouteIDLabel.grid(
            row=0, column=10, columnspan=1, rowspan=1, padx=10, pady=10
        )
        BusRouteIDEntry = Entry(
            NewBusDetailFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=bus_route_id,
        )
        BusRouteIDEntry.grid(
            row=0, column=11, columnspan=1, rowspan=1, padx=10, pady=10
        )

        ButtonFrame = ttk.Frame(root, width=width)
        ButtonFrame.grid(row=3, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

        def getbusdetails():
            bus_id = BusIDEntry.get()
            # bus_name = BusNameEntry.get()
            bus_type_val = bus_type.get()
            bus_capacity = BusCapacityEntry.get()
            bus_route_id = BusRouteIDEntry.get()
            bus_operator_id = BusOperatorIDEntry.get()
            bus_fare = BusFareEntry.get()

            return [
                bus_id,
                bus_capacity,
                bus_fare,
                bus_type_val,
                bus_operator_id,
                bus_route_id,
            ]

        def addbusdetails():
            newbusdetails = getbusdetails()

            print(newbusdetails)

            try:
                cursor.execute(
                    "INSERT INTO businfo VALUES(?, ?, ?, ?, ?, ?)",
                    (
                        newbusdetails[0],
                        newbusdetails[1],
                        newbusdetails[2],
                        newbusdetails[3],
                        newbusdetails[4],
                        newbusdetails[5],
                    ),
                )
                connection.commit()
                messagebox.showinfo(
                    "Success", "Bus Details Added Successfully", parent=root
                )
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Bus ID already exists. Please try again")

        AddBusButton = Button(
            ButtonFrame,
            text="Add Bus",
            font="Arial 12 bold",
            bg="green2",
            fg="Red",
            border=1,
            borderwidth=2,
            relief="solid",
            command=addbusdetails,
            width=10,
        )
        AddBusButton.grid(row=1, column=0, columnspan=1, rowspan=1, padx=10, pady=30)

        def editbus():
            newbusdetails = getbusdetails()
            try:
                cursor.execute(
                    "UPDATE businfo SET capacity=?, fare=?, bustype=?, opid=?, roid=? WHERE busid=?",
                    (
                        newbusdetails[1],
                        newbusdetails[2],
                        newbusdetails[3],
                        newbusdetails[4],
                        newbusdetails[5],
                        newbusdetails[0],
                    ),
                )
                connection.commit()
                messagebox.showinfo(
                    "Success", "Bus Details Updated Successfully", parent=root
                )
            except sqlite3.IntegrityError:
                messagebox.showerror(
                    "Error", "Bus ID Does not exists. Please try again"
                )

        def editbusdetails():
            editbus()
            print("editbusdetails")

        EditBusButton = Button(
            ButtonFrame,
            text="Edit Bus",
            font="Arial 12 bold",
            bg="green2",
            fg="Red",
            border=1,
            borderwidth=2,
            relief="solid",
            command=editbusdetails,
            width=10,
        )
        EditBusButton.grid(row=1, column=1, columnspan=1, rowspan=1, padx=10, pady=30)

        def gohome():
            root.destroy()
            self.menuframe()

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

    def newoperatorframe(self):
        root = Tk()
        root.title("Add Operator")
        root.resizable(False, False)

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
            text="Add New Operator Details",
            # bg="green2",
            fg="green",
            font="Arial 25",
        )
        SubHeading.grid(row=1, column=1, columnspan=9, rowspan=1, padx=0, pady=20)

        NewOperatorDetailFrame = ttk.Frame(root, width=width)
        NewOperatorDetailFrame.grid(
            row=2, column=0, columnspan=9, rowspan=1, padx=0, pady=0
        )

        operator_id = StringVar()
        operator_name = StringVar()
        operator_addr = StringVar()
        operator_email = StringVar()
        operator_phone = StringVar()

        OperatorIDLabel = Label(
            NewOperatorDetailFrame,
            text="Operator ID",
            font="Arial 12 bold",
        )
        OperatorIDLabel.grid(row=0, column=0, columnspan=1, rowspan=1, padx=10, pady=10)
        OperatorIDEntry = Entry(
            NewOperatorDetailFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=operator_id,
        )
        OperatorIDEntry.grid(row=0, column=1, columnspan=1, rowspan=1, padx=10, pady=10)

        OperatorNameLabel = Label(
            NewOperatorDetailFrame,
            text="Name",
            font="Arial 12 bold",
        )
        OperatorNameLabel.grid(
            row=0, column=2, columnspan=1, rowspan=1, padx=10, pady=10
        )
        OperatorNameEntry = Entry(
            NewOperatorDetailFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=operator_name,
        )
        OperatorNameEntry.grid(
            row=0, column=3, columnspan=1, rowspan=1, padx=10, pady=10
        )

        OperatorAddressLabel = Label(
            NewOperatorDetailFrame,
            text="Address",
            font="Arial 12 bold",
        )
        OperatorAddressLabel.grid(
            row=0, column=4, columnspan=1, rowspan=1, padx=10, pady=10
        )
        OperatorAddressEntry = Entry(
            NewOperatorDetailFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=operator_addr,
        )
        OperatorAddressEntry.grid(
            row=0, column=5, columnspan=1, rowspan=1, padx=10, pady=10
        )

        OperatorPhoneLabel = Label(
            NewOperatorDetailFrame,
            text="Phone",
            font="Arial 12 bold",
        )
        OperatorPhoneLabel.grid(
            row=0, column=6, columnspan=1, rowspan=1, padx=10, pady=10
        )
        OperatorPhoneEntry = Entry(
            NewOperatorDetailFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=operator_phone,
        )
        OperatorPhoneEntry.grid(
            row=0, column=7, columnspan=1, rowspan=1, padx=10, pady=10
        )

        OperatorEmailLabel = Label(
            NewOperatorDetailFrame,
            text="Email",
            font="Arial 12 bold",
        )
        OperatorEmailLabel.grid(
            row=0, column=8, columnspan=1, rowspan=1, padx=10, pady=10
        )
        OperatorEmailEntry = Entry(
            NewOperatorDetailFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=operator_email,
        )
        OperatorEmailEntry.grid(
            row=0, column=9, columnspan=1, rowspan=1, padx=10, pady=10
        )

        ButtonFrame = ttk.Frame(root, width=width)
        ButtonFrame.grid(row=3, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

        def getoperator():
            print("getoperator")
            return [
                operator_id.get(),
                operator_name.get(),
                operator_phone.get(),
                operator_email.get(),
                operator_addr.get(),
            ]

        def addoperatordetails():
            op = getoperator()
            if op[0] == "" and op[1] == "" and op[2] == "" and op[3] == "":
                messagebox.showerror("Error", "Please enter all the details")
            else:
                print("addoperator", op)
                try:
                    cursor.execute(
                        "INSERT INTO operatorinfo VALUES(?,?,?,?,?)",
                        (op[0], op[1], op[2], op[3], op[4]),
                    )
                    connection.commit()
                    messagebox.showinfo("Success", "Operator added successfully")
                except sqlite3.IntegrityError:
                    messagebox.showerror(
                        "Error", "Operator ID already exists. Please try again"
                    )

        AddOperatorButton = Button(
            ButtonFrame,
            text="Add Operator",
            font="Arial 12 bold",
            bg="green2",
            fg="Red",
            border=1,
            borderwidth=2,
            relief="solid",
            command=addoperatordetails,
            width=10,
        )
        AddOperatorButton.grid(
            row=1, column=0, columnspan=1, rowspan=1, padx=10, pady=30
        )

        def calleditoperator():
            op = getoperator()
            if op[0] == "" and op[1] == "" and op[2] == "" and op[3] == "":
                messagebox.showerror("Error", "Please enter all the details")
            else:
                print("editoperator", op)
                try:
                    cursor.execute(
                        "UPDATE operatorinfo SET name=?, phone=?, email=?, address=? WHERE operatorid=?",
                        (op[0], op[1], op[2], op[3], op[4]),
                    )
                    connection.commit()
                    messagebox.showinfo("Success", "Operator edited successfully")
                except sqlite3.IntegrityError:
                    messagebox.showerror(
                        "Error", "Operator ID Doesnt exists. Please try again"
                    )
            print("calleditoperator")

        EditOperatorButton = Button(
            ButtonFrame,
            text="Edit Operator",
            font="Arial 12 bold",
            bg="green2",
            fg="Red",
            border=1,
            borderwidth=2,
            relief="solid",
            command=calleditoperator,
            width=10,
        )
        EditOperatorButton.grid(
            row=1, column=1, columnspan=1, rowspan=1, padx=10, pady=30
        )

        homeimage = PhotoImage(file="./home.png")

        def gohome():
            root.destroy()
            self.menuframe()

        GoHomeButton = Button(
            ButtonFrame,
            image=homeimage,
            command=gohome,
        )
        GoHomeButton.grid(row=1, column=2, columnspan=1, rowspan=1, padx=10, pady=30)

        root.mainloop()

    def newrouteframe(self):
        root = Tk()
        root.title("Add Route")
        root.resizable(False, False)

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
            text="Add New Route Details",
            # bg="green2",
            fg="green",
            font="Arial 25",
        )
        SubHeading.grid(row=1, column=1, columnspan=9, rowspan=1, padx=0, pady=20)

        NewRouteFrame = ttk.Frame(root, width=width)
        NewRouteFrame.grid(row=2, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

        route_id = StringVar()
        route_from = StringVar()
        route_to = StringVar()

        RouteIDLabel = Label(
            NewRouteFrame,
            text="Route ID",
            font="Arial 12 bold",
        )
        RouteIDLabel.grid(row=0, column=0, columnspan=1, rowspan=1, padx=10, pady=10)
        RouteIDEntry = Entry(
            NewRouteFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=route_id,
        )
        RouteIDEntry.grid(row=0, column=1, columnspan=1, rowspan=1, padx=10, pady=10)

        RouteFromLabel = Label(
            NewRouteFrame,
            text="Station From",
            font="Arial 12 bold",
        )
        RouteFromLabel.grid(row=0, column=2, columnspan=1, rowspan=1, padx=10, pady=10)
        RouteFromEntry = Entry(
            NewRouteFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=route_from,
        )
        RouteFromEntry.grid(row=0, column=3, columnspan=1, rowspan=1, padx=10, pady=10)

        RouteToLabel = Label(
            NewRouteFrame,
            text="Station To",
            font="Arial 12 bold",
        )
        RouteToLabel.grid(row=0, column=4, columnspan=1, rowspan=1, padx=10, pady=10)
        RouteToEntry = Entry(
            NewRouteFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=route_to,
        )
        RouteToEntry.grid(row=0, column=5, columnspan=1, rowspan=1, padx=10, pady=10)

        ButtonFrame = ttk.Frame(root, width=width)
        ButtonFrame.grid(row=3, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

        def getroute():
            print("getroute")

            return [route_id.get(), route_from.get(), route_to.get()]

        def addnewroute():
            route = getroute()
            if route[1] == "" or route[0] == "" or route[2] == "":
                messagebox.showerror("Error", "Please fill all the details")
            else:
                print(route)
                print("addnewroute")
                try:
                    cursor.execute(
                        "INSERT INTO routeinfo VALUES(?,?,?)",
                        (route[0], route[1], route[2]),
                    )
                    connection.commit()
                    messagebox.showinfo("Success", "Route added successfully")
                except sqlite3.IntegrityError:
                    messagebox.showerror(
                        "Error", "Route ID already exists. Please try again"
                    )

        AddRouteButton = Button(
            ButtonFrame,
            text="Add",
            font="Arial 14 bold",
            bg="green2",
            fg="black",
            border=1,
            borderwidth=2,
            relief="solid",
            command=addnewroute,
            width=10,
            # height=2,
        )
        AddRouteButton.grid(row=1, column=0, columnspan=1, rowspan=1, padx=10, pady=30)

        def deleteroute():
            route = getroute()
            if route[1] == "" or route[0] == "" or route[2] == "":
                messagebox.showerror("Error", "Please fill all the details")
            else:
                print(route)
                print("deleteroute", route)
                try:
                    cursor.execute(
                        "DELETE FROM routeinfo WHERE routeid=?",
                        (route[0],),
                    )
                    connection.commit()
                    messagebox.showinfo("Success", "Route deleted successfully")
                except sqlite3.IntegrityError:
                    messagebox.showerror(
                        "Error", "Route ID does not exist. Please try again"
                    )

        DeleteRouteButton = Button(
            ButtonFrame,
            text="Delete",
            font="Arial 14 bold",
            bg="green2",
            fg="black",
            border=1,
            borderwidth=2,
            relief="solid",
            command=deleteroute,
            width=10,
            # height=2,
        )
        DeleteRouteButton.grid(
            row=1, column=1, columnspan=1, rowspan=1, padx=10, pady=30
        )

        homeimage = PhotoImage(file="./home.png")

        def gohome():
            root.destroy()
            self.menuframe()

        GoHomeButton = Button(
            ButtonFrame,
            image=homeimage,
            command=gohome,
        )
        GoHomeButton.grid(row=1, column=2, columnspan=1, rowspan=1, padx=10, pady=30)

        root.mainloop()

    def newrunframe(self):
        root = Tk()
        root.title("Add New Run Details")
        root.resizable(False, False)

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
            text="Add New Run Details",
            # bg="green2",
            fg="green",
            font="Arial 25",
        )
        SubHeading.grid(row=1, column=1, columnspan=9, rowspan=1, padx=0, pady=20)

        NewRouteFrame = ttk.Frame(root, width=width)
        NewRouteFrame.grid(row=2, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

        bus_id = StringVar()
        running_date = StringVar()
        seat_available = StringVar()

        BusIdLabel = Label(
            NewRouteFrame,
            text="Bus ID",
            font="Arial 12 bold",
        )
        BusIdLabel.grid(row=0, column=0, columnspan=1, rowspan=1, padx=10, pady=10)
        BusIdEntry = Entry(
            NewRouteFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=bus_id,
        )
        BusIdEntry.grid(row=0, column=1, columnspan=1, rowspan=1, padx=10, pady=10)

        RunningdateLabel = Label(
            NewRouteFrame,
            text="Running Date",
            font="Arial 12 bold",
        )
        RunningdateLabel.grid(
            row=0, column=2, columnspan=1, rowspan=1, padx=10, pady=10
        )
        RunningdateEntry = Entry(
            NewRouteFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=running_date,
        )
        RunningdateEntry.grid(
            row=0, column=3, columnspan=1, rowspan=1, padx=10, pady=10
        )

        SeatAvailLabel = Label(
            NewRouteFrame,
            text="Seat available",
            font="Arial 12 bold",
        )
        SeatAvailLabel.grid(row=0, column=4, columnspan=1, rowspan=1, padx=10, pady=10)
        SeatAvailEntry = Entry(
            NewRouteFrame,
            font="Arial 12 bold",
            width=10,
            textvariable=seat_available,
        )
        SeatAvailEntry.grid(row=0, column=5, columnspan=1, rowspan=1, padx=10, pady=10)

        ButtonFrame = ttk.Frame(root, width=width)
        ButtonFrame.grid(row=3, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

        def getrun():
            print("getrun")

            return [bus_id.get(), running_date.get(), seat_available.get()]

        def addnewrun():
            run = getrun()
            if run[1] == "" or run[0] == "" or run[2] == "":
                messagebox.showerror("Error", "Please fill all the details")
            else:
                print(run)
                try:
                    cursor.execute(
                        "INSERT INTO run VALUES(?,?,?)",
                        (run[0], run[1], run[2]),
                    )
                    connection.commit()
                    messagebox.showinfo("Success", "Run added successfully")
                except sqlite3.IntegrityError:
                    messagebox.showerror(
                        "Error", "Bus already Runs on this date. Please try again"
                    )

        AddRunButton = Button(
            ButtonFrame,
            text="Add",
            font="Arial 14 bold",
            bg="green2",
            fg="black",
            border=1,
            borderwidth=2,
            relief="solid",
            command=addnewrun,
            width=10,
            # height=2,
        )
        AddRunButton.grid(row=1, column=0, columnspan=1, rowspan=1, padx=10, pady=30)

        def deleterun():
            run = getrun()
            if run[1] == "" or run[0] == "" or run[2] == "":
                messagebox.showerror("Error", "Please fill all the details")
            else:
                print(run)
                print("deleterun", run)
                try:
                    cursor.execute(
                        "DELETE FROM run WHERE bus_id=? AND date=?",
                        (run[0], run[1]),
                    )
                    connection.commit()
                    messagebox.showinfo("Success", "Run deleted successfully")
                except sqlite3.IntegrityError:
                    messagebox.showerror(
                        "Error", "Run ID doesnt exists. Please try again"
                    )

        DeleteRunButton = Button(
            ButtonFrame,
            text="Delete",
            font="Arial 14 bold",
            bg="green2",
            fg="black",
            border=1,
            borderwidth=2,
            relief="solid",
            command=deleterun,
            width=10,
            # height=2,
        )
        DeleteRunButton.grid(row=1, column=1, columnspan=1, rowspan=1, padx=10, pady=30)

        homeimage = PhotoImage(file="./home.png")

        def gohome():
            root.destroy()
            self.menuframe()

        GoHomeButton = Button(
            ButtonFrame,
            image=homeimage,
            command=gohome,
        )
        GoHomeButton.grid(row=1, column=2, columnspan=1, rowspan=1, padx=10, pady=30)

        root.mainloop()

        print("op")

    def ticketconfirmationframe(self):

        # cursor.execute("SELECT * FROM customer WHERE phone=?", (phone,))
        cursor.execute(
            """select passengerinfo.name,seats,age,bookingid,run.date,source,
                gender,operatorinfo.name,fare,destination
                from bookinginfo,passengerinfo,run,businfo,routeinfo,operatorinfo
                where bookinginfo.bookingid=passengerinfo.passengerid
                and bookinginfo.buid=businfo.busid
                and businfo.roid=routeinfo.routeid
                and businfo.opid=operatorinfo.operatorid
                and bookinginfo.buid=run.bus_id
                and passengerinfo.phone=?""",
            (pho,),
        )

        data = cursor.fetchall()
        ticket = data[0]
        print(ticket)
        root = Tk()
        root.title("Add New Run Details")
        root.resizable(False, False)

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
            font="Arial 30",
            bg="LightSkyBlue1",
            fg="Red",
            border=1,
            borderwidth=2,
            relief="solid",
            width=25,
        )
        Heading.grid(row=0, column=1, columnspan=9, rowspan=1, padx=0, pady=20)

        ##########################################################################################

        """ Check Booking Frame """

        BookingFrame = ttk.Frame(root, width=width)
        BookingFrame.grid(row=3, column=0, columnspan=9, rowspan=1, padx=0, pady=0)

        mobilenumber = IntVar()

        # ticket = []
        BookingDetailsFrame = Frame(
            root,
            width=width,
            border=1,
            borderwidth=2,
            relief="solid",
        )
        BookingDetailsFrame.grid(
            row=4,
            column=0,
            columnspan=9,
            rowspan=1,
            padx=(0, 0),
            pady=(10, 5),
            ipadx=50,
        )
        passengername = ticket[0]
        seatnumber = str(ticket[1])
        age = str(ticket[2])
        busrefnumber = str(ticket[3])
        traveldate = ticket[4]
        boardingpoint = ticket[5]
        gender = ticket[6]
        mobilenumber = pho
        busnumber = "MH 12 AB 1234"
        busname = ticket[7]
        busfare = str(int(ticket[8]) * int(ticket[1]))
        destinationpoint = ticket[9]
        # Name
        PassengerNameLabel = Label(
            BookingDetailsFrame,
            text="Passenger: " + passengername,
            font="Arial 12",
        )
        PassengerNameLabel.grid(
            row=0,
            column=0,
            columnspan=1,
            rowspan=1,
            padx=(0, 30),
            pady=(3, 3),
            sticky=W,
        )
        ##### Seat ##############
        PassengerSeat = Label(
            BookingDetailsFrame, text="Seat: " + seatnumber, font="Arial 12"
        )
        PassengerSeat.grid(
            row=1,
            column=0,
            columnspan=1,
            rowspan=1,
            padx=0,
            pady=(3, 3),
            sticky=W,
        )
        ##### Age ##############
        PassengerAgeLabel = Label(
            BookingDetailsFrame, text="Age: " + str(age), font="Arial 12"
        )
        PassengerAgeLabel.grid(
            row=2,
            column=0,
            columnspan=1,
            rowspan=1,
            padx=0,
            pady=(3, 3),
            sticky=W,
        )
        ##### Booking Ref ##############
        PassengerBookingrefLabel = Label(
            BookingDetailsFrame,
            text="Booking Ref: " + busrefnumber,
            font="Arial 12",
        )
        PassengerBookingrefLabel.grid(
            row=3,
            column=0,
            columnspan=1,
            rowspan=1,
            padx=0,
            pady=(3, 3),
            sticky=W,
        )
        ##### Travel Date ##############
        TravelDateLabel = Label(
            BookingDetailsFrame,
            text="Travel Date: " + traveldate,
            font="Arial 12",
        )
        TravelDateLabel.grid(
            row=4,
            column=0,
            columnspan=1,
            rowspan=1,
            padx=0,
            pady=(3, 3),
            sticky=W,
        )
        ##### Boarding Point ##############
        PassengerBoardingPoint = Label(
            BookingDetailsFrame,
            text="Boarding Point: " + boardingpoint,
            font="Arial 12",
        )
        PassengerBoardingPoint.grid(
            row=5,
            column=0,
            columnspan=1,
            rowspan=1,
            padx=0,
            pady=(3, 3),
            sticky=W,
        )
        ##### Gender ##############
        PassengerGenderLabel = Label(
            BookingDetailsFrame, text="Gender: " + gender, font="Arial 12"
        )
        PassengerGenderLabel.grid(
            row=0,
            column=1,
            columnspan=1,
            rowspan=1,
            padx=(10, 5),
            pady=(3, 3),
            sticky=W,
        )
        ##### Mobile Number ##############
        PassengerPhoneLabel = Label(
            BookingDetailsFrame, text="Phone: " + mobilenumber, font="Arial 12"
        )
        PassengerPhoneLabel.grid(
            row=1,
            column=1,
            columnspan=1,
            rowspan=1,
            padx=(10, 5),
            pady=(3, 3),
            sticky=W,
        )
        PassengerBusNumberLabel = Label(
            BookingDetailsFrame,
            text="Bus Number: " + busnumber,
            font="Arial 12",
        )
        PassengerBusNumberLabel.grid(
            row=2,
            column=1,
            columnspan=1,
            rowspan=1,
            padx=(10, 5),
            pady=(3, 3),
            sticky=W,
        )
        PassengerBusNameLabel = Label(
            BookingDetailsFrame, text="Bus Name: " + busname, font="Arial 12"
        )
        PassengerBusNameLabel.grid(
            row=3,
            column=1,
            columnspan=1,
            rowspan=1,
            padx=(10, 5),
            pady=(3, 3),
            sticky=W,
        )
        PassengerFare = Label(
            BookingDetailsFrame, text="Fare: " + busfare, font="Arial 12"
        )
        PassengerFare.grid(
            row=4,
            column=1,
            columnspan=1,
            rowspan=1,
            padx=(10, 5),
            pady=(3, 3),
            sticky=W,
        )
        PassengerDestPointLabel = Label(
            BookingDetailsFrame,
            text="Destination: " + destinationpoint,
            font="Arial 12",
        )
        PassengerDestPointLabel.grid(
            row=5,
            column=1,
            columnspan=1,
            rowspan=1,
            padx=(10, 5),
            pady=(3, 3),
            sticky=W,
        )

        def goback():
            self.menuframe()
            root.destroy()

        root.bind("<KeyPress>", goback)
        root.mainloop()


B = BBS()
B.rootframe()
