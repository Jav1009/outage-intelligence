import streamlit as st
import plotly.express as px
from modules.data_gen import generate_reports

st.set_page_config(page_title="Outage Intelligence", layout="wide")
st.title("⚡ Outage Intelligence")
st.warning("Research Prototype: Simulated Utility Data. Zones and reports are fictional.")

# Sidebar controls
st.sidebar.header("Simulation settings")
n_incidents = st.sidebar.slider("Number of real incidents", 1, 10, 6)
n_noise = st.sidebar.slider("Isolated one-off reports", 0, 30, 10)
seed = st.sidebar.number_input("Random seed", value=42, step=1)

df = generate_reports(n_incidents, n_noise, int(seed))

# Summary numbers
c1, c2, c3 = st.columns(3)
c1.metric("Total reports", len(df))
c2.metric("Customers affected", int(df["customers_affected"].sum()))
c3.metric("Zones with reports", df["zone"].nunique())

# Map: colour = which incident the report really belongs to (0 = isolated)
df["true_incident"] = df["true_incident"].astype(str)
fig = px.scatter_map(
    df, lat="lat", lon="lon", color="true_incident",
    hover_data=["time", "zone", "description", "customers_affected"],
    zoom=10, height=550, map_style="open-street-map",
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Report table")
st.dataframe(df, use_container_width=True)