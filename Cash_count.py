from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
# from change_forget_pass import change_forget_password_Class as c_f_p
import time
import sqlite3
# from FO import FO_window_Class as FO_w
class Cash_count_Class:
    
    def CashCount(self,root):
        self.office="Till_Audit"
        self.list1=[1,0,1,"Rs"]
        self.list2=[2,0,2,"Rs"]
        self.list5=[5,0,5,"Rs"]
        self.list10=[10,0,10,"Rs"]
        self.list20=[20,0,20,"Rs"]
        self.list50=[50,0,50,"Rs"]
        self.list100=[100,0,100,"Rs"]
        self.list500=[500,0,500,"Rs"]
        self.list1000=[1000,0,1000,"Rs"]
        self.list5000=[5000,0,5000,"Rs"]
        self.Denomination_list=[self.list1,self.list2,self.list5,self.list10,self.list20,self.list50,self.list100,self.list500,self.list1000,self.list5000]
        self.row=[]
        # self.BO_frame_color="green"
        self.Front_office()
        self.BO_frame_color="green"
        self.Back_office()
        self.lbl_employee.destroy()
        Cash_count_Class.Cash_count_frame_function(self)
        self.disable_btn_FO_BO()
        # self.Right_frame
    
    
    def Cash_count_frame_function(self):
        self.total_CC=Label(self.Right_frame,text="Total Cash",font=("times new roman",20,"bold"))
        self.total_CC.place(x=400,y=500,width=260,height=40)
        # width=660,height=50)
        
        self.Cash_count_frame=Frame(self.Right_frame,bd=3,relief=RIDGE)
        self.Cash_count_frame.place(x=0,y=0,width=660,height=482)
        # scrolly=Scrollbar(self.Cash_count_frame,orient=VERTICAL)
        # scrollx=Scrollbar(self.Cash_count_frame,orient=HORIZONTAL)
        # self.Denomination_table=ttk.Treeview(self.Cash_count_frame,columns=("Transection_no","name","Unit_price","qty","Ext_price"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.Denomination_table=ttk.Treeview(self.Cash_count_frame,columns=("Denomination","Qty","@","Amount"))
        # scrollx.pack(side=BOTTOM,fill=X)
        # scrolly.pack(side=RIGHT,fill=Y)
        # scrollx.config(command=self.Denomination_table.xview)
        # scrolly.config(command=self.Denomination_table.yview)
        #====headings ===========================  # Product_name,Product_code,qty,C_P_U
        # self.Denomination_table.heading("Transection_no",text=" my Trans #")


        self.Denomination_table.heading("Denomination",text="Denomination")
        self.Denomination_table.heading("Qty",text="Qty")
        self.Denomination_table.heading("@",text="@")
        self.Denomination_table.heading("Amount",text="Amount")

        #========colom width ====================

        self.Denomination_table.column("Denomination",width=60)
        self.Denomination_table.column("Qty",width=60)
        # self.Denomination_table.column("Unit_price",width=60)
        self.Denomination_table.column("@",width=60)
        self.Denomination_table.column("Amount",width=60)

        self.Denomination_table["show"]="headings"
        self.Denomination_table.pack(fill=BOTH,expand=1)
        self.Denomination_table.delete(*self.Denomination_table.get_children())
        self.Denomination_table.bind("<ButtonRelease-1>", lambda event:Cash_count_Class.get_from_Denomination_table(self))
        Cash_count_Class.left_frame_CC(self)
        # lambda event: keypress(key="enter")
    #     self.Ai_find_item_table.delete(*self.Ai_find_item_table.get_children())
    #     self.Ai_find_item_table.bind("<ButtonRelease-1>",self.get_from_Ai_table
        for row in self.Denomination_list:
            self.Denomination_table.insert('',END,values=row)
                # self.Denomination_table.insert('',END,values=)
    def get_from_Denomination_table(self):
        f=self.Denomination_table.focus()
        content=(self.Denomination_table.item(f))
        self.row=content['values']
        # print(self.row)
        # print(row[1])
        
        self.sales_item_id.set("")
        self.txt_Login.focus_set()
        
    def left_frame_CC(self):
        self.txt_Login.config(show="",textvariable=self.sales_item_id)
        self.lbl_Rl.config(text="Enter Count ") 
        self.lbl_LP.config(text=" ") 
        self.office="Till_Audit"  
        # self.txt_Login.focus_set() 
    def check_list_CC(self):
        if self.sales_item_id.get()=="" or self.sales_item_id.get()==" ":
            messagebox.showinfo("Error","Select Denomination First and Enter Quantity")
        else:    
            if self.row[0]==1:
                self.list1[1]=self.sales_item_id.get()
                self.list1[3]="RS."+str(int(self.sales_item_id.get())*1)
                Cash_count_Class.Cash_count_frame_function(self)
                Cash_count_Class.Total_list_CC(self)
                
            elif self.row[0]==2:
                self.list2[1]=self.sales_item_id.get()
                self.list2[3]="RS."+str(int(self.sales_item_id.get())*2)
                Cash_count_Class.Cash_count_frame_function(self)
                Cash_count_Class.Total_list_CC(self)
            elif self.row[0]==5:
                self.list5[1]=self.sales_item_id.get()
                self.list5[3]="RS."+str(int(self.sales_item_id.get())*5)
                Cash_count_Class.Cash_count_frame_function(self)
                Cash_count_Class.Total_list_CC(self)
            elif self.row[0]==10:  
                self.list10[1]=self.sales_item_id.get()
                self.list10[3]="RS."+str(int(self.sales_item_id.get())*10)
                Cash_count_Class.Cash_count_frame_function(self)
                Cash_count_Class.Total_list_CC(self)
            elif self.row[0]==20:  
                self.list20[1]=self.sales_item_id.get()
                self.list20[3]="RS."+str(int(self.sales_item_id.get())*20)
                Cash_count_Class.Cash_count_frame_function(self)
                Cash_count_Class.Total_list_CC(self)
            elif self.row[0]==50:  
                self.list50[1]=self.sales_item_id.get()
                self.list50[3]="RS."+str(int(self.sales_item_id.get())*50)
                Cash_count_Class.Cash_count_frame_function(self)
                Cash_count_Class.Total_list_CC(self)
            elif self.row[0]==100:  
                self.list100[1]=self.sales_item_id.get()
                self.list100[3]="RS."+str(int(self.sales_item_id.get())*100)
                Cash_count_Class.Cash_count_frame_function(self)
                Cash_count_Class.Total_list_CC(self)
            elif self.row[0]==500:  
                self.list500[1]=self.sales_item_id.get()
                self.list500[3]="RS."+str(int(self.sales_item_id.get())*500)
                Cash_count_Class.Cash_count_frame_function(self)
                Cash_count_Class.Total_list_CC(self)
            elif self.row[0]==1000:  
                self.list1000[1]=self.sales_item_id.get()
                self.list1000[3]="RS."+str(int(self.sales_item_id.get())*1000)
                Cash_count_Class.Cash_count_frame_function(self)  
                Cash_count_Class.Total_list_CC(self)
            elif self.row[0]==5000:  
                self.list5000[1]=self.sales_item_id.get()
                self.list5000[3]="RS."+str(int(self.sales_item_id.get())*5000)
                Cash_count_Class.Cash_count_frame_function(self)
                Cash_count_Class.Total_list_CC(self)
            
    def Total_list_CC(self):
        total_cash=0
        for row in self.Denomination_list:
            if row[3][3::]=="":
            #    print(row[0])
               pass
            else:
                total_cash+=int(row[3][3::])
                  
                    
        self.total_CC.config(text="Total = "+str(total_cash))
        self.sales_item_id.set("")
        # print(total_cash)        
                
            
         
if __name__=="__main__":        
    root=Tk()
    obj=Cash_count_Class(root)
    root.mainloop()           
         