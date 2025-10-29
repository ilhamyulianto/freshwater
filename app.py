import streamlit as st
import pandas as pd
import joblib
import locale
import json
import xgboost as xgb

from utils.dataframe import df_ship, df_ship_distance, df_asj, df_ren, df_aka, df_fwcost
from utils.function import (
    get_capacity,
    get_ship_data,
    get_voyage,
    get_list,
    get_distances,
    predict_freshwater,
)
from utils.PSO import particle_swarm_optimization as pso

model = joblib.load("notebook/xgb_modeljson.pkl")
with open("notebook/xgb_columns.json") as f:
    model_columns = json.load(f)
locale.setlocale(locale.LC_ALL, "")

st.set_page_config(
    page_title="SPIL | Ship Freshwater Management",
    page_icon="image\spil_logo.svg",
    # layout="wide",
)
# Navbar


def checkValue(item):
    if item == None:
        return True
    return False


st.title("Ship Freshwater Management")


with st.container():
    st.header("Choose Ship and Voyage")
    ships = df_ship["ship"].to_list()
    ship_select, voyage_select = st.columns(2)
    with ship_select:
        ship_input = st.selectbox(
            "Select Ship",
            ships,
            index=0,
        )
    # load data
    ship = get_ship_data(ship_input, df_asj, df_ren, df_aka)
    voyages = get_voyage(ship)
    with voyage_select:
        voyage_input = st.selectbox(
            "Select Voyage",
            voyages,
            index=0,
            disabled=checkValue(ship_input),
        )
    # st.write(ship)
    submit_button = st.button(
        "Predict",
        type="primary",
        disabled=checkValue(voyage_input),
        use_container_width=True,
    )

# Ambil Data untuk Disply Rute Perjalanan
capacity = get_capacity(df_ship, ship_input)
ports_list = get_list(ship, voyage_input, "VOYAGE", "PORTS")
trips_list = get_list(ship, voyage_input, "VOYAGE", "TRIPS")

ports = ports_list[0].split(";")
trips = trips_list[0].split(";")

# st.write(capacity)
# st.write(ship_input)
# st.write(voyage_input)
# st.write(str(capacity))
# st.write(ports)
# st.write(trips)

if submit_button:
    # Ambil data untuk FW Prediction
    distance_list = get_distances(df_ship_distance, trips)
    freshwater_needs, freshwater_sum = predict_freshwater(distance_list, model_columns, model)
    distances = [int(item[0]) for item in distance_list]

    df_freshwater = pd.DataFrame(
        {
            "Trips": trips,
            "Distances (nm)": distances,
            "Freshwater Needs (L)": freshwater_needs,
        }
    )
    df_sumFreshwater = pd.DataFrame(
        {"Freshwater Needs in Total": freshwater_sum}, index=[0]
    )
    # st.write(distances)
    # st.write(freshwater_needs)
    # st.write(freshwater_sum)

    # Ambil data buat tabel
    cost = [get_list(df_fwcost, item, "LOKASI", "COST")[0] for item in ports]
    # st.write(cost)
    df_FreswaterCost = {
        "Port Location": ports,
        "Harga (Rp)": cost,
    }
    cost_th = [item / 1000 for item in cost]
    best_solution, best_z = pso(cost_th, capacity[0], freshwater_needs)
    # st.write(cost_th)
    # st.write(best_solution)
    # st.write(best_z)

    with st.container():
        # Display rute yang akan dilalui selama satu kali perjalanan
        st.header("Route")
        routes = "#### "
        for port in ports:
            routes += f"**{port.title()}** :arrow_right:"
            # routes += "**" + port.title() + "**" + " :arrow_right: "
        routes += "**" + ports[0].title() + "**"
        st.markdown(routes)

    with st.container():
        st.header("Freshwater Needs")
        st.markdown(f"#### Kapasitas Tangki Freshwater:  _{str(capacity[0])} L_ ")
        st.dataframe(df_freshwater, use_container_width=True, hide_index=True)
        total = pd.DataFrame(df_sumFreshwater, index=[0])
        st.dataframe(total, use_container_width=True, hide_index=True)

    with st.container():
        st.subheader("Lokasi Pembelian Freshwater beserta Harga")
        st.dataframe(df_FreswaterCost, use_container_width=True, hide_index=True)

    with st.container():
        st.subheader("Rekomendasi")
        st.caption(
            "Untuk memperoleh biaya total pembelian Freshwater termurah, dapat diterapkan strategi pembelian berikut"
        )
        s = ""
        for i, x in zip(ports, best_solution):
            if x > 0:
                s += f"- Melakukan pengisian di **:blue[{i.title()}]** sebanyak **:green[{x}] _liter_**\n"
            else:
                s += f"- Tidak perlu melakukan pengisian di **:blue[{i.title()}]**\n"
        st.write(s)
        cost_estimation = locale.currency(best_z, grouping=True)
        total_biaya = (
            f"#### Total biaya yang diperlukan sebesar :red[{cost_estimation}]"
        )
        st.write(total_biaya)

# if submit_button:
#     st.write("You selected: ", ship_input)
#     st.write("Voyage: ", voyage_input)
