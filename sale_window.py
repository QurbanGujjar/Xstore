from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
# pip install pillow
class sales_window_Class:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        # self.root.title("Inventry Management System | Developed by Qurban Ali")
        self.root.config(bg="white")
        self.root.focus_force()
#===========label Size for all lable
        self.label_size=30
        #=======Colors =====
        self.menu_Btn_color="gray";
        self.FO_color="orange" 

#==========variables=======
        self.var_login_id=StringVar()     
        self.var_category_id=StringVar()
        self.login_pass=[]
        self.office=StringVar()   
#=========== Category Details-====
        # self.root.bind("<Key>",self.Myfunction)
        self.Main_frame=Frame(self.root,bd=0)
        self.Main_frame.place(x=0,y=0,width=1350,height=700)
        
        self.Left_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
        self.Left_frame.place(x=10,y=10,width=660,height=550)
        self.btn_Cash =Button(self.Left_frame,text="Cash",bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",20,"bold"))
        self.btn_Cash.grid(row=0,column=0)
        self.btn_dabet=Button(self.Left_frame,text="Cash",bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",20,"bold"))
        self.btn_dabet.grid(row=1,column=0)
        self.btn_Cradit=Button(self.Left_frame,text="Cash",bg="#5ac910",width=100,anchor="w",cursor="hand2",font=("goudy old style",20,"bold"))
        self.btn_Cradit.grid(row=2,column=0)
        # self.Main_frame.bind("<FocusIn>",self.escape_window)
        # Main_frame.config(highlightbackground="red")
#         self.Left_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
     
#         self.Left_frame.place(x=10,y=10,width=660,height=550)
#         self.w1 =Label(self.Left_frame,text="Info",bg=self.FO_color,height=5)
#         self.w1.grid(row=0,column=0,sticky="nsew",padx=0)
#         self.w2 =Label(self.Left_frame, text="Tasks",bg=self.FO_color,)
#         self.w2.grid(row=0,column=1,sticky="nsew",padx=2)
#         self.w3 =Label(self.Left_frame, text="Goals",bg=self.FO_color,)
#         self.w3.grid(row=0,column=2,sticky="nsew",padx=0)
#         self.w4 =Label(self.Left_frame, text="Message",bg=self.FO_color)
#         self.w4.grid(row=0,column=3,sticky="nsew",padx=2)
#         self.w5 =Label(self.Left_frame, text="Keyboard",bg=self.FO_color)
#         self.w5.grid(row=0,column=4,sticky="nsew",padx=0)
#         self.Left_frame.grid_columnconfigure(0,weight=1)
#         self.Left_frame.grid_columnconfigure(1,weight=1)
#         self.Left_frame.grid_columnconfigure(2,weight=1)
#         self.Left_frame.grid_columnconfigure(3,weight=1)
#         self.Left_frame.grid_columnconfigure(4,weight=1)
        
#         self.Left_frame_text_Area=Frame(self.Left_frame,bd=1,relief=RIDGE,bg=self.FO_color)
#         self.Left_frame_text_Area.place(x=0,y=400,width=655,height=145)
        
#         self.lbl_Rl =Label(self.Left_frame_text_Area,text="Register Login",font=("goudy old style",20),bg=self.FO_color)
#         self.lbl_Rl.grid(row=0,column=0,sticky="w",padx=10,pady=5)
#         self.txt_Login =Entry(self.Left_frame_text_Area,textvariable=self.var_login_id,bg="white",fg='black',font=("goudy old style",20))
#         self.txt_Login.grid(row=1,column=0,sticky="w",padx=10,pady=5)
#         self.lbl_LP =Label(self.Left_frame_text_Area, text="Enter Login and Password",font=("goudy old style",20),bg=self.FO_color)
#         self.lbl_LP.grid(row=2,column=0,sticky="w",padx=10,pady=5)
#         self.Left_frame_text_Area.grid_columnconfigure(0,weight=1)
#         self.office="FO"
#         self.txt_Login.bind("<Return>",self.cliker)
        
        
#         self.Right_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
#         self.Right_frame.place(x=680,y=10,width=660,height=550)
#         Menu_frame=Frame(self.Main_frame,bd=3,relief=RIDGE)
#         Menu_frame.place(x=10,y=570,width=1350,height=100)
#         # Menu_frame.bind("<FocusIn>",self.escape_window)
#         # Main_frame.bind("<Key>")
#         self.btn0 =Button(Menu_frame,text="Exit",command=self.Check_state,bg=self.menu_Btn_color,height=5)
#         self.btn0.grid(row=0,column=0,sticky="nsew",padx=0)
#         # self.btn0.bind("<Key>",self.escape_window)
#         btn1 =Label(Menu_frame,text="Help",bg=self.menu_Btn_color,height=5)
#         btn1.grid(row=0,column=1,sticky="nsew",padx=2)
#         btn2=Label(Menu_frame, text="Clock \n In\out",bg=self.menu_Btn_color,)
#         btn2.grid(row=0,column=2,sticky="nsew",padx=0)
#         btn3=Label(Menu_frame, text="View \nSchedule \n & time",bg=self.menu_Btn_color,)
#         btn3.grid(row=0,column=3,sticky="nsew",padx=2)
#         btn4=Label(Menu_frame, text="Change \n Password",bg=self.menu_Btn_color)
#         btn4.grid(row=0,column=4,sticky="nsew",padx=0)
#         btn5=Label(Menu_frame, text="Receipt \n Reprint \n Options",bg=self.menu_Btn_color)
#         btn5.grid(row=0,column=5,sticky="nsew",padx=2)
#         btn6 =Label(Menu_frame,text="Balance \n Inqury",bg=self.menu_Btn_color,height=5)
#         btn6.grid(row=0,column=6,sticky="nsew",padx=0)
#         btn7=Label(Menu_frame, text="Testing \n Mode",bg=self.menu_Btn_color,)
#         btn7.grid(row=0,column=7,sticky="nsew",padx=2)
#         btn8=Label(Menu_frame, text="My Task",bg=self.menu_Btn_color,)
#         btn8.grid(row=0,column=8,sticky="nsew",padx=0)
#         btn9=Label(Menu_frame, text="Find \n Item",bg=self.menu_Btn_color)
#         btn9.grid(row=0,column=9,sticky="nsew",padx=2)
#         btn10=Label(Menu_frame, text="Till",bg=self.menu_Btn_color)
#         btn10.grid(row=0,column=10,sticky="nsew",padx=0)
#         btn11=Label(Menu_frame, text="Flash \n Sales",bg=self.menu_Btn_color)
#         btn11.grid(row=0,column=11,sticky="nsew",padx=2)
#         self.btn12=Button(Menu_frame, text="Back \n Office",bg=self.menu_Btn_color,command=self.Back_office)
#         self.btn12.grid(row=0,column=12,sticky="nsew",padx=0)
        
#         Menu_frame.grid_columnconfigure(0,weight=1)
#         Menu_frame.grid_columnconfigure(1,weight=1)
#         Menu_frame.grid_columnconfigure(2,weight=1)
#         Menu_frame.grid_columnconfigure(3,weight=1)
#         Menu_frame.grid_columnconfigure(4,weight=1)
#         Menu_frame.grid_columnconfigure(5,weight=1)
#         Menu_frame.grid_columnconfigure(6,weight=1)
#         Menu_frame.grid_columnconfigure(7,weight=1)
#         Menu_frame.grid_columnconfigure(8,weight=1)
#         Menu_frame.grid_columnconfigure(9,weight=1)
#         Menu_frame.grid_columnconfigure(10,weight=1)
#         Menu_frame.grid_columnconfigure(11,weight=1)
#         Menu_frame.grid_columnconfigure(12,weight=1)
    
#         # functions=======================
#     def Back_office(self):
#             self.w1.config(bg= "black", fg= "white")
#             self.w2.config(bg= "black", fg= "white")
#             self.w3.config(bg= "black", fg= "white")
#             self.w4.config(bg= "black", fg= "white")
#             self.w5.config(bg= "black", fg= "white")
#             self.lbl_Rl.config(bg= "black", fg= "white" ,text="Back Office Login ID")
#             self.lbl_LP.config(bg= "black", fg= "white")
#             self.Left_frame_text_Area.config(bg= "black")
#             del self.login_pass[:]
#             self.txt_Login.config(show="")
#             self.var_login_id.set("")
            
#             self.office="BO"
#             self.btn12.config(command=self.Front_office,text="Register")
#     def Front_office(self):
#             self.w1.config(bg= self.FO_color, fg= "black")
#             self.w2.config(bg= self.FO_color, fg= "black")
#             self.w3.config(bg= self.FO_color, fg= "black")
#             self.w4.config(bg= self.FO_color, fg= "black")
#             self.w5.config(bg= self.FO_color, fg= "Black")
#             self.lbl_Rl.config(bg= self.FO_color, fg= "black" ,text="Register Login ID")
#             self.lbl_LP.config(bg= self.FO_color, fg= "Black")
#             self.Left_frame_text_Area.config(bg= self.FO_color,)
#             self.btn12.config(command=self.Back_office,text="Back \n Office")
#             del self.login_pass[:]
#             self.txt_Login.config(show="")
#             self.var_login_id.set("")
#             self.office="FO"
            
#     def cliker(self,ev):
#             self.login_pass.append(self.var_login_id.get())
#             if self.office == "FO":
#                     self.lbl_Rl.config(bg= self.FO_color, fg= "black" ,text="Register Password")
#                     self.txt_Login.config(show="*")
#                     if len(self.login_pass)==2:
#                             self.logedin_FO()
                
#             else:
#                     self.lbl_Rl.config(bg= "black", fg= "white" ,text="Back Office Password") 
#                     self.txt_Login.config(show="*")
#                     if len(self.login_pass)==2:
#                             self.logedin_BO()  
#             self.var_login_id.set("")
            
            
#     def logedin_FO(self):
#             self.var_login_id.set("")
#             if self.login_pass[0] == self.login_pass[1]:
#                     self.Sales_window()    
        
#     def logedin_BO(self):
#             self.var_login_id.set("")
#             if self.login_pass[0]== self.login_pass[1]:
#                 self.Back_Office_window()
#                 # messagebox.showinfo("Success","Welcome BO",parent=self.root)
                    
#     def Myfunction(self,event):
#             if event.keysym=="Escape":
#                    self.Check_state()  
#     def Check_state(self):
#              if self.office=="FO":
#                      self.Front_office()
#              else:
#                      self.Back_office()                     
                           
#     def Sales_window(self):
#             messagebox.showinfo("Success","Welcome FO",parent=self.root)
#     def Back_Office_window(self):
#             messagebox.showinfo("Success","Welcome BO",parent=self.root)   
            
            


                        
if __name__=="__main__":        
    root=Tk()
    obj=sales_window_Class(root)
    root.mainloop()                    