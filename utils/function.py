import pandas as pd
import xgboost as xgb


def get_capacity(df, ship):
    capacity = df[df["ship"] == ship]["tank_capacity"].to_list()
    return capacity


def get_ship_data(ship, asj, ren, aka):
    dataframe = None
    if ship == "ASJ":
        dataframe = asj
    elif ship == "REN":
        dataframe = ren
    elif ship == "AKA":
        dataframe = aka
    return dataframe


def get_voyage(ship):
    voyage = ship["VOYAGE"].to_list()
    return voyage


def get_list(df, reference, reference_column, destination_column):
    lst = df.loc[df[reference_column] == reference, destination_column].values
    return lst


def get_distances(df, trips):
    distance = []
    for trip in trips:
        item = get_list(df, trip, "TRIP", "DISTANCE")
        wrapper = list(item)
        distance.append(wrapper)
    return distance


def predict_freshwater(distances, model_columns, model):
    # Convert to numeric list
    numeric_distances = [int(d[0]) for d in distances]  # assuming d = ['450']
    
    # Build base DataFrame
    test_df = pd.DataFrame({'DISTANCE': numeric_distances})
    
    # Add missing one-hot encoded columns as 0
    for col in model_columns:
        if col != 'DISTANCE':
            test_df[col] = 0

    # Reorder to match training
    test_df = test_df[model_columns]

    # Convert to DMatrix and predict
    dmatrix_test = xgb.DMatrix(test_df)
    predictions = model.predict(dmatrix_test)

    # Round to int, return list + sum
    fwneeds = [int(pred) for pred in predictions]
    return fwneeds, sum(fwneeds)
