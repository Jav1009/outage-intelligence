"""
Dwayne: the data maker.
Make two or more fake storms (incident spreads) and save them as CSV files.

Columns: report_id, time, latitude, longitude, service_zone,
         description, customers_affected, true_incident_id
true_incident_id: 0 = isolated report, 1, 2, 3... = incident number
"""
import numpy as np
import pandas as pd


def make_incident_reports(incident_id, zone_name, centre_lat, centre_lon,
                          start_time, n_reports, spread_km, rng):
    """One incident's reports. Returns a table."""
    pass


def make_isolated_reports(n_reports, rng):
    """One-off reports that belong to no incident. Returns a table."""
    pass


def make_storm(seed):
    """A whole storm, 50 to 100 rows. Returns a table."""
    pass


def save_storm(df, path):
    """Writes the table to a CSV file."""
    pass
