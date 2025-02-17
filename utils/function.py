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


def predict_freshwater(distances, scaler, model):
    distance_scaled = scaler.transform(distances)
    fwneeds = []
    for item in distance_scaled:
        fw = model.predict(item.reshape(1, -1))
        fwneeds.append(int(fw[0]))
    return fwneeds, sum(fwneeds)
