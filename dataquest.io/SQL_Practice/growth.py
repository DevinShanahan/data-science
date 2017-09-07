import pandas as pd
import sqlite3
import math

conn = sqlite3.connect('factbook.db')

facts = pd.read_sql_query("SELECT * FROM facts;",conn)

def population_2050(row):
    return row["population"] * (math.e ** ((row["population_growth"]/100)*35))

facts["2050"] = facts[["population","population_growth"]].apply(population_2050, axis=1)

facts.sort_values("2050", ascending=False, inplace=True)

print(facts.head(10))

conn.close()
