import sqlite3

def check_table(db_name,table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name = ?",(table_name,))
        result = cursor.fetchall()
        if len(result) == 1:
            return True
        else:
            return False

def create_table_Flowerbed(db_name,table_name):
    exists = check_table(db_name,table_name)
    if exists == False:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            #turn on foreign keys
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = """create table Flowerbed(
                  flowerbedID Integer,
                  primary key(flowerbedID))"""
            cursor.execute(sql)
            db.commit()

def create_table_Valve(db_name,table_name):
    exists = check_table(db_name,table_name)
    if exists == False:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            #turn on foreign keys
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = """create table Valve(
                  valveID Integer,
                  flowerbedID Integer,
                  primary key(valveID),
                  foreign key(FlowerbedID) references Flowerbed(flowerbedID))"""
            cursor.execute(sql)
            db.commit()

def create_table_Plant(db_name,table_name):
    exists = check_table(db_name,table_name)
    if exists == False:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            #turn on foreign keys
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = """create table Plant(
                  plantID Integer,
                  plantGrowing Text,
                  datePlanted Text,
                  waterNeed Float,
                  flowerbedID Integer,
                  primary key(plantID),
                  foreign key(flowerbedID) references Flowerbed(flowerbedID))"""
            cursor.execute(sql)
            db.commit()

def create_table_Sensor_Type(db_name,table_name):
    exists = check_table(db_name,table_name)
    if exists == False:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            #turn on foreign keys
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = """create table Sensor_Type(
                  sensorTypeID Integer,
                  sensorType Text,
                  primary key(sensorTypeID))"""
            cursor.execute(sql)
            db.commit()

def create_table_Sensor(db_name,table_name):
    exists = check_table(db_name,table_name)
    if exists == False:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            #turn on foreign keys
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = """create table Sensor(
                  sensorID Integer,
                  sensorTypeID Integer,
                  flowerbedID Integer,
                  primary key(sensorID),
                  foreign key(sensorTypeID) references Sensor_Type(sensorTypeID),
                  foreign key(flowerbedID) references Flowerbed(flowerbedID))"""
            cursor.execute(sql)
            db.commit()

def create_table_Reading_Type(db_name,table_name):
    exists = check_table(db_name,table_name)
    if exists == False:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            #turn on foreign keys
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = """create table Reading_Type(
                  readingTypeID Integer,
                  readingType Text,
                  primary key(readingTypeID))"""
            cursor.execute(sql)
            db.commit()

def create_table_Reading(db_name,table_name):
    exists = check_table(db_name,table_name)
    if exists == False:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            #turn on foreign keys
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = """create table Reading(
                  readingID Integer,
                  date Text,
                  time Text,
                  reading Float,
                  sensorID Integer,
                  readingTypeID Integer,
                  primary key(readingID),
                  foreign key(sensorID) references Sensor(sensorID),
                  foreign key(readingTypeID) references Reading_Type(readingTypeID))"""
            cursor.execute(sql)
            db.commit()

def create_table_Operation(db_name,table_name):
    exists = check_table(db_name,table_name)
    if exists == False:
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            #turn on foreign keys
            cursor.execute("PRAGMA foreign_keys = ON")
            sql = """create table Operation(
                  operationID Integer,
                  date Text,
                  time Text,
                  duration Integer,
                  amount Float,
                  cost Float,
                  readingBeforeID Integer,
                  readingAfterID Integer,
                  valveID Integer,
                  primary key(operationID),
                  foreign key(readingBeforeID) references Reading(readingID),
                  foreign key(readingAfterID) references Reading(readingID),
                  foreign key(valveID) references Valve(valveID))"""
            cursor.execute(sql)
            db.commit()



if __name__ == "__main__":
    db_name = "FlowerbedDatabase.db"
    tableList = ["Flowerbed","Valve","Plant","Sensor_Type","Sensor","Reading_Type","Reading","Operation"]
    create_table_Flowerbed(db_name,tableList[0])
    create_table_Valve(db_name,tableList[1])
    create_table_Plant(db_name,tableList[2])
    create_table_Sensor_Type(db_name,tableList[3])
    create_table_Sensor(db_name,tableList[4])
    create_table_Reading_Type(db_name,tableList[5])
    create_table_Reading(db_name,tableList[6])
    create_table_Operation(db_name,tableList[7])
