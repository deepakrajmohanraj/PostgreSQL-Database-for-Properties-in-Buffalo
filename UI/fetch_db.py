from sqlalchemy import create_engine, text, inspect 
from sqlalchemy.orm import sessionmaker

class DataBase():
    def __init__(self, db_user = 'postgres', db_password = '1234') -> None:
        # Replace with your HelioHost database credentials
        self.db_user = 'postgresql'
        self.db_password = '1234'

        self.db_name = 'assessment'
        self.db_host = 'localhost'
        self.db_port = '5433'
        # Create a connection string
        # Replace the following values with your database credentials
        self.db_url = f"postgresql://{db_user}:{db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        # Set up the SQLAlchemy engine and session
        self.engine = None
        self.Session = None
        self.session = None
        self.results = None


    def connect(self):
        # Set up the SQLAlchemy engine and session
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()


    def close(self):
        print("Closing the database...")
        self.session.close()
        self.engine = None
        self.Session = None
        self.session = None


    def fetch_all(self):
        print("Fetching from the database...")
        # Execute the content of the SQL file
        query = """SELECT *
  FROM main 
  natural join building_style
  natural join construction_grade 
  natural join construction_quality 
  natural join deed
  natural join exterior_wall 
  natural join heat_type 
  natural join house_location
  natural join overall_condition 
  natural join owner_details
  limit 100;"""
        print("Executing...")
        self.results = self.session.execute(query)
        column_names = self.results.keys()
        print(column_names)
        print("Fetching...")
        data = self.results.fetchall()


        return data
    

    def fetch_cols_nms(self):
        if (self.results != None):
            print("Fetching cols name from the database...")
            # Get column names
            column_names = self.results.keys()
            return column_names
        else:
            print("Please run a query to execute")


    def get_pk(self):
        query = text("SELECT sbl FROM main")
        print("Fetching cols from db...")
        self.results = self.session.execute(query)
        # Fetch all the rows as a list of tuples
        return self.results.fetchall()
    
    
    def delete_row(self, sbl):
        # Delete from main
        print(sbl)
        main_query = text("DELETE FROM main WHERE sbl = :sbl")
        self.session.execute(main_query, {'sbl': sbl})
        # Delete from deed
        deed_query = text("DELETE FROM deed WHERE sbl = :sbl")
        self.session.execute(deed_query, {'sbl': sbl})
        # Delete from house_location
        house_location_query = text("DELETE FROM house_location WHERE sbl = :sbl")
        self.session.execute(house_location_query, {'sbl': sbl})
        # Delete from owner_details
        owner_details_query = text("DELETE FROM owner_details WHERE sbl = :sbl")
        self.session.execute(owner_details_query, {'sbl': sbl})
        # Commit the changes
        self.session.commit()
    

    def update_sbl(self, new_sbl, original_sbl):
        # Update sbl in main
        main_query = text("UPDATE main SET sbl = :new_sbl WHERE sbl = :original_sbl")
        self.session.execute(main_query, {'original_sbl': original_sbl, 'new_sbl': new_sbl})
        # Update sbl in deed
        deed_query = text("UPDATE deed SET sbl = :new_sbl WHERE sbl = :original_sbl")
        self.session.execute(deed_query, {'original_sbl': original_sbl, 'new_sbl': new_sbl})
        # Update sbl in house_location
        house_location_query = text("UPDATE house_location SET sbl = :new_sbl WHERE sbl = :original_sbl")
        self.session.execute(house_location_query, {'original_sbl': original_sbl, 'new_sbl': new_sbl})
        # Update sbl in owner_details
        owner_details_query = text("UPDATE owner_details SET sbl = :new_sbl WHERE sbl = :original_sbl")
        self.session.execute(owner_details_query, {'original_sbl': original_sbl, 'new_sbl': new_sbl})
        # Commit the changes
        self.session.commit()


    def update_value_by_sbl1(self, new_value, sbl, column_name, table):
        query = text(f"UPDATE {table} SET {column_name} = {new_value} WHERE sbl = {sbl}")
        self.session.execute(query)
        self.session.commit()


    def update_value_by_sbl2(self, new_value, sbl, column_name, table, table_id):
        subquery = f"SELECT {table_id}_id FROM {table} WHERE {table}_description = :new_value"
        query = text(f"UPDATE main SET {column_name} = ({subquery}) WHERE sbl = :{sbl}")
        self.session.execute(query,)
        self.session.commit()
        self.session.execute(query)
        self.session.commit()

    def create_user_table_if_not_exists(self):
        # Define the SQL CREATE TABLE statement
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS logs (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        """

        # Execute the SQL statement
        with self.engine.begin() as connection:
            connection.execute(text(create_table_sql))

        print(f"Table logs checked/created.")

    def user_exists(self, username):
        # Define the SQL SELECT statement to search for the user
        select_user_sql = f"SELECT * FROM login_info WHERE username = '{username}'"

        # Execute the SQL statement and fetch the result
        with self.engine.begin() as connection:
            result = connection.execute(text(select_user_sql)).fetchone()

        # Return True if a user is found, otherwise return False
        return result is not None
    

    def verify_password(self, username, password):
        # Fetch the stored password for the given username
        query = text(f"SELECT password FROM login_info WHERE username = '{username}'")
        result = self.session.execute(query).fetchone()

        # If the user doesn't exist, return False
        if result is None:
            return False

        stored_password = result[0]

        # Compare the provided password with the stored password
        if password == stored_password:
            return True
        else:
            return False
        
    def insert_user(self, username, password):
        # Define the SQL INSERT statement
        insert_user_sql = """
            INSERT INTO login_info (username, password) VALUES (:username, :password);
        """

        # Execute the SQL statement
        with self.engine.begin() as connection:
            connection.execute(text(insert_user_sql), {'username': username, 'password': password})

    def create_log(self, username):
        # Define the SQL INSERT statement
        insert_user_sql = """
            INSERT INTO user_logs (user_id) 
            select user_id from login_info 
            where username = :username;
        """

        # Execute the SQL statement
        with self.engine.begin() as connection:
            connection.execute(text(insert_user_sql), {'username': username})
