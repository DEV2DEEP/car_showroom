
import tkinter as tk
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,ttk
import pymysql

class Login:
 
 def __init__(self,root): 
  self.root=root
  self.root.title("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒")
  """
  self.root.iconbitmap("Images/Icon.ico")
  """
  self.root.geometry("1536x796")
  self.root.state('zoomed')
  self.Login_UI()
  
 def Login_UI(self):     
  self.bg = ImageTk.PhotoImage(file = "Images/Login.png")
  bg = Label(self.root, image = self.bg).place(x = 0, y = 0, height = 796,width = 1536)
  """
  self.left = ImageTk.PhotoImage(file = "Images/Logo_Login.png")
  left = Label(self.root, image = self.left).place(x = 360, y = 180, height = 435, width = 435)

  """
  Login_Frame = Frame(self.root, bg = "#064663")
  Login_Frame.place(x = 900, y = 180, width = 350, height = 450)
  Title = Label(Login_Frame, text = "Sign In", font = ("Morgana Personal Use", 70), bg =  "#064663", fg = "#FFC04D").place(x = 30, y = 0)
  Username = Label(Login_Frame, text = "Username", font = ("Product Sans", 20, "bold"), bg ="#064663", fg = "#FEEE8C").place(x = 30, y = 110)
  self.Username = Entry (Login_Frame, font = ("Product Sans",20), bg = "#FFFEEA")
  self.Username.place(x = 30, y = 150, height = 35, width = 290)
  Password = Label(Login_Frame, text = "Password", font = ("Product Sans", 20, "bold"), bg ="#064663", fg = "#FEEE8C").place(x = 30, y = 200)
  self.Password = Entry (Login_Frame, font = ("Product Sans", 20), bg = "#FFFEEA", show ="*")
  self.Password.place(x = 30, y = 240, height = 35, width = 290)
  btn_register = Button(Login_Frame, text = "LOGIN",font = ("20th Century Font", 30), bd =5, bg = "#FFA500", cursor = 'hand2', relief = RIDGE, command = self.Login)
  btn_register.place(x = 100, y = 295, height = 50, width = 150)
 
  Title = Label(Login_Frame, text = "Don't Have an Account ?", font = ("Rooster Personal Use",15), bg = "#064663", fg = "#FEEE8C").place(x = 70, y = 350)
  btn_login = Button(self.root, text = "SIGN UP", font = ("20th Century Font", 20), bg = "#FFA500", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Register_UI)
  btn_login.place(x = 1020, y = 575, height = 40, width = 120)
 def Login(self):
 
  if self.Username.get() == "" and self.Password.get() == "" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒", "ᴇɴᴛᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ ᴀɴᴅ ᴘᴀꜱꜱᴡᴏʀᴅ",
   icon = "warning", parent = self.root)
  elif self.Username.get() == "" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒", "ᴇɴᴛᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ", icon = "warning",
   parent = self.root)
  elif self.Password.get() == "" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒", "ᴇɴᴛᴇʀ ᴘᴀꜱꜱᴡᴏʀᴅ", icon = "warning",
   parent = self.root)
  else:
 
   mycon=pymysql.connect(host="localhost",user="root",password="Madman123",database="max")
   cursor=mycon.cursor()
   cursor.execute("SELECT * FROM Registration WHERE Username = %s AND Password = %s", (self.Username.get(), self.Password.get()))
   row = cursor.fetchone()
   if row == None :
    messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒", "ɪɴᴠᴀʟɪᴅ ᴜꜱᴇʀɴᴀᴍᴇ / ᴘᴀꜱꜱᴡᴏʀᴅ",
    icon = "warning", parent = self.root)
   else :
    self.mainscreen()
    mycon.close()
   self.Login_Clear()
 
 def Register_UI(self):
 
  self.bg = ImageTk.PhotoImage(file = "Images/Register.jpg")
  BG = Label(self.root, image = self.bg, bg = "#FAA460").place(x = 0, y = 0, height = 796,width = 1536)
  """
  self.left = ImageTk.PhotoImage(file = "Images/Logo_Register.png")
  left = Label(self.root, image = self.left).place(x = 150, y = 25, height = 220, width = 390)
  """
  Registration_Frame=Frame(self.root, bg = "#064663")
  Registration_Frame.place(x = 150, y = 200, width = 390, height = 550)
  Title = Label(Registration_Frame, text = "Sign Up", font = ("Morgana Personal Use", 65), bg= "#064663", fg = "#FFC04D").place(x = 50, y = 0)
  Username = Label(Registration_Frame, text = "Username", font = ("Product Sans", 15,"bold"), bg = "#064663", fg = "#FEEE8C").place(x = 70, y = 100)
  self.Username = Entry (Registration_Frame, font = ("Product Sans", 15), bg = "#FFFEEA")
  self.Username.place(x = 70, y = 130, width = 250)
  Email = Label(Registration_Frame, text = "E-Mail", font = ("Product Sans", 15, "bold"), bg ="#064663", fg = "#FEEE8C").place(x = 70, y = 170)
  self.Email = Entry (Registration_Frame, font = ("Product Sans", 15), bg = "#FFFEEA")
  self.Email.place(x = 70, y = 200, width = 250)
  Password = Label(Registration_Frame, text = "Password", font = ("Product Sans", 15, "bold"),bg = "#064663", fg = "#FEEE8C").place(x = 70, y = 240)
  self.Password = Entry (Registration_Frame, font = ("Product Sans", 15), bg = "#FFFEEA", show = "*")
  self.Password.place(x = 70, y = 270, width = 250)
  ConfirmPassword = Label(Registration_Frame, text = "Confirm Password", font = ("Product Sans", 15, "bold"), bg = "#064663", fg = "#FEEE8C").place(x = 70, y = 310)
  self.ConfirmPassword = Entry (Registration_Frame, font = ("Product Sans", 15), bg = "#FFFEEA")
  self.ConfirmPassword.place(x = 70, y = 340, width = 250)
  btn_register = Button(Registration_Frame, text = "REGISTER",font = ("20th Century Font",23), bd = 5, bg = "#FFA500", cursor = 'hand2', relief = RIDGE, command = self.Register)
  btn_register.place(x = 110, y = 380, height = 50, width = 170)
 
  Title = Label(Registration_Frame, text = "Already Have An Account ?", font = ("Rooster Personal Use", 15), bg = "#064663", fg = "#FEEE8C").place(x = 83, y = 435)
  btn_login = Button(self.root, text = "SIGN IN", font = ("20th Century Font", 20), bg = "#FFA500", bd = 5, relief = RIDGE, cursor = "hand2", command = self.Login_UI)
  btn_login.place(x = 290, y = 680, height = 40, width = 115)
 
 def Register(self) :
  if self.Username.get() == "" or self.Email.get() == "" or self.Password.get() == "" or self.ConfirmPassword.get() == "":
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒", "ᴀʟʟ ꜰɪᴇʟᴅꜱ ᴀʀᴇ ʀᴇ🇶ᴜɪʀᴇᴅ", icon = "warning", parent = self.root)
  elif self.Password.get() != self.ConfirmPassword.get() :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒", "ᴄᴏɴꜰɪʀᴍ ᴘᴀꜱꜱᴡᴏʀᴅ ɪꜱ ᴅɪꜰꜰᴇʀᴇɴᴛ", icon = "warning", parent = self.root)
  else :
   mycon=pymysql.connect(host="localhost",user="root",password="Madman123",database="max")
   cursor=mycon.cursor()
   cursor.execute("SELECT * FROM Registration WHERE Username = %s", self.Username.get())
   Username = cursor.fetchone()
   cursor.execute("SELECT * FROM Registration WHERE Email = %s", self.Email.get())
   Email = cursor.fetchone()
  if Username != None :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒", "ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ ᴇxɪꜱᴛꜱ, ᴛʀʏ ᴏᴛʜᴇʀ ᴜꜱᴇʀɴᴀᴍᴇ", icon = "warning", parent = self.root)
  elif Email != None :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒", "ᴇᴍᴀɪʟ ᴀʟʀᴇᴀᴅʏ ᴇxɪꜱᴛꜱ, ᴛʀʏ ᴏᴛʜᴇʀ ᴇᴍᴀɪʟ", icon = "warning", parent = self.root)
  else :
   cursor.execute("INSERT INTO Registration ( Username, Email, Password,Confirm_Password) VALUES (%s,%s,%s,%s)",(self.Username.get(),self.Email.get(),self.Password.get(),self.ConfirmPassword.get()))
   messagebox.showinfo("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒", "ᴀᴄᴄᴏᴜɴᴛ ʜᴀꜱ ʙᴇᴇɴ ʀᴇɢɪꜱᴛᴇʀᴇᴅ")
   self.Register_Clear()
   mycon.commit()
   mycon.close()
 def mainscreen(self):
   Frame_login=Frame(self.root,bg="white")
   Frame_login.place(x=0,y=0,height=796,width=1536)

   self.img=ImageTk.PhotoImage(file="Images/Home_Background.png")
   img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1536,height=796)

   label1=Label(self.root,text="𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒",font=('Product Sans',60,'bold'),fg="#FFC04D",bg='#141414')
   label1.place(x=280,y=30)
   Logo_Frame = Frame(Frame_login, bd = 0, bg = "#FFFFFF")
   Logo_Frame.place(x = 170, y = 35, width = 100, height = 100)

   self.Logo = ImageTk.PhotoImage(file="Images/Logo.png")
   Logo = Label(Logo_Frame, image = self.Logo).place(x=0,y=0,height=100,width=100)
   
   Manage_Frame=Frame(Frame_login,bd=5,relief=GROOVE,bg="#FEEE8C")
   Manage_Frame.place(x=100,y=200,height=500,width=400)
   label=Label(Manage_Frame,text="𝕄𝕒𝕟𝕒𝕘𝕖 𝔹𝕠𝕠𝕜𝕚𝕟𝕘𝕤",font=('Product Sans',34,'bold'),fg="#021E2F",justify = CENTER,bg='#F99A05')
   label.place(x=0,y=0,width=388)
 
   label1=Label(Manage_Frame,text="Update Booking ",font=('Product Sans',25,'bold'),fg="#630000",justify = CENTER,bg='#FEEE8C')
   label1.place(x=0,y=80,width=388)
 
   btn1=Button(Manage_Frame,text="UPDATE",command=self.updates,cursor="hand2",font=("Product Sans",15,'bold'),fg="black",bg="#FFC04D",bd=0,width=10,height=1)
   btn1.place(x=135,y=130)

   label2=Label(Manage_Frame,text="Cancel Booking",font=('Product Sans',25,'bold'),justify = CENTER,fg="#630000",bg='#FEEE8C')
   label2.place(x=0,y=180,width=388)

   btn2=Button(Manage_Frame,text="CANCEL",command=self.delete,cursor="hand2",font=("Product Sans",15,'bold'),fg="black",bg="#FFC04D",bd=0,width=10,height=1)
   btn2.place(x=135,y=230)

   label3=Label(Manage_Frame,text="Show All Bookings",font=('Product Sans',25,'bold'),fg="#630000",justify = CENTER,bg='#FEEE8C')
   label3.place(x=0,y=280,width=388)
 
   btn3=Button(Manage_Frame,text="Luxary",command=self.Luxary,cursor="hand2",font=("Product Sans",15,'bold'),fg="black",bg="#FFC04D",bd=0,width=8,height=1)
   btn3.place(x=90,y=330)
 
   btn3=Button(Manage_Frame,text="Economy",command=self.Economy,cursor="hand2",font=("Product Sans",15,'bold'),fg="black",bg="#FFC04D",bd=0,width=8,height=1)
   btn3.place(x=200,y=330)
 
   label4=Label(Manage_Frame,text="Customer ID ",font=('Product Sans',25,'bold'),fg="#630000",justify = CENTER,bg='#FEEE8C')
   label4.place(x=0,y=380,width=388)
 
   btn4=Button(Manage_Frame,text="SEARCH",command=self.Search,cursor="hand2",font=("Product Sans",15,'bold'),fg="#000000",bg="#FFC04D",bd=0,width=10,height=1)
   btn4.place(x=135,y=430)
 
   New_Frame=Frame(Frame_login,bd=5,relief=GROOVE,bg="#FEEE8C")
   New_Frame.place(x=525,y=200,height=500,width=400)
   label=Label(New_Frame,text="𝔸𝕣𝕣𝕚𝕧𝕚𝕟𝕘 𝕊𝕠𝕠𝕟 !",font=('Product Sans',32,'bold'),fg="#021E2F",justify = CENTER,bg='#F99A05')
   label.place(x=0,y=0,width=388)

   self.img1=ImageTk.PhotoImage(file="Images/New_Car.png")
   img2=Label(self.root,image=self.img1).place(x=530,y=270,width=388,height=250)

   label1=Label(New_Frame,text="Bugatti Veyron",font=('Product Sans',20,'bold'),fg="#021E2F",relief=RIDGE,bg='#FFC04D')
   label1.place(x=0,y=321,width=388)
   Specs=Label(New_Frame,text=" Price : ₹12.00 Cr\tTop Speed : 407 km/hr \n"
                              " Engine : 7993 cc\tBody Type : Convertible \n Fuel Type : Petrol\tMileage : 6.8 km/l \n "
                              "Transmission Type : Automatic \n Boot Spaces : 37 litres",font=('Product Sans',14),fg="#021E2F",relief=RIDGE,bg='#FFC04D')
   Specs.place(x=0,y=363,width=388)
   Bookings_Frame=Frame(Frame_login,bd=5,relief=GROOVE,bg="#FEEE8C")
   Bookings_Frame.place(x=1150,y=450,height=250,width=300)
   label3=Label(Bookings_Frame,text="ℂ𝕒𝕣 𝔹𝕠𝕠𝕜𝕚𝕟𝕘𝕤",font=('Product Sans',32,'bold'),fg="#021E2F",justify = CENTER,bg='#F99A05')
   label3.place(x=0,y=0,width=288)
 
   label4=Label(Bookings_Frame,text="Luxary Cars",font=('Product Sans',25,'bold'),fg="#021E2F",justify = CENTER,bg='#FEEE8C')
   label4.place(x=0,y=60,width=288)
   btn5=Button(Bookings_Frame,text="Book Now",command=self.Luxary_Booking_Details,cursor="hand2",font=("Product Sans",15,'bold'),fg="#000000",bg="#FFC04D",bd=0,width=8,height=1)
   btn5.place(x=100,y=110)
 
   label5=Label(Bookings_Frame,text="Economy Cars",font=('Product Sans',25,'bold'),fg="#021E2F",justify = CENTER,bg='#FEEE8C')
   label5.place(x=0,y=150,width=288)
   btn6=Button(Bookings_Frame,text="Book Now",command=self.Economy_Booking_Details,cursor="hand2",font=("Product Sans",15,'bold'),fg="#000000",bg="#FFC04D",bd=0,width=8,height=1)
   btn6.place(x=100,y=195)
   btn=Button(Frame_login,text="Sign Out",command=self.Login_UI,cursor="hand2",font=("Product Sans",16),fg="#000000",bg="#F99A05",bd=0,width=8,height=1)
   btn.place(x=1400,y=725)
   Add=Frame(Frame_login,bd=5,relief=GROOVE,bg="#FEEE8C")
   Add.place(x=950,y=500,height=200,width=170)
   lab=Label(Add,text="𝔸𝕕𝕕 ℂ𝕒𝕣",font=('Product Sans',26),fg="#021E2F",justify = CENTER,bg='#F99A05')
   lab.place(x=0,y=0,height=50,width=158)
   label=Label(Add,text="Luxary Car",font=('Product Sans',15,'bold'),fg="#021E2F",justify = CENTER,bg='#FEEE8C')
   label.place(x=0,y=55,width=158)
   btn=Button(Add,text="ADD",command=self.add_luxary,cursor="hand2",font=("Product Sans",13,'bold'),fg="#000000",bg="#FFC04D",bd=0,width=8,height=1)
   btn.place(x=35,y=85)
   label1=Label(Add,text="Economy Car",font=('Product Sans',15,'bold'),fg="#021E2F",justify = CENTER,bg='#FEEE8C')
   label1.place(x=0,y=120,width=158)
   btn1=Button(Add,text="ADD",command=self.add_economy,cursor="hand2",font=("Product Sans",13,'bold'),fg="#000000",bg="#FFC04D",bd=0,width=8,height=1)
   btn1.place(x=35,y=150)
   delete=Frame(Frame_login,bd=5,relief=GROOVE,bg="#FEEE8C")
   delete.place(x=950,y=200,height=200,width=170)
   lab=Label(delete,text="ℝ𝕖𝕞𝕠𝕧𝕖 ℂ𝕒𝕣",font=('Product Sans',20),fg="#021E2F",justify = CENTER,bg='#F99A05')
   lab.place(x=0,y=0,height=50,width=158)
   label=Label(delete,text="Luxary Car",font=('Product Sans',15,'bold'),fg="#021E2F",justify = CENTER,bg='#FEEE8C')
   label.place(x=0,y=55,width=158)
 
   btn=Button(delete,text="Remove",command=self.delete_luxary,cursor="hand2",font=("Product Sans",13,'bold'),fg="#000000",bg="#FFC04D",bd=0,width=8,height=1)
   btn.place(x=35,y=85)
   label1=Label(delete,text="Economy Car",font=('Product Sans',15,'bold'),fg="#021E2F",justify = CENTER,bg='#FEEE8C')
   label1.place(x=0,y=120,width=158)

   btn1=Button(delete,text="Remove",command=self.delete_economy,cursor="hand2",font=("Product Sans",13,'bold'),fg="#000000",bg="#FFC04D",bd=0,width=8,height=1)
   btn1.place(x=35,y=150)
   dev=Frame(Frame_login,bd=5,relief=GROOVE,bg="#FEEE8C")
   dev.place(x=500,y=720,height=50,width=450)
   lab=Label(dev,text="𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕣 - 𝔻𝕖𝕖𝕡𝕖𝕟𝕕𝕣𝕒",font=('Product Sans',25,'bold'),fg="#021E2F",justify = CENTER,bg='#F99A05')
   lab.place(x=0,y=0,height=38,width=438)
   car=Frame(Frame_login,bd=5,relief=GROOVE,bg="#FEEE8C")
   car.place(x=950,y=410,height=80,width=170)
   lab=Label(car,text="WELCOME TO \n RECEPTOR \n CARSHOWROOM",font=('Product Sans',12,'bold'),fg="#021E2F",justify = CENTER,bg='#F99A05')
   lab.place(x=0,y=0,height=68,width=158)
 def delete_luxary(self):
  delete_luxary = tk.Tk()
  delete_luxary.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  delete_luxary.iconbitmap("Images/Icon.ico")
  """
  app_width = 400
  app_height = 250
  screen_width = delete_luxary.winfo_screenwidth()
  screen_height = delete_luxary.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  delete_luxary.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  delete_luxary.resizable(0,0)
  Frame_bookcar=Frame(delete_luxary,bg="#064663")
  Frame_bookcar.place(x=0,y=0,height=250,width=400)
  label=Label(Frame_bookcar,text="Luxary Car",font=('Product Sans',30,'bold'),fg="#021E2F",justify = CENTER,bg='#FEEE8C')
  label.place(x=90,y=10)
 
  label1=Label(Frame_bookcar,text="Car ID",font=('Product Sans',26,'bold'),fg="#FEEE8C",bg='#064663')
  label1.place(x=145,y=70)
 
  self.car_name=Entry(Frame_bookcar,font=("Product Sans",20,"bold"),justify='center',bg='#FFFEEA')
  self.car_name.place(x=80,y=130,width=250,height=35)
 
  btn=Button(Frame_bookcar,command=self.del_luxary,text="Remove Car",cursor="hand2",font=("Product Sans",17,'bold'),fg="#000000",bg="#F99A05",bd=0,width=10,height=1)
  btn.place(x=135,y=180)
  delete_luxary.mainloop()

 def del_luxary(self):
  if self.car_name.get()=="" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","All fields are required",parent=self.root)
  else:
   try:
    con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
    cur=con.cursor()
    cur.execute('Select car from luxary_car where id=%s',(self.car_name.get()))
    row=cur.fetchone()
    if row==None:
     messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒','No such car!',parent=self.root)
     self.car_name.focus()
    else:
     con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
     cur=con.cursor()
     cur.execute("Delete from luxary_car where id=%s",(self.car_name.get()))
     con.commit()
     messagebox.showinfo("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Your Car Has Been Removed From The Table!*",parent=self.root)
     con.close()
   except Exception as es:
    messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒',f'Error Due to : {str(es)}',parent=self.root)
 
 def delete_economy(self):
  delete_economy = tk.Tk()
  delete_economy.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  delete_economy.iconbitmap("Images/Icon.ico")
  """
  app_width = 400
  app_height = 250
  screen_width = delete_economy.winfo_screenwidth()
  screen_height = delete_economy.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  delete_economy.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  delete_economy.resizable(0,0)
  Frame_bookcar=Frame(delete_economy,bg="#064663")
  Frame_bookcar.place(x=0,y=0,height=250,width=400)
  label=Label(Frame_bookcar,text="Economy Car",font=('Product Sans',30,'bold'),fg="#021E2F",justify = CENTER,bg='#FEEE8C')
  label.place(x=75,y=10)
 
  label1=Label(Frame_bookcar,text="Car ID",font=('Product Sans',30,'bold'),fg="#FEEE8C",bg='#064663')
  label1.place(x=135,y=70)
 
  self.car_name=Entry(Frame_bookcar,font=("Product Sans",20,"bold"),justify='center',bg='#FFFEEA')
  self.car_name.place(x=80,y=130,width=250,height=35)
 
  btn=Button(Frame_bookcar,command=self.del_economy,text="Remove Car",cursor="hand2",font=("Product Sans",17,'bold'),fg="#000000",bg="#F99A05",bd=0,width=10,height=1)
  btn.place(x=135,y=180)
  delete_economy.mainloop()
 
 def del_economy(self):
  if self.car_name.get()=="" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","All fields are required",parent=self.root)
  else:
   try:
    con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
    cur=con.cursor()
    cur.execute('Select car from economy_car where id=%s',(self.car_name.get()))
    row=cur.fetchone()
    if row==None:
     messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒','No such car!',parent=self.root)
     self.car_name.focus()
    else:
     con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
     cur=con.cursor()
     cur.execute("Delete from economy_car where id=%s",(self.car_name.get()))
     con.commit()
     messagebox.showinfo("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Your Car Has Been Removed From The Table!*",parent=self.root)
     con.close()
   except Exception as es:
    messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒',f'Error Due to : {str(es)}',parent=self.root)
 def add_luxary(self):
  Add_Luxary = tk.Tk()
  Add_Luxary.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  Add_Luxary.iconbitmap("Images/Icon.ico")
  """
  app_width = 350
  app_height = 350
  screen_width = Add_Luxary.winfo_screenwidth()
  screen_height = Add_Luxary.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  Add_Luxary.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  Add_Luxary.resizable(0,0)
  Frame_add=Frame(Add_Luxary,bg='#064663')
  Frame_add.place(x=0,y=0,height=500,width=350)
 
  label5=Label(Frame_add,text="Add Luxary Car",font=('Product Sans',27,'bold'),fg="#021E2F",justify = CENTER,bg='#F99A05')
  label5.place(x=45,y=0)
 
  label=Label(Frame_add,text="Car Name",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label.place(x=0,y=50,width=350,height=35)
  self.car_name=Entry(Frame_add,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.car_name.place(x=50,y=80,width=250,height=25)

  label1=Label(Frame_add,text="Car Price",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label1.place(x=0,y=105,width=350,height=25)
  self.price=Entry(Frame_add,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.price.place(x=50,y=130,width=250,height=25)
 
  label2=Label(Frame_add,text="Body Type",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label2.place(x=0,y=155,width=350)
  ty_var = StringVar()
  self.type= ttk.Combobox(Frame_add, font=("Product Sans", 14),width=250,textvariable=ty_var,justify=CENTER,state="readonly")
  self.type['values'] = ('Coupe','SUV','Hatchback','Sedan')
  self.type.place(x=50,y=180,width=250,height=25)
  self.type.set("Select Body Type")
 
  label3=Label(Frame_add,text="Fuel Type",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label3.place(x=0,y=205,width=350)
  fu_var = StringVar()
  self.fuel=ttk.Combobox(Frame_add, font=("Product Sans", 14),width=250, textvariable=fu_var,justify=CENTER,state="readonly")
  self.fuel['values'] = ('Diesel','Petrol','Petrol & Diesel')
  self.fuel.place(x=50,y=230,width=250,height=25)
  self.fuel.set("Select Fuel Type")

  btn=Button(Frame_add,command=self.add_lux,text="ADD CAR",cursor="hand2",font=("Product Sans",15,'bold'),fg="#000000",bg="#F99A05",bd=0,width=8,height=1)
  btn.place(x=125,y=280)
  Add_Luxary.mainloop()
 def add_lux(self):
  if self.car_name.get()=="" or self.price.get()=="" or self.type.get()=="Select Body Type" or self.fuel.get()=="Select Fuel Type" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","All fields are required",parent=self.root)
  else:
   try:
    con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
    cur=con.cursor()
    cur.execute("select car from luxary_car where car=%s",self.car_name.get())
    row=cur.fetchone()
    if row != None:
     messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Car Name Already Exist!",parent=self.root)
     self.car_name.focus()
    else:
     con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
     cur=con.cursor()
     cur.execute("insert into luxary_car (car,price,Body_Type,Fuel_Type) values(%s,%s,%s,%s)",(self.car_name.get(),self.price.get(),self.type.get(),self.fuel.get()))

     con.commit()
     messagebox.showinfo("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Car Added Succesfully ",parent=self.root)

     self.mainscreen()
   except Exception as es:
    messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒',f'Error Due to : {str(es)}',parent=self.root)
 def add_economy(self):
  Add_Economy = tk.Tk()
  Add_Economy.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  Add_Economy.iconbitmap("Images/Icon.ico")
  """
  app_width = 350
  app_height = 350
  screen_width = Add_Economy.winfo_screenwidth()
  screen_height = Add_Economy.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  Add_Economy.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  Add_Economy.resizable(0,0)
  Frame_add=Frame(Add_Economy,bg='#064663')
  Frame_add.place(x=0,y=0,height=500,width=350)
 
  label5=Label(Frame_add,text="Add Economy Car",font=('Product Sans',27,'bold'),fg="#021E2F",justify = CENTER,bg='#F99A05')
  label5.place(x=25,y=0)

  label=Label(Frame_add,text="Car Name",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label.place(x=0,y=50,width=350,height=35)
  self.car_name=Entry(Frame_add,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.car_name.place(x=50,y=80,width=250,height=25)
 
  label1=Label(Frame_add,text="Car Price",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label1.place(x=0,y=105,width=350,height=25)
  self.price=Entry(Frame_add,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.price.place(x=50,y=130,width=250,height=25)
 
  label2=Label(Frame_add,text="Body Type",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label2.place(x=0,y=155,width=350)
  ty_var = StringVar()
  self.type= ttk.Combobox(Frame_add, font=("Product Sans", 14),width=250,textvariable=ty_var,justify=CENTER,state="readonly")
  self.type['values'] = ('Coupe','SUV','Hatchback','Sedan')
  self.type.place(x=50,y=180,width=250,height=25)
  self.type.set("Select Body Type")
 
  label3=Label(Frame_add,text="Fuel Type",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label3.place(x=0,y=205,width=350)
  fu_var = StringVar()
  self.fuel=ttk.Combobox(Frame_add, font=("Product Sans", 14),width=250,textvariable=fu_var,justify=CENTER,state="readonly")
  self.fuel['values'] = ('Diesel','Petrol','Petrol & Diesel')
  self.fuel.place(x=50,y=230,width=250,height=25)
  self.fuel.set("Select Fuel Type")

  btn = Button(Frame_add, command=self.add_eco, text="ADD CAR",cursor="hand2",font=("Product Sans",15,'bold'),fg="#000000",bg="#F99A05",bd=0,width=8,height=1)
  btn.place(x=125,y=280)
  Add_Economy.mainloop()
 def add_eco(self):
  if self.car_name.get()=="" or self.price.get()=="" or self.type.get()=="Select Body Type" or self.fuel.get()=="Select Fuel Type" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","All fields are required",parent=self.root)
  else:
   try:
     con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
     cur=con.cursor()
     cur.execute("select car from economy_car where car=%s",self.car_name.get())
     row=cur.fetchone()
     if row!=None:
       messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Car Name Already Exist!",parent=self.root)
       self.car_name.focus()
     else:
      con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
      cur=con.cursor()
      cur.execute("insert into economy_car (car,price, Body_Type,Fuel_Type) values(%s,%s,%s,%s)",(self.car_name.get(),self.price.get(),self.type.get(),self.fuel.get()))
      con.commit()
      messagebox.showinfo("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Car Added Succesfully ",parent=self.root)
      self.mainscreen()
   except Exception as es:
    messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒',f'Error Due to : {str(es)}',parent=self.root)
 
 
 
 def Luxary_Booking_Details(self):
  con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
  cur=con.cursor()
  options = []
  cur.execute("select car from luxary_car")
  car = cur.fetchall()
  for i in car:
   options.append(str(i[0]))

  car = StringVar()
  Luxary = tk.Tk()
  Luxary.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  Luxary.iconbitmap("Images/Icon.ico")
  """
  app_width = 1000
  app_height = 500
  screen_width = Luxary.winfo_screenwidth()
  screen_height = Luxary.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  Luxary.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  Luxary.resizable(0,0)
  Frame_bookcar=Frame(Luxary,bg='#064663')
  Frame_bookcar.place(x=0,y=0,height=500,width=350)
 
  label=Label(Frame_bookcar,text="Customer ID",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label.place(x=0,y=0,width=350,height=35)
  self.customer_id=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.customer_id.place(x=50,y=30,width=250,height=25)
 
  label1=Label(Frame_bookcar,text="Name",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label1.place(x=0,y=55,width=350,height=25)
  self.name=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.name.place(x=50,y=80,width=250,height=25)
 
  label2=Label(Frame_bookcar,text="Phone No.",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label2.place(x=0,y=105,width=350)
  self.phone_no=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.phone_no.place(x=50,y=130,width=250,height=25)
 
  label3=Label(Frame_bookcar,text="Pincode",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label3.place(x=0,y=155,width=350)
  self.pincode=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.pincode.place(x=50,y=180,width=250,height=25)
 
  label4=Label(Frame_bookcar,text="Address",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label4.place(x=0,y=205,width=350)
  self.address=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.address.place(x=50,y=230,width=250,height=25)
 
  label5=Label(Frame_bookcar,text="Car",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label5.place(x=0,y=255,width=350)
  lux_var = StringVar()
  self.combocar = ttk.Combobox(Frame_bookcar, font=("Product Sans",14),values=options,width=250, textvariable=lux_var,justify=CENTER,state="readonly")
  self.combocar.place(x=50,y=280,width=250,height=25)
  self.combocar.set("Select Car")
 
  label6=Label(Frame_bookcar,text="Photo ID Proof",font=('Product Sans',15,'bold'),fg="#FEEE8C",bg='#064663')
  label6.place(x=0,y=355,width=350)
  id_var = StringVar()
  self.id_proof = ttk.Combobox(Frame_bookcar, font=("Product Sans", 14),width=250,textvariable=id_var,justify=CENTER,state="readonly")
  self.id_proof['values'] = ('Aadhar Card','Driving License','PAN Card','Passport','Pension Passbook','Voter ID')
  self.id_proof.place(x=50,y=380,width=250,height=25)
  self.id_proof.set("Select ID Proof")
 
  label7=Label(Frame_bookcar,text="City",font=('Product Sans',15,'bold'),fg="#FEEE8C",bg='#064663')
  label7.place(x=0,y=305,width=350)
  self.city=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.city.place(x=50,y=332,width=250,height=25)
 
  btn=Button(Frame_bookcar,command=self.detail,text="Book Now",cursor="hand2",font=("Product Sans",15,'bold'),fg="#000000",bg="#F99A05",bd=0,width=8,height=1)
  btn.place(x=125,y=420)
  label8=Label(Frame_bookcar,justify=CENTER,text="Remember Your Customer ID For Payment Process.",font=('Product Sans',11,'bold'),fg="#F99A05",bg='#FFFEEA')
  label8.place(x=0,y=475,width=350)
 
  Luxary_Frame = Frame(Luxary, bd = 0, bg = "#95D1CC" )
  Luxary_Frame.place(x = 351, y = 0, width = 650, height = 500)
  s= ttk.Style(Luxary)
  s.theme_use("clam")
  s.configure(".", font=('Product Sans', 10), bg = "#FFDEAD")
  s.configure("Display_Table.Heading", fg = "#630000", font = ('Product Sans', 20))
  scroll_y = Scrollbar(Luxary_Frame, orient = VERTICAL)
  self.Luxary_Table = ttk.Treeview(Luxary_Frame, columns = ("ID","Car","Price","Body_Type","Fuel_Type"), yscrollcommand = scroll_y.set)
  scroll_y.pack(side = RIGHT, fill = Y)
  scroll_y.config(command = self.Luxary_Table.yview)
  self.Luxary_Table.heading("ID",text="ID",anchor=tk.CENTER)
  self.Luxary_Table.heading("Car",text="Car Name",anchor=tk.CENTER)
  self.Luxary_Table.heading("Price",text="Price",anchor=tk.CENTER)
  self.Luxary_Table.heading("Body_Type",text="Body Type",anchor=tk.CENTER)
  self.Luxary_Table.heading("Fuel_Type",text="Fuel Type",anchor=tk.CENTER)
  self.Luxary_Table['show']="headings"

  self.Luxary_Table.column("ID",width=50,anchor=tk.CENTER)
  self.Luxary_Table.column("Car",width=150,anchor=tk.CENTER)
  self.Luxary_Table.column("Price",width=50,anchor=tk.CENTER)
  self.Luxary_Table.column("Body_Type",width=70,anchor=tk.CENTER)
  self.Luxary_Table.column("Fuel_Type",width=90,anchor=tk.CENTER)
  self.Luxary_Table.pack(fill = BOTH, expand = 1)
  self.Luxary_Table.bind("<ButtonRelease-1>")
  self.Luxary_Data()

 def Luxary_Data(self) :
  mycon=pymysql.connect(host = "localhost", user = "root", password = "Madman123", database = "max")
  cursor=mycon.cursor()
  cursor.execute("SELECT * FROM Luxary_Car")
  rows = cursor.fetchall()
  if len(rows) != 0 :
   self.Luxary_Table.delete(*self.Luxary_Table.get_children())
  for row in rows :
   self.Luxary_Table.insert('', END, values = row)
   mycon.commit()
   mycon.close()
 def detail(self):
  if self.customer_id.get()=="" or self.combocar.get()=="Select Car" or self.city.get()=="" or self.id_proof.get()=="Select ID Proof" or self.name.get()=="" or self.address.get()=="" or self.pincode.get()=="" or self.phone_no.get()=="" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","All fields are required",parent=self.root)
  else:
   try:
     con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
     cur=con.cursor()
     cur.execute("select Customer_id from booking_details where Customer_id=%s",self.customer_id.get())
     row=cur.fetchone()
     if row!=None:
      messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Please try with new Customer ID!",parent=self.root)
      self.customer_id.focus()
     else:
       con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
       cur=con.cursor()
       cur.execute("insert into booking_details values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.customer_id.get(),self.combocar.get(),self.name.get()
                                                                             ,self.id_proof.get(),self.city.get(),self.pincode.get(),
                                                                             self.address.get(),self.phone_no.get()))
       con.commit()
       self.payment()
 
   except Exception as es:
    messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒',f'Error Due to : {str(es)}',parent=self.root)
 
 def Economy_Booking_Details(self):
  con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
  cur=con.cursor()
  options = []
  cur.execute("select car from economy_car")
  car = cur.fetchall()
  for i in car:
   options.append(str(i[0]))
 
  Economy = tk.Tk()
  Economy.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  Economy.iconbitmap("Images/Icon.ico")
  """
  app_width = 1000
  app_height = 500
  screen_width = Economy.winfo_screenwidth()
  screen_height = Economy.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  Economy.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  Economy.resizable(0,0)
  Frame_bookcar=Frame(Economy,bg='#064663')
  Frame_bookcar.place(x=0,y=0,height=500,width=350)
 
  label1=Label(Frame_bookcar,text="Customer ID",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label1.place(x=0,y=0,width=350,height=35)
  self.customer_id=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.customer_id.place(x=50,y=30,width=250,height=25)
 
  label2=Label(Frame_bookcar,text="Name",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label2.place(x=0,y=55,width=350,height=25)
  self.name=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.name.place(x=50,y=80,width=250,height=25)
 
  label3=Label(Frame_bookcar,text="Phone No.",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label3.place(x=0,y=105,width=350)
  self.phone_no=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.phone_no.place(x=50,y=130,width=250,height=25)
 
  label4=Label(Frame_bookcar,text="Pincode",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label4.place(x=0,y=155,width=350)
  self.pincode=Entry(Frame_bookcar,font=("Product Sans",15,"bold"), justify='center',bg='#FFFEEA')
  self.pincode.place(x=50,y=180,width=250,height=25)
 
  label5=Label(Frame_bookcar,text="Address",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label5.place(x=0,y=205,width=350)
  self.address=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.address.place(x=50,y=230,width=250,height=25)
 
  label6=Label(Frame_bookcar,text="Car",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label6.place(x=0,y=255,width=350)
  eco_var = StringVar()
  self.combocar = ttk.Combobox(Frame_bookcar, font=("Product Sans",14),values=options,width=250, textvariable=eco_var,justify=CENTER,state="readonly")
  self.combocar.place(x=50,y=280,width=250,height=25)
  self.combocar.set("Select Car")
 
  label7=Label(Frame_bookcar,text="Photo ID Proof",font=('Product Sans',15,'bold'),fg="#FEEE8C",bg='#064663')
  label7.place(x=0,y=355,width=350)
  id_var = StringVar()
  self.id_proof = ttk.Combobox(Frame_bookcar, font=("Product Sans", 14),width=250,textvariable=id_var,justify=CENTER,state="readonly")
  self.id_proof['values'] = ('Aadhar Card','Driving License','PAN Card','Passport','Pension Passbook','Voter ID')
  self.id_proof.place(x=50,y=380,width=250,height=25)
  self.id_proof.set("Select ID Proof")
 
  label8=Label(Frame_bookcar,text="City",font=('Product Sans',15,'bold'),fg="#FEEE8C",bg='#064663')
  label8.place(x=0,y=305,width=350)
  self.city=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.city.place(x=50,y=332,width=250,height=25)
  btn=Button(Frame_bookcar,command=self.detail,text="Book Now",cursor="hand2",font=("Product Sans",15,'bold'),fg="#000000",bg="#F99A05",bd=0,width=8,height=1)
  btn.place(x=125,y=420)
  label9=Label(Frame_bookcar,justify=CENTER,text="Remember Your Customer ID For Payment Process.",font=('Product Sans',11,'bold'),fg="#F99A05",bg='#FFFEEA')
  label9.place(x=0,y=475,width=350)
 
  Economy_Frame = Frame(Economy, bd = 0, bg = "#95D1CC" )
  Economy_Frame.place(x = 351, y = 0, width = 650, height = 500)
  s= ttk.Style(Economy)
  s.theme_use("clam")
  s.configure(".", font=('Product Sans', 10), bg = "#FFDEAD")
  s.configure("Display_Table.Heading", fg = "#630000", font = ('Product Sans', 20))
  scroll_y = Scrollbar(Economy_Frame, orient = VERTICAL)
  self.Economy_Table = ttk.Treeview(Economy_Frame, columns = ("ID","Car","Price","Body_Type","Fuel_Type"), yscrollcommand = scroll_y.set)
  scroll_y.pack(side = RIGHT, fill = Y)
  scroll_y.config(command = self.Economy_Table.yview)
  self.Economy_Table.heading("ID",text="ID",anchor=tk.CENTER)
  self.Economy_Table.heading("Car",text="Car Name",anchor=tk.CENTER)
  self.Economy_Table.heading("Price",text="Price",anchor=tk.CENTER)
  self.Economy_Table.heading("Body_Type",text="Body Type",anchor=tk.CENTER)
  self.Economy_Table.heading("Fuel_Type",text="Fuel Type",anchor=tk.CENTER)
  self.Economy_Table['show']="headings"
  self.Economy_Table.column("ID",width=50,anchor=tk.CENTER)
  self.Economy_Table.column("Car",width=150,anchor=tk.CENTER)
  self.Economy_Table.column("Price",width=50,anchor=tk.CENTER)
  self.Economy_Table.column("Body_Type",width=70,anchor=tk.CENTER)
  self.Economy_Table.column("Fuel_Type",width=90,anchor=tk.CENTER)
  self.Economy_Table.pack(fill = BOTH, expand = 1)
  self.Economy_Table.bind("<ButtonRelease-1>")
  self.Economy_Data()
 def Economy_Data(self) :
  mycon = pymysql.connect(host = "localhost", user = "root", password = "Madman123", database = "max")
  cursor = mycon.cursor()
  cursor.execute("SELECT * FROM Economy_Car")
  rows = cursor.fetchall()
  if len(rows) != 0 :
   self.Economy_Table.delete(*self.Economy_Table.get_children())
   for row in rows :
     self.Economy_Table.insert('', END, values = row)
     mycon.commit()
     mycon.close()
 def updates(self):
  update = tk.Tk()
  update.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  update.iconbitmap("Images/Icon.ico")
  """
  app_width = 350
  app_height = 430
  screen_width = update.winfo_screenwidth()
  screen_height = update.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  update.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  update.resizable(0,0)
  Frame_bookcar=Frame(update,bg='#064663')
  Frame_bookcar.place(x=0,y=0,height=430,width=350)
  label1=Label(Frame_bookcar,text="Customer ID",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label1.place(x=0,y=0,width=350,height=35)
  self.customer_id=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.customer_id.place(x=50,y=30,width=250,height=25)
 
  label2=Label(Frame_bookcar,text="Name",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label2.place(x=0,y=55,width=350,height=25)
  self.name=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.name.place(x=50,y=80,width=250,height=25)
 
  label3=Label(Frame_bookcar,text="Phone No.",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label3.place(x=0,y=105,width=350)
  self.phone_no=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.phone_no.place(x=50,y=130,width=250,height=25)
 
  label4=Label(Frame_bookcar,text="Pincode",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label4.place(x=0,y=155,width=350)
  self.pincode=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.pincode.place(x=50,y=180,width=250,height=25)

  label5=Label(Frame_bookcar,text="Address",font=('Product Sans',15,'bold'),fg="#FEEE8C",justify=CENTER,bg='#064663')
  label5.place(x=0,y=205,width=350)
  self.address=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.address.place(x=50,y=230,width=250,height=25)
  label6=Label(Frame_bookcar,text="City",font=('Product Sans',15,'bold'),fg="#FEEE8C",bg='#064663')
  label6.place(x=0,y=255,width=350)
  self.city=Entry(Frame_bookcar,font=("Product Sans",15,"bold"),justify='center',bg='#FFFEEA')
  self.city.place(x=50,y=280,width=250,height=25)
  label7=Label(Frame_bookcar,text="ID PROOF",font=('Product Sans',15,'bold'),fg="#FEEE8C",bg='#064663')
  label7.place(x=0,y=305,width=350)
  id_var = StringVar()
  self.id_proof = ttk.Combobox(Frame_bookcar, font=("Product Sans", 14),width=250, textvariable=id_var,justify=CENTER,state="readonly")
  self.id_proof['values'] = ('Aadhar Card','Driving License','PAN Card','Passport','Pension Passbook','Voter ID')
  self.id_proof.place(x=50,y=332,width=250,height=25)
  self.id_proof.set("Select ID Proof")
  btn=Button(Frame_bookcar,command=self.update,text="UPDATE",cursor="hand2",font=("Product Sans",15,'bold'),fg="#000000",bg="#F99A05",bd=0,width=8,height=1)
  btn.place(x=125,y=370)
  update.mainloop()
 def update(self):
  if self.customer_id.get()=="" or self.city.get()=="" or self.name.get()=="" or self.id_proof.get()=="Select ID Proof" or self.address.get()=="" or self.pincode.get()=="" or self.phone_no.get()=="" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","All fields are required",parent=self.root)
  else:
   try:
    con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
    cur=con.cursor()
    cur.execute('Select Customer_ID from booking_details where Customer_ID=%s',(self.customer_id.get()))
    row=cur.fetchone()
    if row==None:
     messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒','No such booking',parent=self.root)
     self.customer_id.focus()
     self.rg()
    else:
     con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
     cur=con.cursor()
     cur.execute("update booking_details set name= %s ,city = %s ,address= %s , id_proof = %s ,pincode= %s ,phone_no= %s where Customer_id= %s ",
                 (self.name.get(),self.city.get(),self.address.get(),self.id_proof.get(),self.pincode.get(),
                  self.phone_no.get(),self.customer_id.get()))
     con.commit()
     messagebox.showinfo("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Car Succesfully Updated",parent=self.root)
     self.mainscreen()
     con.close()
   except Exception as es:
    messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒',f'Error Due to : {str(es)}',parent=self.root)
 
 def payment(self):
  payment = tk.Tk()
  payment.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  payment.iconbitmap("Images/Icon.ico")
  """
  app_width = 400
  app_height = 325
  screen_width = payment.winfo_screenwidth()
  screen_height = payment.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  payment.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  payment.resizable(0,0)
  Frame_pay=Frame(payment,bg="#064663")
  Frame_pay.place(x=0,y=0,height=350,width=400)
 
  label1=Label(Frame_pay,text="Payment Method",font=('Product Sans',25,'bold'),fg="#FEEE8C",bg='#064663')
  label1.place(x=0,y=15,width=400)
  pay=StringVar()
  self.combopay = ttk.Combobox(Frame_pay, font=("Product Sans",16),textvariable=pay,justify=CENTER,state="readonly")
  self.combopay['values'] = ("Internet Banking","Credit Card","Debit Card","UPI","PayTm")
  self.combopay.place(x=75,y=60,width=250,height=35)
  self.combopay.set("Select Payment Method")
 
  label2=Label(Frame_pay,text="Name",font=('Product Sans',25,'bold'),fg="#FEEE8C",bg='#064663')
  label2.place(x=0,y=90,width=400)
  self.name=Entry(Frame_pay,font=("Product Sans",20,"bold"),bg='#FFFEEA')
  self.name.place(x=75,y=135,width=250,height=30)
 
  label3=Label(Frame_pay,text="Customer_ID",font=('Product Sans',25,'bold'),fg="#FEEE8C",bg='#064663')
  label3.place(x=0,y=165,width=400)
  self.customer_id=Entry(Frame_pay,font=("Product Sans",17,"bold"),bg='#FFFEEA')
  self.customer_id.place(x=75,y=210,width=250,height=30)
 
  btn=Button(Frame_pay,command=self.payments,text="PAY",cursor="hand2",font=("Product Sans",16,'bold'),fg="#000000",bg="#F99A05",bd=0,width=6,height=1)
  btn.place(x=160,y=260)
  payment.mainloop()
 def payments(self):
  if self.customer_id.get()=="" or self.name.get()=="" or self.combopay.get()=="Select Payment Method" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","All fields are required",parent=self.root)
  else:
   try:
    con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
    cur=con.cursor()
    cur.execute("select Customer_id from booking_details where Customer_id=%s",self.customer_id.get())
    row=cur.fetchone()
    if row!=None:
     con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
     cur=con.cursor()
     cur.execute("insert into payment values(%s,%s,%s)",(self.customer_id.get(),self.name.get(),self.combopay.get()))
     con.commit()
     messagebox.showinfo("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Car Succesfully Booked",parent=self.root)
     self.mainscreen()
     con.close()
    else:
     messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Please try with new Customer ID!",parent=self.root)
     self.customer_id.focus()
   except Exception as es:
    messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒',f'Error Due to : {str(es)}',parent=self.root)
 
 def delete(self):
  delete = tk.Tk()
  delete.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  delete.iconbitmap("Images/Icon.ico")
  """
  app_width = 400
  app_height = 250
  screen_width = delete.winfo_screenwidth()
  screen_height = delete.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  delete.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  delete.resizable(0,0)
  Frame_bookcar=Frame(delete,bg="#064663")
  Frame_bookcar.place(x=0,y=0,height=250,width=400)
 
  label=Label(Frame_bookcar,text="Customer ID",font=('Product Sans',30,'bold'),fg="#FEEE8C",bg='#064663')
  label.place(x=85,y=35)
 
  self.customer_id=Entry(Frame_bookcar,font=("Product Sans",20,"bold"),justify='center',bg='#FFFEEA')
  self.customer_id.place(x=80,y=100,width=250,height=35)
 
 
  btn=Button(Frame_bookcar,command=self.Cancel,text="CANCEL",cursor="hand2",font=("Product Sans",17,'bold'),fg="#000000",bg="#F99A05",bd=0,width=8,height=1)
  btn.place(x=145,y=150)
  delete.mainloop()
 
 def Cancel(self):
  if self.customer_id.get()=="" :
   messagebox.showerror("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","All fields are required",parent=self.root)
  else:
   try:
    con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
    cur=con.cursor()
    cur.execute('Select Customer_ID from Booking_Details where Customer_ID=%s',(self.customer_id.get()))
    row=cur.fetchone()
    if row==None:
     messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒','No such booking',parent=self.root)
     self.customer_id.focus()
    else:
     con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
     cur=con.cursor()
     cur.execute("Delete from Booking_Details where Customer_ID=%s",(self.customer_id.get()))
     con.commit()
     messagebox.showinfo("𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒","Your Car Booking Has Been Cancelled!*",parent=self.root)
     con.close()
   except Exception as es:
    messagebox.showerror('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒',f'Error Due to : {str(es)}',parent=self.root)
 
 def Luxary(self):
  display = tk.Tk()
  display.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  display.iconbitmap("Images/Icon.ico")
  """
  app_width = 1400
  app_height = 500
  screen_width = display.winfo_screenwidth()
  screen_height = display.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  display.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  display.resizable(0,0)
  Display_Frame = Frame(display, bd = 0, bg = "#95D1CC" )
  Display_Frame.place(x = 0, y = 0, width = 1400, height = 500)
  s= ttk.Style(display)
  s.theme_use("clam")
  s.configure(".", font=('Product Sans', 10), bg = "#FFDEAD")
  s.configure("Display_Table.Heading",foreground="blue", font = ('Product Sans', 20))
  scroll_y = Scrollbar(Display_Frame, orient = VERTICAL)
  self.Display_Table = ttk.Treeview(Display_Frame, columns = ("Customer_ID","Name","Car","City","Address","Pincode","Phone_No","ID_Proof","Price","Body_type"),
                                    yscrollcommand = scroll_y.set)
  scroll_y.pack(side = RIGHT, fill = Y)
  scroll_y.config(command = self.Display_Table.yview)
  self.Display_Table.heading("Customer_ID",text="Customer ID",anchor=tk.CENTER)
  self.Display_Table.heading("Name",text="Name",anchor=tk.CENTER)
  self.Display_Table.heading("Car",text="Car Name",anchor=tk.CENTER)
  self.Display_Table.heading("City",text="City",anchor=tk.CENTER)
  self.Display_Table.heading("Address",text="Address",anchor=tk.CENTER)
  self.Display_Table.heading("Pincode",text="Pincode",anchor=tk.CENTER)
  self.Display_Table.heading("Phone_No",text="Phone No",anchor=tk.CENTER)
  self.Display_Table.heading("ID_Proof",text="ID Proof",anchor=tk.CENTER)
  self.Display_Table.heading("Price",text="Car Price",anchor=tk.CENTER)
  self.Display_Table.heading("Body_type",text="Body Type",anchor=tk.CENTER)
  self.Display_Table['show']="headings"
  self.Display_Table.column("Customer_ID",width=70,anchor=tk.CENTER)
  self.Display_Table.column("Name",width=140,anchor=tk.CENTER)
  self.Display_Table.column("Car",width=220,anchor=tk.CENTER)
  self.Display_Table.column("City",width=100,anchor=tk.CENTER)
  self.Display_Table.column("Address",width=200,anchor=tk.CENTER)
  self.Display_Table.column("Pincode",width=100,anchor=tk.CENTER)
  self.Display_Table.column("Phone_No",width=100,anchor=tk.CENTER)
  self.Display_Table.column("ID_Proof",width=100,anchor=tk.CENTER)
  self.Display_Table.column("Price",width=100,anchor=tk.CENTER)
  self.Display_Table.column("Body_type",width=120,anchor=tk.CENTER)
  self.Display_Table.pack(fill = BOTH, expand = 1)
  self.Show_Luxary_Data()
  display.mainloop()
 def Economy(self):
  disply = tk.Tk()
  disply.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  disply.iconbitmap("Images/Icon.ico")
  """
  app_width = 1400
  app_height = 500
  screen_width = disply.winfo_screenwidth()
  screen_height = disply.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  disply.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  disply.resizable(0,0)
  Display_Frame = Frame(disply, bd = 0, bg = "#95D1CC" )
  Display_Frame.place(x = 0, y = 0, width = 1400, height = 500)
  s= ttk.Style(disply)
  s.theme_use("clam")
  s.configure(".", font=('Product Sans', 10), bg = "#FFDEAD")
  s.configure("Display_Table.Heading",foreground="blue", font = ('Product Sans', 20))
  scroll_y = Scrollbar(Display_Frame, orient = VERTICAL)
  self.Display_Table = ttk.Treeview(Display_Frame, columns = ("Customer_ID","Name","Car","City","Address","Pincode","Phone_No","ID_Proof","Price","Body_type"),
                                    yscrollcommand = scroll_y.set)
  scroll_y.pack(side = RIGHT, fill = Y)
  scroll_y.config(command = self.Display_Table.yview)
  self.Display_Table.heading("Customer_ID",text="Customer ID",anchor=tk.CENTER)
  self.Display_Table.heading("Name",text="Name",anchor=tk.CENTER)
  self.Display_Table.heading("Car",text="Car Name",anchor=tk.CENTER)
  self.Display_Table.heading("City",text="City",anchor=tk.CENTER)
  self.Display_Table.heading("Address",text="Address",anchor=tk.CENTER)
  self.Display_Table.heading("Pincode",text="Pincode",anchor=tk.CENTER)
  self.Display_Table.heading("Phone_No",text="Phone No",anchor=tk.CENTER)
  self.Display_Table.heading("ID_Proof",text="ID Proof",anchor=tk.CENTER)
  self.Display_Table.heading("Price",text="Car Price",anchor=tk.CENTER)
  self.Display_Table.heading("Body_type",text="Body Type",anchor=tk.CENTER)
  self.Display_Table['show']="headings"
  self.Display_Table.column("Customer_ID",width=70,anchor=tk.CENTER)
  self.Display_Table.column("Name",width=140,anchor=tk.CENTER)
  self.Display_Table.column("Car",width=220,anchor=tk.CENTER)
  self.Display_Table.column("City",width=100,anchor=tk.CENTER)
  self.Display_Table.column("Address",width=200,anchor=tk.CENTER)
  self.Display_Table.column("Pincode",width=100,anchor=tk.CENTER)
  self.Display_Table.column("Phone_No",width=100,anchor=tk.CENTER)
  self.Display_Table.column("ID_Proof",width=100,anchor=tk.CENTER)
  self.Display_Table.column("Price",width=100,anchor=tk.CENTER)
  self.Display_Table.column("Body_type",width=120,anchor=tk.CENTER)
  self.Display_Table.pack(fill = BOTH, expand = 1)
  self.Show_Economy_Data()
  disply.mainloop()
 
 def Show_Economy_Data(self):
  mycon = pymysql.connect(host = "localhost", user = "root", password = "Madman123", database = "max")
  cursor = mycon.cursor()
  cursor.execute("selectcustomer_id,name,economy_car.car,city,address,pincode ,phone_no,ID_Proof,economy_car.price,economy_car.Body_type from economy_car join booking_details where economy_car.car= booking_details.car;")
  rows = cursor.fetchall()
  if len(rows) != 0 :
   self.Display_Table.delete(*self.Display_Table.get_children())
   for row in rows :
    self.Display_Table.insert('', END, values = row)
    mycon.close()
 
 def Show_Luxary_Data(self):
  mycon = pymysql.connect(host = "localhost", user = "root", password = "Madman123", database = "max")
  cursor = mycon.cursor()
  cursor.execute("select customer_id,name,luxary_car.car,city,address,pincode,phone_no,ID_Proof,luxary_car.price,luxary_car.Body_type from luxary_car "
                 "join booking_details where luxary_car.car= booking_details.car;")
  rows = cursor.fetchall()
  if len(rows) != 0 :
   self.Display_Table.delete(*self.Display_Table.get_children())
   for row in rows :
    self.Display_Table.insert('', END, values = row)
    mycon.close()
 def Search(self):
  Search = tk.Tk()
  Search.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')

  """
  Search.iconbitmap("Images/Icon.ico")
  """
  app_width = 400
  app_height = 250
  screen_width = Search.winfo_screenwidth()
  screen_height = Search.winfo_screenheight()
  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2 ) - (app_height / 2)
  Search.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  Search.resizable(0,0)
  Frame_bookcar=Frame(Search,bg="#064663")
  Frame_bookcar.place(x=0,y=0,height=250,width=400)
  label3=Label(Frame_bookcar,text="Customer ID",font=('Product Sans',30,'bold'),fg="#FEEE8C",bg='#064663')
  label3.place(x=85,y=35)
  self.customer_id=Entry(Frame_bookcar,font=("Product Sans",20,"bold"),justify='center',bg='#FFFEEA')
  self.customer_id.place(x=80,y=100,width=250,height=35)
  btn3=Button(Frame_bookcar,command=self.SearchFn,text="SEARCH" ,cursor="hand2",font=("Product Sans",17,'bold'),fg="#000000",bg="#F99A05",bd=0,width=8,height=1)
  btn3.place(x=145,y=150)
  Search.mainloop()
 def SearchFn(self):
  root = tk.Tk()
  root.title('𝕽𝖊𝖈𝖊𝖕𝖙𝖔𝖗 𝕮𝖆𝖗 𝕾𝖍𝖔𝖜𝖗𝖔𝖔𝖒')
  """
  root.iconbitmap("Images/Icon.ico")
  """
  root.geometry("1050x200")
  root.resizable(0,0)
  con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
  cur=con.cursor()
  cur.execute('select * from booking_details where Customer_id = %s',(self.customer_id.get()))
  tree=ttk.Treeview(root)
  tree["show"]='headings'
  s=ttk.Style(root)
  s.theme_use("clam")
  s.configure(".",font=('Helvetica',11))
  s.configure("Treeview.Heading",foreground="blue",font=('Product Sans',11,'bold'))
 
  tree["columns"]=("Customer_id","Car","Name","ID_Proof","City","Pincode","Address","Phone_no")
  tree.column("Customer_id",width=100,anchor=tk.CENTER)
  tree.column("Car",width=230,anchor=tk.CENTER)
  tree.column("Name",width=100,anchor=tk.CENTER)
  tree.column("ID_Proof",width=100,anchor=tk.CENTER)
  tree.column("City",width=100,anchor=tk.CENTER)
  tree.column("Pincode",width=100,anchor=tk.CENTER)
  tree.column("Address",width=200,anchor=tk.CENTER)
  tree.column("Phone_no",width=100,anchor=tk.CENTER)
  tree.heading("Customer_id",text="Customer ID",anchor=tk.CENTER)
  tree.heading("Car",text="Car Name",anchor=tk.CENTER)
  tree.heading("Name",text="Name",anchor=tk.CENTER)
  tree.heading("ID_Proof",text="ID Proof",anchor=tk.CENTER)
  tree.heading("City",text="City",anchor=tk.CENTER)
  tree.heading("Pincode",text="Pincode",anchor=tk.CENTER)
  tree.heading("Address",text="Address",anchor=tk.CENTER)
  tree.heading("Phone_no",text="Phone no",anchor=tk.CENTER)
  row=cur.fetchone()
  if row==None:
   label=Label(root,text="No Such Booking",font=('times new roman',32,'bold'),fg="orangered",bg='white')
   label.place(x=400,y=100)
  else:
   con=pymysql.connect(host='localhost',user='root',password='Madman123',db='max')
   cur=con.cursor()
   cur.execute('select * from booking_details where customer_id=%s',(self.customer_id.get()))
   i=0
   for ro in cur:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7]))
    i=i+1
 
  hsb=ttk.Scrollbar(root,orient="vertical")
  hsb.configure(command=tree.yview)
  tree.configure(yscrollcommand=hsb.set)
  hsb.pack(fill=Y,side=RIGHT)
  tree.pack()
  root.mainloop()
 
 def Login_Clear(self):
  self.Username.delete(0,END)
  self.Password.delete(0,END)
 def Register_Clear(self) :
    
  self.Username.delete(0,END)
  self.Email.delete(0,END)
  self.Password.delete(0,END)
  self.ConfirmPassword.delete(0,END)
 def fd(self):
  self.password.delete(0,END)
  self.email_id.delete(0,END)
 def loginclear(self):
  self.name.delete(0,END)
  self.password.delete(0,END)
 def rg(self):
  self.name.delete(0,END)
  self.address.delete(0,END)
  self.pincode.delete(0,END)
  self.phone_no.delete(0,END)
  self.combocar.delete(0,END)
  self.customer_id.delete(0,END)
 def pas(self):
  self.name.delete(0,END)
  self.password.delete(0,END)
  self.copassword.delete(0,END)
root=Tk()
ob=Login(root)
root.mainloop()
