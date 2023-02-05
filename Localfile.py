import sqlite3
import os

connection = sqlite3.connect("busdatabase.db")
cursor = connection.cursor()


def create_table():
    ## operatorinfo table
    cursor.execute(
        "create table if not exists operatorinfo (operatorid int primary key, name text,phone text,email text,address text);"
    )
    ## routeinfo table
    cursor.execute(
        "create table if not exists routeinfo (routeid int primary key,source text,destination text);"
    )
    ## businfo table
    cursor.execute(
        "create table if not exists businfo (busid int primary key,capacity int,fare int,bustype varchar(15),opid int,roid int,foreign key(opid) references operatorinfo(operatorid),foreign key(roid) references routeinfo(routeid));"
    )
    ## passengerinfo table
    cursor.execute(
        "create table if not exists passengerinfo (passengerid integer primary key autoincrement,name text,phone text,age int,address text,gender text);"
    )
    ## bookinginfo table
    cursor.execute(
        "create table if not exists bookinginfo (bookingid integer primary key autoincrement,buid int,date text,seats int);"
    )
    ## run table
    cursor.execute(
        "create table if not exists run (bus_id int,date date,seat_avail int,foreign key(bus_id) references businfo(busid) primary key (bus_id,date));"
    )

    # ## Fkey in businfo
    # cursor.execute(
    #     "alter table businfo add foreign key(opid) references operatorinfo(operatorid);"
    # )
    # cursor.execute(
    #     "alter table businfo add foreign key(roid) references routeinfo(routeid);"
    # )
    # ## Fkey in bookinginfo
    # cursor.execute(
    #     "alter table bookinginfo add foreign key(buid) references businfo(busid);"
    # )
    # cursor.execute(
    #     "alter table bookinginfo add foreign key(passengerid) references passengerinfo(passengerid);"
    # )
    # ## Fkey in run
    # cursor.execute("alter table run add foreign key(busid) references businfo(busid);")
    # cursor.execute(
    #     "alter table run add foreign key(bookingid) references bookinginfo(bookingid);"
    # )
    connection.commit()


create_table()

connection.close()
