from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
#=================== Generate Bill ==================
class Bill_Class:
    def bill_Generate(self):
        self.sales_list=[]
        print("Generate Bill function call")
        
        #     # bill_top
        Bill_Class.bill_top(self)
        #     # bill_middle.
        Bill_Class.bill_middle(self)
        #     # bill_bottom
        Bill_Class.bill_bottom(self)
        
        fp=open(f"bill/{str(self.invoice_no)}.txt","w")
        fp.write(self.txt_bill_area.get('1.0',END))
        fp.close()
        messagebox.showinfo("Success","Bill has been Genrated and Saved in backed Successfully!")       
        self.chk_print=1
        # self.sales_list=[]
        # salesTable=("Date","invoiceNo","Brand","ProductName","ProductCode","ExectPrice","Qty","TransType","SalesPerson","Casher")
        for row in self.cart_list:
                self.sales_list.append([str(time.strftime("%Y/%m/%d")),str(self.invoice_no),str(row[5]),str(row[0]),str(row[1]),str(row[3]),str(row[2]),str(row[6]),self.user_name,self.user_name])
        Bill_Class.send_sales_data_into_databse(self)
        Bill_Class.update_product_table(self)
            
        self.Sales_window()
        
    def send_sales_data_into_databse(self):
       
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            sql_insert='''insert into salesTable values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)'''
            cur.executemany(sql_insert,self.sales_list)
            con.commit()
            # pass
            # df = pd.DataFrame(data)
            # df.to_csv('data.csv', index = False)  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                
    def bill_top(self):
        self.invoice_no=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%y"))
        print(self.invoice_no)
        bill_top_temp=f'''
    \tXYZ Inventory
    phone No.04211223344
    \tLHR-54401
    {str("="*33)}
    
    Bill No.{str(self.invoice_no)}
    Date:   {str(time.strftime("%Y/%m/%d"))}
    Sales Person {self.user_name}
    Cashier      {self.user_name}
    {str("="*33)}
    Product Name Qty Price
    {str("="*33)}
            '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert("1.0",bill_top_temp)
        
        
    def bill_bottom(self):
       
        self.txt_bill_area.insert(END,"\n \t"+"Total Sum ="+str(self.pro_price_sum))
        # self.txt_bill_area.insert(END,abc1)   
    # ==========bill Middle======= 
    def bill_middle(self):
        
        for row in self.cart_list:
            # self.txt_bill_area.insert(END,"\n"+name.ljust(12)+"  "+row[3]+"   RS."+price)
            self.txt_bill_area.insert(END,"\n \t"+str(row[0])+"  "+str(row[1])+" "+str(row[2])+" "+str(row[3]))
    # update product table function  
    def update_product_table(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            # sql_insert='''insert into salesTable values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)'''
            # cur.executemany(sql_insert,self.sales_list)
            # con.commit()
            # pass
            
            for row in self.cart_list:
                Product_code=row[1]
                name=row[1]
                cur.execute(f"Select qty,C_P_U,T_C from products where Product_code='{Product_code}'")
                Rowitem=cur.fetchone()
                
                if row[6]=="return":
                    qty=int(row[2])+int(Rowitem[0]) 
                    status="Active"
                    UpdatedStockPrice=str(qty*int(Rowitem[1]))
                else:
                    
                    qty=int(Rowitem[0])-int(row[2])
                    UpdatedStockPrice=str(qty*int(Rowitem[1]))
                    if int(row[2])==int(Rowitem[0]):
                        status="Inactive"
                    if int(row[2])!=int(Rowitem[0]):
                        status="Active"
                #======Update QTY in Product Table
                cur.execute("update products set qty=?,T_C=?,Pstatus=? where Product_code=?",(
                    qty,
                    UpdatedStockPrice,
                    status,
                    Product_code
                ))
                con.commit()
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)       
    