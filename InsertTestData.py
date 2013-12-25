import sqlite3

def insert_data(values):
    with sqlite3.connect("FlowerbedDatabase.db") as db:
        cursor = db.cursor()
        #sql = "insert into Operation(date, time, duration, amount, cost, readingBeforeID, readingAfterID, valveID, flowerbedID) values (?,?,?,?,?,?,?,?,?)"
        sql = "insert into Plant(plantGrowing, datePlanted, waterNeed, flowerbedID) values (?,?,?,?)"
        #sql = "insert into Reading(readingID, date, time, reading, sensorID, readingTypeID) values (?,?,?,?,?,?)"
        #sql = "insert into Sensor_Type(sensorTypeID, sensorType) values (?,?)"
        #sql = "insert into Reading_Type(readingTypeID, readingType) values (?,?)"
        #sql = "insert into Flowerbed(flowerbedID) values (?)"
        #sql = "insert into Valve(valveID, flowerbedID) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    products = []
##    products.append((1,"08/09/2013","17:40",27,2,1))
##    products.append((2,"08/09/2013","17:40",28,2,1))
##    products.append((3,"08/09/2013","17:40",29,2,1))
##    products.append((4,"08/09/2013","17:40",30,2,1))
##    products.append((5,"08/09/2013","17:40",31,2,1))
##    products.append((6,"08/09/2013","17:40",32,2,1))
##    products.append((7,"08/09/2013","17:40",33,2,1))
##    products.append((8,"08/09/2013","17:40",34,2,1))
    
    products.append(("Roses","08/09/2013",5,3))
    products.append(("Lilies","08/09/2013",5,2))
    products.append(("Daffodils","08/09/2013",5,3))
    products.append(("Cake","08/09/2013",5,4))
    products.append(("Roses","08/09/2013",5,5))
    products.append(("Lilies","08/09/2013",5,7))
    products.append(("Daffodils","08/09/2013",5,6))
    products.append(("Cake","08/09/2013",5,8))
    
##    products.append(("08/09/2013","17:40",20,5,16,1,2,1,1))
##    products.append(("09/09/2013","17:40",20,5,16,3,4,1,1))
##    products.append(("10/09/2013","17:40",20,5,16,5,6,1,1))
##    products.append(("11/09/2013","17:40",20,5,16,7,8,1,1))

##    products.append((1,"Moisture"))
##    products.append((2,"Sun"))
##    products.append((3,"Rain"))

##    products.append((1,"Moisture"))
##    products.append((2,"Intensity"))
##    products.append((3,"Depth"))
##    products.append((4,"Duration"))

##    products.append((1,))
##    products.append((2,))
##    products.append((3,))
##    products.append((4,))
##    products.append((5,))
##    products.append((6,))
##    products.append((7,))
##    products.append((8,))

##    products.append((1,1))
##    products.append((2,2))
##    products.append((3,3))
##    products.append((4,4))
##    products.append((5,5))
##    products.append((6,6))
##    products.append((7,7))
##    products.append((8,8))

    
    for each in products:
        insert_data(each)
