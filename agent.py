import os
import json
from groq import Groq
from dotenv import load_dotenv

from monday_api_simulator import fetch_deals_board, fetch_workorders_board
from data_cleaning import clean_deals_data, clean_workorders_data
from insights import pipeline_summary, revenue_summary

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content


def understand_query(user_query):
    prompt = f"""
You are a business analyst AI.

Extract from this query:
1. sector (if mentioned)
2. ask about pipeline OR revenue OR both
3. timeframe if mentioned

Return JSON only.

Query: {user_query}
"""

    res = ask_llm(prompt)

    try:
        data = json.loads(res)
    except:
        data = {"sector": None, "type": "pipeline"}

    return data


def run_agent(user_query):
    print("\n AGENT STARTED")
    print("User:", user_query)

    print(" Understanding query...")
    intent = understand_query(user_query)

    sector = intent.get("sector")
    qtype = intent.get("type", "pipeline")

    print(" Calling monday DEALS board API...")
    deals_df = fetch_deals_board()

    print(" Calling monday WORK ORDERS board API...")
    work_df = fetch_workorders_board()

 
    deals_df = clean_deals_data(deals_df)
    work_df = clean_workorders_data(work_df)

    insights_data = {}

    if qtype == "pipeline":
        insights_data = pipeline_summary(deals_df, sector)

    elif qtype == "revenue":
        insights_data = revenue_summary(work_df)

    else:
        insights_data["pipeline"] = pipeline_summary(deals_df, sector)
        insights_data["revenue"] = revenue_summary(work_df)

    print(" Generating founder insights...")

    final_prompt = f"""
You are a sharp startup COO giving insights to founder.

Data:
{json.dumps(insights_data, indent=2)}

Explain:
- key insight
- risk
- recommendation
- keep it short
"""

    answer = ask_llm(final_prompt)

    return answer