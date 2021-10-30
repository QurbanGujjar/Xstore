import sqlite3
def create_db():
    con=sqlite3.connect(database=r'xStore.db')
    cur=con.cursor()
    #================Creating Employee Table=============
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,loginID text,pass text,utype text,address text,salary text)")
    # print("Done")
    con.commit()
    
     #================Creating Product Table=============
    cur.execute("CREATE TABLE IF NOT EXISTS products(pid INTEGER PRIMARY KEY AUTOINCREMENT,warehouse text,Brand text,Product_name text,Product_code text,qty text,C_P_U text,T_C text,Pstatus text)")
    con.commit()
    # print("Done")
    
    #================Creating sales Table=============
    cur.execute("CREATE TABLE IF NOT EXISTS salesTable(Sno INTEGER PRIMARY KEY AUTOINCREMENT,Date text,invoiceNo text,Brand text,ProductName text,ProductCode text,ExectPrice text,Qty text,TransType text,SalesPerson text,Casher text)")
    con.commit()
    
    #================Creating Clock in\out Table=============
    cur.execute("CREATE TABLE IF NOT EXISTS clock_in_out(Cno INTEGER PRIMARY KEY AUTOINCREMENT,name text,eid text,Date text,day text,time text,status text)")
    con.commit()
    #================Creating businss Date Table=============
    cur.execute("CREATE TABLE IF NOT EXISTS business_date(B_d_no INTEGER PRIMARY KEY AUTOINCREMENT,name text,eid text,Date text,day text,time text,store text,register text)")
    con.commit()
    
    # INSERT INTO employee(name ,email ,gender ,contact ,dob ,doj ,pass ,utype ,address ,salary )
# VALUES( 'Qurban', 'qur@gmail.com', 'male','0347', '10-02-2021', '10-02-2021','1234', 'SM', 'LHR','na');
    # VALUES( 'Qurban', 'qur@gmail.com', 'male','0347', '10-02-2021', '10-02-2021','1234', 'SM', 'LHR','na');
    # INSERT INTO products(warehouse ,Brand ,Product_name ,Product_code ,qty ,C_P_U ,T_C )
# VALUES( 'MainWarehouse', 'Unilever', 'Lux','L1000001', '100', '68','6800');
    
    
    
create_db()    