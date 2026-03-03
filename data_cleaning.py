import pandas as pd

def clean_deals_data(df):
    print(" Cleaning deals data...")

    df.columns = df.columns.str.strip()

    if "Masked Deal value" in df.columns:
        df["Masked Deal value"] = pd.to_numeric(
            df["Masked Deal value"], errors="coerce"
        ).fillna(0)

    if "Tentative Close Date" in df.columns:
        df["Tentative Close Date"] = pd.to_datetime(
            df["Tentative Close Date"], errors="coerce"
        )

    df["Closure Probability"] = df.get("Closure Probability", "").fillna("Unknown")

    return df


def clean_workorders_data(df):
    print(" Cleaning work orders data...")

    df.columns = df.columns.str.strip()

    money_cols = [col for col in df.columns if "Amount" in col or "Billed" in col]

    for col in money_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    return df