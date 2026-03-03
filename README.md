## Anjana
## Monday Business Intelligence Agent

This prototype does not use the live monday.com API.

During development, the monday workspace was not accessible, so I built a simulated API layer that behaves like monday.com. The system loads board data live at query time from local Excel files, just like it would fetch from monday boards.

The architecture is designed in a way that real monday.com API calls can be plugged in easily by replacing the data-fetching functions.

All analysis still happens live when a user asks a question.

## Project Overview

Founders often ask questions like:
How is our pipeline looking in the mining sector?
What is our total receivable amount?
Are we closing enough high-probability deals?

Normally, someone has to export data from multiple boards, clean messy values, and manually analyze everything. That takes time.

This project builds an AI Business Intelligence Agent that can answer those questions in a conversational way. It reads data from:
Deals board
Work Orders board

It cleans the data, analyzes it, and gives a simple business explanation.

## What This Agent Does

This system:
Understands business questions written in normal language
Loads board data every time a question is asked
Cleans messy and inconsistent data
Calculates pipeline and revenue insights
Gives short executive-style answers
Shows visible steps of what the agent is doing

## How The System Works

When a user asks a question:
The AI understands what the user is asking (sector, pipeline, revenue, etc.)
It loads Deals and Work Orders data live
It cleans the data (fixes missing values and formats)
It calculates business metrics
It generates a short insight written for a founder
For deployment, everything runs inside a single Streamlit application, but the code is modular and separated into different files.

## Data Cleaning

The data contains inconsistencies on purpose. The agent handles:
Missing values
Text-based probability fields (High, Medium, Low)
Currency fields stored as text
Date formatting issues
Empty or null fields
All cleaning happens every time a question is asked.

## Business Intelligence Features

The agent can analyze:
Pipeline
Total open pipeline value
High-probability deals
Sector-specific pipeline
Revenue
Total billed amount
Total collected amount
Outstanding receivables
Each answer includes:
A key insight
A possible risk
A simple recommendation
