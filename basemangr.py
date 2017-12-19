# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:33:20 2017

@author: Сергей
"""

import sqlite3
import datetime
import matplotlib.pyplot as plt

conn = sqlite3.connect("currencies.db")

cursor = conn.cursor()
data = []

def CreateTable():
    cursor.execute('''CREATE TABLE currencies
                 (date text, symbol text, sell real, buy real)''')

def AppendDataForToday(tdata, date = ""):
    """
    USD	56.6	58
    EUR	66.6	68
    GBP	74.5	76.5
    """
    d = datetime.date.today()
    
    for row in tdata:
        if date == "":
            date2put = d.strftime("%d.%m.%Y")
        else:
            date2put = date
        tdatarow = (date2put, row[0], row[1], row[2])
        conn.execute('''INSERT INTO currencies VALUES (?, ?, ?, ?)''', tdatarow)
    
    """data1 = (d.strftime("%d.%m.%Y"), "USD", 56.6, 58)
    data2 = (d.strftime("%d.%m.%Y"), "EUR", 66.6, 68)
    data3 = (d.strftime("%d.%m.%Y"), "GBP", 74.5, 76.5)
    
    conn.execute('''INSERT INTO currencies VALUES (?, ?, ?, ?)''', data1)
    conn.execute('''INSERT INTO currencies VALUES (?, ?, ?, ?)''', data2)
    conn.execute('''INSERT INTO currencies VALUES (?, ?, ?, ?)''', data3)"""
    
    conn.commit()

def GetData():
    data1 = []
    for row in cursor.execute('SELECT * FROM currencies'):
        data1.append(row)
        print(row)
    return data1

def GetDataOnDate(cdate):
    data1 = []
    for row in cursor.execute('SELECT * FROM currencies WHERE date = (?)', (cdate,)):
        data1.append(row)
        #print(row)
    return data1

def PlotData(dataset):
    #count = len(data)
    plt.figure(figsize=(15,9))
    plt.axis((0,30,55,83))
    USD = [x[3] for x in dataset if x[1] == "USD"]
    EUR = [x[3] for x in dataset if x[1] == "EUR"]
    GBP = [x[3] for x in dataset if x[1] == "GBP"]
    xUSD = range(len(USD))
    xEUR = range(len(EUR))
    xGBP = range(len(GBP))
    plt.plot(xUSD, USD,"r-", label="USD")
    plt.plot(xEUR, EUR,"b--", label="EUR")
    plt.plot(xGBP, GBP,"g:", label="GBP")
    for i,j in zip(xUSD,USD):
        plt.annotate(str(j),xy=(i,j+0.5))
    for i,j in zip(xEUR,EUR):
        plt.annotate(str(j),xy=(i,j+0.5))
    for i,j in zip(xGBP,GBP):
        plt.annotate(str(j),xy=(i,j+0.5))
    plt.legend()    
    plt.show()
    
    
    
def DeleteByDate(cdate):
    print(cdate)
    conn.execute('''DELETE FROM currencies WHERE date = (?)''', (cdate,))
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)
    
"""USD 	57.5 	59.5
EUR 	68.0 	70.0
GBP 	77.25 	79.25
"""

#DeleteByDate("17.11.2017")
#print(GetDataOnDate("25.10.2017"))

DS = 57.5
DB = 59.5
ES = 68.0
EB = 70.0
PS = 77.25
PB = 79.25
    
AppendDataForToday([("USD",DS,DB),("EUR",ES,EB),("GBP",PS,PB)])    

data = GetData()
PlotData(data)
#DeleteByDate("10.10.2020")
    
conn.close()