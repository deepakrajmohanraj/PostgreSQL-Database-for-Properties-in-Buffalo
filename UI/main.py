from flask import Flask, render_template, request, session, make_response
import json as j
from flask import redirect
from urllib.parse import urlparse, urlunparse
import parse as par
from parse import all_columns, column_dict
import data as d

sheet_data = -1
sbl_dict = -1
sheet_data = par.read()
sbl_dict = par.make_sbl_dict()

app = Flask(__name__)
app.secret_key = 'alphabeta'

@app.route('/get_table_options', methods=['GET'])
def get_table_options():
    options = d.get_table_options_sql()
    html = ''
    for option in options.values.tolist():
        html += f'<option value="{option[0]}">{option[0].capitalize().replace("_", " ")}</option>\n'
    return html


@app.route('/submit', methods=['POST'])
def submit():
    operation = request.form.get('dropdown1')
    limit = request.form.get('dropdown2')
    table_name = request.form.get('dropdown3')
    sbl_key = request.form.get('textfield')
    key = request.form.get('textfield_key')  
    column_name = request.form.get('textfield2')  
    text = request.form.get('textfield3')  

    if operation == "read":  # Read
        return d.read(table_name,limit)

    elif operation == "insert":  # Insert
        return d.insert(table_name, text, limit)

    elif operation == "delete":  # Delete
        return  d.delete(table_name, column_name, limit, text)

    elif operation == "update":  # Update
        return  d.update(table_name, sbl_key, column_name, text, limit, key)


    elif operation == "find":  # Update
        return  d.find_value(table_name, column_name, text)
    elif operation == "pincode":  # Update
        return  d.get_pincode_stat(int(text))
    elif operation == "Number of buildings":  # Update
        return  d.num_of_houses(text, limit)
    elif operation == "Average Statistics":  # Update
        return  d.avg_stat(text, limit)
    else:
        return "Invalid operation"


@app.route('/')
def index():
  return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return 'You are now logged out'

@app.route('/home')
def home():
  # show the home page for logged-in users
  global sbl_dict
  global sheet_data
  if sbl_dict == -1:
    sbl_dict = par.make_sbl_dict()
  else:
    print("Server loaded [===...]")
  print("Server loaded [====..]")
  if sheet_data == -1:
    sheet_data = par.read()
  else:
    print("Server loaded [======]")
  return render_template('home.html')

# @app.route('/load_init', methods=['GET', 'POST'])
# def load_init():
#   global sbl_dict
#   global sheet_data
#   # assuming this function retrieves the SQL result
#   if sheet_data == -1:
#     sheet_data = par.read()
#   else:
#     print("Fetch from cache")
#   return j.dumps(sheet_data)

# @app.route('/update', methods=['GET', 'POST'])
# def update():
#   global sbl_dict
#   global sheet_data
#   data = request.get_json()
#   row = data["row"]
#   column = data["column"]
#   txt = data["text"]
#   sbl = sbl_dict[row]
#   column_nm = all_columns[column_dict[column]]
#   table = column_nm[0]
#   flag = column_nm[1]
  
#   if column_nm == 'sbl':
#     par.update_sbl(txt, sbl_dict[row])
#     sbl_dict[row] = txt
#   elif flag == "":
#     par.update_value_by_sbl1(txt, sbl, column_nm, table)
#   else:
#     par.update_value_by_sbl1(txt, sbl, column_nm, table)

#   return "Done"

# @app.route('/delete', methods=['GET', 'POST'])
# def actions():
#   global sbl_dict
#   global sheet_data
#   data = request.get_json()
#   sbl_dict = par.delete_row(sbl_dict, data["row"])
#   return "Deleted"



@app.route('/login', methods=['POST'])
def login():
  # process the form data
  username = request.json['username']
  password = request.json['password']

  # if username  == 'zemingzhang1_admin' and password == 'Database@admin':
  #   return response

  if par.checkuser(username):
    if par.verify_password(username, password):
      # log the user in and redirect to the home page
      session['admin'] = True
      session['logged_in'] = True
      session['username'] = username
      par.insert_log(username)
    else:
      # show an error message for incorrect password
      error = 'Invalid password, please try again'
      response = make_response(error)
      response.status_code = 400
      return response
    
  else:
    # show an error message
    error = 'Invalid username or password, please register'
    response = make_response(error)
    response.status_code = 400
  return j.dumps({"flag":1})

    
# route for handling user registration
@app.route('/register', methods=['POST'])
def register():
  # get the JSON data from the request
  data = request.json
  # extract the values from the data
  username = data['username']
  password = data['password']

  if not par.checkuser(username):
    par.insert(username,password)
    session['admin'] = True
    session['logged_in'] = True
    session['username'] = username
  
  
  else:
    # show an error message
    error = 'Invalid username or password, please register'
    response = make_response(error)
    response.status_code = 400
    return response 

  return j.dumps({"flag":1})

app.run(host='0.0.0.0', port=8080)