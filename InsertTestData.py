import sqlite3

def insert_data(values):
    with sqlite3.connect("FlowerbedDatabase.db") as db:
        cursor = db.cursor()
        ##sql = "insert into Operation(date, time, duration, amount, cost, readingBeforeID, readingAfterID, valveID, flowerbedID) values (?,?,?,?,?,?,?,?,?)"
        sql = "insert into Plant(plantGrowing, datePlanted, waterNeed, flowerbedID) values (?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    products = []
    products.append(("Roses","08/09/2013",5,1))
    products.append(("Lilies","08/09/2013",5,1))
    products.append(("Daffodils","08/09/2013",5,1))
    products.append(("Cake","08/09/2013",5,1))
    ##products.append(("08/09/2013","17:40",20,5,16,1,2,1,1))
    ##products.append(("09/09/2013","17:40",20,5,16,3,4,1,1))
    ##products.append(("10/09/2013","17:40",20,5,16,5,6,1,1))
    ##products.append(("11/09/2013","17:40",20,5,16,7,8,1,1))
    
    for each in products:
        insert_data(each)
