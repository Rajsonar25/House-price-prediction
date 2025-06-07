import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 🎨 Page Config
st.set_page_config(
    page_title="📞 Contact Us",
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
            margin-bottom: clamp(15px, 3vw, 25px);
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
            flex-wrap: wrap;
            justify-content: center;
            gap: clamp(15px, 3vw, 50px);
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
        @media (max-width: 768px) {
            [data-testid="column"] {
                width: 100% !important;
                padding: 0 !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# 🧭 Navbar
st.markdown("""
<div class="header-nav">
    <div class="header-content">
        <div class="header-title">📞 Contact Us</div>
        <div class="navbar">
            <a href="/Home" target="_self">Home</a>
            <a href="/Analytics" target="_self">Analytics</a>
            <a href="/MarketTrends" target="_self">Market Trends</a>
            <a href="/About" target="_self">About</a>
            <a href="/Contact" class="active" target="_self">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 📬 Section
st.subheader("📬 Get in Touch")
st.write("Feel free to contact us with any questions or inquiries.")
st.markdown("**Email:** rajsonar2504@gmail.com")
st.markdown("**Phone:** +91 9766-09-0082")

# ✍️ Contact Form
st.subheader("✍️ Send a Message")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
with col2:
    subject = st.text_input("Subject")
    phone = st.text_input("Phone Number")

message = st.text_area("Your Message", height=150)

def send_email(sender_name, sender_email, phone, subject, message):
    try:
        sender = "rajsonar779@gmail.com"  # Your Gmail
        receiver = "rajsonar779@gmail.com"
        password = "yourapppassword"  # Replace with app password

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = f"Contact Form: {subject}"

        body = f"""
        Name: {sender_name}
        Email: {sender_email}
        Phone: {phone}
        Message:
        {message}
        """
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

if st.button("Send"):
    if name and email and subject and message:
        if send_email(name, email, phone, subject, message):
            st.success("✅ Message sent successfully!")
    else:
        st.warning("Please fill out all required fields.")

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

# Font Awesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)
