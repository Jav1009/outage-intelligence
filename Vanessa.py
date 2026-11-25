"""
Vanessa: data checking and priority. (Akeive as partner)

Columns: report_id, time, latitude, longitude, service_zone,
         description, customers_affected, true_incident_id
After grouping there is also: cluster (-1 = isolated, 0, 1, 2... = possible incident)

Priority rules:
  Critical = fictional hospital in the zone, or 300+ customers
  High     = 100 to 299 customers
  Routine  = under 100 customers
  Order: priority, then more customers, then more reports
"""
import pandas as pd


def load_storm(path):
    """Reads a storm CSV. Returns a table."""
    pass


def check_storm(df):
    """Returns a list of problems ([] if the data is fine)."""
    pass


def build_incident_table(df):
    """One row per possible incident (cluster -1 is not one). Returns a table."""
    pass


def add_priority(incident_table):
    """Adds priority, priority_label and reason, sorted. Returns a table."""
    pass
