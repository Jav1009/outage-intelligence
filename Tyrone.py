"""
Tyrone: the app.
Calls your teammates' functions and shows what they return.

Pages: Map and incidents | Priority list | Accuracy check
Banner on every page: Research Prototype: Simulated Utility Data

Functions coming from teammates:
  Vanessa:  load_storm, check_storm, build_incident_table, add_priority
  Javaughn: cluster_reports, baseline_by_zone, score_grouping, make_map
"""
import streamlit as st

st.set_page_config(page_title="Outage Intelligence", layout="wide")
st.title("Outage Intelligence")

page = st.sidebar.radio("Page", ["Map and incidents", "Priority list", "Accuracy check"])

if page == "Map and incidents":
    pass
elif page == "Priority list":
    pass
else:
    pass
