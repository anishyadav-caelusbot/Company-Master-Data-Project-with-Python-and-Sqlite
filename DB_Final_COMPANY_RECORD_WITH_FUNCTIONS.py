'''
Created on 30-May-2017

@author: anshu
'''


import sqlite3  

def insertcm(db,row):
    db.execute('insert into Company_master (cccode,C_name,C_address,C_Phone) values(?,?,?,?)',
               (row['cccode'],row['C_name'],row['C_address'],row['C_Phone']))
    db.commit()
    
def insertim(db,row):
    db.execute('insert into Item_master (item_code,cccode,Item_name,Item_UNIT) values(?,?,?,?)',
               (row['item_code'],row['cccode'],row['Item_name'],row['Item_UNIT']))
    db.commit()

def insertsm(db,row):
    db.execute('insert into Stock_master (Stock_code,item_code,Quantity) values(?,?,?)',
               (row['Stock_code'],row['item_code'],row['Quantity']))
    db.commit()
    
def inserttt(db,row):
    db.execute('insert into Trans_table (Trans_id,item_code,Quantity,Trans_type,Trans_Date) values(?,?,?,?,?)',
               (row['Trans_id'],row['item_code'],row['Quantity'],row['Trans_type'],row['Trans_Date']))
    db.commit()    
    
def joincm_im(db,row):
    cursor=db.execute('SELECT Company_master.cccode, Item_master.item_code FROM Orders INNER JOIN Item_master ON Company_master.cccode=Item_master.cccode')
    return cursor.fetchone()
        
def retrieve(db,cccode):
    cursor=db.execute('select * from Company_master where cccode = ?',(cccode,))
    return cursor.fetchone()

def update(db,row):
    db.execute('update Company_master set C_name=? where cccode=?',(row[C_name],row[cccode]))
    db.commit()
    
def delete(db,cccode):
    db.execute('delete from Company_master where cccode=?',(cccode,))
    db.commit()
    
def disp_rowscm(db):
    cursor=db.execute('select* from Company_master order by cccode')
    print ('Company code: Comapny Name: Comapny Address: Company Phone')
    for row in cursor:
        print('{}:{}:{}:{}'.format(row['cccode'],row['C_name'],row['C_address'],row['C_Phone']))
        
def disp_rowsim(db):
    cursor=db.execute('select* from Item_master order by cccode')
    print ('Item Code : Company code: Item Name: Item Unit')
    for row in cursor:
        print('{}:{}:{}:{}'.format(row['item_code'],row['cccode'],row['Item_name'],row['Item_UNIT']))

def disp_rowssm(db):
    cursor=db.execute('select* from Stock_master order by Stock_code')
    print ('Stock code : Item code: Quantity')
    for row in cursor:
        print('{}:{}:{}'.format(row['Stock_code'],row['item_code'],row['Quantity']))
        
def disp_rowstt(db): 
    cursor=db.execute('select* from Trans_table order by Trans_id')
    print ('Transsaction ID : Item code: Quantity: Transaction Type S/P: Transaction Date ')
    for row in cursor:
        print('{}:{}:{}:{}:{}'.format(row['Trans_id'],row['item_code'],row['Quantity'],row['Trans_type'],row['Trans_Date']))
        
def show_tables(db):
    cursor=db.execute('show tables')
    return cursor.fetchone()

def main():
    
          
    db=sqlite3.connect('Stockmaster.db')
    db.row_factory=sqlite3.Row
    print('Welcome to Stock Master Database')
    print('-----------------Company_master Table----------------')
    #db.execute('drop table if exists Company_master')
    #db.execute('create table Company_master (cccode text,C_name text,C_address text,C_Phone text)')
    #print('Create Rows')
    disp_rowscm(db)
    #insertcm(db,dict(cccode=(input("Enter company code")),
                  # C_name=(input("Enter company name")),
                   #C_address=(input("Enter company Address")),
                   #C_Phone=(input("Enter company Phone no"))
                  # ))
   # insertcm(db,dict(cccode=(input("Enter company code")),
                  # C_name=(input("Enter company name")),
                   #C_address=(input("Enter company Address")),
                  # C_Phone=(input("Enter company Phone no"))
                   #))
    #insertcm(db,dict(cccode=(input("Enter company code")),
                   #C_name=(input("Enter company name")),
                  # C_address=(input("Enter company Address")),
                  # C_Phone=(input("Enter company Phone no"))
                   #))
    #insertcm(db,dict(cccode=(input("Enter company code")),
                   #C_name=(input("Enter company name")),
                   #C_address=(input("Enter company Address")),
                   #C_Phone=(input("Enter company Phone no"))
                   #))
    #disp_rowscm(db)
    
   
    #item master______________________________________________________________________________________________________
    
    print('----------------------Item Master Table----------------------')
    #db.execute('drop table if exists Item_master')
    #db.execute('create table Item_master (item_code text,cccode text,Item_name text,Item_Unit text)')
    #print('Create Rows')
    disp_rowsim(db)
    #insert(db,cccode,C_name,C_address,C_Phone)
    #insertim(db,dict(item_code=(input("Enter Item code")),
                  # cccode=(input("Enter company code")),
                   #Item_name=(input("Enter Item Name")),
                   #Item_UNIT=(input("Enter Item UNIT"))
                   #))
    
    #insertim(db,dict(item_code=(input("Enter Item code")),
                  # cccode=(input("Enter company code")),
                  # Item_name=(input("Enter Item Name")),
                   #Item_UNIT=(input("Enter Item UNIT"))
                   #))
   # insertim(db,dict(item_code=(input("Enter Item code")),
                  # cccode=(input("Enter company code")),
                   #Item_name=(input("Enter Item Name")),
                   #Item_UNIT=(input("Enter Item UNIT"))
                  # ))
    #insertim(db,dict(item_code=(input("Enter Item code")),
                   #cccode=(input("Enter company code")),
                   #Item_name=(input("Enter Item Name")),
                   #Item_UNIT=(input("Enter Item UNIT"))
                   #))
   
   
    
    
    #Stock Master______________________________________________________________________________________________________
    
    print('------------------------Stock Master Table---------------------')
    disp_rowssm(db)
    #db.execute('drop table if exists Stock_master')
    #db.execute('create table Stock_master (Stock_code text,item_code text,Quantity text)')
    #print('Create Rows')
    #insert(db,cccode,C_name,C_address,C_Phone)
    #insertsm(db,dict(Stock_code=(input("Enter Stock code")),
    #               item_code=(input("Enter Item code")),
    #               Quantity=(input("Enter Quantity")),                   
    #               ))
    #insertsm(db,dict(Stock_code=(input("Enter Stock code")),
   #                item_code=(input("Enter Item code")),
    #               Quantity=(input("Enter Quantity")),                   
     #              ))
    #insertsm(db,dict(Stock_code=(input("Enter Stock code")),
    #               item_code=(input("Enter Item code")),
    #               Quantity=(input("Enter Quantity")),                   
     #              ))
   # insertsm(db,dict(Stock_code=(input("Enter Stock code")),
      #             item_code=(input("Enter Item code")),
      #             Quantity=(input("Enter Quantity")),                   
          #         ))
        
    
    
    #Transaction______________________________________________________________________________________________________
    
    print('-----------------Transaction Table-----------------')
    disp_rowstt(db)
    #db.execute('drop table if exists Trans_table')
    #db.execute('create table Trans_table (Trans_id text,item_code text,Quantity text,Trans_type text,Trans_Date text)')
    #print('Create Rows')
    #insert(db,cccode,C_name,C_address,C_Phone)
    #inserttt(db,dict(Trans_id=(input("Enter Transaction ID")),
                #   item_code=(input("Enter Item code")),
                #   Quantity=(input("Enter Quantity")),
                 #  Trans_type=(input("Enter Transaction Type: S / P")),
                  # Trans_Date=(input("Enter Transaction Date"))
                  # ))
    
   # inserttt(db,dict(Trans_id=(input("Enter Transaction ID")),
                #   item_code=(input("Enter Item code")),
               #    Quantity=(input("Enter Quantity")),
                #   Trans_type=(input("Enter Transaction Type: S / P")),
                #   Trans_Date=(input("Enter Transaction Date"))
                #   ))
    
 #   inserttt(db,dict(Trans_id=(input("Enter Transaction ID")),
     #              item_code=(input("Enter Item code")),
     #              Quantity=(input("Enter Quantity")),
     #              Trans_type=(input("Enter Transaction Type: S / P")),
      #             Trans_Date=(input("Enter Transaction Date"))
       #            ))
    
   # inserttt(db,dict(Trans_id=(input("Enter Transaction ID")),
               #    item_code=(input("Enter Item code")),
               #    Quantity=(input("Enter Quantity")),
               #    Trans_type=(input("Enter Transaction Type: S / P")),
                #   Trans_Date=(input("Enter Transaction Date"))
                 #  ))
    
    
   
    
    
    #print('Retrieve Rows')
    #print(dict(retrieve(db,'Rahul')),dict(retrieve(db,'Anish')))
    
    #print('Update Rows')
    #update(db,dict(cccode='Rahul',C_name=6936))
    #update(db,dict(cccode='Karan',C_name=8588))
    #disp_rows(db)
    
    #print('Delete Rows')
    #delete(db,'Rahul')
    #delete(db,'Vivek')
       
    #disp_rows(db)
    
    
    

main()