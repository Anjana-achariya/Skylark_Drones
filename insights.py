def pipeline_summary(deals_df, sector=None):
    df = deals_df.copy()

    if sector:
        df = df[df["Sector/service"].str.contains(sector, case=False, na=False)]

    open_deals = df[df["Deal Status"] == "Open"]

    total_pipeline = open_deals["Masked Deal value"].sum()

    high_prob = open_deals[
        open_deals["Closure Probability"].str.lower() == "high"
    ]["Masked Deal value"].sum()

    return {
        "total_pipeline": float(total_pipeline),
        "high_probability_pipeline": float(high_prob),
        "deal_count": int(len(open_deals)),
        "sector": sector or "All"
    }


def revenue_summary(work_df):
    total_billed = work_df[
        "Billed Value in Rupees (Incl of GST.) (Masked)"
    ].sum()

    total_collected = work_df[
        "Collected Amount in Rupees (Incl of GST.) (Masked)"
    ].sum()

    receivable = total_billed - total_collected

    return {
        "total_billed": float(total_billed),
        "total_collected": float(total_collected),
        "receivable": float(receivable),
    }