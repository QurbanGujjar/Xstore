from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import time
import sqlite3
from Cash_count import Cash_count_Class as CCC
from inventry_manage import inventryManageClass as imc
class BO_window_Class: 
    def BO_Function(self,root): 
        self.BO_office='BO'
        self.Main_frame=Frame(self.root,bd=0)
        self.Main_frame.place(x=0,y=0,width=1350,height=700)
        self.business_date_check()
        self.Outer_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Outer_frame.place(x=350,y=10,width=550,height=555)
        # Top frame
        self.Top_frame=Frame(self.Outer_frame,bd=3,relief=RIDGE)
        self.Top_frame.place(x=0,y=0,width=545,height=75)
        
        BO_window_Class.Main_menu(self)
        # Menu frame
        BO_window_Class.Btn_Menu_frame(self)
        
        
    def Main_menu(self):
        # Middle frame
        
        self.Middle_frame=Frame(self.Outer_frame,bd=0,relief=RIDGE)
        self.Middle_frame.place(x=80,y=75,width=348,height=380)
    
        self.btn_Associate =Button(self.Middle_frame,text="1 \t Assocaite",bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",19,"bold"))
        self.btn_Associate.grid(row=0,column=0)
        self.btn_Customer=Button(self.Middle_frame,text="2 \t Customer",bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",19,"bold"))
        self.btn_Customer.grid(row=1,column=0)
        self.btn_Employee=Button(self.Middle_frame,text="3 \t Employee",bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",19,"bold"))
        self.btn_Employee.grid(row=2,column=0)  
        self.btn_Hardware=Button(self.Middle_frame,text="4 \t Hardware",bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",19,"bold"))
        self.btn_Hardware.grid(row=3,column=0)
        self.btn_Inventory=Button(self.Middle_frame,text="5 \t Inventory",command=lambda:BO_window_Class.inventry(self),bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",19,"bold"))
        self.btn_Inventory.grid(row=4,column=0)
        self.btn_Reporting=Button(self.Middle_frame,text="6 \t Reporting",command=lambda:BO_window_Class.Reporting(self), bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",19,"bold"))
        self.btn_Reporting.grid(row=5,column=0)
        self.btn_Till=Button(self.Middle_frame,text="7 \t Till",command=lambda:BO_window_Class.Till_btn(self),bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",19,"bold"))
        self.btn_Till.grid(row=6,column=0) 
        # self.BO_office='BO'
        self.BO_office='BO_menu'
        self.Start_date=StringVar()
        self.End_date=StringVar()  
        self.trans_type=StringVar()   
        self.data=[]
    def inventry(self):
        # self.Outer_frame.destroy()
        # imc.inventryManage(self,self.root)  
        pass  
    def Btn_Menu_frame(self):
        
        self.Menu_frame=Frame(self.Outer_frame,bd=0,relief=RIDGE)
        self.Menu_frame.place(x=80,y=455,width=350,height=90) 
        # print("Buttons frame")
        self.btn_back =Button(self.Menu_frame,text="Back",command= lambda:BO_window_Class.Back(self),bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_back.grid(row=0,column=0)
        self.btn_help=Button(self.Menu_frame,text="Help",bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_help.grid(row=0,column=1)
        self.btn_ok=Button(self.Menu_frame,text="OK",command= lambda:BO_window_Class.ok_btn(self), bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_ok.grid(row=0,column=2)     
        self.btn_Register=Button(self.Menu_frame,text="Register",command= lambda:BO_window_Class.Back_to_sales_win(self),bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_Register.grid(row=0,column=3)
    def Back_to_sales_win(self):
        self.business_date_check()
        self.Outer_frame.destroy()
        
        self.Sales_window()
    def Reporting(self):
        self.BO_office="Reporting"
        self.btn_Associate.config(text="1 Sales Report",command=lambda:BO_window_Class.Reports_Frame(self,"sale",self.BO_office))
        self.btn_Customer.config(text="2 Return Report",command=lambda:BO_window_Class.Reports_Frame(self,'return',self.BO_office))
        self.btn_Employee.config(text="3 Employee Report",)
        self.btn_Hardware.config(text="4 Stock Report",command= lambda:BO_window_Class.Run_Report(self))
        self.btn_Inventory.config(text="5 Cancel Report",)
        self.btn_Reporting.config(text="6 Report",)
        self.btn_Till.config(text="7 Till Report",command= lambda:BO_window_Class.Till_btn(self))
        
    def Till_btn(self):
        self.BO_office="Till_btn"
        self.btn_Associate.config(text="1 \t Open/Close Option",command= lambda:BO_window_Class.Till_open_close_option(self))
        self.btn_Customer.config(text="2 \t Bank Maintainence",)
        self.btn_Employee.config(text="3 \t Till Option",command= lambda:BO_window_Class.Till_Option(self))
        self.btn_Hardware.config(text="4 \t Stock Report",command= lambda:BO_window_Class.Run_Report(self),state="disable")
        self.btn_Inventory.config(state="disable")
        self.btn_Reporting.config(state="disable")
        self.btn_Till.config(state="disable")
        print(self.BO_office)
    def Till_Option(self):
        self.BO_office="Till_Option"
        self.btn_Associate.config(text="1 \t Till Audit",command= lambda:BO_window_Class.Till_Audit(self))
        self.btn_Customer.config(text="2 \t No Sale",)
        self.btn_Employee.config(text="3 \t Paid In",state="disable")
        self.btn_Hardware.config(text="4 \t Paid Out",state="disable")
        self.btn_Inventory.config(text="4 \t Post Void",state="disable")
        self.btn_Reporting.config(state="disable")
        self.btn_Till.config(state="disable")
        print(self.BO_office)
            
    def Till_Audit(self):
        CCC.CashCount(self,self.root)
            
    def check_S_R_button(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            cur.execute("select * from business_date")
            rows=cur.fetchall()
            # print(len(rows))
            len(rows)
            if len(rows)==0:
                pass
            else:
                    if rows[len(rows)-1][6]=="open" and  rows[len(rows)-1][7]=="open":
                            self.btn_Associate.config(text="1 \t Register Close",command= lambda:BO_window_Class.Register_close(self))
                            self.btn_Customer.config(text="2 \t Store Close",command= lambda:BO_window_Class.Store_close(self))
                    elif rows[len(rows)-1][6]=="open" and  rows[len(rows)-1][7]=="close":
                            self.btn_Associate.config(text="1 \t Register Open",)
                            self.btn_Customer.config(text="2 \t Store Close",command= lambda:BO_window_Class.Store_close(self))

                    else:    
                           pass   
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}",parent=self.root)            
      
        
    def Register_close(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            cur.execute("select * from business_date")
            rows=cur.fetchall()
            # print(len(rows))
            if rows[len(rows)-1][6]=="open" and  rows[len(rows)-1][7]=="open": 
                # print(rows[3])  
                op=messagebox.askyesno("Confirm",f"Do You Want to Close Register of {rows[len(rows)-1][3]} date ?",parent=self.root)
                if op==True:
                    messagebox.showinfo("Success","Start your counting",parent=self.root)
                    BO_window_Class.Reg_close(self)
                   
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}",parent=self.root)
    def Reg_close(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            cur.execute("insert into business_date(name ,eid ,Date ,day ,time ,store,register ) values(?,?,?,?,?,?,?)",(
            self.user_info[0],
            self.user_info[1],
            time.strftime("%Y/%m/%d"),
            time.strftime("%A"),
            time.strftime("%H:%M:%S"),
            "open",
            "close"
            ))   
            con.commit()
            BO_window_Class.Register_close_color(self)
            BO_window_Class.Till_open_close_option(self)
            # self.Register.config(bg="green")
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}",parent=self.root)        
    def Store_open_color(self):
        self.shop_name.config(bg="green") 
    def Store_close_color(self):
        self.shop_name.config(bg="Red")            
                         
    def Register_close_color(self):
        self.Register.config(bg="Red")
        
       
        # pass
        
    def Store_close(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            cur.execute("select * from business_date")
            rows=cur.fetchall()
            # print(len(rows))
            len(rows)
            if len(rows)==0:
                self.footer_frame_()
            else:
                    if rows[len(rows)-1][6]=="open" and  rows[len(rows)-1][7]=="close":
                        messagebox.showinfo("Success","Are you sure want to close store",parent=self.root)
                        BO_window_Class.Store_close_color(self)                     
        
                        cur.execute("update business_date set store =?  WHERE time=?",(
                        "close",
                        rows[len(rows)-1][5]
                        ))  
                    con.commit()
            BO_window_Class.Till_open_close_option(self)        
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}",parent=self.root)                     
        
        # pass         
    def Till_open_close_option(self):
        self.BO_office="Till_open_close_option"
        self.btn_Associate.config(text="1 \t Register Open")
        self.btn_Customer.config(text="2 \t Store Open",command= lambda:BO_window_Class.Store_open(self))
        self.btn_Employee.config(text="3 \t Employee Report",state="disable")
        self.btn_Hardware.config(text="4 \t Stock Report",command= lambda:BO_window_Class.Run_Report(self),state="disable")
        self.btn_Inventory.config(state="disable")
        self.btn_Reporting.config(state="disable")
        self.btn_Till.config(state="disable")
        BO_window_Class.check_S_R_button(self)
        # print("Register open close")   
        print(self.BO_office)        
    def Back(self):
        print(self.BO_office)
        if self.BO_office=="BO_menu" or self.BO_office=="BO":
            self.Outer_frame.destroy()
            self.Front_office()
            self.Back_office()
            self.business_date_check()
        if self.BO_office=="FO":
            self.Outer_frame.destroy()
            # self.Front_office()
            self.Front_office()  
            self.business_date_check()
        elif self.BO_office=="Reporting":
            self.Outer_frame.destroy()
            BO_window_Class.BO_Function(self,self.root)
            self.business_date_check()
            
        elif self.BO_office=="Stock_Report":
            self.Outer_frame.destroy()
            BO_window_Class.BO_Function(self,self.root)
            BO_window_Class.Reporting(self)
            self.business_date_check()
        elif self.BO_office=="Sales_Report":
                self.Outer_frame.destroy()
                BO_window_Class.BO_Function(self,self.root)
                BO_window_Class.Reporting(self)
                self.business_date_check()
        elif self.BO_office=="Till_btn":
                self.Outer_frame.destroy()
                BO_window_Class.BO_Function(self,self.root)
                self.business_date_check()
        elif self.BO_office=="Till_open_close_option":
                self.Outer_frame.destroy()
                BO_window_Class.BO_Function(self,self.root) 
                BO_window_Class.Till_btn(self)       
                self.business_date_check()
        elif self.BO_office=="Till_Option":
                self.Outer_frame.destroy()
                BO_window_Class.BO_Function(self,self.root)
                self.business_date_check()
                BO_window_Class.Till_btn(self)        
                # BO_window_Class.Reporting(self)        
    def Store_open(self):
        op=messagebox.askyesno("Confirm",f"Do You Want to open store at {time.strftime('%d/%m/%y')} date ?",parent=self.root)
        if op==True:
            BO_window_Class.Store_open_color(self)
            # BO_window_Class.Till_open_close_option(self)
            # self.shop_name.config(bg="Green")
            Regis=messagebox.askyesno("Confirm",f"Do You Want to open Register ",parent=self.root)
            if Regis==True:
                messagebox.showinfo("Success","Start your counting",parent=self.root)
                BO_window_Class.Reg_open(self)
               
                
                
            else:
                self.Outer_frame.destroy()
                BO_window_Class.BO_Function(self,self.root) 
                BO_window_Class.Till_btn(self)
                    
        else:
            messagebox.showerror("Error","You can't start new Business",parent=self.root)     
        
        
        # messagebox.showwarning("Warning",f"Do You Want to open store {time.strftime('%d/%m/%y')}")            
            
    def Reg_open(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            cur.execute("insert into business_date(name ,eid ,Date ,day ,time ,store,register ) values(?,?,?,?,?,?,?)",(
            self.user_info[0],
            self.user_info[1],
            time.strftime("%Y/%m/%d"),
            time.strftime("%A"),
            time.strftime("%H:%M:%S"),
            "open",
            "open"
            ))   
            con.commit()
            self.Register.config(bg="green")
            BO_window_Class.Till_open_close_option(self)
        except Exception as ex:
            messagebox.showerror("Error",f"Error Due to {str(ex)}",parent=self.root)

       
    def Reports_Frame(self,trans_type,office):
        
        self.BO_office=office
        
        print(self.BO_office)
        self.Start_date.set(time.strftime("%Y/%m/%d"))
        self.End_date.set(time.strftime("%Y/%m/%d"))
        self.trans_type=trans_type    
        self.Outer_frame.destroy()
        self.Outer_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Outer_frame.place(x=0,y=0,width=1350,height=660)    
        
        self.Top_frame=Frame(self.Outer_frame,bd=3,relief=RIDGE)
        self.Top_frame.place(x=350,y=10,width=550,height=550)
        self.lbl_Rl =Label(self.Top_frame,text="Enter Starting Date",font=("goudy old style",20),bg=self.FO_color)
        self.lbl_Rl.grid(row=0,column=0,sticky="w",padx=10,pady=5)
        self.txt_start_date =Entry(self.Top_frame,textvariable=self.Start_date,bg="white",fg='black',font=("goudy old style",20))
        self.txt_start_date.grid(row=0,column=1,sticky="w",padx=10,pady=5)
        self.lbl_Rl =Label(self.Top_frame,text="Enter Ending Date",font=("goudy old style",20),bg=self.FO_color)
        self.lbl_Rl.grid(row=1,column=0,sticky="w",padx=10,pady=5)
        self.txt_end_date =Entry(self.Top_frame,textvariable=self.End_date,bg="white",fg='black',font=("goudy old style",20))
        self.txt_end_date.grid(row=1,column=1,sticky="w",padx=10,pady=5)
        # self.txt_end_date.bind("<Return>",self, BO_window_Class.focus2,)
        # self.txt_start_date.bind("<Return>", BO_window_Class.focus1,self)
        self.txt_start_date.focus_set()
        

        BO_window_Class.Btn_Menu_frame(self)
        self.Menu_frame.place(x=450,y=450)
        
        
        
    def Run_Report(self):
        self.Outer_frame.destroy()
        self.Menu_frame.destroy()
        self.Outer_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Outer_frame.place(x=0,y=0,width=1350,height=660) 
        Product_frame=Frame(self.Outer_frame,bd=3,relief=RIDGE)
        Product_frame.place(x=1,y=1,width=1350,height=405)
        scrolly=Scrollbar(Product_frame,orient=VERTICAL)
        scrollx=Scrollbar(Product_frame,orient=HORIZONTAL)
        self.ProductsTable=ttk.Treeview(Product_frame,columns=("pid","Warehouse","Brand","name","code","qty","CPU","TC","status"),yscrollcommand=scrolly.set,xscrollcommand=scrolly.set)
       
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductsTable.xview)
        scrolly.config(command=self.ProductsTable.yview)
       #====headings ===========================
        self.ProductsTable.heading("pid",text="P ID")
        self.ProductsTable.heading("Warehouse",text="Warehouse")
        self.ProductsTable.heading("Brand",text="Brand")
        self.ProductsTable.heading("name",text="Product Name")
        self.ProductsTable.heading("code",text="Product Code")
        self.ProductsTable.heading("qty",text="QTY")
        self.ProductsTable.heading("CPU",text="Cost Pre Unit")
        self.ProductsTable.heading("TC",text="Total Cost")
        self.ProductsTable.heading("status",text="Status")
        #========colom width ====================
        self.ProductsTable.column("pid",width=10)
        self.ProductsTable.column("Warehouse",width=10)
        self.ProductsTable.column("Brand",width=10)
        self.ProductsTable.column("name",width=40)
        self.ProductsTable.column("code",width=10)
        self.ProductsTable.column("qty",width=40)
        self.ProductsTable.column("CPU",width=40)
        self.ProductsTable.column("TC",width=10)
        self.ProductsTable.column("status",width=40)
        self.ProductsTable["show"]="headings"
        self.ProductsTable.pack(fill=BOTH,expand=1)
        BO_window_Class.My_invoice(self)
        BO_window_Class.Total_calculations(self)
        self.trans_frame_total.place(x=1,y=400)
        self.tander.insert('',END,values=self.data) 
        BO_window_Class.Btn_Menu_frame(self)
        self.Menu_frame.place(x=450,y=550)
        self.BO_office="Stock_Report"
        
        # self.ProductsTable.bind("<ButtonRelease-1>",self.get_data)  
        
    def My_invoice(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from products")
            rows=cur.fetchall()        
            self.ProductsTable.delete(*self.ProductsTable.get_children())   
            qty_sum=0
            cost_sum=0     
            for row in rows:
                qty_sum+=int(row[5])
                cost_sum+=int(row[7])
                self.ProductsTable.insert('',END,values=row) 
            self.data=["","",str(qty_sum),str(cost_sum)]
                
                   
        except Exception as ex:
               messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def ok_btn(self):
        if  self.BO_office=="Reporting" or self.BO_office=="BO" or self.BO_office=="FO":
            
            if self.Start_date.get()=="" and self.End_date.get()=="":
                messagebox.showerror("Error",f"Please enter starting and ending date first",parent=self.root) 
            else:    
                con=sqlite3.connect(database=r"xStore.db")
                cur=con.cursor()
                try:
                    print(self.trans_type)
                    
                    cur.execute(f"SELECT * FROM salesTable WHERE TransType=='{self.trans_type}' and Date BETWEEN '{self.Start_date.get()}' AND '{self.End_date.get()}'")
                    rows=cur.fetchall()
                    BO_window_Class.sales_Report_display(self)
                    # BO_window_Class.Total_calculations(self)
                    qty_sum=0
                    cost_sum=0
                    for row in rows:
                        
                        # self.ProductsTable.insert('',END,values=row)
                        qty_sum+=int(row[6])
                        cost_sum+=int(row[5])
                        self.ProductsTable.insert('',END,values=row) 
                        self.data=["","",str(qty_sum),str(cost_sum)]
                    self.tander.insert('',END,values=self.data) 
                    self.tander.heading("Tax",text="Sub Total") 
                    self.tander.heading("fee",text="Qty")              
                    BO_window_Class.Btn_Menu_frame(self)
                    self.Menu_frame.place(x=450,y=550)
                    
                except Exception as ex:
                    messagebox.showerror("Error",f"Error Due to {str(ex)}",parent=self.root)   
        # else:
        #     pass                 

    def sales_Report_display(self):
        self.Outer_frame.destroy()
        self.Menu_frame.destroy()
        self.Outer_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Outer_frame.place(x=0,y=0,width=1350,height=660) 
        Product_frame=Frame(self.Outer_frame,bd=3,relief=RIDGE)
        Product_frame.place(x=1,y=1,width=1350,height=405)
        scrolly=Scrollbar(Product_frame,orient=VERTICAL)
        scrollx=Scrollbar(Product_frame,orient=HORIZONTAL)
        self.ProductsTable=ttk.Treeview(Product_frame,columns=("Date","Invoice_no","Brand","name","code","Price","qty","Type","Sales_Person","Casher"),yscrollcommand=scrolly.set,xscrollcommand=scrolly.set)
       
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductsTable.xview)
        scrolly.config(command=self.ProductsTable.yview)
       #====headings ===========================
        # self.ProductsTable.heading("pid",text="P ID")
        self.ProductsTable.heading("Date",text="Date")
        self.ProductsTable.heading("Invoice_no",text="Invoice_no")
        self.ProductsTable.heading("Brand",text="Brand")
        self.ProductsTable.heading("name",text="Product Name")
        self.ProductsTable.heading("code",text="Product Code")
        self.ProductsTable.heading("Price",text="Exect Price")
        self.ProductsTable.heading("qty",text="Quantity")
        self.ProductsTable.heading("Type",text="Sales Type")
        self.ProductsTable.heading("Sales_Person",text="Sales Person")
        self.ProductsTable.heading("Casher",text="Casher")
        #========colom width ====================
        # self.ProductsTable.column("pid",width=10)
        self.ProductsTable.column("Date",width=10)
        self.ProductsTable.column("Invoice_no",width=10)
        self.ProductsTable.column("Brand",width=10)
        self.ProductsTable.column("name",width=40)
        self.ProductsTable.column("code",width=40)
        self.ProductsTable.column("Price",width=10)
        self.ProductsTable.column("qty",width=10)
        self.ProductsTable.column("Type",width=10)
        self.ProductsTable.column("Sales_Person",width=40)
        self.ProductsTable.column("Casher",width=40)
        self.ProductsTable["show"]="headings"
        self.ProductsTable.pack(fill=BOTH,expand=1)
        BO_window_Class.Total_calculations(self)
        self.trans_frame_total.place(x=1,y=400)
        BO_window_Class.Btn_Menu_frame(self)
        self.Menu_frame.place(x=450,y=550)
        if self.BO_office=="Reporting":
            self.BO_office="Sales_Report"
    def Total_calculations(self):
        self.trans_frame_total=Frame(self.Outer_frame,bd=3,relief=RIDGE)
        self.trans_frame_total.place(x=0,y=700,width=1350,height=120)
        scrolly=Scrollbar(self.trans_frame_total,orient=VERTICAL)
        scrollx=Scrollbar(self.trans_frame_total,orient=HORIZONTAL)
                # self.ProductsTable=ttk.Treeview(trans_frame_total,columns=("Transection_no","name","Unit_price","qty","Ext_price"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.tander=ttk.Treeview(self.trans_frame_total,columns=("Items","Tax","fee","sub_total"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
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
     
        
        

if __name__=="__main__":        
    root=Tk()
    obj=BO_window_Class(root)
    root.mainloop()                    