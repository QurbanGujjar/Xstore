from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
# from change_forget_pass import change_forget_password_Class as c_f_p
import time
import sqlite3
class Clock_in_out_Class:
    def Schedule_Function(self,root):
        Clock_in_out_Class.Clock_office(self)
        self.lbl_Rl.config(bg= "gray", fg= "white" ,text="To View Time Card  Enter Login ID")
        self.office="View time"
        
        
    def Clock_in_out_Function(self,root): 
        self.Clock_office='Clock'
        # self.Main_frame=Frame(self.root,bd=0)
        # self.Main_frame.place(x=0,y=0,width=1350,height=700)
        # self.footer_frame_()
        # self.R_login.config(text=f"{self.user_name}")
        Clock_in_out_Class.Clock_office(self)
         
    def Clock_office(self):
        self.info.config(bg= "gray", fg= "white")
        self.Task.config(bg= "gray", fg= "white")
        self.Goals.config(bg= "gray", fg= "white")
        self.Message.config(bg= "gray", fg= "white")
        self.Keyboard.config(bg= "gray", fg= "white")
        self.lbl_Rl.config(bg= "gray", fg= "white" ,text="Clock in/Out Login ID")
        self.lbl_LP.config(bg= "gray", fg= "white")
        self.Left_frame_text_Area.config(bg= "gray")
        del self.login_pass[:]
        self.txt_Login.config(show="")
        self.var_login_id.set("")
       
        
        self.office="Clock"
        # self.btn12.config(command=self.Front_office,text="Register")    
    def Btn_Menu_frame(self,info):
        
        # pass
        self.lbl_Rl.config(bg= "gray", fg= "white" ,text="Select In/Out")
        # self.info=info
        
        self.Menu_frame=Frame(self.Left_frame,bd=0,relief=RIDGE,bg="gray")
        self.Menu_frame.place(x=0,y=450,width=652,height=145) 
        # print("Buttons frame")
        self.btn_back =Button(self.Menu_frame,text="Back",bg="gray",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_back.grid(row=0,column=0)
        self.btn_help=Button(self.Menu_frame,text="Help",bg="gray",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_help.grid(row=0,column=1)
        self.btn_ok=Button(self.Menu_frame,text="Clock In",command= lambda:Clock_in_out_Class.Clock_In(self,info), bg="gray",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_ok.grid(row=0,column=2)     
        self.btn_Register=Button(self.Menu_frame,text="Clock Out",command= lambda:Clock_in_out_Class.Clock_Out(self,info),bg="gray",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_Register.grid(row=0,column=3)    
        
        
    def Clock_In(self,info):
        print(info)
        
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
         #     # name ,eid ,Date ,day ,time ,status
        try:
            cur.execute("insert into clock_in_out(name ,eid ,Date ,day ,time ,status ) values(?,?,?,?,?,?)",(
            info[2],
            info[0],
            time.strftime("%Y/%m/%d"),
            time.strftime("%A"),
            time.strftime("%H:%M:%S"),
            "in"
            ))   
            # "03/10/21"
            con.commit()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)     
        self.Menu_frame.destroy()
        self.Front_office()
        self.Back_office()
    def Clock_Out(self,info):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
         #     # name ,eid ,Date ,day ,time ,status
        try:
            cur.execute("insert into clock_in_out(name ,eid ,Date ,day ,time ,status ) values(?,?,?,?,?,?)",(
            info[2],
            info[0],
            time.strftime("%Y/%m/%d"),
            time.strftime("%A"),
            time.strftime("%H:%M:%S"),
            "out"
            ))   
            con.commit()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)     
        self.Menu_frame.destroy()
        self.Front_office()
        self.Back_office()
        
         
    def view_card(self):
        # self.Outer_frame.destroy()
        self.Menu_frame.destroy()
        self.Card_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Card_frame.place(x=0,y=0,width=1350,height=660) 
        T_C_frame=Frame(self.Card_frame,bd=3,relief=RIDGE)
        T_C_frame.place(x=1,y=1,width=1350,height=560)
        scrolly=Scrollbar(T_C_frame,orient=VERTICAL)
        scrollx=Scrollbar(T_C_frame,orient=HORIZONTAL)
        self.Cart_table=ttk.Treeview(T_C_frame,columns=("Date","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",),yscrollcommand=scrolly.set,xscrollcommand=scrolly.set)
       
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Cart_table.xview)
        scrolly.config(command=self.Cart_table.yview)
       #====headings ===========================
        self.Cart_table.heading("Date",text="Date")
        self.Cart_table.heading("Monday",text="Monday\nin\tOut")
        self.Cart_table.heading("Tuesday",text="Tuesday\nin\tOut")
        self.Cart_table.heading("Wednesday",text="Wednesday\nin\tOut")
        self.Cart_table.heading("Thursday",text="Thursday\nin\tOut")
        self.Cart_table.heading("Friday",text="Friday\nin\tOut")
        self.Cart_table.heading("Saturday",text="Saturday\nin\tOut")
        self.Cart_table.heading("Sunday",text="Sunday\nin\tOut")
        # self.Cart_table.heading("status",text="Status")
        #========colom width ====================
        self.Cart_table.column("Date",width=10)
        self.Cart_table.column("Monday",width=10)
        self.Cart_table.column("Tuesday",width=10)
        self.Cart_table.column("Wednesday",width=40)
        self.Cart_table.column("Thursday",width=10)
        self.Cart_table.column("Friday",width=40)
        self.Cart_table.column("Saturday",width=40)
        self.Cart_table.column("Sunday",width=10)
        # self.Cart_table.column("status",width=40)
        self.Cart_table["show"]="headings"
        self.Cart_table.pack(fill=BOTH,expand=1)
        
        Clock_in_out_Class.Employee_card(self)
        self.Menu_frame=Frame(self.Card_frame,bd=0,relief=RIDGE)
        self.Menu_frame.place(x=80,y=560,width=350,height=100)
        # print("Buttons frame")
        self.btn_back =Button(self.Menu_frame,text="Back",command=lambda:Clock_in_out_Class.C_i_o_Back(self),bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_back.grid(row=0,column=0)
        self.btn_help=Button(self.Menu_frame,text="Help",bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_help.grid(row=0,column=1)
        self.btn_ok=Button(self.Menu_frame,text="Submit",command=lambda:Clock_in_out_Class.C_P_Submit(self), bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"),state="disable")
        self.btn_ok.grid(row=0,column=2)     
        self.btn_Register=Button(self.Menu_frame,text="Register",command=lambda:Clock_in_out_Class.C_P_Register(self),bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"),state="disable")
        self.btn_Register.grid(row=0,column=3) 
    def C_i_o_Back(self):
        self.Card_frame.destroy()
        self.FO_Menu_frame_()
        self.Front_office()
        self.Back_office()
           
    def Employee_card(self):
        con=sqlite3.connect(database=r"xStore.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from clock_in_out")
            rows=cur.fetchall()        
            self.Cart_table.delete(*self.Cart_table.get_children())   
            # qty_sum=0
            # cost_sum=0 
            Date_=""
            time_in=""
            time_out=""   
            sunday=[]
            # monday=[],tuesday=[],wednesday=[],thursday=[],friday=[],saturday=[] 
            for row in rows:
                Date_=row[3]
                # time_in=row[5]
                if row[4]=='Sunday':
                    if row[6]=="in":
                       time_in=row[5]
                       time_out=""
                       sunday=[Date_,"","","","","","",time_in+time_out]
                    else:
                        time_in=""
                        time_out=row[5]
                        sunday=[Date_,"","","","","","",time_in+time_out]
                    self.Cart_table.insert('',END,values=sunday)
                elif row[4]=='Monday':
                    if row[6]=="in":
                       time_in=row[5]
                       time_out=""
                       sunday=[Date_,time_in+time_out,"","","","","","",]
                    else:
                        time_in=""
                        time_out=row[5]
                        sunday=[Date_,time_in+time_out,"","","","","","",]
                    self.Cart_table.insert('',END,values=sunday)
                    
                elif row[4]=='Tuesday':
                    if row[6]=="in":
                       time_in=row[5]
                       time_out=""
                       sunday=[Date_,"",time_in+time_out,"","","","",""]
                    else:
                        time_in=""
                        time_out=row[5]
                        sunday=[Date_,"",time_in+time_out,"","","","","",]
                    self.Cart_table.insert('',END,values=sunday)
                elif row[4]=='Wednesday':
                    if row[6]=="in":
                       time_in=row[5]
                       time_out=""
                       sunday=[Date_,"","",time_in+time_out,"","","",""]
                    else:
                        time_in=""
                        time_out=row[5]
                        sunday=[Date_,"","",time_in+time_out,"","","",""]
                    self.Cart_table.insert('',END,values=sunday)
                elif row[4]=='Thursday':
                    if row[6]=="in":
                       time_in=row[5]
                       time_out=""
                       sunday=[Date_,"","","",time_in+time_out,"","",""]
                    else:
                        time_in=""
                        time_out=row[5]
                        sunday=[Date_,"","","",time_in+time_out,"","",""]
                    self.Cart_table.insert('',END,values=sunday)
                elif row[4]=='Friday':
                    if row[6]=="in":
                       time_out=""
                       time_in=row[5]
                       sunday=[Date_,"","","","",time_in+time_out,"",""]
                    else:
                        time_in=""
                        time_out=row[5]
                        sunday=[Date_,"","","","",time_in+time_out,"",""]
                    self.Cart_table.insert('',END,values=sunday)
                elif row[4]=='Saturday':
                    if row[6]=="in":
                       time_out=""
                       time_in=row[5]
                       sunday=[Date_,"","","","","",time_in+time_out,""]
                    else:
                        time_in=""
                        time_out=row[5]
                        sunday=[Date_,"","","","","",time_in+time_out,""]
                    self.Cart_table.insert('',END,values=sunday)                    
        except Exception as ex:
               messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)   


if __name__=="__main__":        
    root=Tk()
    obj=Clock_in_out_Class(root)
    root.mainloop()     
     