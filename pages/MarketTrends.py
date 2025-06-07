import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🎨 Page Config
st.set_page_config(
    page_title="📈 Market Trends",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 💄 Custom CSS
st.markdown("""
    <style>
        .header-nav {
            width: 100%;
            background: linear-gradient(135deg, #4CAF50, #388E3C);
            color: white;
            border-radius: 10px;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .header-content {
            padding: 20px 10px 10px;
            text-align: center;
        }
        .header-title {
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .navbar {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
            padding: 10px 0;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            padding: 8px 20px;
            border-radius: 4px;
            transition: all 0.3s;
            font-size: 15px;
        }
        .navbar a:hover {
            background-color: rgba(255,255,255,0.2);
            transform: translateY(-2px);
        }
        .navbar a.active {
            background-color: rgba(255,255,255,0.3);
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        .custom-footer {
            width: 100%;
            background: rgba(76, 175, 80, 0);
            padding: 20px 10px;
            text-align: center;
            margin-top: 40px;
            border-top: 1px solid rgba(76, 175, 80, 0.3);
            backdrop-filter: blur(5px);
        }
        .footer-content {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            max-width: 1200px;
            margin: 0 auto;
        }
        .footer-section {
            flex: 1;
            min-width: 250px;
            padding: 10px;
            text-align: left;
        }
        .footer-section h4 {
            color: #4CAF50;
            margin-bottom: 15px;
            font-size: 18px;
        }
        .footer-section p, .footer-section a {
            color: #555;
            font-size: 14px;
            line-height: 1.6;
            text-decoration: none;
        }
        .footer-section a:hover {
            color: #4CAF50;
        }
        .footer-bottom {
            margin-top: 20px;
            padding-top: 10px;
            border-top: 1px solid rgba(76, 175, 80, 0.2);
            color: #666;
            font-size: 13px;
        }
        .social-icons {
            display: flex;
            gap: 15px;
            margin-top: 10px;
        }
        .social-icons a {
            color: #4CAF50;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# 🧭 Navbar
st.markdown("""
<div class="header-nav">
    <div class="header-content">
        <div class="header-title">📈 Market Trends</div>
        <div class="navbar">
            <a href="/Home" target="_self">Home</a>
            <a href="/Analytics" target="_self">Analytics</a>
            <a href="/MarketTrends" class="active" target="_self">Market Trends</a>
            <a href="/About" target="_self">About</a>
            <a href="/Contact" target="_self">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 📄 Page Description
st.markdown("""
### 📊 Market Trends

The real estate market is dynamic, influenced by economics, lifestyle, and policies. This section gives insight into housing price trends, key factors, and regional patterns.

With visuals like line graphs and bar charts, we reveal insights to help buyers and sellers make informed decisions based on real data.
""")

# 📁 Load and visualize data
try:
    df = pd.read_csv("house.csv")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📏 Size vs Price")
        fig1, ax1 = plt.subplots()
        sns.lineplot(data=df.sort_values("Size"), x="Size", y="Price", ax=ax1, color='green')
        ax1.set_xlabel("Size (sq ft)")
        ax1.set_ylabel("Price (₹)")
        st.pyplot(fig1, use_container_width=True)

        st.markdown("---")
        st.subheader("🛏 Bedrooms vs Price")
        fig2, ax2 = plt.subplots()
        sns.boxplot(data=df, x="Bedrooms", y="Price", palette="pastel", ax=ax2)
        ax2.set_title("Price Distribution by Bedroom Count")
        st.pyplot(fig2, use_container_width=True)

    with col2:
        st.subheader("📍 Average Price by Location")
        avg_price = df.groupby("Location")["Price"].mean().sort_values(ascending=False).head(10)
        fig3, ax3 = plt.subplots()
        sns.barplot(x=avg_price.values, y=avg_price.index, palette="muted", ax=ax3)
        ax3.set_xlabel("Average Price (₹)")
        ax3.set_title("Top 10 Locations")
        st.pyplot(fig3, use_container_width=True)

except FileNotFoundError:
    st.error("❌ 'house.csv' not found. Please place it in the same directory.")
except Exception as e:
    st.error(f"Error loading data: {str(e)}")

# 🧾 Footer
st.markdown("""
<div class="custom-footer">
    <div class="footer-content">
        <div class="footer-section">
            <h4>About Us</h4>
            <p>Premium House Price Predictor uses machine learning to deliver accurate real estate pricing insights. Stay informed with data-driven guidance.</p>
        </div>
        <div class="footer-section">
            <h4>Quick Links</h4>
            <p><a href="/About" target="_self">Know Us</a></p>
            <p><a href="/MarketTrends" target="_self">Market Reports</a></p>
        </div>
        <div class="footer-section">
            <h4>Contact</h4>
            <p>Email: rajsonar2504@gmail.com</p>
            <p>Phone: +91 9766-09-0082</p>
            <div class="social-icons">
                <a href="https://x.com/RajSonar2504"><i class="fab fa-twitter"></i></a>
                <a href="https://www.facebook.com/profile.php?id=100069695018460"><i class="fab fa-facebook"></i></a>
                <a href="https://www.linkedin.com/in/raj-sonar-9a6628291/"><i class="fab fa-linkedin"></i></a>
                <a href="https://www.instagram.com/raj_sonar_4621/"><i class="fab fa-instagram"></i></a>
            </div>
        </div>
    </div>
    <div class="footer-bottom">
        <p>© 2025 Premium House Price Predictor. All rights reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# 🧠 Font Awesome (for icons)
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)
