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

survey = pd.read_csv("data.csv")
survey.columns = survey.columns.str.strip()

st.subheader("What People Find Scariest")

count = survey["Fear"].value_counts()

fig3, ax3 = plt.subplots()
ax3.bar(count.index, count.values)
ax3.set_title("Scariest Things on Campus")
ax3.set_xlabel("Fear")
ax3.set_ylabel("Number of votes")
ax3.tick_params(axis="x", rotation=30)

st.pyplot(fig3)

st.subheader("Where People Spend Halloween")

if "filter" not in st.session_state:
    st.session_state["filter"] = "All"

st.selectbox(
    "Show people most scared of:",
    ["All", "Freshman 15", "CS 1301 exams", "Course registration", "Communal bathrooms", "8 AMs"],
    key="filter",
)

selected = st.session_state["filter"]

if selected == "All":
    filteredSurvey = survey
else:
    filteredSurvey = survey[survey["Fear"] == selected]

booCounts = filteredSurvey["Touse"].value_counts()

if len(booCounts) == 0:
    st.write("No one has picked that yet.")
else:
    fig4, ax4 = plt.subplots()
    ax4.pie(booCounts, labels=booCounts.index, autopct="%1.0f%%")
    ax4.set_title(f"Where People Spend Halloween ({selected})")
    st.pyplot(fig4)

    meanVotes = float(round(booCounts.mean(), 2))
    medianVotes = float(booCounts.median())

    if "oldMean" not in st.session_state:
        st.session_state["oldMean"] = meanVotes
        st.session_state["oldMedian"] = medianVotes

    meanChange = round(meanVotes - st.session_state["oldMean"], 2)
    medianChange = medianVotes - st.session_state["oldMedian"]

    col1, col2 = st.columns(2)
    col1.metric("Mean votes per spot", meanVotes, meanChange)
    col2.metric("Median votes per spot", medianVotes, medianChange)

    st.session_state["oldMean"] = meanVotes
    st.session_state["oldMedian"] = medianVotes
