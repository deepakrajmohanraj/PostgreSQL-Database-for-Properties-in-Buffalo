import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import os
import plotly.graph_objs as go

username="postgres"
password="1234"
host="localhost"
port="5433"
database="assessment"

def create_conn():
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=username,
        password=password,
        port=port
    )
    return conn

def execute_sql(sql):
    conn = create_conn()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()
def get_table_options_sql():
    conn = create_conn()
    query = """SELECT tablename
    FROM pg_catalog.pg_tables
    WHERE schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';"""
    df = pd.read_sql_query(query, conn)
    # Convert the DataFrame to HTML and return it
    return df
def read(table_name, limit):
    # Create a connection to your PostgreSQL database
    conn = create_conn()
    # Write a SQL query to select the first 20 records from the table
    query = f"SELECT * FROM {table_name} LIMIT {limit} "
    if limit == "ALL":
        query = f"SELECT * FROM {table_name}"
    # Execute the query and store the result in a DataFrame
    print("loading")
    df = pd.read_sql_query(query, conn)
    # Convert the DataFrame to HTML and return it
    return df.to_html(index=False)

def insert(table_name, values, limit):
    sql = f"INSERT INTO {table_name} VALUES ({values})"
    execute_sql(sql)
    return read(table_name, limit)

def update(table_name, sbl_key, column_name, text, limit, key):
    sql = f"UPDATE {table_name} SET {column_name} = '{text}' WHERE {key} = '{sbl_key}'"
    execute_sql(sql)
    return read(table_name, limit)

def delete(table_name, column_name, limit, value):
    sql = f"DELETE FROM {table_name} WHERE {column_name} = '{value}'"
    execute_sql(sql)
    return read(table_name, limit)

def find_value(table_name, column_name, value):
    # Create a connection to your PostgreSQL database
    conn = create_conn()
    # Write a SQL query to select the records from the table where the column value matches the input value
    query = f"SELECT * FROM {table_name} WHERE {column_name} = '{value}'"
    # Execute the query and store the result in a DataFrame
    df = pd.read_sql_query(query, conn)
    # Convert the DataFrame to HTML and return it
    return df.to_html(index=False)

def get_pincode_stat(pincode):
    # Create a connection to your PostgreSQL database
    conn = create_conn()
    # Write a SQL query to select the records from the table where the column value matches the input value
    query = f"SELECT * FROM get_zipcode_stats({pincode});"
    # Execute the query and store the result in a DataFrame
    df = pd.read_sql_query(query, conn)
    # Convert the DataFrame to HTML and return it
    return df.to_html(index=False)

def num_of_houses(pincode, limit):
    # Create a connection to your PostgreSQL database
    conn = create_conn()
    # Write a SQL query to select the records from the table where the column value matches the input value
    query = """
WITH location_info AS (
    SELECT
        h.sbl, h.house_number, h.street, h.zipcode, h.latitude, h.longitude, h.neighborhood, m.year_built, 
		m.total_value, m.land_value, m.number_of_units, m.no_of_stories, m.total_living_area, 
		bs.building_style_description, cg.construction_grade_description, cq.construction_quality_description, 
		ew.exterior_wall_description
    FROM
        house_location h JOIN main m ON h.sbl = m.sbl JOIN building_style bs ON m.building_style_code = bs.building_style_code
        JOIN construction_grade cg ON m.construction_grade = cg.construction_grade
        JOIN construction_quality cq ON m.construction_quality_code = cq.construction_quality_code
        JOIN exterior_wall ew ON m.exterior_wall_code = ew.exterior_wall_code WHERE h.zipcode = """+pincode+"""
),
grouped_info AS (
    SELECT
        li.neighborhood, AVG(li.year_built) AS avg_year_built, AVG(li.total_value) AS avg_total_value, AVG(li.land_value) AS avg_land_value,
        SUM(li.number_of_units) AS total_units, AVG(li.no_of_stories) AS avg_no_of_stories, AVG(li.total_living_area) AS avg_total_living_area,
        COUNT(*) AS num_buildings FROM location_info li GROUP BY li.neighborhood
),
ordered_info AS (
    SELECT
        gi.neighborhood, gi.avg_year_built, gi.avg_total_value, gi.avg_land_value, gi.total_units, gi.avg_no_of_stories, gi.avg_total_living_area,
        gi.num_buildings, ROW_NUMBER() OVER (ORDER BY gi.avg_total_value DESC) AS rank FROM grouped_info gi
)
SELECT * FROM ordered_info WHERE rank <= """+limit+""";"""
    # Execute the query and store the result in a DataFrame
    df = pd.read_sql_query(query, conn)
    return df.to_html(index=False)


def avg_stat(total_value, limit):
    # Create a connection to your PostgreSQL database
    conn = create_conn()
    # Write a SQL query to select the records from the table where the column value matches the input value
    query = """SELECT bs.building_style_description, cg.construction_grade_description, COUNT(*) AS total_houses,
  AVG(m.total_value) AS avg_total_value, MIN(m.year_built) AS min_year_built, MAX(m.year_built) AS max_year_built
FROM main m
JOIN building_style bs ON m.building_style_code = bs.building_style_code
JOIN construction_grade cg ON m.construction_grade = cg.construction_grade
GROUP BY bs.building_style_description, cg.construction_grade_description
HAVING COUNT(*) > 10 AND AVG(m.total_value) > """+total_value+"""
ORDER BY total_houses DESC limit """+limit+""";"""
    # Execute the query and store the result in a DataFrame
    df = pd.read_sql_query(query, conn)
    # Convert the DataFrame to HTML and return it
    return df.to_html(index=False)



