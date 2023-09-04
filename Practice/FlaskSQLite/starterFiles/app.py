# Importing the modules we will use for the app
import sqlite3
import random
from flask import Flask, session, render_template, request, g

# Initializing a class for our application and calling it app
app = Flask(__name__)
# Define a secret key used to encrypt our cookies
app.secret_key = "aymiguelyousureaboutthatimdone"

# Defining the main route for our application with an index function
@app.route("/", methods = ["POST", "GET"])
def index():

    # Calling our get_db function
    session["all_items"], session["shopping_items"] = get_db()

    # Returning the string instance of data
    return render_template("index.html", all_items = session["all_items"], shopping_items = session["shopping_items"])

# ADD ITEMS
# Must match 100% the action that we gave to our form 
@app.route("/add_items", methods=["post"])
def add_items():

    session["shopping_items"].append(request.form["select_items"])
    
    session.modified = True

    return render_template("index.html", all_items = session["all_items"], shopping_items = session["shopping_items"])

# REMOVE ITEMS
@app.route("/remove_items", methods=["post"])

def remove_items():

    checked_boxes = request.form.getlist("check")

    for item in checked_boxes: 

        if item in session["shopping_items"]:
           
            idx = session["shopping_items"].index(item)

            session["shopping_items"].pop(idx)

            session.modified = True

    return render_template("index.html", all_items = session["all_items"], shopping_items = session["shopping_items"])


# Our get database function (get_db) 
# Basically connects our SQLite db to our app
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        # Establishing a connection with our database and called it db
        db = g._database = sqlite3.connect('grocery_list.db')

        # Creating a cursor object to execute SQL commands
        cursor = db.cursor()

        # SQL command that selects the name column from the table inside our db
        cursor. execute("select name from groceries")

        # Holds the results of our execute command
        all_data = cursor.fetchall()

        # We only want the string inside, not the whole tuple
        # Variable all_data will now hold the values converted to strings
        all_data = [str(val[0]) for val in all_data]

        shopping_list = all_data.copy()
        random.shuffle(shopping_list)
        shopping_list = shopping_list[:5]

    # Return the contents of all_data
    return all_data, shopping_list

# For terminating our database connection once we are done using it
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# if __name__ is equal to main then our app will run
if __name__ == '__main__':
    app.run()