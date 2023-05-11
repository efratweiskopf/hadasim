import sqlite3

DATABASE = "../data/hadas.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_tables():
    customer_data = """CREATE TABLE IF NOT EXISTS customer_data 
            (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                fullname TEXT,
                address TEXT,
                date_of_birth DATE,
                home_number INTEGER,
                cellphone_number INTEGER
            )
            """
    
    corona_data = """CREATE TABLE IF NOT EXISTS corona_data
            (customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_vac DATE,
            first_vac_manu TEXT,
            second_vac DATE,
            second_vac_manu TEXT,
            third_vac DATE,
            third_vac_manu TEXT,
            fourth_vac DATE,
            fourth_vac_manu TEXT)
            """
    
    image_data = """CREATE TABLE IF NOT EXISTS image_data
            (customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT)
            """

    db = get_db()
    cursor = db.cursor()
    for table in [customer_data,corona_data,image_data]:
        cursor.execute(table)
    cursor.close()


