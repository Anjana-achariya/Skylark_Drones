import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Monday BI Agent", layout="wide")

st.title(" Monday.com Business Intelligence Agent")
st.caption("Founder-level insights across Deals & Work Orders")

query = st.chat_input("Ask a business question...")

if query:
    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing live business data..."):

            st.markdown("###  Agent Actions")
            st.write("→ Understanding query")
            st.write("→ Calling monday DEALS board API (live)")
            st.write("→ Calling monday WORK ORDERS board API (live)")
            st.write("→ Cleaning messy business data")
            st.write("→ Generating founder insights")

            answer = run_agent(query)

            st.markdown("###  Business Insight")
            st.write(answer)