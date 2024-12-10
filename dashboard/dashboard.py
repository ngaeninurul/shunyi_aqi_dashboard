import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style="dark")

# load dataset
data_path = "data/PRSA_Data_Shunyi_20130301-20170228.csv"
df = pd.read_csv(data_path)

# data preprocessing
df['Date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
df.sort_values("Date", inplace=True)

# sidebar
with st.sidebar:
    st.markdown(
    """
    <h1 style="text-align: center;">DASHBOARD</h1>
    """,
    unsafe_allow_html=True
    )
    st.image("logo.png")
    
    st.markdown("<br>", unsafe_allow_html=True)
        
    # date filter
    min_date, max_date = df["Date"].min(), df["Date"].max()
    start_date, end_date = st.date_input(
        "Select Date Range",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date,
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    # AQI filter
    aqi_min, aqi_max = df["PM2.5"].min(), df["PM2.5"].max()
    aqi_range = st.slider(
        "Select AQI Range", 
        min_value=int(aqi_min), 
        max_value=int(aqi_max), 
        value=(int(aqi_min), int(aqi_max))
    )

# filter dataset
filtered_df = df[
    (df["Date"] >= pd.Timestamp(start_date)) &
    (df["Date"] <= pd.Timestamp(end_date)) &
    (df["PM2.5"].between(aqi_range[0], aqi_range[1]))
]

# layout
st.title("SHUNYI AIR QUALITY INDEX (AQI)")
st.subheader("Overview of Air Quality Index in Shunyi through 2013-2017")
st.markdown("<br>", unsafe_allow_html=True)

# key metric display
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Average AQI", value=round(filtered_df["PM2.5"].mean(), 2))
with col2:
    st.metric("Max AQI", value=int(filtered_df["PM2.5"].max()))
with col3:
    st.metric("Min AQI", value=int(filtered_df["PM2.5"].min()))
    
st.markdown("<br>", unsafe_allow_html=True)
    
# line chart: AQI over time
st.subheader("AQI Trends Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=filtered_df, x="Date", y="PM2.5", ax=ax, color="blue")
ax.set_title("AQI Trends", fontsize=16)
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("AQI", fontsize=12)
st.pyplot(fig)

st.markdown("<br>", unsafe_allow_html=True)

# annual AQI trend
st.subheader("Annual AQI Trend")
filtered_df['Year'] = filtered_df['Date'].dt.year
annual_avg_aqi = filtered_df.groupby('Year')['PM2.5'].mean()
annual_avg_aqi_df = annual_avg_aqi.reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=annual_avg_aqi_df, x='Year', y='PM2.5', color="blue")
ax.set_title("Average AQI per Year", fontsize=16)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Average AQI", fontsize=12)
st.pyplot(fig)

st.markdown("<br>", unsafe_allow_html=True)

# monthly AQI trend
st.subheader("Monthly AQI Trend")
filtered_df['Month'] = filtered_df['Date'].dt.month
monthly_avg_aqi = filtered_df.groupby(['Year', 'Month'])['PM2.5'].mean().unstack()
monthly_avg_aqi_df = monthly_avg_aqi.reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
monthly_avg_aqi_df.set_index('Year').T.plot(ax=ax, cmap='Blues', marker='o')
ax.set_title("Average AQI by Month (Grouped by Year)", fontsize=16)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Average AQI", fontsize=12)
plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig)

st.markdown("<br>", unsafe_allow_html=True)

# seasonal trends
st.subheader("Seasonal AQI Patterns")
filtered_df["Month"] = filtered_df["Date"].dt.month
monthly_avg_aqi = filtered_df.groupby("Month")["PM2.5"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=monthly_avg_aqi.index, y=monthly_avg_aqi.values, palette="Blues", ax=ax)
ax.set_title("Average AQI by Month", fontsize=16)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Average AQI", fontsize=12)
st.pyplot(fig)

st.markdown("<br>", unsafe_allow_html=True)

# bar chart: AQI category distribution
bins = [0, 50, 100, 150, 200, 300, 500]
labels = ['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous']
filtered_df['aqi_category'] = pd.cut(filtered_df['PM2.5'], bins=bins, labels=labels, right=True)
st.subheader("AQI Category Distribution")
aqi_categories = filtered_df["aqi_category"].value_counts()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=aqi_categories.index, y=aqi_categories.values, palette="coolwarm", ax=ax)
ax.set_title("Frequency of AQI Categories", fontsize=16)
ax.set_ylabel("Count", fontsize=12)
ax.set_xlabel("Category", fontsize=12)
plt.xticks(rotation=45, ha='right')  # Memiringkan label sebesar 45 derajat dan mengatur posisi horizontalnya ke kanan
st.pyplot(fig)

# footer
st.markdown(
    """
    <style>
        /* Footer Style */
        .footer {
            position: relative;
            bottom: -130px;
            left: 50%;
            transform: translateX(-50%);
            padding: 10px;
            text-align: center;
            font-size: 14px;
            color: #fff7;
            width: auto;
            z-index: 1000;
        }
    </style>
    <div class="footer">
        SHUNYI AQI &copy; 2013-2017
    </div>
    """,
    unsafe_allow_html=True
)
