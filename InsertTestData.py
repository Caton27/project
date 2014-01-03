import sqlite3

def insert_data(values):
    with sqlite3.connect("FlowerbedDatabase.db") as db:
        cursor = db.cursor()
        #sql = "insert into Operation(date, time, duration, amount, cost, readingBeforeID, readingAfterID, valveID, flowerbedID) values (?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,values)
        #sql = "insert into Plant(plantGrowing, datePlanted, waterNeed, flowerbedID) values (?,?,?,?)"
        cursor.execute(sql,values)
        #sql = "insert into Reading(readingID, date, time, reading, sensorID, readingTypeID) values (?,?,?,?,?,?)"
        cursor.execute(sql,values)
        #sql = "insert into Sensor_Type(sensorTypeID, sensorType) values (?,?)"
        cursor.execute(sql,values)
        #sql = "insert into Reading_Type(readingTypeID, readingType) values (?,?)"
        cursor.execute(sql,values)
        #sql = "insert into Flowerbed(flowerbedID) values (?)"
        cursor.execute(sql,values)
        #sql = "insert into Valve(valveID, flowerbedID) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    products = []
    products.append(("08/09/2013","17:40",27,25,3,1))
    products.append(("08/09/2013","17:40",28,25,3,1))
    products.append(("08/09/2013","17:40",29,25,3,1))
    products.append(("08/09/2013","17:40",30,25,3,1))
    products.append(("08/09/2013","17:40",31,25,4,1))
    products.append(("08/09/2013","17:40",32,25,4,1))
    products.append(("08/09/2013","17:40",33,25,5,1))
    products.append(("08/09/2013","17:40",34,25,5,1))
    for each in products:
        with sqlite3.connect("FlowerbedDatabase.db") as db:
            cursor = db.cursor()
            sql = "insert into Reading(date, time, reading, averageReading, sensorID, readingTypeID) values (?,?,?,?,?,?)"
            cursor.execute(sql,each)
            db.commit()

    products = []
    products.append(("Roses","08/09/2013",5,1))
    products.append(("Lilies","08/09/2013",5,1))
    products.append(("Daffodils","08/09/2013",5,1))
    products.append(("Cake","08/09/2013",5,1))
    for each in products:
        with sqlite3.connect("FlowerbedDatabase.db") as db:
            cursor = db.cursor()
            sql = "insert into Plant(plantGrowing, datePlanted, waterNeed, flowerbedID) values (?,?,?,?)"
            cursor.execute(sql,each)
            db.commit()

    products = []
    products.append(("Roses","08/09/2013",5,3))
    products.append(("Lilies","08/09/2013",5,2))
    products.append(("Daffodils","08/09/2013",5,3))
    products.append(("Cake","08/09/2013",5,4))
    products.append(("Roses","08/09/2013",5,5))
    products.append(("Lilies","08/09/2013",5,7))
    products.append(("Daffodils","08/09/2013",5,6))
    products.append(("Cake","08/09/2013",5,8))
    for each in products:
        with sqlite3.connect("FlowerbedDatabase.db") as db:
            cursor = db.cursor()
            sql = "insert into Plant(plantGrowing, datePlanted, waterNeed, flowerbedID) values (?,?,?,?)"
            cursor.execute(sql,each)
            db.commit()
    
    products = []
    products.append(("08/09/2013","17:40",20,5,16,1,2,1,1))
    products.append(("09/09/2013","17:40",20,5,16,3,4,1,1))
    products.append(("10/09/2013","17:40",20,5,16,5,6,1,1))
    products.append(("11/09/2013","17:40",20,5,16,7,8,1,1))
    for each in products:
        with sqlite3.connect("FlowerbedDatabase.db") as db:
            cursor = db.cursor()
            sql = "insert into Operation(date, time, duration, amount, cost, readingBeforeID, readingAfterID, valveID, flowerbedID) values (?,?,?,?,?,?,?,?,?)"
            cursor.execute(sql,each)
            db.commit()

    products = []
    products.append((1,"Moisture"))
    products.append((2,"Sun"))
    products.append((3,"Rain"))
    for each in products:
        with sqlite3.connect("FlowerbedDatabase.db") as db:
            cursor = db.cursor()
            sql = "insert into Sensor_Type(sensorTypeID, sensorType) values (?,?)"
            cursor.execute(sql,each)
            db.commit()

    products = []
    products.append((1,"Moisture"))
    products.append((2,"Intensity"))
    products.append((3,"Depth"))
    products.append((4,"Duration"))
    for each in products:
        with sqlite3.connect("FlowerbedDatabase.db") as db:
            cursor = db.cursor()
            sql = "insert into Reading_Type(readingTypeID, readingType) values (?,?)"
            cursor.execute(sql,each)
            db.commit()

    products = []
    products.append((1,))
    products.append((2,))
    products.append((3,))
    products.append((4,))
    products.append((5,))
    products.append((6,))
    products.append((7,))
    products.append((8,))
    for each in products:
        with sqlite3.connect("FlowerbedDatabase.db") as db:
            cursor = db.cursor()
            sql = "insert into Flowerbed(flowerbedID) values (?)"
            cursor.execute(sql,each)
            db.commit()

    products = []
    products.append((1,))
    products.append((2,))
    products.append((3,))
    products.append((4,))
    products.append((5,))
    products.append((6,))
    products.append((7,))
    products.append((8,))
    for each in products:
        with sqlite3.connect("FlowerbedDatabase.db") as db:
            cursor = db.cursor()
            sql = "insert into Valve(flowerbedID) values (?)"
            cursor.execute(sql,each)
            db.commit()


    products = []
    products.append((2,0))
    products.append((3,0))
    products.append((1,1))
    products.append((1,1))
    products.append((1,1))
    products.append((1,2))
    products.append((1,2))
    products.append((1,2))
    for each in products:
        with sqlite3.connect("FlowerbedDatabase.db") as db:
            cursor = db.cursor()
            sql = "insert into Sensor(sensorTypeID, flowerbedID) values(?,?)"
            cursor.execute(sql,each)
            db.commit()
