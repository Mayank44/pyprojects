"""item list stuff"""
import sqlite3
class Item:
    def __init__(self, itemID, itemname, weight):
        self.itemID = itemID
        self.itemname = itemname
        self.weight = weight

conn = sqlite3.connect("""E:\\Mayank\\Documents\\A-level work\\Computing\\python\\NEA actual things\\program file\\Database\\items_data.db""")

results = conn.execute("""SELECT ItemID, Name, Weight FROM Item""")
itemindex = []
for row in results:
    x= list(row)
    obj_thing = Item(x[0],x[1],x[2])
    itemindex.append(obj_thing)
name = []
for i in itemindex:
    name.append(i.itemname)
print(name)    



#itemindex=[Chair,Table,Mouse,Keyboard,Monitor,Computer,Speakers,Headphones,Earphones,Mousemat,Bedframe,Matress]
