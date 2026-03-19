import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sqlite3

# Page configuration
st.set_page_config(
    page_title="Namma Yatri Analytics Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Load data function with caching
@st.cache_data
def load_data():
    conn = sqlite3.connect('namma_yatri.db')
    rides = pd.read_sql_query("SELECT * FROM rides", conn)
    drivers = pd.read_sql_query("SELECT * FROM drivers", conn)
    conn.close()
    
    rides['request_time'] = pd.to_datetime(rides['request_time'])
    rides['date'] = rides['request_time'].dt.date
    rides['hour'] = rides['request_time'].dt.hour
    rides['day_name'] = rides['request_time'].dt.day_name()
    
    return rides, drivers

# Load data
rides, drivers = load_data()

# Sidebar filters
st.sidebar.title("🎛️ Filters")
st.sidebar.markdown("---")

# Date range filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(rides['date'].min(), rides['date'].max()),
    min_value=rides['date'].min(),
    max_value=rides['date'].max()
)

# Location filter
locations = ['All'] + sorted(rides['pickup_location'].unique().tolist())
selected_location = st.sidebar.selectbox("Select Location", locations)

# Ride status filter
status_options = st.sidebar.multiselect(
    "Ride Status",
    options=rides['ride_status'].unique().tolist(),
    default=rides['ride_status'].unique().tolist()
)

# Apply filters
filtered_rides = rides[
    (rides['date'] >= date_range[0]) & 
    (rides['date'] <= date_range[1]) &
    (rides['ride_status'].isin(status_options))
]

if selected_location != 'All':
    filtered_rides = filtered_rides[filtered_rides['pickup_location'] == selected_location]

completed_rides = filtered_rides[filtered_rides['ride_status'] == 'completed']

# Header
st.title("🚗 Namma Yatri Analytics Dashboard")
st.markdown("### Operational Excellence Through Data-Driven Insights")
st.markdown("---")

# Key Metrics Row
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    total_rides = len(filtered_rides)
    st.metric("Total Rides", f"{total_rides:,}", delta=None)

with col2:
    completed = len(completed_rides)
    completion_rate = (completed / total_rides * 100) if total_rides > 0 else 0
    st.metric("Completed Rides", f"{completed:,}", f"{completion_rate:.1f}%")

with col3:
    cancellation_rate = ((total_rides - completed) / total_rides * 100) if total_rides > 0 else 0
    st.metric("Cancellation Rate", f"{cancellation_rate:.1f}%", 
              delta=f"-{cancellation_rate:.1f}%" if cancellation_rate > 20 else None,
              delta_color="inverse")

with col4:
    total_revenue = completed_rides['final_fare'].sum()
    st.metric("Total Revenue", f"₹{total_revenue:,.0f}")

with col5:
    avg_fare = completed_rides['final_fare'].mean() if len(completed_rides) > 0 else 0
    st.metric("Avg Fare", f"₹{avg_fare:.2f}")

st.markdown("---")

# Two column layout
col_left, col_right = st.columns([1, 1])

with col_left:
    # Hourly demand pattern
    st.subheader("📊 Hourly Demand Pattern")
    hourly_data = filtered_rides.groupby(['hour', 'ride_status']).size().reset_index(name='count')
    
    fig_hourly = px.bar(
        hourly_data,
        x='hour',
        y='count',
        color='ride_status',
        title='Ride Distribution by Hour',
        labels={'hour': 'Hour of Day', 'count': 'Number of Rides'},
        color_discrete_map={
            'completed': '#2ecc71',
            'cancelled_by_driver': '#e74c3c',
            'cancelled_by_rider': '#f39c12'
        }
    )
    fig_hourly.update_layout(height=350)
    st.plotly_chart(fig_hourly, use_container_width=True)

with col_right:
    # Revenue trend
    st.subheader("💰 Daily Revenue Trend")
    daily_revenue = completed_rides.groupby('date')['final_fare'].sum().reset_index()
    
    fig_revenue = go.Figure()
    fig_revenue.add_trace(go.Scatter(
        x=daily_revenue['date'],
        y=daily_revenue['final_fare'],
        mode='lines+markers',
        fill='tozeroy',
        line=dict(color='#27ae60', width=2),
        marker=dict(size=6)
    ))
    fig_revenue.update_layout(
        title='Revenue Over Time',
        xaxis_title='Date',
        yaxis_title='Revenue (₹)',
        height=350
    )
    st.plotly_chart(fig_revenue, use_container_width=True)

# Second row - Location analysis
col_left2, col_right2 = st.columns([1, 1])

with col_left2:
    st.subheader("📍 Top Pickup Locations")
    top_pickups = filtered_rides['pickup_location'].value_counts().head(10).reset_index()
    top_pickups.columns = ['location', 'count']
    
    fig_pickup = px.bar(
        top_pickups,
        x='count',
        y='location',
        orientation='h',
        title='Most Demanded Locations',
        color='count',
        color_continuous_scale='Blues'
    )
    fig_pickup.update_layout(height=400)
    st.plotly_chart(fig_pickup, use_container_width=True)

with col_right2:
    st.subheader("🎯 Cancellation Analysis")
    
    # Cancellation by location
    cancel_data = filtered_rides[filtered_rides['ride_status'] != 'completed']
    cancel_by_loc = cancel_data['pickup_location'].value_counts().head(10).reset_index()
    cancel_by_loc.columns = ['location', 'cancellations']
    
    fig_cancel = px.bar(
        cancel_by_loc,
        x='cancellations',
        y='location',
        orientation='h',
        title='Top Locations with Cancellations',
        color='cancellations',
        color_continuous_scale='Reds'
    )
    fig_cancel.update_layout(height=400)
    st.plotly_chart(fig_cancel, use_container_width=True)

# Third row - Driver analytics
st.markdown("---")
st.subheader("👨‍✈️ Driver Performance Analytics")

col_d1, col_d2, col_d3 = st.columns([1, 1, 1])

with col_d1:
    # Driver earnings distribution
    driver_earnings = completed_rides.groupby('driver_id')['final_fare'].sum()
    
    fig_earnings = go.Figure()
    fig_earnings.add_trace(go.Histogram(
        x=driver_earnings.values,
        nbinsx=30,
        marker_color='#9b59b6',
        opacity=0.7
    ))
    fig_earnings.add_vline(
        x=driver_earnings.mean(),
        line_dash="dash",
        line_color="red",
        annotation_text=f"Mean: ₹{driver_earnings.mean():.0f}"
    )
    fig_earnings.update_layout(
        title='Driver Earnings Distribution',
        xaxis_title='Total Earnings (₹)',
        yaxis_title='Number of Drivers',
        height=350
    )
    st.plotly_chart(fig_earnings, use_container_width=True)

with col_d2:
    # Driver ratings
    driver_ratings = completed_rides['driver_rating'].dropna()
    
    fig_rating = go.Figure()
    fig_rating.add_trace(go.Histogram(
        x=driver_ratings,
        nbinsx=20,
        marker_color='#f39c12',
        opacity=0.7
    ))
    fig_rating.update_layout(
        title='Driver Rating Distribution',
        xaxis_title='Rating',
        yaxis_title='Frequency',
        height=350
    )
    st.plotly_chart(fig_rating, use_container_width=True)

with col_d3:
    # Top drivers
    top_drivers = completed_rides.groupby('driver_id').agg({
        'final_fare': 'sum',
        'ride_id': 'count',
        'driver_rating': 'mean'
    }).round(2).nlargest(10, 'final_fare').reset_index()
    top_drivers.columns = ['Driver ID', 'Earnings', 'Trips', 'Avg Rating']
    
    st.markdown("**🏆 Top 10 Drivers**")
    st.dataframe(
        top_drivers.style.format({
            'Earnings': '₹{:.2f}',
            'Trips': '{:.0f}',
            'Avg Rating': '{:.2f}⭐'
        }),
        height=350
    )

# Insights section
st.markdown("---")
st.subheader("💡 Key Insights & Recommendations")

insights_col1, insights_col2 = st.columns(2)

with insights_col1:
    st.markdown("""
    **🔴 Critical Issues Identified:**
    - **25% Cancellation Rate** - Significant revenue leakage
    - **Driver Cancellations (15.1%)** higher than rider cancellations
    - High variance in driver earnings suggests optimization opportunities
    - Peak hour demand requires better supply management
    """)

with insights_col2:
    st.markdown("""
    **✅ Recommended Actions:**
    - Implement driver incentives in high-demand locations
    - Reduce cancellation through better matching algorithms
    - Deploy surge pricing optimization during peak hours
    - Provide training to underperforming driver segments
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #7f8c8d;'>
        <p>Namma Yatri Analytics Dashboard | Built with Streamlit & Plotly</p>
        <p>Data Analysis Project for Placement Recruitment</p>
    </div>
    """, unsafe_allow_html=True)