import sqlalchemy

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base


# Everyone on your team should be using the same database user (not 'postgres'), I created a user named 'wowprojectuser'.
# Everyone on your team should have the same password for that user.
# The server you connect to is "localhost", that is your localcomputer, and will be resolved by DNS as 127.0.0.1
# Everyone on your team should use the data database name, I have chosen "WOWProjectOfficer"

engine = sqlalchemy.create_engine('postgresql://wowprojectuser:thisismypassword@localhost/WOWProjectOfficer', echo=True)


# these two lines perform the "database reflection" to analyze tables and relationships
Base = automap_base()
Base.prepare(engine, reflect=True)



allegations = Base.classes.allegations
session = Session(engine)


app = Flask(__name__)





@app.route('/',methods=["GET","POST"])
def home():
    return render_template('home.html')


# this allows the python file to run
if __name__ == "__main__":
    app.run()