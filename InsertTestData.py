import sqlite3

def insert_data(values):
    with sqlite3.connect("FlowerbedDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Operation(date, time, duration, amount, cost, readingBeforeID, readingAfterID, valveID, flowerbedID) values (?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    products = []
    products.append(("08/09/2013","17:40",20,5,16,4,6,1,1))
    
    for each in products:
        insert_data(each)
