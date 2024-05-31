# util.py
import pickle
import json
import numpy as np

# Load the saved model and other artifacts
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    with open("./server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # First 3 columns are sqft, bath, bhk

    with open("./server/artifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

# Load artifacts when the module is imported
load_saved_artifacts()
