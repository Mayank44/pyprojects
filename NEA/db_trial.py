"""test db"""
import sqlite3

conn = sqlite3.connect("""Database\\items_data.db""")

conn.execute("""CREATE TABLE `Item` (
	`ItemID`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT,
	`Weight`	REAL,
	`Quantity`	INTEGER,
	`DeliveryStatus`	INTEGER DEFAULT 0
)""")

conn.execute("""INSERT INTO Item ( Name, Weight, Quantity ) VALUES ( "chair"    , 5  , 1) , ( "table"     , 7  , 1), 
                                                                   ( "mouse"    , 0.5, 1) , ( "keyboard"  , 1  , 1),
                                                                   ( "monitor"  , 2.5, 1) , ( "computer"  , 8  , 1),
                                                                   ( "speaker"  , 2  , 1) , ( "headphones", 1  , 1),
                                                                   ( "earphones", 0.5, 1) , ( "mousemat"  , 0.5, 1),
                                                                   ( "bedframe" , 10 , 1) , ( "matress"   , 8  , 1)""")
conn.commit()
conn.close()