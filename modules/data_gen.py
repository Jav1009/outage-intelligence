import numpy as np
import pandas as pd
from config import ZONES, DESCRIPTIONS, SEED


def generate_reports(n_incidents=6, n_noise=10, seed=SEED):
    """Make fictional outage reports.

    true_incident = 1, 2, 3... for reports from one real incident,
    0 for isolated one-off reports (the 'answer key').
    """
    rng = np.random.default_rng(seed)
    zone_names = list(ZONES)
    start = pd.Timestamp("2026-11-20 18:00")
    rows = []

    # Reports that belong to a real incident: tightly bunched around a centre
    for inc in range(1, n_incidents + 1):
        zone = str(rng.choice(zone_names))
        centre_lat = ZONES[zone]["lat"] + rng.normal(0, 0.01)
        centre_lon = ZONES[zone]["lon"] + rng.normal(0, 0.01)
        incident_start = start + pd.Timedelta(minutes=int(rng.integers(0, 180)))
        for _ in range(int(rng.integers(5, 12))):
            rows.append({
                "time": incident_start + pd.Timedelta(minutes=int(rng.integers(0, 25))),
                "lat": centre_lat + rng.normal(0, 0.003),   # ~300 m spread
                "lon": centre_lon + rng.normal(0, 0.003),
                "zone": zone,
                "description": str(rng.choice(DESCRIPTIONS)),
                "customers_affected": int(rng.integers(1, 40)),
                "true_incident": inc,
            })

    # Isolated reports: scattered anywhere in a zone
    for _ in range(n_noise):
        zone = str(rng.choice(zone_names))
        rows.append({
            "time": start + pd.Timedelta(minutes=int(rng.integers(0, 240))),
            "lat": ZONES[zone]["lat"] + rng.normal(0, 0.03),
            "lon": ZONES[zone]["lon"] + rng.normal(0, 0.03),
            "zone": zone,
            "description": str(rng.choice(DESCRIPTIONS)),
            "customers_affected": int(rng.integers(1, 5)),
            "true_incident": 0,
        })

    return pd.DataFrame(rows).sort_values("time").reset_index(drop=True)