import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from modules.data_gen import generate_reports
from modules.clustering import cluster_reports, baseline_by_zone
from modules.evaluation import cluster_accuracy, incidents_found


def test_dbscan_beats_baseline():
    df = generate_reports(6, 10, 42)
    ai = cluster_reports(df, eps_km=0.5, min_samples=3)
    base = baseline_by_zone(df)
    ai_acc, base_acc = cluster_accuracy(ai), cluster_accuracy(base)
    print(f"DBSCAN {ai_acc:.0%} | baseline {base_acc:.0%} | found {incidents_found(ai)} of 6")
    assert ai_acc > base_acc
    assert ai_acc >= 0.80


if __name__ == "__main__":
    test_dbscan_beats_baseline()
    print("All tests passed")