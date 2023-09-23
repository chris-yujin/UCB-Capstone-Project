# Import the dependencies
import pandas as pd
import numpy as np
import datetime as dt

from flask import Flask, redirect, url_for, render_template, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, text
import psycopg2

# You can put your ML functions somewhere out here
import testimport as t

#################################################
# Database Setup
#################################################

a = t.build_blobs()
model = t.train_model(a)
a2 = t.view_clusters(model, a)

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/test_db")

# Convert dataframe to sql table                                   
a2.to_sql('datapoints', engine, index=False, if_exists="replace")

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# We can nest other functions within the first function to do some fancy stuff
@app.route("/")
def loader():
    # Start at loading page
    return render_template("loader.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/mltrain")
def mltrain():
    print("Function Started")
    t.timewaster()
    print("Function Ended")
    return redirect(url_for("home"))

@app.route("/predict/<a>/<b>/<c>")
def predict(a,b,c):
    test = float(a)+float(b)+float(c)
    return jsonify(sum=round(test,2), cluster=int(t.predict(model, a,b,c)))

@app.route("/gettable")
def gettable():
    with engine.connect() as conn:
        results = conn.execute("SELECT * FROM datapoints").fetchall()
    resultlist = []
    for row in results:
        resultlist.append([row[0], row[1], row[2], row[3]])

    return jsonify(data=resultlist)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)