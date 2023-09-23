# Import dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d
import hvplot

# Visualization parameter
plt.rcParams['figure.figsize'] = [12, 10]

import random
import time
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering, Birch
    
def build_blobs():
    X, y = make_blobs(n_samples=400, n_features=3, centers=4)
    a = pd.DataFrame(data={"x1":X[:,0], "x2":X[:,1], "x3":X[:,2], "y":y})
    a2 = a.drop(columns="y")

    return a2

def train_model(df):
    model = KMeans(n_init=10, n_clusters=4)
    model.fit(df)
    return model

def view_clusters(model, df):
    predictions = model.predict(df)
    df["pred"]=predictions

    return df

def predict(model, a,b,c):
    arr = np.array([a,b,c])
    return model.predict(arr.reshape(1,-1))[0]


def timewaster():
    start_time = time.time()

    time.sleep(5)

    print("--- I wasted %s seconds ---" % (time.time() - start_time))