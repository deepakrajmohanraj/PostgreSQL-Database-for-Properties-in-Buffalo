from fetch_db import *
import time as t
import book_keep as bk

db_user = 'postgres'
db_password = '1234'

# Replace with your HelioHost database credentials
all_columns = bk.all_columns
column_dict = bk.column_dict

def to_XData(sql_result):
    sheet_data = {
        "name": "Sheet1",
        "rows": {}
    }

    for r, row in enumerate(sql_result):
        cells = {}
        for c, cell in enumerate(row):
            cell_text = str(cell)
            cells[c] = {"text": cell_text}
        sheet_data["rows"][r] = {"cells": cells}

    return [sheet_data]


def from_XData(x_data):
    sql_result = []
    sheet_data = x_data[0]
    rows = sheet_data["rows"]

    for r in rows:
        row_data = rows[r]["cells"]
        row_tuple = tuple(row_data[c]["text"] for c in row_data)
        sql_result.append(row_tuple)

    return sql_result

def list_to_dict(values):
    return {idx: value for idx, value in enumerate(values)}

def make_sbl_dict():
    db = DataBase(db_user, db_password)
    db.connect()
    data = db.get_pk()
    db.close()

    # Extract the first value from each tuple (since we're only selecting one column)
    values = [row[0] for row in data]
    return list_to_dict(values)


def delete_row(dict, sbl):
    db = DataBase(db_user, db_password)
    db.connect()
    db.delete_row(dict[sbl])
    db.close()
    dict = dict.pop(sbl)    
    # Create a list of values from the dictionary
    values_list = list(dict.values())
    return list_to_dict(values_list)

def update_sbl(text, sbl):
    db = DataBase(db_user, db_password)
    db.connect()
    db.update_sbl(text, sbl)
    db.close()

def update_value_by_sbl1(txt, sbl, column_nm, table):
    db = DataBase(db_user, db_password)
    db.connect()
    db.update_value_by_sbl1(txt, sbl, column_nm, table)
    db.close()
    pass

def update_value_by_sbl2(txt, sbl, column_nm, table):
    db = DataBase(db_user, db_password)
    db.connect()
    if (table in ['building_style', 'construction_quality', 'exterior_wall']):
        table_id = f"{table}_code"
        print((txt, sbl, column_nm, table))
        db.update_value_by_sbl2(txt, sbl, column_nm, table, table_id)
    else:
        db.update_value_by_sbl2(txt, sbl, column_nm, table, table)
        pass

    db.close()

def create_user_table_if_not_exists():
    # Usage example
    db = DataBase(db_user, db_password)
    db.connect()
    db.create_user_table_if_not_exists()
    db.close()

def read():
    db = DataBase(db_user, db_password)
    db.connect()
    start_time = t.time()
    data = db.fetch_all()
    end_time = t.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    db.close()
    print("loading")

    return to_XData(data)

def checkuser(username_to_check):
    # Usage example
    db = DataBase(db_user, db_password)
    db.connect()

    if db.user_exists(username_to_check):
        print(f"User '{username_to_check}' exists in the 'user' table.")
        db.close()
        return True

    else:
        print(f"User '{username_to_check}' does not exist in the 'user' table.")
        db.close()
        return False

def insert(username, password):
    db = DataBase(db_user, db_password)
    db.connect()
    db.insert_user(username, password)
    db.close()

def insert_log(username):
    db = DataBase(db_user, db_password)
    db.connect()
    db.create_log(username)
    db.close()

def verify_password(username, password):
    db = DataBase(db_user, db_password)
    try:
        db.connect()
        bool = db.verify_password(username, password)
        db.close()
        return bool
    except:
        return False


# if __name__ == "__main__":
#     insert("test1", "test123")
