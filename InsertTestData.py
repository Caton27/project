import sqlite3

def insert_data(values):
    with sqlite3.connect("FlowerbedDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Plant (plantGrowing,datePlanted,waterNeed,flowerbedID) values (?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    products = []
    products.append(("Roses","08/09/2013",0.22,1))
    products.append(("Cake","23/11/2013",4.20,1))
    
    for each in products:
        insert_data(each)
