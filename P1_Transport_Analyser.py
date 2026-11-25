import streamlit as st
import pandas as pd

# st.set_page_config is used to configure the overall browser window or tab for the application
st.set_page_config(page_title="Commute Delay Analyzer", page_icon="🚆", layout="centered")
st.title("🚆 UK Commute Delay Analyzer")
# st.caption is used as a little message displayed under the titel 
st.caption("Find out which Train, Bus or Taxi routes waste the most time of your week. ")

data = {
    #the * 5 at the end of the route list? That's a clever Python shortcut. 
    # Instead of typing out all 30 routes manually, it takes those 6 train times and repeats them 5 times (once for each weekday: Mon, Tue, Wed, Thu, Fri). 
    # That gives us 30 total rows of data.
    "Route": ["07:45 Express", "08:15 Local", "08:45 Express", "17:15 Peak", "17:45 Peak", "18:30 Off-Peak"] * 5,
   # The Day list: This lists out the days of the week matching up with our 30 rows (6 train times $\times$ 5 days = 30 items).
    "Day": ["Mon", "Mon", "Mon", "Mon", "Mon", "Mon",
            "Tue", "Tue", "Tue", "Tue", "Tue", "Tue",
            "Wed", "Wed", "Wed", "Wed", "Wed", "Wed",
            "Thu", "Thu", "Thu", "Thu", "Thu", "Thu",
            "Fri", "Fri", "Fri", "Fri", "Fri", "Fri"],
#The Delay_Mins list: These are the numbers representing how many minutes late each specific train was on that day. 
# For example, on Monday, the 17:15 Peak train was delayed by 22 minutes.
    "Delay_Mins": [4, 14, 9, 22, 18, 3,
                   2, 11, 6, 19, 15, 2,
                   5, 16, 12, 25, 21, 4,
                   3, 12, 8, 28, 17, 5,
                   6, 19, 14, 31, 24, 7]
}

df = pd.DataFrame(data)
# Take that raw dictionary of lists and organize it into a proper table (df)
#  with rows and columns so we can filter it, calculate averages, and draw charts

avg_delay = round(df["Delay_Mins"].mean(), 1)
worst_route = df.groupby("Route")["Delay_Mins"].mean().idxmax()
yearly_hours_lost = round((avg_delay * 2 * 5 * 40) / 60, 1)
col1, col2, col3 = st.columns(3)
col1.metric("Avg Delay", f"{avg_delay} mins")
col2.metric("Worst Service", worst_route)
col3.metric("Hours Lost / Year", f"{yearly_hours_lost} hrs")

st.divider()

# 5. Let the user filter data interactively
selected_day = st.selectbox("Filter by Day of the Week:", ["All Days"] + list(df["Day"].unique()))
filtered_df = df if selected_day == "All Days" else df[df["Day"] == selected_day]

# 6. Draw the bar chart of average delays by route
st.subheader("Average Delay by Service (Minutes)")
route_summary = filtered_df.groupby("Route")["Delay_Mins"].mean().sort_values(ascending=False)
st.bar_chart(route_summary)

# 7. Add a dynamic warning/verdict box based on the data
worst_filtered_route = route_summary.idxmax()
worst_filtered_delay = round(route_summary.max(), 1)
st.warning(f"⚠️ **Verdict:** Avoid the **{worst_filtered_route}**—it averages **{worst_filtered_delay} mins** late during your selection.")