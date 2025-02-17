import pandas as pd

df_ship = pd.read_excel("./data/freshwater_datamaster.xlsx", sheet_name="ship")
df_ship_distance = pd.read_excel(
    "./data/freshwater_datamaster.xlsx", sheet_name="ship_distance"
)
df_asj = pd.read_excel("./data/freshwater_datamaster.xlsx", sheet_name="ASJ")
df_ren = pd.read_excel("./data/freshwater_datamaster.xlsx", sheet_name="REN")
df_aka = pd.read_excel("./data/freshwater_datamaster.xlsx", sheet_name="AKA")
df_fwcost = pd.read_excel("./data/freshwater_datamaster.xlsx", sheet_name="fw_cost")
