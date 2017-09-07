import sqlite3
import pandas as pd

conn = sqlite3.connect('factbook.db')

c = conn.cursor()

c.execute("SELECT SUM(area_land) FROM facts WHERE area_land != \"\";")
area_land = c.fetchall()[0][0]

c.execute("SELECT SUM(area_water) FROM facts WHERE area_water != \"\";")
area_water = c.fetchall()[0][0]
total_area = area_land + area_water
print("Land Area: "+str(area_land/total_area),"Water Area: "+str(area_water/total_area))

conn.close()
