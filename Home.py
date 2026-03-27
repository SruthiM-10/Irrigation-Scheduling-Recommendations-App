import streamlit as st

st.set_page_config(
    page_title="Irrigation Recommendation System",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Outfit:wght@400;700;900&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Fixed Background for the whole app */
    .stApp {
        background: url("https://png.pngtree.com/thumb_back/fw800/background/20251102/pngtree-center-pivot-irrigation-in-a-field-at-sunset-light-image_20201383.webp");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
    }

    /* White Mode Glassmorphism Hero Section */
    .hero-glass {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(0, 0, 0, 0.1);
        padding: 5rem 3rem;
        border-radius: 24px;
        color: #111111;
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 4rem;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        animation: fadeIn 1s ease-out;
    }
    
    .hero-glass h1 {
        font-size: 4.5rem;
        font-weight: 900;
        margin-bottom: 1.5rem;
        color: #2e8b57;
    }
    
    .hero-glass p {
        font-size: 1.4rem;
        font-weight: 400;
        line-height: 1.7;
        color: #444;
        max-width: 900px;
        margin: 0 auto 1.5rem auto;
    }

    .award-badge {
        display: inline-block;
        background: linear-gradient(90deg, #FFD700, #FDB931);
        color: #111;
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1rem;
        margin-top: 1rem;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
    }

    /* White Mode Glassmorphism Metric Cards */
    .metric-card-glass {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        text-align: center;
        border: 1px solid rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        color: #111;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .metric-card-glass:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(46, 139, 87, 0.2);
        border-color: #2e8b57;
    }
    
    .metric-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: #2e8b57;
        display: inline-block;
    }
    
    .metric-label-glass {
        font-size: 1.6rem;
        font-weight: 700;
        font-family: 'Outfit', sans-serif;
        color: #111;
        margin-bottom: 1rem;
        letter-spacing: 0.5px;
    }
    
    .metric-desc-glass {
        color: #555;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    h2.section-title {
        text-align: center;
        margin-bottom: 3rem;
        color: #2e8b57;
        background: rgba(255,255,255,0.95);
        padding: 1rem;
        border-radius: 15px;
        display: inline-block;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -1px;
    }
    
    .title-wrapper {
        text-align: center;
    }
    
    /* Modern white CTA Section */
    .cta-glass {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 4rem 2rem;
        text-align: center;
        border: 2px solid #2e8b57;
        margin-bottom: 4rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    }
    
    .cta-title {
        color: #2e8b57;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
    }
    
    .cta-subtitle {
        color: #444;
        font-size: 1.3rem;
        margin-bottom: 2.5rem;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown(
    """
    <div class="hero-glass">
        <h1>Smart Irrigation AI</h1>
        <p>Empowering farmers to discover field-tested irrigation schedules. <b>Get personalized suggestions that take very little time and effort to implement!</b> Start applying optimal methods right away to match your desired workflow.</p>
        <div class="award-badge">🏆 Based on IEEE IS-Tech 2026 Award-Winning Research</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title-wrapper'><h2 class='section-title'>Why Optimize Your Irrigation?</h2></div>", unsafe_allow_html=True)

# Metrics Columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <div class="metric-card-glass">
            <div class="metric-icon">⚡</div>
            <div class="metric-label-glass">Low Effort</div>
            <p class="metric-desc-glass">Quick to start and very easy to implement. Takes practically no extra time from your daily routine while delivering massive value.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="metric-card-glass">
            <div class="metric-icon">💧</div>
            <div class="metric-label-glass">Water Savings</div>
            <p class="metric-desc-glass">Precision irrigation changes, such as moving to sensor networks, cut wasteful usage by 20% or more easily!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="metric-card-glass">
            <div class="metric-icon">🌱</div>
            <div class="metric-label-glass">Higher Yield</div>
            <p class="metric-desc-glass">Healthier plants and robust harvests. Correct soil moisture maximizes your crops' absolute growth potential.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <div class="metric-card-glass">
            <div class="metric-icon">📉</div>
            <div class="metric-label-glass">Cost Reduction</div>
            <p class="metric-desc-glass">Lowering pumping energy and minimizing fertilizer runoff efficiently transforms into greater operational profit.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# CTA Section
st.markdown("<div class='cta-glass'>", unsafe_allow_html=True)
st.markdown("<div class='cta-title'>Ready to transform your farm with zero hassle?</div>", unsafe_allow_html=True)
st.markdown("<div class='cta-subtitle'>Get personalized estimates requiring minimal effort for massive plant yield and water usage improvements.</div>", unsafe_allow_html=True)

col_empty1, col_btn, col_empty2 = st.columns([1, 2, 1])
with col_btn:
    if st.button("💧 Get Your Recommendation Now 🚀", use_container_width=True):
        try:
            st.switch_page("pages/1_Irrigation_Tool.py")
        except Exception:
            # Fallback for Streamlit Cloud paths
            st.write("Navigation error! Please select the tool manually from the sidebar.")

st.markdown("</div>", unsafe_allow_html=True)
