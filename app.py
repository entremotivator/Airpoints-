import streamlit as st
import pandas as pd

# Sample airline rewards data
demo_data = {
    "American Airlines": 12000,
    "Delta Airlines": 8500,
    "United Airlines": 6000,
    "Southwest Airlines": 15000,
    "JetBlue": 9500,
    "Alaska Airlines": 5000,
    "Frontier Airlines": 3000,
}

# Airline rewards links
airline_links = {
    "American Airlines": "https://www.aa.com/en-us/aadvantage-program",
    "Delta Airlines": "https://www.delta.com/us/en/skymiles-program/skymiles-program",
    "United Airlines": "https://www.united.com/ual/en/us/fly/mileageplus.html",
    "Southwest Airlines": "https://www.southwest.com/rapidrewards/",
    "JetBlue": "https://www.jetblue.com/trueblue",
    "Alaska Airlines": "https://www.alaskaair.com/mileage-plan/",
    "Frontier Airlines": "https://www.flyfrontier.com/frontier-miles/",
}

# Initialize user data
user_points = {airline: 0 for airline in demo_data.keys()}
user_history = []

# Streamlit UI
st.title("Airline Rewards Points Tracker")

# User registration
st.sidebar.header("User Registration")
username = st.sidebar.text_input("Enter your username", "")
if st.sidebar.button("Register"):
    if username:
        st.success(f"Registration successful for {username}!")
        st.session_state['username'] = username  # Store user info in session state
    else:
        st.error("Please enter a username to register.")

# Input fields for points
st.header("Enter Your Points:")
for airline in demo_data.keys():
    user_points[airline] = st.number_input(f"{airline} Points:", min_value=0, value=demo_data[airline])

# Button to save points
if st.button("Save Points"):
    total_points = sum(user_points.values())
    user_history.append(user_points.copy())  # Store the current session's points
    st.success(f"Points saved! Total Points Across All Airlines: {total_points}")

# Display the points entered for each airline with links
st.header("Your Points Summary:")
points_df = pd.DataFrame(list(user_points.items()), columns=["Airline", "Points"])
for airline, points in user_points.items():
    st.markdown(f"{airline}: {points} points - [Learn More]({airline_links[airline]})")

# Detailed rewards information with links
st.sidebar.header("Rewards Information")
st.sidebar.write("""
Each airline has a unique rewards system. Click the links to explore more about each program:
""")
for airline, link in airline_links.items():
    st.sidebar.markdown(f"**[{airline}]({link})**: Visit the rewards program page for details.")

# Points history tracking
st.header("Points History")
if user_history:
    history_df = pd.DataFrame(user_history)
    history_df.index += 1  # Start index from 1 for display purposes
    st.write(history_df)
else:
    st.write("No points history found for this session.")

# Explanation of the app
st.sidebar.header("How to Use This App")
st.sidebar.write("""
1. Register with a username to start tracking your airline rewards.
2. Enter your points for each airline you are a member of.
3. Click 'Save Points' to save your current points.
4. Review your points summary and history in the respective sections.
5. Refer to the rewards information for details on each airline's program.
6. Click on the 'Learn More' links to go directly to the rewards page for more information.
""")
