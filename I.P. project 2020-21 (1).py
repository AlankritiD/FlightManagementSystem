#!/usr/bin/env python
# coding: utf-8

# In[ ]:


MENUS-

Main Menu
1.Login
2.Search
3.Sign up
4.Exit


Admin Home Menu
1.Flight
2.Seats
3.Search
4.Log out

Admin Flight Menu
1.Create new flight
2.Update flight
3.Delete flight 
4.Search flight
5.Back

Admin Seats Menu
1.Create new Seats
2.Update Seats
3.Delete Seats
4.Back


Customer Menu
1.Search flight
2.Web check in
3.Book ticket 
4.Edit booking
5.Print ticket
6.Update profile
7.My Trips 
8.Check Rules
9.Check offers
10.back


# In[ ]:


SQL TABLES-
Create database airlines


Tables 
User -
create table user
(	userid int primary key,
    	username varchar(20),
    	usertype varchar(20),
    	password varchar(30),
    	dob date,
    	address varchar(30),
    	contactno varchar(20)
);
+--------+----------+----------+----------+------------+------------+-----------+
| userid | username | usertype | password | dob        | address    | contactno |
+--------+----------+----------+----------+------------+------------+-----------+
|   1233 | riya     | Customer | r45      | 2002-03-30 | kolar road | 998877664 |
|   2344 | Raman    | Admin    | a46      | 2002-02-02 | delhi      | 908908898 |
+--------+----------+----------+----------+------------+------------+-----------+


Flight -
create table flight
    (fno int primary key,
    departureloc varchar(25),
    arrivalloc varchar(25),
    deptdate date,
    depttime time,
arrdate date,
    arrtime time);
    
Alter table flight
Add deptdate date, arrdate date;

+------+--------------+------------+----------+----------+------------+------------+
| fno  | departureloc | arrivalloc | depttime | arrtime  | deptdate   | arrdate    |
+------+--------------+------------+----------+----------+------------+------------+
| 1256 | Kan          | Mah        | 22:30:00 | 15:00:00 | 2020-01-02 | 2020-01-04 |
| 4343 | Pun          | Ind        | 22:00:00 | 05:30:00 | NULL       | NULL       |
+------+--------------+------------+----------+----------+------------+------------+

Table seats:
Create table Seats
       ( fno int,
	Type varchar(15) not null,
	Qty int(5),
	Cost decimal(10,2),
	Seatnos varchar(15),
	Primary key(fno, seatnos),
	Foreign key (fno) references flight (fno)
	);
    
+------+---------+------+----------+---------+
| fno  | Type    | Qty  | Cost     | Seatnos |
+------+---------+------+----------+---------+
| 1256 | Economy |    3 | 30000.00 | E0-03   |
| 4343 | Economy |    2 | 51000.00 | B0-02   |
+------+---------+------+----------+---------+


Transaction table:
Create table transaction
 	(tid int primary key auto_increment,
	tdate date,
	Userid int,
Fno int,
Ticket_details varchar(100) not null,
Amount decimal(10,2),
Bstatus varchar(20) default 'booked',
Ramount decimal(10,2),
Foreign key (userid) references user (userid),
Foreign key (fno) references flight (fno)
);

    +-----+------------+--------+------+------------------------------------------------------------------------------------------------------+-----------+-----------+----------+
| tid | tdate      | Userid | Fno  | Ticket_details                                                                                       | Amount    | Bstatus   | ramount  |
+-----+------------+--------+------+------------------------------------------------------------------------------------------------------+-----------+-----------+----------+
|   2 | 2020-12-03 |   1233 | 4343 | xyz                                                                                                  | 102000.00 | Cancelled | 81600.00 |
|   3 | 2020-12-03 |   1233 | 4343 | from :Pun To: Ind departuretime: 22:00:00 arrivaltime: 5:30:00 departuredate: None arrivaldate: None | 102000.00 | booked    |     NULL |
+-----+------------+--------+------+------------------------------------------------------------------------------------------------------+-----------+-----------+----------+


# In[ ]:


import mysql.connector as msc
from datetime import date 
#creating new flight
def Create_flight():
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        print("Successfully connected to MySQL database")
        cur=mycon.cursor()
        print("Enter the details for new flight:")
        fno=int(input('Enter the flight number:'))
        #checking whether fno already exists or not
        cur.execute("select * from flight where fno={}".format(fno))
        if cur.fetchall()==[]:
            departureloc=input("Enter the departure location:")
            arrivalloc=input("Enter the arrival location:")
            deptdate=input("Enter the departure date(YYYY-MM-DD):")
            depttime=input("Enter the departure time(HH:MM:SS):")
            arrdate=input("Enter the arrival date(YYYY-MM-DD):")
            arrtime=input("Enter the arrival time(HH-MM-SS):")
            query="INSERT into flight (fno,departureloc,arrivalloc,deptdate,depttime,arrdate,arrtime)VALUES ({},'{}','{}','{}','{}','{}','{}')".format(fno,departureloc,arrivalloc,deptdate,depttime,arrdate,arrtime)     
            cur.execute(query)
            mycon.commit()     #So that changes may take place
            #now selecting record
            cur.execute("select * from flight ")
            data=cur.fetchall()
            for row in data:
                print(row)
        else:
            print("fno number already exists")
            mycon.close()
    else:
        print("MySQL Connection problem")
        
#update flight
def Upd_flight():
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        print("Successfully connected to MySQL database")
        cur=mycon.cursor()
        fno=int(input('Enter the flight number to be updated:'))
        #checking whether fno already exists or not
        cur.execute("select * from flight where fno={}".format(fno))
        data=cur.fetchall()
        if data!=[]:
            print("Old details: ", data)
            print("Enter new details for flight:")
            departureloc=input("Enter the departure location:")
            arrivalloc=input("Enter the arrival location:")
            deptdate=input("Enter the departure date(YYYY-MM-DD):")
            depttime=input("Enter the departure time(HH:MM:SS):")
            arrdate=input("Enter the arrival date(YYYY-MM-DD):")
            arrtime=input("Enter the arrival time(HH-MM-SS):")
            query="Update flight set departureloc= '{}', arrivalloc='{}' ,deptdate='{}',depttime='{}',arrdate='{}', arrtime='{}' where fno={}".format(departureloc,arrivalloc,deptdate,depttime,arrdate,arrtime,fno)     
            cur.execute(query)
            mycon.commit()     #So that changes may take place
            cur.execute("select * from flight; ")
            data=cur.fetchall()
            for row in data:
                print(row)
        else:
            print("Flight number does not exists")
        mycon.close()
    else:
        print("MySQL Connection problem")

#delete flight 
def Del_flight():
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        print("Successfully connected to MySQL database")
        cur=mycon.cursor()
        fno=int(input('Enter the flight number to be deleted:'))
        #checking whether fno already exists or not
        cur.execute("select * from flight where fno={}".format(fno))
        data=cur.fetchall()
        if data!=[]:
            print("Old details: ", data)
            query="Delete from flight where fno={}".format(fno)     
            cur.execute(query)
            mycon.commit()     #So that changes may take place
            print('flight deleted successfully')          
            #now selecting record	
            cur.execute("select * from flight; ")
            data=cur.fetchall()
            for row in data:
                print(row)
        else:
            print("flight number does not exists")
        mycon.close()
    else:
        print("MySQL Connection problem")
        
#search flight
def Search_flight():
        mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
        if mycon.is_connected():
            print("successfully connected to MySQL")
            cur=mycon.cursor()
            departureloc=input("enter departure location")
            arrivalloc=input("enter arrival location")
            cur.execute("select * from flight where departureloc like '%{d}%' or arrivalloc like'%{a}%'".format(d=departureloc,a=arrivalloc))
            data=cur.fetchall()
            if data!=[]:
                print("record found details are as follows:")
                for row in data:
                    print(row)
            else:
                print("record not found") 
            mycon.close()
        else:
            print("MySQL connection problem")

def Flight_menu():
    print("Flight Menu")
    while True:
        print("ADMIN FLIGHT MENU")
        print("1.Create new flight")
        print("2.Update an existing flight")
        print("3.Delete flight")
        print("4.Select/Search flight")
        print("5.Back")
                
        choice=int(input("Enter your choice "))
        if choice==1:
            Create_flight()
        elif choice==2:
            Upd_flight()
        elif choice==3:
            Del_flight()
        elif choice==4:
            Search_flight()
        elif choice==5:
            break
        else:
            print("Invalid Choice")
            
#creating new seat
def Create_seat():
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        print("Successfully connected to MySQL database")
        cur=mycon.cursor()
        print("Enter the details for new seat:")
        fno=int(input('Enter the flight number:'))
        #checking whether fno already exists or not
        cur.execute("select * from seats where fno={}".format(fno))
        if cur.fetchall()==[]:
            Type=input("Enter the type of seat(Business/Economy):")
            Qty=int(input("Enter the number of seats available:"))
            Cost=float(input("Enter the cost per seat:"))
            Seatnos=input("Enter the the seat number:")
            query="INSERT into seats (fno,Type,Qty,Cost,Seatnos)VALUES ({},'{}',{},{},'{}')".format(fno,Type,Qty,Cost,Seatnos)     
            cur.execute(query)
            mycon.commit()     #So that changes may take place
#now selecting record	
            cur.execute("select * from seats")
            data=cur.fetchall()
            for row in data:
                print(row)
        else:
            print("fno number already exists")
            mycon.close()
    else:
        print("MySQL Connection problem")
        
#update seat
def Upd_seat():
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        print("Successfully connected to MySQL database")
        cur=mycon.cursor()
        fno=int(input('Enter the flight number to be updated:'))
        #checking whether fno already exists or not
        cur.execute("select * from seats where fno={}".format(fno))
        data=cur.fetchall()
        if data!=[]:
            print("Old details: ", data)
            print("Enter new details for seat:")
            Type=input("Enter the type of seat(Business/Economy):")
            Qty=int(input("Enter the number of seats available:"))
            Cost=float(input("Enter the cost per seat:"))
            Seatnos=input("Enter the the seat number:")
            query="Update seats set Type= '{}',Qty={} ,Cost={},Seatnos='{}' where fno={}".format(Type,Qty,Cost,Seatnos,fno)     
            cur.execute(query)
            mycon.commit()     #So that changes may take place
            #now selecting record	
            cur.execute("select * from seats; ")
            data=cur.fetchall()
            for row in data:
                print(row)
        else:
            print("Flight number does not exists")
        mycon.close()
    else:
        print("MySQL Connection problem")
        
#delete seat 
def Del_seat():
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        print("Successfully connected to MySQL database")
        cur=mycon.cursor()
        Seatnos=input('Enter the seat number to be deleted:')
        #checking whether Seatnos already exists or not
        cur.execute("select * from seats where Seatnos='{}'".format(Seatnos))
        data=cur.fetchall()
        if data!=[]:
            print("Old details: ", data)
            query="Delete from seats where Seatnos='{}'".format(Seatnos)
            cur.execute(query)
            mycon.commit()     #So that changes may take place
            print("Seat deleted successfully")      
            #now selecting record	
            cur.execute("select * from seats")
            data=cur.fetchall()
            for row in data:
                print(row)
        else:
            print("flight number does not exists")
        mycon.close()
    else:
        print("MySQL Connection problem")

def Seat_menu():
    print("Seats menu")
    while True:
        print("ADMIN SEAT MENU")
        print("1.Create new seat")
        print("2.Update an existing seat")
        print("3.Delete seat")
        print("4.Back")
                
        choice=int(input("Enter your choice "))
        if choice==1:
            Create_seat()
        elif choice==2:
            Upd_seat()
        elif choice==3:
            Del_seat()
        elif choice==4:
            break
        else:
            print("Invalid Choice")

def Upd_profile(uid):
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        print("Successfully connected to MySQL database")
        cur=mycon.cursor()
        cur.execute("select * from user where userid={}".format(uid))
        data=cur.fetchall()
        if data!=[]:
            print("Old details: ", data)
            print("Enter new details for profile:")
            username=input("Enter the username:")
            usertype=input("Enter the usertype:")
            password=input("Enter the password:")
            dob=input("Enter the date of birth:")
            address=input("Enter the address:")
            contactno=input("Enter the contact number:")
            query="Update user set username='{}',usertype='{}' ,password='{}',dob='{}',address='{}',contactno='{}' where userid={}".format(username,usertype,password,dob,address,contactno,uid)     
            cur.execute(query)
            mycon.commit()     #So that changes may take place
        #now selecting record	
            cur.execute("select * from user where userid={}".format(uid))
            data=cur.fetchall()
            for row in data:
                print(row)
        else:
            print("userid does not exists")
        mycon.close()
    else:
        print("MySQL Connection problem")
        
def Search_seat(fno):
        mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
        amount=0
        if mycon.is_connected():
            print("successfully connected to MySQL")
            cur=mycon.cursor()
            Type=input("Enter the seat type(Business/Economy)=")
            nos=int(input("Enter the number of seats="))
            cur.execute("select * from seats where fno={} and Type='{}'".format(fno,Type))
            data=cur.fetchall()
            if data!=[]:
                print("seat details are as follows:")
                print(data)
                amount=nos*data[0][3]
            else:
                print("seat not found") 
            mycon.close()
        else:
            print("MySQL connection problem")
        return amount 
        
def Book_ticket(uid):
    Search_flight()
    fno=int(input("Enter the flight number="))
    FD=""   #flightdetails
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        cur=mycon.cursor()
        cur.execute("select * from flight where fno={}".format(fno))
        data=cur.fetchall()
        if data!=[]:
            FD="from :"+data[0][1]+" To: "+data[0][2]+" departuretime: "+str(data[0][3])+" arrivaltime: "+str(data[0][4])+" departuredate: "+str(data[0][5])+" arrivaldate: "+str(data[0][6])
            #FD="xyz"
            amt=Search_seat(fno)   
            cur.execute("insert into transaction (tdate,userid,fno,ticket_details,amount) values ('{}',{},{},'{}',{})".format(str(date.today()),uid,fno,FD,amt))
            mycon.commit()
            print("Your ticket has been booked successfully!")
        else:
            print("Invalid flight number") 
        mycon.close()
    else:
        print("MySQL connection problem")

def Cancel_booking(uid):
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        print("Successfully connected to MySQL database")
        cur=mycon.cursor()
        cur.execute("select * from transaction where userid={}".format(uid))
        data=cur.fetchall()
        if data!=[]:
            print("Booking details: ")
            for row in data:
                print(row)
            tid=int(input("Enter the transaction id to be cancelled:"))
            cur.execute("select amount from transaction where tid={} and userid={}".format(tid,uid))
            data=cur.fetchall()
            if data!=[]:
                ch=input("Are you sure you want to cancel your booking?(y/n)")
                if ch=='y':
                    query="Update transaction set Bstatus='Cancelled',ramount={} where tid={} and userid={}".format(data[0][0]*80/100 ,tid,uid)     
                    cur.execute(query)
                    mycon.commit() 
                    print("Your ticket has been cancelled successfully,Amount refunded is ",data[0][0]*80/100)
            else:
                print("Invalid transaction id")
        else:
            print("Invalid user id")
        mycon.close()
    else:
        print("MySQL Connection problem")
        
def My_trips(uid):
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        print("Successfully connected to MySQL database")
        cur=mycon.cursor()
        cur.execute("select * from transaction where userid={}".format(uid))
        data=cur.fetchall()
        if data!=[]:
            print("MY trips: ")
            for row in data:
                print(row)
        else:
            print("INvalid user id")
        mycon.close()
    else:
        print("MySQL Connection problem")
def Web_checkin(uid):
    fno=int(input("Enter your flight number="))
    Prefseat=input("Enter the type of seat you prefer(Aisle/Window/Middle)=")
    email_ad=input("Enter the email address where you would like to recieve the follow ups=")
    print("Web check-in successful. Your boarding pass and baggage tags will be mailed to you.")

def Print_ticket():
    tid=input("Provide your ticket id")
    print("Your ticket will be printed in a short while.")

def Login():
    print("Login to Beatific Airlines.")
    userid=int(input('Enter the userID:'))
    password=input("enter the password:")
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airline")
    if mycon.is_connected():
        cur=mycon.cursor()
        #checking whether ID exists or not
        cur.execute("select * from user where userid={} and password='{}'".format(userid,password))
        data=cur.fetchall()
        if data!=[]:
            print(data[0][1],",Welcome to Beatific Airlines")
            if data[0][2]=="Admin":
                while True:
                    print('''Admin Home Menu
                      1.Flight
                      2.Seats
                      3.Search
                      4.Update Profile
                      5.Back to main''')
                    choice=int(input("Enter your choice:"))
                    if choice==1:
                        Flight_menu()       
                    elif choice==2:
                        Seat_menu()
                    elif choice==3:
                        Search_flight()
                    elif choice==4:
                        Upd_profile(data[0][0])
                    elif choice==5:
                        break
                    else:
                        print("Invalid choice")
            elif data[0][2]=="Customer":
                while True:
                    print("\t\t\tCustomer Menu")
                    print('''\t\t\t1.Search flight
                        2.Web check in
                        3.Book ticket 
                        4.Cancel booking
                        5.Print ticket
                        6.Update profile
                        7.My Trips 
                        8.Check rules
                        9.Check offers
                        10.back''')
                    choice=int(input("Enter your choice..."))
                    if choice==1:
                        Search_flight()       
                    elif choice==2:
                        Web_checkin(data[0][0])
                    elif choice==3:
                        Book_ticket(data[0][0])
                    elif choice==4:
                        Cancel_booking(data[0][0])
                    elif choice==5:
                        Print_ticket()
                    elif choice==6:
                        Upd_profile(data[0][0])
                    elif choice==7:
                        My_trips(data[0][0])
                    elif choice==8:
                         print('''Passenger to dos-
                                1.Health Declaration: Please don't forget to fill In the health status online 48 hours-60 minutes before your flight which will be provided on your email address.
                                2.Install Arogya Setu App on your mobile phones.
                                3.Don't for to complete your online web check-in for free 48 hours-60 minutes before your flight.
                                4.Please carry a printed or soft copy of your boarding pass and baggage tags.
                                5.Baggage allowance per person is 20 kgs only.
                                6.Please wear a mask and maintain the social distancing.''')
                    elif choice==9:
                        print('''Offers Available-
                                1.Beatific Hotels offer on stay: Enjoy 30% off  on your stay with free breakfast. T&C apply.
                                2.BE rewards: Get welcome benefits worth ₹5500.
                                3.Upto 25% off for our brave doctors and nurses.
                                4.Avail 10% off on base fare for senior citizens.''')

                    elif choice==10:
                        break
                    else:                          
                        print("Invalid choice")
        else:
            print("Incorrect userid and password")
        mycon.close()
    else:
        print("MySQL Connection problem")
        
def SignUp():
    mycon=msc.connect(host="localhost",user="root",passwd="123456",database="airlines")
    if mycon.is_connected():
        print("Successfully connected to MySQL database")
        cur=mycon.cursor()
        print("Enter the details for new user:")
        userid=int(input('Enter the userID:'))
        #checking whether ID already exists or not
        cur.execute("select * from user where userid={}".format(userid))
        if cur.fetchall()==[]:
            username=input("Enter the user name:")
            usertype=input("enter the user type (Admin/Customer)")
            password=input("enter the password:")
            dob=input("enter the date of birth (YYYY-MM-DD)")
            address= input("enter the address:")
            contactno= input("enter the contact number:")
            
            query="INSERT into user (userid,username,usertype,password,dob,address,contactno)VALUES ({},'{}','{}','{}','{}','{}','{}')".format(userid,username,usertype,password,dob,address,contactno)     
            cur.execute(query)
            mycon.commit()     #So that changes may take place
    
            #now selecting record	
            cur.execute("select * from user; ")
            data=cur.fetchall()
            for row in data:
                print(row)
        else:
            print("ID number already exists")
            mycon.close()
    else:
        print("MySQL Connection problem")
#main
while True:
    print("BEATIFIC AIRLINES")
    print("1.Login")
    print("2.Search")
    print("3.Sign Up")
    print("4.Exit")
    choice=int(input("Enter your choice..."))
    if choice==1:
        Login()       #calling login() function
    elif choice==2:
        Search_flight()
    elif choice==3:
        Sign_Up() 
    elif choice==4:
        break
    else:                          
        print("Invalid choice")


# In[ ]:




