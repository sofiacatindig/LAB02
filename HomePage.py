# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Spooky Season Dashboard🎃")

# INTRODUCTORY TEXT
st.write("""
Explore spooky data collected from the Jackets :)
Find out where touse is on Halloween and what spooks Tech students the most!
You can also visualize the survey responses through interactive charts on 'Visuals.'
(Navigate between the pages using the sidebar)

### How to use this app:
- **Survey Page**: Go here to input new data into our CSV file.
- **Visuals Page**: Go here to see the data visualized in different graphs.

This project is part of CS 1301's Lab 2.
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
# st.image("images/welcome_image.png")
