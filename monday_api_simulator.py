import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch_deals_board():
    print("TOOL CALL: Fetching DEALS board (live)")
    path = os.path.join(BASE_DIR, "data", "deals.xlsx")
    df = pd.read_excel(path)
    return df

def fetch_workorders_board():
    print("TOOL CALL: Fetching WORK ORDERS board (live)")
    path = os.path.join(BASE_DIR, "data", "work_orders.xlsx")
    df = pd.read_excel(path)
    return df
