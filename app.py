import streamlit as st
import plotly.express as px

from modules.data_gen import generate_reports
from modules.clustering import cluster_reports, baseline_by_zone
from modules.evaluation import cluster_accuracy, incidents_found

st.set_page_config(page_title="Outage Intelligence", layout="wide")
st.title("⚡ Outage Intelligence")
st.warning("Research Prototype: Simulated Utility Data. Zones and reports are fictional.")

# ---- Sidebar controls ----
st.sidebar.header("Simulation")
n_incidents = st.sidebar.slider("Number of real incidents", 1, 10, 6)
n_noise = st.sidebar.slider("Isolated one-off reports", 0, 30, 10)
seed = st.sidebar.number_input("Random seed", value=42, step=1)

st.sidebar.header("DBSCAN settings")
eps_km = st.sidebar.slider("Max distance between reports (km)", 0.1, 3.0, 0.5, 0.1)
min_samples = st.sidebar.slider("Min reports to form an incident", 2, 10, 3)

# ---- Data + AI ----
df = generate_reports(n_incidents, n_noise, int(seed))
df = cluster_reports(df, eps_km, min_samples)
base = baseline_by_zone(df)

# ---- Headline numbers ----
ai_acc = cluster_accuracy(df)
base_acc = cluster_accuracy(base)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Reports", len(df))
c2.metric("Possible incidents found", incidents_found(df), f"real: {n_incidents}", delta_color="off")
c3.metric("DBSCAN placed correctly", f"{ai_acc:.0%}")
c4.metric("Baseline (by zone)", f"{base_acc:.0%}")


def make_map(data, column, title):
    plot_df = data.copy()
    plot_df[column] = plot_df[column].astype(str)
    fig = px.scatter_map(
        plot_df, lat="lat", lon="lon", color=column,
        hover_data=["time", "zone", "description", "customers_affected"],
        zoom=10, height=520, map_style="open-street-map", title=title,
    )
    st.plotly_chart(fig, width="stretch")


tab_ai, tab_truth = st.tabs(["AI grouping (DBSCAN)", "Ground truth (answer key)"])
with tab_ai:
    make_map(df, "predicted_incident", "Possible incidents (0 = isolated report)")
with tab_truth:
    make_map(df, "true_incident", "Real simulated incidents (0 = isolated report)")

# ---- Incident summary ----
st.subheader("Possible incidents")
incidents = (
    df[df["predicted_incident"] != 0]
    .groupby("predicted_incident")
    .agg(
        reports=("lat", "size"),
        customers_affected=("customers_affected", "sum"),
        zones=("zone", lambda s: ", ".join(sorted(set(s)))),
        first_report=("time", "min"),
    )
    .reset_index()
    .rename(columns={"predicted_incident": "incident"})
)
st.dataframe(incidents, width="stretch", hide_index=True)

with st.expander("All reports"):
    st.dataframe(df, width="stretch")