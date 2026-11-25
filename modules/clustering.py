import numpy as np
from sklearn.cluster import DBSCAN

EARTH_RADIUS_KM = 6371.0


def cluster_reports(df, eps_km=0.5, min_samples=3):
    """Group nearby reports into possible incidents with DBSCAN.

    predicted_incident: 1, 2, 3... = possible incident, 0 = isolated report.
    """
    coords = np.radians(df[["lat", "lon"]].to_numpy())  # haversine needs radians
    model = DBSCAN(
        eps=eps_km / EARTH_RADIUS_KM,  # km -> radians
        min_samples=min_samples,
        metric="haversine",
        algorithm="ball_tree",
    )
    labels = model.fit_predict(coords)  # DBSCAN: -1 = noise, clusters start at 0
    out = df.copy()
    out["predicted_incident"] = labels + 1  # shift so 0 = isolated, 1+ = incident
    return out


def baseline_by_zone(df):
    """No-AI baseline: every report in the same zone = one 'incident'."""
    out = df.copy()
    codes = {z: i + 1 for i, z in enumerate(sorted(df["zone"].unique()))}
    out["predicted_incident"] = out["zone"].map(codes)
    return out