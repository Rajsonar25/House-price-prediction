import streamlit as st

# 🎨 Page Config
st.set_page_config(
    page_title="ℹ️ About - Premium House Price Predictor",
    layout="wide",
    initial_sidebar_state="collapsed" 
)

# 💄 Custom CSS for Navbar
st.markdown("""
    <style>
        /* Responsive Navbar styling */
        .header-nav {
            width: 100%;
            background: linear-gradient(135deg, #4CAF50, #388E3C);
            color: white;
            border-radius: 10px;
            margin-bottom: clamp(30px, 5vw, 60px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .header-content {
            padding: clamp(10px, 2vw, 20px) 10px;
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
            gap: clamp(10px, 3vw, 50px);
            padding: 10px 0;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            padding: clamp(5px, 1vw, 8px) clamp(10px, 2vw, 20px);
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
        
        /* Responsive content styling */
        .about-content {
            width: 100%;
            margin-top: 20px;
            margin-bottom: clamp(40px, 8vw, 80px);
            padding: clamp(20px, 5vw, 60px);
            color: black;
            background-color: #E5E4E2;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .about-content p {
            font-size: clamp(14px, 1.8vw, 16px);
            line-height: 1.6;
        }
        
        /* Responsive feature cards */
        .feature-card {
            background: linear-gradient(135deg, #4CAF50, #388E3C);
            padding: clamp(15px, 2vw, 20px);
            border-radius: 8px;
            margin: clamp(10px, 2vw, 15px) 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            border-left: 4px solid #4CAF50;
        }
        .feature-card h3 {
            font-size: clamp(16px, 2.2vw, 20px);
            margin-top: 0;
        }
        .feature-card p, .feature-card li {
            font-size: clamp(13px, 1.6vw, 15px);
        }
        .feature-card ul {
            padding-left: 20px;
        }
        
        /* Responsive footer */
        .custom-footer {
            width: 100%;
            background: rgba(76, 175, 80, 0);
            padding: clamp(15px, 2vw, 20px) 10px;
            text-align: center;
            margin-top: clamp(30px, 5vw, 40px);
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
            min-width: min(250px, 100%);
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
            gap: clamp(10px, 2vw, 15px);
            margin-top: 10px;
            flex-wrap: wrap;
        }
        .social-icons a {
            color: #4CAF50;
            font-size: clamp(16px, 2vw, 20px);
        }
        
        /* Mobile-specific adjustments */
        @media (max-width: 600px) {
            .navbar {
                gap: 8px;
            }
            .about-content {
                padding: 20px;
            }
            .feature-card {
                padding: 15px;
            }
            .footer-section {
                text-align: center;
            }
            .social-icons {
                justify-content: center;
            }
        }
    </style>
""", unsafe_allow_html=True)

# 🧭 Navbar (same as main app)
st.markdown("""
<div class="header-nav">
    <div class="header-content">
        <div class="header-title">ℹ️ About - Premium House Price Predictor</div>
        <div class="navbar">
            <a href="/Home" target="_self">Home</a>
            <a href="/Analytics" target="_self">Analytics</a>
            <a href="/MarketTrends" target="_self">Market Trends</a>
            <a href="/About" class="active" target="_self">About</a>
            <a href="/Contact" target="_self">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content container
st.markdown("""
# Welcome to **Premium House Price Predictor** 
""")

st.markdown('''
<div class="about-content">
    <p>
        Welcome to our Premium House Price Predictor – your trusted companion for smarter real estate decisions.
        This tool is designed to provide accurate, data-driven predictions for house prices based on key features like size, location, number of bedrooms, and more.
        Whether you're a buyer looking to invest or a seller wanting the best deal, our platform empowers you with real-time insights.
        With a clean interface and easy-to-use inputs, you can explore property values confidently.
        We believe in transparency, simplicity, and helping you make informed decisions in the ever-changing housing market.
    </p>
</div>
''', unsafe_allow_html=True)

# Feature cards
st.markdown("""
<div class="feature-card">
<h3>🔍 About This Project</h3>
<p>This application helps homeowners, buyers, and real estate professionals estimate property values using advanced machine learning algorithms. Our models are trained on comprehensive real estate data to provide accurate price predictions.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
<h3>🛠️ Tech Stack</h3>
<ul>
<li><strong>Frontend:</strong> Streamlit, HTML/CSS</li>
<li><strong>Backend:</strong> Python, Scikit-Learn</li>
<li><strong>Data Processing:</strong> Pandas, NumPy</li>
<li><strong>Visualization:</strong> Matplotlib, Seaborn</li>
<li><strong>Deployment:</strong> Streamlit Cloud</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
<h3>👨‍💻 Built By</h3>
<p><strong>Raj Sonar</strong> - Data Scientist & Full Stack Developer</p>
<p>Connect with me: 
<a href="mailto:rajsonar2504.com">📧 Email</a> | 
<a href="https://linkedin.com/in/raj-sonar">🔗 LinkedIn</a> | 
<a href="https://github.com/rajsonar">🐙 GitHub</a>
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
<h3>📜 License</h3>
<p>This project is open-source under the MIT License.</p>
<p>Copyright © 2023 Premium House Price Predictor</p>
</div>
""", unsafe_allow_html=True)

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