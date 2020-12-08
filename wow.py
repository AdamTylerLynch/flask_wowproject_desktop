import sqlalchemy

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base




engine = sqlalchemy.create_engine('postgresql://postgres:dmcin003@hostname/postgres', echo=True)


# these two lines perform the "database reflection" to analyze tables and relationships
Base = automap_base()
Base.prepare(engine, reflect=True)



allegations = Base.classes.Allegations
session = Session(engine)


app = Flask(__name__)





@app.route('/',methods=["GET","POST"])
def home():
    return render_template('home.html')


# this allows the python file to run
if __name__ == "__main__":
    app.run()