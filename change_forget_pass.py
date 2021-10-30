# from _typeshed import Self
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import time
import sqlite3
class change_forget_password_Class:

    def Change_password(self,root):
        # c_f_p_c=change_forget_password_Class
        self.new_Pass=StringVar()
        self.New_Confirm=StringVar()  
        change_forget_password_Class.Change_pass_1st_w(self)
        # c_f_p_c.Change_pass_1st_w()

    def Change_pass_1st_w(self):
        self.info.config(bg= "gray", fg= "white")
        self.Task.config(bg= "gray", fg= "white")
        self.Goals.config(bg= "gray", fg= "white")
        self.Message.config(bg= "gray", fg= "white")
        self.Keyboard.config(bg= "gray", fg= "white")
        self.lbl_Rl.config(bg= "gray", fg= "white" ,text="Enter Login ID To Change Password")
        self.lbl_LP.config(bg= "gray", fg= "white")
        self.Left_frame_text_Area.config(bg= "gray")
        del self.login_pass[:]
        self.txt_Login.config(show="")
        self.var_login_id.set("")
        
        self.office="Change_pass"
    def Confirm_password(self,info):
        self.Left_frame.destroy()
        self.disable_btn()
        self.Left_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Left_frame.place(x=10,y=10,width=660,height=550)
        
        self.Change_pass_frame=Frame(self.Left_frame,bd=0,relief=RIDGE)
        self.Change_pass_frame.place(x=0,y=100,width=550,height=150)
        self.lbl_Rl =Label(self.Change_pass_frame,text="Enter Password",font=("goudy old style",20),)
        self.lbl_Rl.grid(row=0,column=0,sticky="w",padx=10,pady=5)
        self.txt_start_date =Entry(self.Change_pass_frame,textvariable=self.new_Pass,show="*",bg="white",fg='black',font=("goudy old style",20))
        self.txt_start_date.grid(row=0,column=1,sticky="w",padx=10,pady=5)
        self.lbl_Rl =Label(self.Change_pass_frame,text="Confirm Password",font=("goudy old style",20))
        self.lbl_Rl.grid(row=1,column=0,sticky="w",padx=10,pady=5)
        self.txt_end_date =Entry(self.Change_pass_frame,textvariable=self.New_Confirm,show="*",bg="white",fg='black',font=("goudy old style",20))
        self.txt_end_date.grid(row=1,column=1,sticky="w",padx=10,pady=5) 
        # change_forget_password_Class.Btn_Menu_frame(self,info)
        self.Menu_frame=Frame(self.Left_frame,bd=0,relief=RIDGE)
        self.Menu_frame.place(x=80,y=440,width=350,height=100)
        # print("Buttons frame")
        self.btn_back =Button(self.Menu_frame,text="Back",command=lambda:change_forget_password_Class.C_P_Back(self),bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_back.grid(row=0,column=0)
        self.btn_help=Button(self.Menu_frame,text="Help",bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_help.grid(row=0,column=1)
        self.btn_ok=Button(self.Menu_frame,text="Submit",command=lambda:change_forget_password_Class.C_P_Submit(self,info), bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        self.btn_ok.grid(row=0,column=2)     
        self.btn_Register=Button(self.Menu_frame,text="Register",command=lambda:change_forget_password_Class.C_P_Register(self),bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"),state="disable")
        self.btn_Register.grid(row=0,column=3)
        
    # def Btn_Menu_frame(self,info):
        # self.Menu_frame=Frame(self.Left_frame,bd=0,relief=RIDGE)
        # self.Menu_frame.place(x=80,y=440,width=350,height=100)
        # # print("Buttons frame")
        # self.btn_back =Button(self.Menu_frame,text="Back",command=lambda:change_forget_password_Class.C_P_Back(self),bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        # self.btn_back.grid(row=0,column=0)
        # self.btn_help=Button(self.Menu_frame,text="Help",bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        # self.btn_help.grid(row=0,column=1)
        # self.btn_ok=Button(self.Menu_frame,text="Submit",command=lambda:change_forget_password_Class.C_P_Submit(self,info), bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"))
        # self.btn_ok.grid(row=0,column=2)     
        # self.btn_Register=Button(self.Menu_frame,text="Register",command=lambda:change_forget_password_Class.C_P_Register(self),bg="#5ac910",width=7,height=3,anchor="center",cursor="hand2",font=("goudy old style",15,"bold"),state="disable")
        # self.btn_Register.grid(row=0,column=3) 
        # pass
    
    def C_P_Back(self):
        self.Front_office()
    def C_P_Submit(self,info):
        if self.new_Pass.get()=="" or self.New_Confirm.get()=="":
            messagebox.showerror("Error","Password should not be empty",parent=self.root)
        elif self.new_Pass.get()==self.New_Confirm.get():
          con=sqlite3.connect(database=r"xStore.db")
          cur=con.cursor()
          try:
              cur.execute("update employee set pass =?  WHERE loginID=?",(
                  self.new_Pass.get(),
                  info[0]
                  ))
              con.commit()
              messagebox.showinfo("Success",f"Password has been changed successully",parent=self.root)
              self.Front_office()
          except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
           
        else:
            messagebox.showerror("Error","Password is not same")

        
       
            

if __name__=="__main__":        
    root=Tk()
    obj=change_forget_password_Class(root)
    root.mainloop()     
