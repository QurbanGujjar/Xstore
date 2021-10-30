import time
print(time.strftime("%Y/%m/%d"))



# Ai_find_item_frame=Frame(self.Left_frame,bd=3,relief=RIDGE)
# Ai_find_item_frame.place(x=0,y=200,width=660,height=200)
# scrolly=Scrollbar(Ai_find_item_frame,orient=VERTICAL)
# scrollx=Scrollbar(Ai_find_item_frame,orient=HORIZONTAL)
# # self.Ai_find_item_table=ttk.Treeview(Ai_find_item_frame,columns=("Transection_no","name","Unit_price","qty","Ext_price"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
# self.Ai_find_item_table=ttk.Treeview(Ai_find_item_frame,columns=("Product_name","Product_code","qty","C_P_U"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
# scrollx.pack(side=BOTTOM,fill=X)
# scrolly.pack(side=RIGHT,fill=Y)
# scrollx.config(command=self.Ai_find_item_table.xview)
# scrolly.config(command=self.Ai_find_item_table.yview)
# #====headings ===========================  # Product_name,Product_code,qty,C_P_U
# # self.Ai_find_item_table.heading("Transection_no",text=" my Trans #")


# self.Ai_find_item_table.heading("Product_name",text=" Product Name")
# self.Ai_find_item_table.heading("Product_code",text="Code")
# self.Ai_find_item_table.heading("qty",text="QTY")
# self.Ai_find_item_table.heading("C_P_U",text="Unit Price")

# #========colom width ====================

# self.Ai_find_item_table.column("Product_name",width=60)
# self.Ai_find_item_table.column("Product_code",width=60)
# # self.Ai_find_item_table.column("Unit_price",width=60)
# self.Ai_find_item_table.column("qty",width=60)
# self.Ai_find_item_table.column("C_P_U",width=60)

# self.Ai_find_item_table["show"]="headings"
# self.Ai_find_item_table.pack(fill=BOTH,expand=1)
# # self.Ai_find_item_table.tag_configure('return', background='red', foreground='white')
# # self.Ai_find_item_table.tag_configure('sales', background='#2d5bb9', foreground='white')
# # self.Ai_find_item_table.bind("<ButtonRelease-1>",self.get_data)
# self.Ai_find_item_table.delete(*self.Ai_find_item_table.get_children())
# # self.Ai_find_item_table.bind("<ButtonRelease-1>",self.get_data)
# for row in self.Ai_find_list:
#     self.Ai_find_item_table.insert('',END,values=row)
#         # self.Ai_find_item_table.insert('',END,values=)
                
                


# from tkinter import *

# def blink():
#     e.config(bg='green')
#     e.after(2000, lambda: e.config(bg='white')) # after 1000ms

# root = Tk()
# e = Entry(root)
# e.pack()
# b = Button(root, text='blink', command=blink)
# b.pack()
# root.mainloop()


# import speech_recognition as sr
# import webbrowser
# import sqlite3



# def search_from_db(query):
#     con=sqlite3.connect(database=r"xStore.db")
#     cur=con.cursor()
#     try:
#         cur.execute("select * from products where Product_name LIKE '%"+query+"%'")
#         # cur.execute("select Product_name,Product_code,qty,C_P_U,pid,Brand from products where Product_name=?",(query,))
#         rows=cur.fetchall()
#         print(rows)
#     except Exception as e:
#         print("Error ",e)    
# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source,duration=1)
#         print("Listening...1")
#         r.pause_threshold = 1 
#         audio = r.listen(source)
#         print("Listening...2")
#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
#         print(f"User said: {query}\n")  #User query will be printed.
#         search_from_db(query.lower())

#     except Exception as e:
#         print(e)    
#         print("Say that again please...")   #Say that again will be printed in case of improper voice 
#         return "None" #None string will be returned
#     return query    
        
        
        
        
# if __name__=="__main__" :
# #   while True:
#         query=takeCommand().lower()
#         # if 'open youtube' in query:
#         #         webbrowser.open('youtube.com')
