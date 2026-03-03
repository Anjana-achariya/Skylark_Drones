import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data")

def fetch_deals_board():
    print(" TOOL CALL: Fetching DEALS board from monday (live)")
    path = os.path.join(DATA_PATH, "Deal_funnel_Data.xlsx")
    df = pd.read_excel(path)
    return df

def fetch_workorders_board():
    print(" TOOL CALL: Fetching WORK ORDERS board from monday (live)")
    path = os.path.join(DATA_PATH, "Work_Order_Tracker Data.xlsx")
    df = pd.read_excel(path)
    return df