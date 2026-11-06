# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json

with open("data.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data["costumes"])
st.subheader(data["chart_title"])
st.dataframe(df)

st.subheader("Cost of Each Costume")

fig, ax = plt.subplots()
ax.bar(df["character"], df["cost"])
ax.set_title("Costume Costs")
ax.set_xlabel("Costume")
ax.set_ylabel("Cost ($)")
ax.tick_params(axis="x", rotation=30)

st.pyplot(fig)

st.subheader("Spending by Store")

if "arrival_filter" not in st.session_state:
    st.session_state["arrival_filter"] = "All"

st.radio(
    "Which costumes do you want to include?",
    ["All", "Arrives before Oct 31", "Arrives after Oct 31"],
    key="arrival_filter",
)

choice = st.session_state["arrival_filter"]

if choice == "Arrives before Oct 31":
    filtered = df[df["arrives_before_oct_31"] == True]
elif choice == "Arrives after Oct 31":
    filtered = df[df["arrives_before_oct_31"] == False]
else:
    filtered = df

store_totals = filtered.groupby("store")["cost"].sum()

fig2, ax2 = plt.subplots()
ax2.pie(store_totals, labels=store_totals.index, autopct="%1.0f%%")
ax2.set_title(f"Spending by Store ({choice})")

st.pyplot(fig2)


# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---
