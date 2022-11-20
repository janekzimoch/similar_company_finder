import sqlite3 as db
import pandas as pd

def getSector(db_path, company):
    con = db.connect(db_path)
    df = pd.read_sql_query(f"SELECT sector, sector_id FROM Companies WHERE name='{company}'", con)
    sector = df['sector'].values[0]
    sector_id = df['sector_id'].values[0]
    con.close()
    return sector, sector_id

def getSectorCompanies(db_path, sector_id):
    con = db.connect(db_path)
    sector = None
    df = pd.read_sql_query(f"SELECT name FROM Companies WHERE sector_id={sector_id}", con)
    companies = df[:10].to_dict(orient="index")
    con.close()
    return companies
