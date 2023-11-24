import pymysql

con = pymysql.connect(host='localhost', user='root', password='Madman123')
cur = con.cursor()
cur.execute('drop database max')
cur.execute('create database if not exists max')
cur.execute('use max;')
cur.execute('''create table luxary_car(ID int NOT NULL 
AUTO_INCREMENT,Car varchar(60),Price varchar(20),Body_Type 
varchar(20) DEFAULT 'Sedan',Fuel_Type varchar(20),primary 
key(Car),UNIQUE KEY (ID));''')
cur.execute('''create table economy_car(ID int NOT NULL 
AUTO_INCREMENT,Car varchar(60),Price varchar(20),Body_Type 
varchar(20) DEFAULT 'Sedan',Fuel_Type varchar(20),primary 
key(Car),UNIQUE KEY (ID));''')
cur.execute('''create table registration(username char(30),email 
varchar(30),password varchar(30) ,confirm_password varchar(30));''')
cur.execute('''create table booking_details(customer_id int(10) ,car 
varchar(50),name varchar(20),ID_Proof varchar(20),city varchar(20),pincode 
varchar(20),address varchar(50),phone_no varchar(20),primary 
key(Customer_id));''')
cur.execute('''create table payment(Customer_id int(10) ,Name varchar(20), 
Payment_Method varchar(50),foreign key(Customer_id) references 
booking_details(Customer_id) on delete cascade)''')
con.commit()

print("DATABASE AND TABLES CREATED SUCCESSFULLY")
