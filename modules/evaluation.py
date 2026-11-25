def cluster_accuracy(df, pred_col="predicted_incident", true_col="true_incident"):
    """Share of reports placed in the right incident (0 = isolated).

    Each predicted group is matched to the real incident most of its reports
    belong to; a report is correct if it belongs to that incident.
    """
    correct = 0
    for pred_id, group in df.groupby(pred_col):
        if pred_id == 0:
            correct += (group[true_col] == 0).sum()
        else:
            majority = group[true_col].mode().iloc[0]
            correct += (group[true_col] == majority).sum()
    return correct / len(df)


def incidents_found(df, pred_col="predicted_incident"):
    """How many possible incidents were found (not counting isolated reports)."""
    return df.loc[df[pred_col] != 0, pred_col].nunique()