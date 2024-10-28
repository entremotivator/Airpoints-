import streamlit as st
import pandas as pd
from datetime import datetime

# Sample airline rewards data and links
demo_data = {
    "American Airlines": 12000,
    "Delta Airlines": 8500,
    "United Airlines": 6000,
    "Southwest Airlines": 15000,
    "JetBlue": 9500,
    "Alaska Airlines": 5000,
    "Frontier Airlines": 3000,
}

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
user_miles_goals = {airline: 0 for airline in demo_data.keys()}
user_travel_dates = {airline: [] for airline in demo_data.keys()}
user_history = []

# Streamlit UI
st.title("Enhanced Airline Rewards Points & Travel Tracker")

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
st.header("Enter Your Points and Travel Goals:")
for airline in demo_data.keys():
    user_points[airline] = st.number_input(f"{airline} Points:", min_value=0, value=demo_data[airline])
    user_miles_goals[airline] = st.number_input(f"Set Mileage Goal for {airline}:", min_value=0, value=50000)

# Travel dates management
st.header("Manage Your Travel Dates")
st.write("Add your upcoming travel dates for each airline. This helps track how close you are to reaching your mileage goals.")
for airline in demo_data.keys():
    with st.expander(f"{airline} Travel Dates"):
        travel_date = st.date_input(f"Select a travel date for {airline}:", key=f"date_{airline}")
        if st.button(f"Add Date for {airline}", key=f"add_date_{airline}"):
            if travel_date not in user_travel_dates[airline]:
                user_travel_dates[airline].append(travel_date)
                st.success(f"Travel date {travel_date} added for {airline}!")
            else:
                st.warning("This travel date is already added.")

# Save points and calculate mileage goals
if st.button("Save Points & Track Goals"):
    total_points = sum(user_points.values())
    user_history.append(user_points.copy())  # Store the current session's points
    st.success(f"Points saved! Total Points Across All Airlines: {total_points}")

    # Track mileage goals
    st.header("Mileage Goals Status:")
    for airline, points in user_points.items():
        miles_goal = user_miles_goals[airline]
        miles_remaining = miles_goal - points
        st.write(f"{airline} - Current Points: {points} / Goal: {miles_goal} - Miles Remaining: {max(0, miles_remaining)}")

# Display the points entered for each airline with links
st.header("Your Points Summary with Links")
points_df = pd.DataFrame(list(user_points.items()), columns=["Airline", "Points"])
for airline, points in user_points.items():
    st.markdown(f"{airline}: {points} points - [Learn More]({airline_links[airline]})")

# Display travel dates per airline
st.header("Your Travel Dates Summary")
for airline, dates in user_travel_dates.items():
    st.write(f"**{airline}**:")
    if dates:
        for date in dates:
            st.write(f"- {date.strftime('%Y-%m-%d')}")
    else:
        st.write("No travel dates added.")

# Detailed rewards information with links
st.sidebar.header("Rewards Information")
st.sidebar.write("Click the links to explore each airline's program details:")
for airline, link in airline_links.items():
    st.sidebar.markdown(f"**[{airline}]({link})**: Visit the rewards program page for more details.")

# Points history tracking
st.header("Points & Travel History")
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
2. Enter your points and mileage goals for each airline.
3. Add upcoming travel dates to stay on top of your rewards and goals.
4. Click 'Save Points & Track Goals' to log your current points and check progress.
5. Review your points summary, mileage goals, travel dates, and history.
6. Click on 'Learn More' to visit each airline's rewards program page for more information.
""")
