def read(table_name):
  sql = "SELECT * FROM " + table_name
def insert(table_name):
  sql = "INSERT INTO " +table_name + " ("+")"+" VALUES ("+")"
def update(table_name, sbl_key, column_name, text):
  sql = "UPDATE " +table_name +"SET "+column_name+" = "+text+" where sql = "+sbl_key
def delete(table_name, sbl_key):
  sql = "delete from"+table_name +"where sbl =" + sbl_key