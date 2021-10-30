from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import speech_recognition as sr
import webbrowser
import sqlite3
import time
from BO import BO_window_Class as bo_w
from bill import Bill_Class as bill 
from Clock_in_out import Clock_in_out_Class as C_in_out
from change_forget_pass import change_forget_password_Class as C_P
from Cash_count import Cash_count_Class as CCC
# pip install pillow
class FO_window_Class:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventry Management System | Developed by Qurban Ali")
        self.root.config(bg="white")
        self.root.focus_force()
#===========label Size for all lable
        self.label_size=30
        #=======Colors =====
        self.menu_Btn_color="gray";
        # self.FO_color="#cc00cc"
        self.FO_color="#B8BFB3" 
        self.sales_color="#142952"
        self.return_color="red"
        self.tander_color="#5ac910"
        self.BO_frame_color="black"

        self.product_name=StringVar()
        self.var_price=StringVar()
        self.sale_active=StringVar()
        self.user_name="True"
        
        self.list_init()
        
        # ---------Style the Treeview------
        
        self.style = ttk.Style()
        self.style.configure('Treeview.Heading', background="green3",font=("goudy old style",15,"bold"))
        self.style.configure("Treeview",
                        background='silver',
                        forground='red',
                        color="#142952",
                
                        rowheight=45,
                        font=("goudy old style",20,'bold'),
                        fieldbackground='white')
        self.style.map('Treeview',
                background=[('selected','green')]),
        # self.style.theme_
                
                
#==========variables=======
        self.var_login_id=StringVar()
        self.sales_item_id=StringVar()     
        self.var_category_id=StringVar()
        self.user_info=[]
        self.login_pass=[]
        self.sales_item=[]
        self.Ai_find_list=[]
        self.Ai_frame=""
        self.is_on ="True"
        self.query=""
        self.office=StringVar()

        self.root.bind("<Key>",self.Myfunction)
        
        self.Main_frame=Frame(self.root,bd=0)
        self.Main_frame.place(x=0,y=0,width=1350,height=700)
        
        # self.my_theme()
        self.FO_Menu_frame_()
        self.FO_left_frame_()
        self.FO_Right_frame_()
        # if self.My_reg==0:
        #     self.footer_frame_()
        # else:
        self.business_date_check()
        # self.footer_frame_()
        #     bo_w.Reg_color(self)
        #     bo_w.Store_color(self)
        
        
        self.Update_date_time()
    def list_init(self):
        self.item=0
        self.pro_price_list=[]
        self.pro_price_sum=0
        self.counting=0
        self.my_row="-1"
        self.my_row=[]
        self.cart_list=[]
    def business_date_check(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            cur.execute("select * from business_date")
            rows=cur.fetchall()
        #     print(len(rows))
            len(rows)
            if len(rows)==0:
                self.footer_frame_()
            else:
                    if rows[len(rows)-1][6]=="open" and  rows[len(rows)-1][7]=="open":
                            self.sale_active="True"
                            self.footer_frame_()
                            self.shop_name.config(bg="green")
                            self.Register.config(bg="green")
                        #     print(type(self.user_name))
                            if  self.user_name=="True":
                                self.R_login.config(text="Register Login")
                            else:
                                self.R_login.config(text=f"{self.user_name}")
                    elif rows[len(rows)-1][6]=="open" and  rows[len(rows)-1][7]=="close":
                            self.sale_active=""
                            self.footer_frame_()
                            self.shop_name.config(bg="green")
                            self.Register.config(bg="red")
                        #     print(type(self.user_name))
                            if  self.user_name=="True":
                                self.R_login.config(text="Register Login")
                            else:
                                self.R_login.config(text=f"{self.user_name}")             
                    else:
                            self.sale_active=""
                            self.footer_frame_()
                                         
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}",parent=self.root)            
      
    def FO_Right_frame_(self):
        self.Right_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Right_frame.place(x=680,y=10,width=660,height=550) 
       
        self.icon_ = Image.open('images_f/parts1.png')
        self.icon_ = self.icon_.resize((660,550), Image.ANTIALIAS)
        self.icon_ = ImageTk.PhotoImage(self.icon_)
        self.lbl_employee=Label(self.Right_frame,image=self.icon_,fg="white")
        self.lbl_employee.place(x=0,y=0,width=660,height=550)

          
    def FO_left_frame_(self):
        self.Left_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Left_frame.place(x=10,y=10,width=660,height=550)
        self.info=Label(self.Left_frame,text="Info",font=("goudy old style",10,"bold"),bg=self.FO_color,height=5,anchor='nw')
        self.info.grid(row=0,column=0,sticky="nsew",padx=0)
        self.Task =Label(self.Left_frame, text="Tasks",bg=self.FO_color,)
        self.Task.grid(row=0,column=1,sticky="nsew",padx=2)
        self.Goals =Label(self.Left_frame, text="Goals",bg=self.FO_color,)
        self.Goals.grid(row=0,column=2,sticky="nsew",padx=0)
        self.Message =Label(self.Left_frame, text="Message",bg=self.FO_color)
        self.Message.grid(row=0,column=3,sticky="nsew",padx=2)
        self.Keyboard =Label(self.Left_frame, text="Keyboard",bg=self.FO_color)
        self.Keyboard.grid(row=0,column=4,sticky="nsew",padx=0)
        self.Left_frame.grid_columnconfigure(0,weight=1)
        self.Left_frame.grid_columnconfigure(1,weight=1)
        self.Left_frame.grid_columnconfigure(2,weight=1)
        self.Left_frame.grid_columnconfigure(3,weight=1)
        self.Left_frame.grid_columnconfigure(4,weight=1)
        
        self.Left_frame_text_Area=Frame(self.Left_frame,bd=1,relief=RIDGE,bg=self.FO_color)
        self.Left_frame_text_Area.place(x=0,y=400,width=655,height=145)
        
        self.lbl_Rl =Label(self.Left_frame_text_Area,text="Register Login",font=("goudy old style",20),bg=self.FO_color)
        self.lbl_Rl.grid(row=0,column=0,sticky="w",padx=10,pady=5)
        self.txt_Login =Entry(self.Left_frame_text_Area,textvariable=self.var_login_id,bg="white",fg='black',font=("goudy old style",20))
        self.txt_Login.grid(row=1,column=0,sticky="w",padx=10,pady=5)
        self.txt_Login.focus_set()
        self.lbl_LP =Label(self.Left_frame_text_Area, text="Enter Login and Password",font=("goudy old style",20),bg=self.FO_color)
        self.lbl_LP.grid(row=2,column=0,sticky="w",padx=10,pady=5)
        self.Left_frame_text_Area.grid_columnconfigure(0,weight=1)
        self.office="FO"
        self.txt_Login.bind("<Return>",self.Enter_btn)    
                
    def FO_Menu_frame_(self):
        self.Menu_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Menu_frame.place(x=10,y=570,width=1350,height=89)
        
        self.btn0 =Button(self.Menu_frame,text="Exit",font=("goudy old style",10,"bold"),command=self.Check_state,bg=self.menu_Btn_color,height=5,state="disabled",anchor='nw')
        self.btn0.grid(row=0,column=0,sticky="nsew",padx=0)
        # self.btn0.bind("<Key>",self.escape_window)
        self.btn1=Button(self.Menu_frame,anchor='nw',text="Help\n\n\nF1",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,height=5)
        self.btn1.grid(row=0,column=1,sticky="nsew",padx=2)
        self.btn2=Button(self.Menu_frame, text="Clock\nIn\out\n\nF2",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,command=self.Clock_in_out_fun,anchor='nw')
        self.btn2.grid(row=0,column=2,sticky="nsew",padx=0)
        self.btn3=Button(self.Menu_frame, text="View\nSchedule\n&time\nF3",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,command=self.View_Schedule,anchor='nw')
        self.btn3.grid(row=0,column=3,sticky="nsew",padx=2)
        self.btn4=Button(self.Menu_frame, text="Change\nPassword\n\nF4",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,command=self.Change_Password,anchor='nw')
        self.btn4.grid(row=0,column=4,sticky="nsew",padx=0)
        self.btn5=Button(self.Menu_frame, text="Receipt\nReprint\nOptions\nF5",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,state="disabled",anchor='nw')
        self.btn5.grid(row=0,column=5,sticky="nsew",padx=2)
        self.btn6 =Button(self.Menu_frame,text="Balance\nInqury\n\nF6",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,height=5,state="disabled",anchor='nw')
        self.btn6.grid(row=0,column=6,sticky="nsew",padx=0)
        self.btn7=Button(self.Menu_frame, text="Testing \n Mode\n\nF7",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,state="disabled",anchor='nw')
        self.btn7.grid(row=0,column=7,sticky="nsew",padx=2)
        self.btn8=Button(self.Menu_frame, text="My Task\n\n\nF8",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,state="disabled",anchor='nw')
        self.btn8.grid(row=0,column=8,sticky="nsew",padx=0)
        self.btn9=Button(self.Menu_frame, text="Find \n Item\n\nF9",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,state="disabled",anchor='nw')
        self.btn9.grid(row=0,column=9,sticky="nsew",padx=2)
        self.btn10=Button(self.Menu_frame, text="Till\n\n\nF10",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,state="disabled",anchor='nw')
        self.btn10.grid(row=0,column=10,sticky="nsew",padx=0)
        self.btn11=Button(self.Menu_frame, text="Flash\nSales\n\nF11",font=("goudy old style",10,"bold"),command=self.Flash_sales,bg=self.menu_Btn_color,anchor='nw')
        self.btn11.grid(row=0,column=11,sticky="nsew",padx=2)
        self.btn12=Button(self.Menu_frame, text="Back\nOffice\n\nF12",font=("goudy old style",10,"bold"),bg=self.menu_Btn_color,command=self.Back_office,anchor='nw')
        self.btn12.grid(row=0,column=12,sticky="nsew",padx=0)
        
        self.Menu_frame.grid_columnconfigure(0,weight=1)
        self.Menu_frame.grid_columnconfigure(1,weight=1)
        self.Menu_frame.grid_columnconfigure(2,weight=1)
        self.Menu_frame.grid_columnconfigure(3,weight=1)
        self.Menu_frame.grid_columnconfigure(4,weight=1)
        self.Menu_frame.grid_columnconfigure(5,weight=1)
        self.Menu_frame.grid_columnconfigure(6,weight=1)
        self.Menu_frame.grid_columnconfigure(7,weight=1)
        self.Menu_frame.grid_columnconfigure(8,weight=1)
        self.Menu_frame.grid_columnconfigure(9,weight=1)
        self.Menu_frame.grid_columnconfigure(10,weight=1)
        self.Menu_frame.grid_columnconfigure(11,weight=1)
        self.Menu_frame.grid_columnconfigure(12,weight=1)
       
    
    def footer_frame_(self):
        self.footer_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        # # self.Menu_frame.place(x=10,y=570,width=1350,height=89)
        self.footer_frame.place(x=10,y=660,width=1350,height=35)
        self.R_login=Label(self.footer_frame,text="Register Login",bg=self.FO_color,height=2,width=37)
        self.R_login.grid(column=0,row=0)
        self.shop_name=Label(self.footer_frame,text="IMS",bg="red",height=2,width=37)
        self.shop_name.grid(column=1,row=0,padx=2)
        self.Register=Label(self.footer_frame,text="Register",bg="red",height=2,width=37)
        self.Register.grid(column=2,row=0)
        self.system_time1=Label(self.footer_frame,text="hh/mm/ss P/A M",bg="white",height=2,width=37)
        self.system_time1.grid(column=3,row=0,padx=2)
        self.system_date=Label(self.footer_frame,text="dd/mm/yyyy",bg="white",height=2,width=37)
        self.system_date.grid(column=4,row=0)    
        
    
        # functions=======================
    #====================date and time update=====
    def Update_date_time(self):
        time_=time.strftime("%H:%M:%S")
        date_=time.strftime("%d/%m/%y")
        self.system_time1.config(text=f"Time: {str(time_)}")
        self.system_date.config(text=f" Date: {str(date_)}")
        
        self.system_time1.after(200,self.Update_date_time)
    def Back_office(self):
        self.info.config(bg=self.BO_frame_color, fg= "white")
        self.Task.config(bg=self.BO_frame_color, fg= "white")
        self.Goals.config(bg=self.BO_frame_color, fg= "white")
        self.Message.config(bg=self.BO_frame_color, fg= "white")
        self.Keyboard.config(bg=self.BO_frame_color, fg= "white")
        self.lbl_Rl.config(bg=self.BO_frame_color, fg= "white" ,text="Back Office Login ID")
        self.lbl_LP.config(bg=self.BO_frame_color, fg= "white")
        self.Left_frame_text_Area.config(bg=self.BO_frame_color)
        del self.login_pass[:]
        self.txt_Login.config(show="")
        self.var_login_id.set("")
        
        self.office="BO"
        self.btn12.config(command=self.Front_office,text="Register\n\n\nF12")
        #     self.Menu_frame_btns()
    def Front_office(self):
        self.__init__(root)
        # self.Outer_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        # self.Outer_frame.place(x=350,y=10,width=550,height=550)
        # self.Top_frame=Frame(self.Outer_frame,bd=3,relief=RIDGE)
        # self.Top_frame.place(x=0,y=0,width=545,height=80)
        # self.office="FO"
        #     self.Menu_frame_btns()
    def Flash_sales(self):
        self.Back_Office_window()
        bo_w.Reports_Frame(self,'sale',self.office)    
        #     pass    
    def Menu_frame_btns(self):
        self.btn0.config(text="Help",bg=self.menu_Btn_color)        
    def Enter_btn(self,ev):
        print(self.office)
        if self.office == "View time":
                self.login_pass.append(self.var_login_id.get())
                self.lbl_Rl.config(bg= "gray", fg= "black" ,text="To View Time Card  Enter Password")
                self.txt_Login.config(show="*")
                
                if len(self.login_pass)==2:
                        print(self.login_pass)
                        self.logedin_FO()
        elif self.office == "Clock":
                self.login_pass.append(self.var_login_id.get())
                self.lbl_Rl.config(bg= "gray", fg= "black" ,text="Clock in/out Password")
                self.txt_Login.config(show="*")
                
                if len(self.login_pass)==2:
                        print(self.login_pass)
                        self.logedin_FO()
        elif self.office == "Change_pass":
                self.login_pass.append(self.var_login_id.get())
                self.lbl_Rl.config(bg= "gray", fg= "White" ,text="Enter Password To Change Password")
                self.txt_Login.config(show="*")
                
                if len(self.login_pass)==2:
                        print(self.login_pass)
                        self.logedin_FO()                
        
        elif self.office == "FO":
                self.login_pass.append(self.var_login_id.get())
                self.lbl_Rl.config(bg= self.FO_color, fg= "black" ,text="Register Password")
                self.txt_Login.config(show="*")
                if len(self.login_pass)==2:
                        self.logedin_FO()
                
        elif self.office == "BO":
                self.login_pass.append(self.var_login_id.get())
                self.lbl_Rl.config(bg= "black", fg= "white" ,text="Back Office Password") 
                self.txt_Login.config(show="*")
                if len(self.login_pass)==2:
                        self.logedin_BO()  
        elif self.office == "sales_window":
                if self.sales_item_id.get()=="" and len(self.cart_list)==0:
                        messagebox.showwarning("Warning","add Product first")
                else:        
                        if self.sales_item_id.get()=="":
                                self.Add_Tenders()
                        else:
                                self.search()
                                self.sales_item_id.set("")
                                self.transection_no()
                                self.output_frame()
        elif self.office == "return_window":
                if self.sales_item_id.get()=="" and len(self.sales_item)==0:
                        messagebox.showwarning("Warning","add Product first")
                else:        
                        if self.sales_item_id.get()=="":
                                self.Add_Tenders()
                        else:
                                self.search()
                                self.sales_item_id.set("")
                                self.transection_no()
                                self.output_frame()                             
        elif self.office == "change_qty":
                if self.sales_item_id.get()=="" and len(self.sales_item)==0:
                        messagebox.showwarning("Warning","add Product Qty")
                else:        
                        if self.sales_item_id.get()=="":
                                self.Add_Tenders()
                        else:
                                data=self.cart_list[int(self.my_row)]
                                data1=list(data)
                                print(data1)
                                
                                data1[2]=self.sales_item_id.get()
                                data1[3]=str(int(self.sales_item_id.get())*int(data1[3]))
                                # print()
                                x = tuple(data1)
                                self.cart_list.pop(int(self.my_row))
                                self.cart_list.append(x)
                                self.sales_item_id.set("")
                                self.transection_no()
                                self.output_frame()                          
        elif self.office == "cash_amount":
                        self.price_total()
        elif self.office == "Till_Audit":
             CCC.check_list_CC(self)              
                
        self.var_login_id.set("")
        
            
    def logedin_FO(self):
        self.var_login_id.set("")
        self.login()
        
    def logedin_BO(self):
        self.login()        
    def Myfunction(self,event):
        if event.keysym=="Escape":
                self.Check_state()
                # self.__init__(root)
                #    self.Check_state()  
    def Check_state(self):
        if self.office=="FO":
                self.Front_office()
        elif self.office=="BO":
                self.Back_office()
                self.Right_frame()
        elif self.office=="Till_Audit":  
                self.Back_Office_window() 
                bo_w.Till_Option(self)                          
        elif  self.office=="sales_window":
                MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to Cancle the transection',icon = 'warning')
                print("return to fo",MsgBox)
                if MsgBox == 'yes':
                        self.Left_frame.destroy()
                        self.Right_frame.destroy()
                        self.Menu_frame.destroy()
                        self.Front_office()
        elif self.office=="add_tenders":
                self.FO_left_frame_()
                self.sales_left_frame_config() 
                self.Active_btn()
                
        elif self.office=="cash_amount":
                self.Add_Tenders()
        elif self.office=="change_item":
                # self.FO_left_frame_()
                # self.Active_btn() 
                self.sales_left_frame_config() 
                self.FO_Menu_frame_()
                self.sales_win_Active_btn()
                # self.btn4.config(text="Add\nDiscount",bg= self.sales_color , fg= "white",command=self.Discount,state="disabled")   
                # 
        elif self.office=="change_qty":
                self.FO_left_frame_()
                self.sales_left_frame_config() 
                self.Active_btn()    
        elif self.office=="Clock":
                self.Back_office()
                self.Clock_in_out_fun()
                # self.FO_left_frame_()
                # self.sales_left_frame_config() 
                # self.Active_btn()                
                                      
    def Sales_window(self):
        if self.sale_active=="True":    
                self.list_init()
                self.FO_Right_frame_()
                self.FO_left_frame_()
                self.FO_Menu_frame_() 
                
                self.sales_left_frame_config()
                self.sales_win_Active_btn()
                #     self.var_login_id.set("")
                self.office="sales_window"
                # messagebox.showinfo("Success","Welcome FO",parent=self.root)
        else:
                messagebox.showerror("Error",f"Can't access the register\nuntill store or register is close",parent=self.root)  
                # self.Check_state()  
                self.Front_office() 
    def sales_win_Active_btn(self):
        self.btn0.config(text="Cancle \nSale",bg= self.sales_color , fg= "white",command=self.Cancel_Sales,state="normal")
        self.btn1.config(text="Help",bg=self.sales_color,fg="white",command=self.Window_Help)
        self.btn2.config(text="Return\nItem",bg= self.sales_color , fg= "white",command=self.Return_Item)
        self.btn3.config(text="Change\nItem",bg= self.sales_color , fg= "white",command=self.Change_item)
        self.btn4.config(text="Add\nDiscount",bg= self.sales_color , fg= "white",command=self.Discount,state="disabled")
        self.btn5.config(text="Sell\nNon-Merch",bg= self.sales_color , fg= "white",command=self.Sell_non_merch)
        self.btn6.config(text="Gift\nReceipt",bg= self.sales_color , fg= "white",command=self.Gift_Receipt)
        self.btn7.config(text="Extended\nTransaction",bg= self.sales_color , fg= "white",command=self.Extended_trans)
        self.btn8.config(text="Register\nOption",bg= self.sales_color , fg= "white",command=self.Register_Option)
        self.btn9.config(text="Find\nItem",bg= self.sales_color , fg= "white",command=self.Find_Item)
        self.btn10.config(text="Add\nTenders",bg= self.sales_color , fg= "white",command=self.Add_Tenders)
        self.btn11.config(text="Customer\nOptions",bg= self.sales_color , fg= "white",command=self.Customer_Option)
        self.btn12.config(text="Suspend\nTransection",bg= self.sales_color , fg= "white",command=self.Suspend_transection)
        del self.login_pass[:]
        self.txt_Login.config(show="",textvariable=self.sales_item_id)
                             
    def sales_left_frame_config(self):
            
        self.office="sales_window"   
        # print("after escap",self.office) 
        self.info.config(bg= self.sales_color , fg= "white")
        self.Task.config(bg= self.sales_color , fg= "white")
        self.Goals.config(bg= self.sales_color , fg= "white")
        self.Message.config(bg= self.sales_color , fg= "white")
        self.Keyboard.config(bg= self.sales_color , fg= "white")
        self.lbl_Rl.config(bg= self.sales_color, fg= "white" ,text="Scan Item or UPC")
        self.lbl_LP.config(bg= self.sales_color, fg= "white")
        self.Left_frame_text_Area.config(bg= self.sales_color,)
        # self.txt_Login.config(textvariable=self.product_name)
        self.txt_Login.config(show="",textvariable=self.sales_item_id)
        self.lbl_LP.config(text="Scan or Key an item ID ")  
        self.AI_btn()
          
            
    
    def transection_no(self):
        if self.item==0:
                
                trans_frame=Frame(self.Right_frame,bd=3,relief=RIDGE)
                trans_frame.place(x=0,y=0,width=660,height=450)
                scrolly=Scrollbar(trans_frame,orient=VERTICAL)
                scrollx=Scrollbar(trans_frame,orient=HORIZONTAL)
                # self.ProductsTable=ttk.Treeview(trans_frame,columns=("Transection_no","name","Unit_price","qty","Ext_price"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                self.ProductsTable=ttk.Treeview(trans_frame,columns=("Product_name","Product_code","qty","C_P_U"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                scrollx.pack(side=BOTTOM,fill=X)
                scrolly.pack(side=RIGHT,fill=Y)
                scrollx.config(command=self.ProductsTable.xview)
                scrolly.config(command=self.ProductsTable.yview)
        #====headings ===========================  # Product_name,Product_code,qty,C_P_U
                # self.ProductsTable.heading("Transection_no",text=" my Trans #")
                
      
                self.ProductsTable.heading("Product_name",text=" Product Name")
                self.ProductsTable.heading("Product_code",text="Code")
                self.ProductsTable.heading("qty",text="QTY")
                self.ProductsTable.heading("C_P_U",text="Unit Price")
                
                #========colom width ====================
                
                self.ProductsTable.column("Product_name",width=60)
                self.ProductsTable.column("Product_code",width=60)
                # self.ProductsTable.column("Unit_price",width=60)
                self.ProductsTable.column("qty",width=60)
                self.ProductsTable.column("C_P_U",width=60)
                
                self.ProductsTable["show"]="headings"
                self.ProductsTable.pack(fill=BOTH,expand=1)
                self.ProductsTable.tag_configure('return', background='red', foreground='white')
                self.ProductsTable.tag_configure('sales', background='#2d5bb9', foreground='white')
                # self.ProductsTable.bind("<ButtonRelease-1>",self.get_data)
                self.ProductsTable.delete(*self.ProductsTable.get_children())
                self.ProductsTable.bind("<ButtonRelease-1>",self.get_data)
                self.btn10.config(text="Add\nTenders",bg= self.sales_color , fg= "white",command=self.Add_Tenders,state="normal")
                
                
                
                self.item=1
                index_count=0
                for row in self.cart_list:
                        if int(row[3])<0:
                                self.ProductsTable.insert('',END,values=row,text=str(index_count),tags=('return'))
                                
                        else:
                                self.ProductsTable.insert('',END,values=row,text=str(index_count),tags=('sales'))
                        index_count+=1
                   
                         
                

        else:
                self.item=self.item+1
                self.ProductsTable.delete(*self.ProductsTable.get_children())
                index_count=0
                for row in self.cart_list:
                        if int(row[3])<0:
                                self.ProductsTable.insert('',END,values=row,text=str(index_count),tags=('return'))
                        else:
                                self.ProductsTable.insert('',END,values=row,text=str(index_count),tags=('sales'))
                        index_count+=1             
    def Suspend_transection(self):
            messagebox.showinfo("Success","Suspend ransection",parent=self.root)
    def Back_Office_window(self):
            self.Left_frame.destroy()
            self.Right_frame.destroy()
            self.Menu_frame.destroy()
            bo_w.BO_Function(self,root)
            
        #     messagebox.showinfo("Success","Welcome BO",parent=self.root)               
    def Cancel_Sales(self):
        self.Check_state()
        #     messagebox.showinfo("Success","Do you want to Cancel Transection!",parent=self.root) 
    def Window_Help(self):
            messagebox.showinfo("Success","Help",parent=self.root)
    def Return_Item(self):
            op=messagebox.askyesno("Confirm","Did Customer Have orignal slip",parent=self.root)
            if op==True:
                messagebox.showinfo("Success","Did Customer Have orignal slip",parent=self.root) 
            else:
                    self.return_window()                                
    def Change_item(self):
        self.disable_btn();
        self.office="change_item"
        self.btn0.config(state="normal",text="Back",command=self.Check_state)
        self.btn4.config(state="normal",text="Delete",command=self.Delete_row)
        self.btn5.config(state="normal",text="Qty",command=self.Change_Qty)
        # self.btn6.config(state="normal",text="")
        

        #     messagebox.showinfo("Success","Change Item",parent=self.root)               
    def Discount(self):
            messagebox.showinfo("Success","Discount",parent=self.root)              
    def Sell_non_merch(self):
            messagebox.showinfo("Success","Sell Non merchantizing",parent=self.root)                
    def Gift_Receipt(self):
            messagebox.showinfo("Success","Gift Receipt",parent=self.root)      
    def Extended_trans(self):
            messagebox.showinfo("Success","Extend Transection",parent=self.root)
    def Register_Option(self):
            messagebox.showinfo("Success","Register Options",parent=self.root)      
    def Find_Item(self):
            messagebox.showinfo("Success","Find Item",parent=self.root)
    def Add_Tenders(self):
            self.office="add_tenders"
        #     print("add_tenders")
            self.disable_btn()
            self.choose_tander()
        #     messagebox.showinfo("Success","Add tender",parent=self.root)              
    def Customer_Option(self):
            messagebox.showinfo("Success","Customer Options",parent=self.root)   
    def output_frame(self):
        trans_frame_total=Frame(self.Right_frame,bd=3,relief=RIDGE)
        trans_frame_total.place(x=0,y=450,width=660,height=120)
        scrolly=Scrollbar(trans_frame_total,orient=VERTICAL)
        scrollx=Scrollbar(trans_frame_total,orient=HORIZONTAL)
                # self.ProductsTable=ttk.Treeview(trans_frame_total,columns=("Transection_no","name","Unit_price","qty","Ext_price"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.tander=ttk.Treeview(trans_frame_total,columns=("Items","Tax","fee","sub_total"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.tander.xview)
        scrolly.config(command=self.tander.yview)
        #====headings ===========================
        self.tander.heading("Items",text="Items")
        self.tander.heading("Tax",text="")
        self.tander.heading("fee",text="")
        self.tander.heading("sub_total",text="Subtotal Rs")
        # self.tander.heading("Ext_price",text="Ext Price")
        
        #========colom width ====================
        self.tander.column("Items",width=160,anchor="center")
        self.tander.column("Tax",width=160,anchor="center")
        self.tander.column("fee",width=160,anchor="center")
        self.tander.column("sub_total",width=160,anchor="center")
        # self.tander.column("Ext_price",width=60)
        
        self.tander["show"]="headings"
        self.tander.pack(fill=BOTH,expand=1)
        # self.tander.bind("<ButtonRelease-1>",self.get_data)
        self.tander.delete(*self.tander.get_children())
        del self.pro_price_list[:]
        
        # print("length",len(self.cart_list))
        total_product_count=0
        
        #     self.item=1
        if len(self.cart_list)==0:
                 self.tander.insert('',END,values=0)
        else:
                for row in self.cart_list:
                        total_product_count+=int(row[2])
                        self.pro_price_list.append(int(row[3]))
                        self.pro_price_sum=sum(self.pro_price_list)
                data=[total_product_count,"","",str(self.pro_price_sum)]        
                self.tander.insert('',END,values=data)
    def choose_tander(self):
        if len(self.cart_list)==0:
                messagebox.showwarning("Warning","Please insert prouct before add tendar")
                self.FO_left_frame_()
                self.sales_left_frame_config()
                self.Active_btn()
        else:
                        
                self.Left_frame.destroy()
                
                self.Left_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
                self.Left_frame.place(x=10,y=10,width=660,height=550)
                self.btn_Cash =Button(self.Left_frame,text="Cash",command=self.Cash_Amount,bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",20,"bold"))
                self.btn_Cash.grid(row=0,column=0)
                self.btn_dabet=Button(self.Left_frame,text="Cradit Card",bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",20,"bold"))
                self.btn_dabet.grid(row=1,column=0)
                self.btn_Cradit=Button(self.Left_frame,text="Debit Card",bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",20,"bold"))
                self.btn_Cradit.grid(row=2,column=0)
                self.office="add_tenders"
                self.disable_btn()
            
    def Cash_Amount(self):
            
        self.Left_frame.destroy()
        self.office="cash_amount"
        # print(self.office)
        self.Left_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Left_frame.place(x=10,y=10,width=660,height=550)
        self.info=Label(self.Left_frame,text="Info",bg=self.tander_color,height=5)
        self.info.grid(row=0,column=0,sticky="nsew",padx=0)
        self.Task =Label(self.Left_frame, text="Tasks",bg=self.tander_color,)
        self.Task.grid(row=0,column=1,sticky="nsew",padx=2)
        self.Goals =Label(self.Left_frame, text="Goals",bg=self.tander_color,)
        self.Goals.grid(row=0,column=2,sticky="nsew",padx=0)
        self.Message =Label(self.Left_frame, text="Message",bg=self.tander_color)
        self.Message.grid(row=0,column=3,sticky="nsew",padx=2)
        self.Keyboard =Label(self.Left_frame, text="Keyboard",bg=self.tander_color)
        self.Keyboard.grid(row=0,column=4,sticky="nsew",padx=0)
        self.Left_frame.grid_columnconfigure(0,weight=1)
        self.Left_frame.grid_columnconfigure(1,weight=1)
        self.Left_frame.grid_columnconfigure(2,weight=1)
        self.Left_frame.grid_columnconfigure(3,weight=1)
        self.Left_frame.grid_columnconfigure(4,weight=1)
        
        #====================billing frame
        self.C_billing_fram=Frame(self.Left_frame,bd=1,relief=RIDGE,bg="white")
        self.C_billing_fram.place(x=20,y=85,width=400,height=300) 
        title=Label(self.C_billing_fram,text="Customer Billing Area",font=("goudy old style",20,"bold"),bg="red",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(self.C_billing_fram,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(self.C_billing_fram,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
        self.Left_frame_text_Area=Frame(self.Left_frame,bd=1,relief=RIDGE,bg=self.tander_color)
        self.Left_frame_text_Area.place(x=0,y=400,width=655,height=145)
        self.var_price.set(str(self.pro_price_sum))
        self.lbl_Rl =Label(self.Left_frame_text_Area,text="Enter Amount",font=("goudy old style",20),bg=self.tander_color)
        self.lbl_Rl.grid(row=0,column=0,sticky="w",padx=10,pady=5)
        self.txt_Price =Entry(self.Left_frame_text_Area,textvariable=self.var_price,bg="white",fg='black',font=("goudy old style",20))
        self.txt_Price.grid(row=1,column=0,sticky="w",padx=10,pady=5)
        # self.lbl_LP =Label(self.Left_frame_text_Area, text="Enter Login and Password",font=("goudy old style",20),bg=self.tander_color)
        # self.lbl_LP.grid(row=2,column=0,sticky="w",padx=10,pady=5)
        self.Left_frame_text_Area.grid_columnconfigure(0,weight=1)

        self.txt_Price.bind("<Return>",self.Enter_btn)

    def price_total(self):
        #     print(self.pro_price_sum)
        #     print(self.var_price.get())
        #     messagebox.showinfo("Price"," Due amount zero",parent=self.root)
        # if int(self.var_price.get())==self.pro_price_sum:
        #         messagebox.showinfo("Price"," Due amount zero",parent=self.root)
        bill.bill_Generate(self)
    def disable_btn(self):
        self.btn0.config(text="Cancle \n Sale",bg= self.sales_color , fg= "white",command=self.Cancel_Sales,state="disabled")
        self.btn1.config(text="Help",bg=self.sales_color,fg="white",command=self.Window_Help,state="disabled")
        self.btn2.config(text="Return\nItem",bg= self.sales_color , fg= "white",command=self.Return_Item,state="disabled")
        self.btn3.config(text="Change\nItem",bg= self.sales_color , fg= "white",command=self.Change_item,state="disabled")
        self.btn4.config(text="Add\nDiscount",bg= self.sales_color , fg= "white",command=self.Discount,state="disabled")
        self.btn5.config(text="Sell\nNon-Merch",bg= self.sales_color , fg= "white",command=self.Sell_non_merch,state="disabled")
        self.btn6.config(text="Gift\nReceipt",bg= self.sales_color , fg= "white",command=self.Gift_Receipt,state="disabled")
        self.btn7.config(text="Extended\nTransaction",bg= self.sales_color , fg= "white",command=self.Extended_trans,state="disabled")
        self.btn8.config(text="Register\nOption",bg= self.sales_color , fg= "white",command=self.Register_Option,state="disabled")
        self.btn9.config(text="Find\nItem",bg= self.sales_color , fg= "white",command=self.Find_Item,state="disabled")
        self.btn10.config(text="Add\nTenders",bg= self.sales_color , fg= "white",command=self.Add_Tenders,state="disabled")
        self.btn11.config(text="Customer\nOptions",bg= self.sales_color , fg= "white",command=self.Customer_Option,state="disabled")
        self.btn12.config(text="Suspend\nTransection",bg= self.sales_color , fg= "white",command=self.Suspend_transection,state="disabled")  
    def disable_btn_FO_BO(self):
        self.btn0.config(text="Exit",font=("goudy old style",10,"bold"), fg= "white",command=self.Cancel_Sales,state="disabled")
        self.btn1.config(text="Help",font=("goudy old style",10,"bold"), fg= "white",command=self.Cancel_Sales,state="disabled")
        self.btn2.config(text="Clock\nIn\out\n\nF2",fg="white",command=self.Window_Help,state="disabled")
        self.btn3.config(text="View\nSchedule\n&time\nF3",fg= "white",command=self.Return_Item,state="disabled")
        self.btn4.config(text="Change\nPassword\n\nF4", fg= "white",command=self.Change_item,state="disabled")
        self.btn5.config(text="Receipt\nReprint\nOptions\nF5", fg= "white",command=self.Discount,state="disabled")
        self.btn6.config(text="Balance\nInqury\n\nF6", fg= "white",command=self.Sell_non_merch,state="disabled")
        self.btn7.config(text="Testing \n Mode\n\nF7", fg= "white",command=self.Gift_Receipt,state="disabled")
        self.btn8.config(text="My Task\n\n\nF8", fg= "white",command=self.Extended_trans,state="disabled")
        self.btn9.config(text="Find \n Item\n\nF9", fg= "white",command=self.Register_Option,state="disabled")
        self.btn10.config(text="Till\n\n\nF10", fg= "white",command=self.Find_Item,state="disabled")
        self.btn11.config(text="Flash\nSales\n\nF11", fg= "white",command=self.Add_Tenders,state="disabled")
        self.btn12.config(text="Back\nOffice\n\nF12", fg= "white",command=self.Customer_Option,state="disabled")
        # self.btn12.config(text="Back\nOffice\n\nF12", , fg= "white",command=self.Suspend_transection,state="disabled")      
            
                       
    def Active_btn(self):
            
        self.btn0.config(text="Cancle \n Sale",bg= self.sales_color , fg= "white",command=self.Cancel_Sales,state="normal")
        self.btn1.config(text="Help",bg=self.sales_color,fg="white",command=self.Window_Help,state="normal")
        self.btn2.config(text="Return\nItem",bg= self.sales_color , fg= "white",command=self.Return_Item,state="normal")
        self.btn3.config(text="Change\nItem",bg= self.sales_color , fg= "white",command=self.Change_item,state="normal")
        self.btn4.config(text="Add\nDiscount",bg= self.sales_color , fg= "white",command=self.Discount,state="normal")
        self.btn5.config(text="Sell\nNon-Merch",bg= self.sales_color , fg= "white",command=self.Sell_non_merch,state="normal")
        self.btn6.config(text="Gift\nReceipt",bg= self.sales_color , fg= "white",command=self.Gift_Receipt,state="normal")
        self.btn7.config(text="Extended\nTransaction",bg= self.sales_color , fg= "white",command=self.Extended_trans,state="normal")
        self.btn8.config(text="Register\nOption",bg= self.sales_color , fg= "white",command=self.Register_Option,state="normal")
        self.btn9.config(text="Find\nItem",bg= self.sales_color , fg= "white",command=self.Find_Item,state="normal")
        self.btn10.config(text="Add\nTenders",bg= self.sales_color , fg= "white",command=self.Add_Tenders,state="normal")
        self.btn11.config(text="Customer\nOptions",bg= self.sales_color , fg= "white",command=self.Customer_Option,state="normal")
        self.btn12.config(text="Suspend\nTransection",bg= self.sales_color , fg= "white",command=self.Suspend_transection,state="normal")
        #     self.btn_Cash.config(state="active")             
        #     messagebox.showinfo("Price","price",parent=self.root)   
    def Ai_frame_Function(self):
        self.Ai_frame="Active"
        self.Ai_find_item_frame=Frame(self.Left_frame,bd=3,relief=RIDGE)
        self.Ai_find_item_frame.place(x=0,y=200,width=660,height=200)
        scrolly=Scrollbar(self.Ai_find_item_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.Ai_find_item_frame,orient=HORIZONTAL)
        # self.Ai_find_item_table=ttk.Treeview(self.Ai_find_item_frame,columns=("Transection_no","name","Unit_price","qty","Ext_price"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.Ai_find_item_table=ttk.Treeview(self.Ai_find_item_frame,columns=("Product_name","Product_code","qty","C_P_U"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Ai_find_item_table.xview)
        scrolly.config(command=self.Ai_find_item_table.yview)
        #====headings ===========================  # Product_name,Product_code,qty,C_P_U
        # self.Ai_find_item_table.heading("Transection_no",text=" my Trans #")


        self.Ai_find_item_table.heading("Product_name",text=" Product Name")
        self.Ai_find_item_table.heading("Product_code",text="Code")
        self.Ai_find_item_table.heading("qty",text="QTY")
        self.Ai_find_item_table.heading("C_P_U",text="Unit Price")

        #========colom width ====================

        self.Ai_find_item_table.column("Product_name",width=60)
        self.Ai_find_item_table.column("Product_code",width=60)
        # self.Ai_find_item_table.column("Unit_price",width=60)
        self.Ai_find_item_table.column("qty",width=60)
        self.Ai_find_item_table.column("C_P_U",width=60)

        self.Ai_find_item_table["show"]="headings"
        self.Ai_find_item_table.pack(fill=BOTH,expand=1)
        # self.Ai_find_item_table.tag_configure('return', background='red', foreground='white')
        # self.Ai_find_item_table.tag_configure('sales', background='#2d5bb9', foreground='white')
        # self.Ai_find_item_table.bind("<ButtonRelease-1>",self.get_data)
        self.Ai_find_item_table.delete(*self.Ai_find_item_table.get_children())
        self.Ai_find_item_table.bind("<ButtonRelease-1>",self.get_from_Ai_table)
        for row in self.Ai_find_list:
            self.Ai_find_item_table.insert('',END,values=row)
                # self.Ai_find_item_table.insert('',END,values=)
    
    def get_data(self,ev):
        
        f=self.ProductsTable.focus()
        content=(self.ProductsTable.item(f))
        self.change_qty=content['values']    

        real_coords = (self.ProductsTable.winfo_pointerx() - self.ProductsTable.winfo_rootx(),
                       self.ProductsTable.winfo_pointery() - self.ProductsTable.winfo_rooty())
        item = self.ProductsTable.identify("row",*real_coords)
       
        
        self.my_row=self.ProductsTable.item(item)['text']
        print(self.my_row)
        
    def Delete_row(self):
        if int(self.my_row)<0:
           messagebox.showerror("Error","Please Select Product from the list",parent=self.root)
        else:
                # print("abc",(self.my_row))
                # print(self.cart_list)
                self.cart_list.pop(int(self.my_row))
                self.transection_no()
                self.output_frame()  
                self.my_row="-1"  
    def Change_Qty(self):
        self.office="change_qty"
        
        print(self.change_qty[2])
        self.sales_item_id.set(self.change_qty[2])
        
        
                           
    def return_window(self):
        self.office="return_window"   
        # print("after escap",self.office) 
        self.info.config(bg= self.return_color , fg= "white")
        self.Task.config(bg= self.return_color , fg= "white")
        self.Goals.config(bg= self.return_color , fg= "white")
        self.Message.config(bg= self.return_color , fg= "white")
        self.Keyboard.config(bg= self.return_color , fg= "white")
        self.lbl_Rl.config(bg= self.return_color, fg= "white" ,text="Scan Item or UPC")
        self.lbl_LP.config(bg= self.return_color, fg= "white")
        self.Left_frame_text_Area.config(bg= self.return_color,)
        # self.txt_Login.config(textvariable=self.product_name)
        self.txt_Login.config(show="",textvariable=self.sales_item_id)
        self.lbl_LP.config(text="Scan or Key an item ID ")  
        self.btn2.config(text="Exit\nReturn",bg= self.sales_color , fg= "white",command=self.Exit_Return)    
    def AI_btn(self):
        self.AI_frame=Frame(self.Left_frame,bd=0,relief=RIDGE,bg=self.sales_color,)
        self.AI_frame.place(x=350,y=405,width=200,height=130)    
        self.on = PhotoImage(file = "images_f/on.png")
        self.off = PhotoImage(file = "images_f/off.png")
        
        self.my_label = Label(self.AI_frame,text = "The Switch is Off",fg = "green",font = ("Helvetica",15),bg=self.sales_color)
        self.my_label.grid(row=0,column=0,sticky="w",padx=10,pady=5)
        self.on_button = Button(self.AI_frame, image = self.off,bg=self.sales_color,fg = self.sales_color, bd = 2,command = self.switch)
        self.on_button.grid(row=1,column=0,sticky="w",padx=10,pady=5)
    
#     def delay(self):
#         self.delay.after(2000,self.takeCommand())
        
    def switch(self):
        if self.is_on=="True":
          self.is_on = "False" 
          self.on_button.config(image = self.on,fg=self.sales_color,)
          self.my_label.config(text ="AI Listening...",fg = "grey")
          if self.Ai_frame=="Active":
                self.Ai_find_item_frame.destroy()
                self.Ai_frame=""
          self.on_button.after(200,lambda:self.takeCommand())
        else:
          self.on_button.config(image = self.off,fg=self.sales_color,)
          self.my_label.config(text = "The Switch is Off ", fg = "red")
          self.is_on = "True"
          if self.Ai_frame=="Active":
             self.Ai_find_item_frame.destroy()
             self.Ai_frame=""
        # if call_Ai=="Active":
        #         root.after(2000,self.takeCommand())  
    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=1)
                print("Listening...1")
                r.pause_threshold = 1 
                audio = r.listen(source)

        try:
                print("Recognizing...")    
                self.query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
                print(f"User said: {self.query}\n")  #User query will be printed.
                self.switch()
                self.search_from_db()

        except Exception as e:
                print(e)    
                # self.takeCommand()
                messagebox.showerror("Error","Can't here \nSay that again please...",parent=self.root)
                # print("Say that again please...")   #Say that again will be printed in case of improper voice 
                self.switch()
                return "None" #None string will be returned
        # return self.query.lower() 
   
    def search_from_db(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        query=self.query.lower()
        del self.Ai_find_list[:]
        try:
                # Product_name,Product_code,qty,C_P_U,pid,Brand from products where Product_code
            cur.execute("select Product_name,Product_code,qty,C_P_U,pid,Brand from products where Product_name LIKE '%"+query+"%'")
            # cur.execute("select Product_name,Product_code,qty,C_P_U,pid,Brand from products where Product_name=?",(query,))
            rows=cur.fetchall()
            for row in rows:
                self.Ai_find_list.append(row)
            print(rows)
            self.Ai_frame_Function()
        except Exception as e:
            print("Error ",e)   
    def get_from_Ai_table(self,ev):
        f=self.Ai_find_item_table.focus()
        content=(self.Ai_find_item_table.item(f))
        row=content['values']
        # print(row)
        
        self.sales_item_id.set(row[1])
        self.txt_Login.focus_set()
        # self.produc.set(row[0]),       
    def Exit_Return(self):
        self.FO_left_frame_()
        self.sales_left_frame_config() 
        self.btn2.config(text="Return\nItem",bg= self.sales_color , fg= "white",command=self.Return_Item)  
        
#=======================All Functions=================
    def login(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            if self.login_pass[0]=="" or self.login_pass[1]=="":
                messagebox.showerror("Error","Login or Password field is empty",parent=self.root)
            else:
                cur.execute("select utype ,name from employee where loginID=? AND pass=?",(self.login_pass[0],self.login_pass[1]))
                user=cur.fetchone()
                if not user:
                    messagebox.showerror("Error","Invalid user EmployeeID|Password",parent=self.root)
                #     self.login_pass[:]
                #     print()
                    self.Check_state()
                elif user[0]=="SM":
                        self.user_info.append(user[1])
                        self.user_info.append(self.login_pass[0])
                        self.user_name=user[1]
                        if self.office=="FO":
                           self.R_login.config(text=f"{self.user_name}")     
                           self.Sales_window()
                        if self.office=="BO":
                           self.Back_Office_window()
                        if self.office=="Clock":
                           self.login_pass.append(user[1])
                           C_in_out.Btn_Menu_frame(self,self.login_pass)  
                        #    self.office="Clock"
                        if self.office=="View time":
                               C_in_out.view_card(self) 
                        if self.office=="Change_pass":
                               C_P.Confirm_password(self,self.login_pass)
                                
                elif user[0]=="SA":
                     self.user_name=user[1]   
                     self.R_login.config(text=f"{self.user_name}")
                     self.Sales_window()
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}",parent=self.root)            


#========================  Search Function======================
      
    def search(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
        
        #         # cur.execute("select * from products where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
        #         cur.execute("select * from products where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
        # Product_name text,Product_code text,qty text,C_P_U
             cur.execute("select Product_name,Product_code,qty,C_P_U,pid,Brand from products where Product_code=?",(self.sales_item_id.get(),))
             rows=cur.fetchone()
             if  self.office=="return_window":
                # rows.append("return")
                y=list(rows)
                y.append("return")
                y[3]="-"+y[3]
                y[2]="1"
                # print(y)
                x = tuple(y)
                self.cart_list.append(x)
                # cart_data=x
             else:
                y=list(rows)
                y.append("sale")
                y[2]="1"
                
                # print(y)
                x = tuple(y)
                self.cart_list.append(x)
                     
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
    def Clock_in_out_fun(self):
            self.disable_btn_FO_BO()
            C_in_out.Clock_in_out_Function(self,root)
            
    def View_Schedule(self):
        self.disable_btn_FO_BO()    
        C_in_out.Schedule_Function(self,root)
    def Change_Password(self):
        self.disable_btn_FO_BO()
        C_P.Change_password(self,root)   
        # C_in_out.Schedule_Function(self,root)                     
 
                  
             
if __name__=="__main__":        
    root=Tk()
    obj=FO_window_Class(root)
    root.mainloop()