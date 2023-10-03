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

# import postgres credentials
from config import postgres_username, db_password

# You can put your ML functions somewhere out here
# import testimport as t
import pickle_models as pkl

#################################################
# Database Setup
#################################################
from etl_pipeline import load 


clean_df = load.loadcleandata()

#################################################
# Read in saved models
#################################################
o_model = pkl.read_om_model()
c_model = pkl.read_c_model()
d_model = pkl.read_d_model()

# Create SQLAlchemy engine to connect to Postgresql Database


engine = create_engine(f"postgresql+psycopg2://{postgres_username}:{db_password}@localhost:5432/test_db")

# Convert clean_df dataframe to sql table                                   
clean_df.to_sql('datapoints', engine, index=False, if_exists="replace")

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

# @app.route("/")
# def home():
#     return render_template("home.html")
@app.route("/dataload")
def dataload():
    print("Function Started")
    load.timewaster()
    print("Function Ended")
    return redirect(url_for("home"))

@app.route("/predict/<a>/<b>/<c>/<d>/<e>/<f>/<g>/<h>/<i>")
def predict(a,b,c,d,e,f,g,h,i):
    test = float(a)+float(b)+float(c)+float(d)+float(e)+float(f)+float(g)+float(h)+float(i)
    return jsonify(sum=round(test,2), 
                   obesity_prevalance=float(pkl.all_predict(o_model,c_model, d_model, a,b,c,d,e,f,g,h,i)[0]),
                   cancer_prevalance=float(pkl.all_predict(o_model,c_model, d_model, a,b,c,d,e,f,g,h,i)[1]),
                   diabetes_prevalance=float(pkl.all_predict(o_model,c_model, d_model, a,b,c,d,e,f,g,h,i)[2]),
                   )



@app.route("/gettable")
def gettable():
    with engine.connect() as conn:
        query = text("SELECT * FROM datapoints LIMIT 10")
        results = conn.execute(query).fetchall()
    resultlist = []
    for row in results:
        resultlist.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]])

    return jsonify(data=resultlist)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route("/update_data/<zipcode>")
def update_data(zipcode):
    #convert user input as an integer
    zipcode = int(zipcode)

    with engine.connect() as conn:
        query = text(f'SELECT * FROM datapoints WHERE "ZIPCODE" = {zipcode}')
        results = conn.execute(query).fetchall()

    if not results:
        # Handle the case where no data is found for the given zipcode
        return jsonify(error="No data found for the provided zipcode")

    # Process the results and extract the necessary values
    data = results[0]
    state = data[1]
    income_per_individual = data[2]
    lacking_health_insurance = data[3]
    binge_drinking = data[4]
    high_blood_pressure = data[5]
    routine_check_ups = data[6]
    currently_smoking = data[7]
    depressed = data[8]
    no_leisure_physical_activity =data[9]
    less_7_hours_sleep = data[10]
    

    # Return the extracted data as JSON
    return jsonify(
        zipcode=zipcode,
        state = state,
        income_per_individual=income_per_individual,
        lacking_health_insurance=lacking_health_insurance,
        binge_drinking = binge_drinking,
        high_blood_pressure = high_blood_pressure,
        routine_check_ups = routine_check_ups,
        currently_smoking = currently_smoking,
        depressed = depressed,
        no_leisure_physical_activity = no_leisure_physical_activity,
        less_7_hours_sleep = less_7_hours_sleep
    )

if __name__ == "__main__":
    app.run(debug=True)