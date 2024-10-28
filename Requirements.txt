import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Display the points entered for each airline
st.header("Your Points Summary:")
points_df = pd.DataFrame(list(user_points.items()), columns=["Airline", "Points"])
for airline, points in user_points.items():
    st.write(f"{airline}: {points} points")

# Data visualization
st.header("Points Comparison")
fig, ax = plt.subplots()
ax.bar(points_df["Airline"], points_df["Points"], color='skyblue')
ax.set_xlabel("Airlines")
ax.set_ylabel("Points")
ax.set_title("Points Comparison Across Airlines")
plt.xticks(rotation=45)
st.pyplot(fig)

# Detailed rewards information
st.sidebar.header("Rewards Information")
st.sidebar.write("""
    Each airline has a unique rewards system. Here's a quick summary:
    - **American Airlines**: AAdvantage program, points for flights, upgrades.
    - **Delta Airlines**: SkyMiles program, flexible award tickets.
    - **United Airlines**: MileagePlus, points for flights and shopping.
    - **Southwest Airlines**: Rapid Rewards, points for flights and more.
    - **JetBlue**: TrueBlue, points for flights and vacation packages.
    - **Alaska Airlines**: Mileage Plan, points for flights and partners.
    - **Frontier Airlines**: Frontier Miles, points for flights and purchases.
""")

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
""")
