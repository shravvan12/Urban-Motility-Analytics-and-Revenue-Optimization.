# 🚕 Urban Mobility Analytics: Revenue & Operations Optimization

> **Comprehensive analytics platform analyzing 10,000+ ride transactions to optimize driver-rider matching, identify ₹3.98L monthly revenue leakage, and improve operational efficiency by 15-20%.**

Built for placement application at **Namma Yatri** - India's auto-rickshaw mobility platform.

---

## 📊 **Project Overview**

This project simulates real-world mobility platform challenges faced by ride-hailing companies like Namma Yatri, Uber, and Ola. Through end-to-end data analysis, I identified critical business problems and delivered actionable insights using SQL, Python, and Power BI.

### **Business Problem**
Mobility platforms face significant operational challenges:
- High cancellation rates leading to revenue loss
- Inefficient driver allocation during peak hours
- Suboptimal surge pricing strategies
- Unequal driver earnings distribution

### **Solution Approach**
Built a comprehensive analytics pipeline to:
1. **Identify revenue leakage** through cancellation analysis
2. **Optimize driver allocation** using demand pattern insights
3. **Enhance surge pricing** strategy based on time-location analytics
4. **Improve driver welfare** through earnings distribution analysis

---

## 🎯 **Key Findings & Business Impact**

### **Revenue Insights**
- 💰 **₹3.98L monthly revenue loss** identified from 25.1% cancellation rate
- 📈 **₹4.8L - ₹23.9L annual recovery** potential through recommended interventions
- 🚀 **42% of rides** utilized surge pricing, generating ₹2.51L additional revenue
- 💡 **15-20% operational efficiency** improvement projected

### **Operational Insights**
- 🕐 **Peak demand hours**: 8-9 AM (10.4% of daily rides), 6-8 PM (17.4%)
- 📍 **Top pickup locations**: Hebbal (717 rides), Sarjapur Road (694), Electronic City (693)
- ❌ **Driver cancellations** (15.1%) higher than rider cancellations (10.1%)
- 💵 **Top 10% drivers** earn 2x the average (₹5,653 vs ₹2,812)

### **Data-Driven Recommendations**
1. **Dynamic Driver Allocation**: Deploy 30% more drivers during 8-9 AM and 6-8 PM peaks
2. **Cancellation Reduction Strategy**: Implement penalty-free cancellation within 2 mins, stricter penalties after
3. **Surge Pricing Optimization**: Adjust surge multipliers based on location-time patterns
4. **Driver Welfare Program**: Earnings guarantee for low-performing drivers, incentivize peak-hour availability

---

## 🛠️ **Tech Stack**

| Category | Technologies |
|----------|-------------|
| **Languages** | Python 3.8+, SQL (PostgreSQL) |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **BI Tools** | Power BI (DAX, Power Query) |
| **Web App** | Streamlit |
| **Database** | PostgreSQL (normalized schema) |
| **Version Control** | Git, GitHub |

---

## 📁 **Project Structure**

```
namma-yatri-analytics/
│
├── data/
│   ├── drivers_data.csv           # 500 driver profiles
│   ├── rides_data.csv              # 10,000 ride transactions
│   └── driver_availability.csv    # 1,500 availability snapshots
│
├── notebooks/
│   ├── 01_data_generation.ipynb   # Synthetic data creation
│   ├── 02_eda_analysis.ipynb      # Exploratory Data Analysis
│   └── 03_visualization.ipynb     # Chart generation
│
├── sql/
│   ├── schema.sql                 # Database schema design
│   ├── queries.sql                # Analytical SQL queries
│   └── insights.sql               # Business intelligence queries
│
├── src/
│   ├── generate_data.py           # Data generation script
│   ├── analysis.py                # EDA functions
│   └── visualizations.py          # Plotting utilities
│
├── dashboard/
│   ├── streamlit_app.py           # Interactive web dashboard
│   └── requirements.txt           # Dashboard dependencies
│
├── powerbi/
│   ├── namma_yatri_dashboard.pbix # Power BI report
│   └── dashboard_screenshots/     # Dashboard images
│
├── images/
│   ├── hourly_demand.png          # Visualization outputs
│   ├── location_heatmap.png
│   ├── revenue_analysis.png
│   ├── driver_performance.png
│   └── cancellation_analysis.png
│
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── LICENSE                        # MIT License
```

---

## 🚀 **Getting Started**

### **Prerequisites**
- Python 3.8 or higher
- PostgreSQL (optional, for SQL analysis)
- Power BI Desktop (optional, for dashboard)

### **Installation**

1. **Clone the repository**
```bash
git clone https://github.com/shravvan12/namma-yatri-analytics.git
cd namma-yatri-analytics
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Generate synthetic data**
```bash
python src/generate_data.py
```

5. **Run Exploratory Data Analysis**
```bash
jupyter notebook notebooks/02_eda_analysis.ipynb
```

6. **Launch Streamlit Dashboard**
```bash
cd dashboard
streamlit run streamlit_app.py
```

---

## 📊 **Visualizations & Dashboards**

### **1. Hourly Demand Pattern Analysis**
*Peak hours: 8-9 AM (morning commute) and 6-8 PM (evening rush)*

### **2. Location-Based Demand Heatmap**
*Hotspots: Hebbal, Electronic City, Whitefield show highest demand*

### **3. Revenue & Surge Pricing Analysis**
*42% surge adoption generating ₹2.51L additional monthly revenue*

### **4. Driver Performance Distribution**
*Top 10% drivers earning 2x average - earnings inequality identified*

### **5. Cancellation Root Cause Analysis**
*Driver cancellations (15.1%) exceed rider cancellations (10.1%)*

### **6. Power BI Interactive Dashboard**
*12+ KPIs with drill-down capabilities for stakeholder analysis*

---

## 💾 **Dataset Overview**

### **Synthetic Data Generation**
Since Namma Yatri's operational data is proprietary, I created a realistic synthetic dataset modeling Bangalore's ride-hailing patterns.

#### **Drivers Data (500 records)**
- Driver ID, Name, Phone, Vehicle Type
- Ratings, Total Trips, Total Earnings
- Registration Date, Status

#### **Rides Data (10,000 records)**
- Ride ID, Driver ID, Rider ID
- Pickup/Drop Locations (15 Bangalore zones)
- Timestamps, Duration, Distance
- Fare, Surge Multiplier, Payment Method
- Ride Status (Completed/Cancelled)
- Ratings, Weather Conditions

#### **Driver Availability (1,500 snapshots)**
- Driver ID, Timestamp
- Location, Availability Status
- Current Earnings (session-based)

---


---

## 📈 **Power BI Dashboard Features**

### **KPIs Tracked**
1. **Revenue Metrics**: Total revenue, daily trends, surge impact
2. **Operational Metrics**: Completion rate, cancellation rate, avg trip duration
3. **Driver Metrics**: Total active drivers, avg earnings, rating distribution
4. **Demand Metrics**: Rides per hour, location hotspots, weather impact

### **Interactive Filters**
- Date range selector
- Location filter (15 Bangalore zones)
- Driver/Rider segmentation
- Weather condition filter
- Time of day slider


## 🎯 **Key Learnings & Skills Demonstrated**

### **Technical Skills**
✅ **SQL Mastery**: Complex queries using JOINs, CTEs, window functions, subqueries  
✅ **Python Data Analysis**: Pandas, NumPy for large dataset manipulation  
✅ **Data Visualization**: Matplotlib, Seaborn, Plotly for insights communication  
✅ **Business Intelligence**: Power BI dashboard design with DAX measures  
✅ **Database Design**: Normalized schema (3NF) for relational data  
✅ **Statistical Analysis**: Distribution analysis, correlation studies, trend identification

### **Business Skills**
✅ **Revenue Modeling**: Identified ₹3.98L monthly leakage, projected ₹4.8L-23.9L recovery  
✅ **Stakeholder Communication**: Translated technical findings into executive insights  
✅ **Strategic Thinking**: Recommended operational improvements with 15-20% impact  
✅ **Domain Knowledge**: Understanding of mobility platform economics and challenges

---

## 🔮 **Future Enhancements**

### **Phase 2: Advanced Analytics**
- [ ] Predictive modeling for demand forecasting (ARIMA, Prophet)
- [ ] Machine learning for cancellation prediction (Random Forest, XGBoost)
- [ ] Driver churn prediction using survival analysis
- [ ] Route optimization using graph algorithms

### **Phase 3: Real-Time Analytics**
- [ ] Streaming data pipeline (Apache Kafka)
- [ ] Real-time dashboard updates
- [ ] Live surge pricing recommendations
- [ ] Dynamic driver allocation system

### **Phase 4: A/B Testing Framework**
- [ ] Experimentation platform for pricing strategies
- [ ] Statistical significance testing
- [ ] Multi-armed bandit optimization

---


## 👨‍💻 **Author**

**Mekala Sravan Kumar**

📧 Email: shravan.kumar1745590@gmail.com  
🔗 LinkedIn: [linkedin.com/in/sravan-kumar](https://linkedin.com/in/sravan-kumar)  
💻 GitHub: [github.com/shravvan12](https://github.com/shravvan12)  

## 📚 **References & Resources**

1. [Namma Yatri Official Website](https://nammayatri.in/)
2. [Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)
3. [Pandas Documentation](https://pandas.pydata.org/docs/)
4. [Streamlit Documentation](https://docs.streamlit.io/)
5. SQL Query Optimization Techniques

---



<div align="center">

### ⭐ If this project helped you, please give it a star! ⭐

**Built with ❤️ for Data-Driven Decision Making**

</div>
