
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
# pip install pillow
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("700x500+150+100")
        # self.root.title("Inventry Management System | Developed by Qurban Ali")
        self.root.config(bg="gray")
        self.root.focus_force()
        mybtn=Button(self.root, text="Click me")
        mybtn.bind("<Key>",self.cliker)
        mybtn.pack(pady=20)
        



    def cliker(self,event):
            mylabel=Label(self.root,text="You Cliked this Button  " +event.keysym)
            mylabel.pack()
    
    
    

if __name__=="__main__":        
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()