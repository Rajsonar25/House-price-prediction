# 🧠 Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# 🎨 Page Config - Set initial_sidebar_state to 'collapsed'
st.set_page_config(
    page_title="🏠 Premium House Price Predictor",
    layout="wide",
    initial_sidebar_state="collapsed"  # This makes sidebar initially collapsed
)

# 💄 Custom CSS
# 💄 Custom CSS
st.markdown("""
    <style>
        /* Sidebar toggle button */
        .sidebar-toggle {
            position: fixed;
            top: 10px;
            left: 10px;
            z-index: 999;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            font-size: 20px;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        .sidebar-toggle:hover {
            background-color: #45a049;
        }
        
        /* Responsive header */
        .header-nav {
            width: 100%;
            background: linear-gradient(135deg, #4CAF50, #388E3C);
            color: white;
            border-radius: 10px;
            margin-bottom: 40px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .header-content {
            padding: 20px 10px 10px;
            text-align: center;
        }
        .header-title {
            font-size: clamp(24px, 3vw, 32px);
            font-weight: bold;
            margin-bottom: 10px;
        }
        .navbar {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
            padding: 10px 0;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            padding: 8px 15px;
            border-radius: 4px;
            transition: all 0.3s;
            font-size: clamp(12px, 2vw, 15px);
        }
        .navbar a:hover {
            background-color: rgba(255,255,255,0.2);
            transform: translateY(-2px);
        }
        .navbar a.active {
            background-color: rgba(255,255,255,0.3);
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        /* Responsive footer */
        .custom-footer {
            width: 100%;
            background: rgba(76, 175, 80, 0);
            padding: 20px 10px;
            text-align: center;
            margin-top: 40px;
            border-top: 1px solid rgba(76, 175, 80, 0.3);
        }
        .footer-content {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            max-width: 1200px;
            margin: 0 auto;
            gap: 20px;
        }
        .footer-section {
            flex: 1;
            min-width: 200px;
            padding: 10px;
            text-align: left;
        }
        .footer-section h4 {
            color: #4CAF50;
            margin-bottom: 15px;
            font-size: clamp(16px, 2vw, 18px);
        }
        .footer-section p, .footer-section a {
            color: #555;
            font-size: clamp(12px, 1.5vw, 14px);
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
            font-size: clamp(11px, 1.5vw, 13px);
        }
        .social-icons {
            display: flex;
            gap: 10px;
            margin-top: 10px;
            flex-wrap: wrap;
        }
        .social-icons a {
            color: #4CAF50;
            font-size: clamp(16px, 2vw, 20px);
        }

        /* Responsive buttons and forms */
        .stButton>button {
            background-color: #1a1a1a;
            color: white;
            font-weight: bold;
            border-radius: 5px;
            padding: 10px 24px;
            font-size: clamp(12px, 1.5vw, 14px);
        }
        
        /* Responsive sidebar */
        .sidebar-title {
            color: #4CAF50;
            font-size: clamp(18px, 2vw, 24px);
            font-weight: bold;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #4CAF50;
        }
        
        /* Responsive prediction card */
        .prediction-result {
            background: linear-gradient(135deg, #4CAF50, #388E3C);
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #4CAF50;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .prediction-result h4 {
            font-size: clamp(14px, 2vw, 16px);
        }
        .prediction-result span {
            font-size: clamp(18px, 3vw, 26px) !important;
        }
        
        /* Responsive home content */
        .home-content {
            width: 100%;
            margin-top: 20px;
            margin-bottom: 80px;
            padding: clamp(20px, 5vw, 60px);
            color: black;
            background-color: #E5E4E2;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .home-content p {
            font-size: clamp(14px, 1.8vw, 16px);
            line-height: 1.6;
        }
        
        /* Responsive carousel */
        .carousel {
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            gap: 20px;
            padding: 10px;
            margin-bottom: 50px;
        }
        .carousel img {
            width: clamp(200px, 40vw, 300px);
            height: clamp(120px, 25vw, 200px);
            border-radius: 15px;
            scroll-snap-align: start;
            flex-shrink: 0;
            object-fit: cover;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: transform 0.3s;
        }
        
        /* Responsive tabs and charts */
        @media (max-width: 768px) {
            .stDataFrame {
                font-size: 12px;
            }
            .stTabs [role="tablist"] button {
                font-size: 12px;
                padding: 8px 12px;
            }
        }
        
        /* General responsive adjustments */
        @media (max-width: 600px) {
            .navbar {
                gap: 8px;
            }
            .navbar a {
                padding: 6px 10px;
            }
            .home-content {
                padding: 20px;
                margin-bottom: 40px;
            }
            .footer-section {
                min-width: 100%;
                text-align: center;
            }
            .social-icons {
                justify-content: center;
            }
        }
    </style>
""", unsafe_allow_html=True)
# Add sidebar toggle button
st.markdown(
    '<button class="sidebar-toggle">☰</button>',
    unsafe_allow_html=True
)

# JavaScript to toggle sidebar
st.markdown(
    """
    <script>
        document.querySelector('.sidebar-toggle').addEventListener('click', function() {
            const sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
            if (sidebar.style.transform === 'translateX(-100%)') {
                sidebar.style.transform = 'translateX(0)';
            } else {
                sidebar.style.transform = 'translateX(-100%)';
            }
        });
    </script>
    """,
    unsafe_allow_html=True
)

# 🧭 Header
st.markdown("""
<div class="header-nav">
    <div class="header-content">
        <div class="header-title">🏠 Premium House Price Predictor</div>
        <div class="navbar">
            <a href="#" class="active" target="_self">Home</a>
            <a href="/Analytics" target="_self">Analytics</a>
            <a href="/MarketTrends" target="_self">Market Trends</a>
            <a href="/About" target="_self">About</a>
            <a href="/Contact" target="_self">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)



st.markdown('''
<div class="home-content">
    <p>
        Welcome to the Home page of the <strong>Premium House Price Predictor</strong> — your intelligent tool for estimating home prices with precision and confidence! 🏠✨<br><br>
        This platform uses real housing data and powerful machine learning models like Linear Regression, Decision Tree, and Random Forest to predict property values across various locations.
        Whether you're a homeowner, buyer, investor, or just curious about the real estate market, this app will help you understand how features like size, number of bedrooms, bathrooms, age, garage, garden, and furnishing style influence the final price.<br><br>
        👉 To get started, use the sidebar to enter the property details — pick your amenities, select a location type, and choose the algorithm you want to try.<br>
        Once done, hit the <strong>"🚀 Predict Price"</strong> button and instantly get a predicted price along with its category: Economy, Standard, or Premium.<br><br>
        You can also explore interactive charts like <em>Size vs Price</em>, price distribution histograms, and correlation heatmaps to dive deeper into the data trends. These visual tools make it easier to understand what really drives property pricing.<br><br>
        Let's make smart real estate decisions together. 🧠💰
    </p>
</div>
''', unsafe_allow_html=True)
st.markdown("""
<style>
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: 48px;
  padding: 10px;
margin-bottom:50px;
}
.carousel img {
  width: 300px;
  height: 200px;
  border-radius: 15px;
  scroll-snap-align: start;
  flex-shrink: 0;
  object-fit: cover;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  transition: transform 0.3s;
}
.carousel img:hover {
  transform: scale(1.05);
}
</style>

<div class="carousel">
  <img src="https://images.unsplash.com/photo-1568605114967-8130f3a36994" alt="House 1">
  <img src="https://images.unsplash.com/photo-1572120360610-d971b9d7767c" alt="House 2">
  <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c" alt="House 3">
  <img src="https://images.unsplash.com/photo-1580587771525-78b9dba3b914" alt="House 4">
</div>
""", unsafe_allow_html=True)



# 🗂️ Data Loading
@st.cache_data
def load_data():
    if not os.path.exists('house.csv'):
        st.error("❌ 'house.csv' not found! Please ensure the file is in the same directory as this app.")
        st.stop()
    return pd.read_csv('house.csv')

df = load_data()

# Check required columns
required_cols = {'Size', 'Bedrooms', 'Bathrooms', 'Price', 'Location', 'Age', 'Garage', 'Garden', 'Furnished'}
if not required_cols.issubset(df.columns):
    st.error(f"⚠️ Required columns missing in CSV. Must contain: {', '.join(required_cols)}")
    st.stop()

# Preprocessing
le = LabelEncoder()
df['Furnished'] = le.fit_transform(df['Furnished'])
df['Garage'] = df['Garage'].map({'Yes': 1, 'No': 0})
df['Garden'] = df['Garden'].map({'Yes': 1, 'No': 0})
df = pd.get_dummies(df, columns=['Location'], drop_first=True)

features = ["Size", "Bedrooms", "Bathrooms", "Age", "Garage", "Garden", "Furnished"] + \
           [col for col in df.columns if col.startswith("Location_")]
X = df[features]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Save encoders
joblib.dump(le, 'furnished_encoder.joblib')

# 🏗️ Model Training
@st.cache_resource
def train_models():
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(random_state=42)
    }
    trained_models = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model
        joblib.dump(model, f"model_{name.replace(' ', '_').lower()}.joblib")
    return trained_models

models = train_models()

# 📌 Sidebar Inputs - All sections initially collapsed
with st.sidebar:
    st.markdown('<div class="sidebar-title">House Configuration</div>', unsafe_allow_html=True)
    
    with st.expander("📋 Property Details", expanded=False):
        size = st.number_input("Size (sqft)", 
                              min_value=500, 
                              max_value=10000, 
                              value=1500, 
                              step=50)
        beds = st.slider("Bedrooms", 1, 6, 3)
        baths = st.slider("Bathrooms", 1, 4, 2)
        age = st.number_input("Age (years)", 0, 50, 5)

    with st.expander("🌿 Amenities", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            garage = st.radio("Garage", ["Yes", "No"], index=1, horizontal=True)
        with col2:
            garden = st.radio("Garden", ["Yes", "No"], index=1, horizontal=True)
        furnished = st.selectbox("Furnishing", ["Furnished", "Semi-Furnished", "Unfurnished"])

    with st.expander("📍 Location & Model", expanded=False):
        location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
        algorithm = st.selectbox("Algorithm", ["Linear Regression", "Decision Tree", "Random Forest"])

    predict_btn = st.button("🚀 Predict Price")

# 📊 Main Content
col1, col2 = st.columns([2.5, 1], gap="large")

with col1:
    with st.expander("📄 Dataset Overview", expanded=True):
        st.dataframe(df, use_container_width=True, height=350)

    tab1, tab2, tab3 = st.tabs(["📈 Size vs Price", "📊 Price Distribution", "📌 Correlation"])

    with tab1:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.regplot(x=df['Size'], y=df['Price'], color='#4CAF50', scatter_kws={'alpha':0.6})
        ax.set_title("Size vs Price", fontweight='bold')
        st.pyplot(fig)

    with tab2:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(df['Price'], bins=20, color='#2196F3', kde=True)
        ax.set_title("Price Distribution", fontweight='bold')
        st.pyplot(fig)

    with tab3:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        ax.set_title("Feature Correlation Heatmap", fontweight='bold')
        st.pyplot(fig)

with col2:
    st.markdown("### 📊 Model Performance")
    model = models[algorithm]
    y_pred = model.predict(X_test)
    st.metric("Mean Squared Error", f"{mean_squared_error(y_test, y_pred):,.0f}")
    st.metric("R² Score", f"{r2_score(y_test, y_pred):.4f}")

    if predict_btn:
        try:
            le = joblib.load('furnished_encoder.joblib')
            
            # Correct location encoding
            location_suburban = 1 if location == "Suburban" else 0
            location_urban = 1 if location == "Urban" else 0
            
            input_data = {
                "Size": size,
                "Bedrooms": beds,
                "Bathrooms": baths,
                "Age": age,
                "Garage": 1 if garage == "Yes" else 0,
                "Garden": 1 if garden == "Yes" else 0,
                "Furnished": le.transform([furnished])[0],
                "Location_Suburban": location_suburban,
                "Location_Urban": location_urban
            }
            
            # Create DataFrame ensuring same feature order as training
            input_df = pd.DataFrame([input_data])[X_train.columns]
            
            predicted_price = model.predict(input_df)[0]
            
            # Calculate percentiles from training data
            price_25th = np.percentile(y_train, 25)
            price_75th = np.percentile(y_train, 75)
            
            if predicted_price < price_25th:
                label = "Economy"
                color = "#FFFFFF"
            elif predicted_price < price_75th:
                label = "Standard"
                color = "#FFC107"
            else:
                label = "Premium"
                color = "#FF9900"

            st.markdown(f"""
                   <div style='box-shadow: 0 4px 8px rgba(0,0,0,1);
' class="prediction-result">
        <h4 style='color: #333; margin-top: 0;'>Prediction Result</h4>
        <div style='
            background: linear-gradient(135deg, #8A2BE2, #9932CC);
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.5);
        '>
            <span style='
                font-size: 26px;
                font-weight: bold;
                color: white;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            '>₹{predicted_price:,.0f}</span>
        </div>
        <div style='
            margin-top: 10px;
            text-align: right;
            font-weight: bold;
            color: {color};
        '>
            {label} Category
        </div>
    </div>
            """, unsafe_allow_html=True)

            # Show feature importance for tree-based models
            if algorithm != "Linear Regression":
                with st.expander("🔍 Feature Importance", expanded=True):
                    if algorithm == "Decision Tree":
                        importances = model.feature_importances_
                    else:  # Random Forest
                        importances = model.feature_importances_
                    
                    feat_imp = pd.DataFrame({
                        'Feature': X_train.columns,
                        'Importance': importances
                    }).sort_values('Importance', ascending=False)
                    
                    fig, ax = plt.subplots(figsize=(8, 4))
                    sns.barplot(x='Importance', y='Feature', data=feat_imp, palette='viridis')
                    ax.set_title('Feature Importance')
                    st.pyplot(fig)

        except Exception as e:
            st.error(f"Error in prediction: {str(e)}")

# 🧾 Footer
st.markdown("""
<div class="custom-footer">
    <div class="footer-content">
        <div class="footer-section">
            <h4>About Us</h4>
            <p>Premium House Price Predictor uses advanced machine learning to provide accurate real estate valuations. Our models are trained on the latest market data.</p>
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
                <a href="https://www.instagram.com/raj_sonar_4621/?next=%2F"><i class="fab fa-instagram"></i></a>
            </div>
        </div>
    </div>
    <div class="footer-bottom">
        <p>© 2025 Premium House Price Predictor. All rights reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Add Font Awesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)