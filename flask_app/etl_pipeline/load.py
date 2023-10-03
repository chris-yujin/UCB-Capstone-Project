import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d
import hvplot
from pathlib import Path

# Visualization parameter
plt.rcParams['figure.figsize'] = [12, 10]

import random
import time

# load to front end 

def loadcleandata():
    # import the cleaned data path
    medical_path = Path("../resources/medical_df.csv")
    medical_df = pd.read_csv(medical_path)
    # select only the columns we want to view
    ## include zipcode for users to view
    clean_df = medical_df[['ZIPCODE',
                           'STATE',
                           'Total Income per Individual',
                            'Lacking Health Insurance',
                            'Binge Drinking',
                            'High Blood Pressure',
                            'Routine Health Checkups',
                            'Currently Smoking', 
                            'Depression', 
                            'No Leisure-Time Physical Activity',
                            "Less than 7 Hours of Sleep" ]]

    return clean_df

# def viewcleandata(clean_df):


def timewaster():
    start_time = time.time()

    time.sleep(5)

    print("--- I wasted %s seconds ---" % (time.time() - start_time))

