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

    /* Global Typography */
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3 {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Fixed Background for the whole app */
    .stApp {
        background: linear-gradient(rgba(10, 25, 47, 0.7), rgba(10, 25, 47, 0.85)), 
                    url("https://png.pngtree.com/thumb_back/fw800/background/20251102/pngtree-center-pivot-irrigation-in-a-field-at-sunset-light-image_20201383.webp");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
    }

    /* Hide standard UI elements for a cleaner look */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Glassmorphism Hero Section */
    .hero-glass {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 5rem 3rem;
        border-radius: 24px;
        color: #ffffff;
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 4rem;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        animation: fadeIn 1s ease-out;
    }
    
    .hero-glass h1 {
        font-size: 4.5rem;
        font-weight: 900;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #00F260, #0575E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 4px 15px rgba(0,242,96,0.3);
    }
    
    .hero-glass p {
        font-size: 1.4rem;
        font-weight: 300;
        line-height: 1.7;
        opacity: 0.9;
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

    /* Glassmorphism Metric Cards */
    .metrics-container {
        margin-bottom: 4rem;
    }
    
    .metric-card-glass {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.15);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .metric-card-glass:hover {
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,242,96,0.2);
        border-color: rgba(0, 242, 96, 0.4);
        background: rgba(255, 255, 255, 0.12);
    }
    
    .metric-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #00F260, #0575E6);
        -webkit-background-clip: text;
        color: transparent;
        display: inline-block;
    }
    
    .metric-label-glass {
        font-size: 1.6rem;
        font-weight: 700;
        font-family: 'Outfit', sans-serif;
        color: #fff;
        margin-bottom: 1rem;
        letter-spacing: 0.5px;
    }
    
    .metric-desc-glass {
        color: rgba(255, 255, 255, 0.75);
        font-size: 1.05rem;
        line-height: 1.6;
    }

    h2.section-title {
        text-align: center;
        margin-bottom: 3rem;
        color: #ffffff;
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -1px;
    }
    
    /* Modern CTA Section */
    .cta-glass {
        background: linear-gradient(135deg, rgba(0, 242, 96, 0.1), rgba(5, 117, 230, 0.1));
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 4rem 2rem;
        text-align: center;
        border: 1px solid rgba(0, 242, 96, 0.3);
        margin-bottom: 4rem;
    }
    
    .cta-title {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
    }
    
    .cta-subtitle {
        color: rgba(255, 255, 255, 0.85);
        font-size: 1.2rem;
        margin-bottom: 2.5rem;
    }

    /* Page-link button styling */
    .stPageLink {
        display: flex;
        justify-content: center;
    }
    
    .stPageLink a {
        background: linear-gradient(90deg, #00F260, #0575E6) !important;
        color: white !important;
        font-family: 'Outfit', sans-serif;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        padding: 1rem 3rem !important;
        border-radius: 50px !important;
        text-decoration: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 25px rgba(0, 242, 96, 0.4) !important;
        border: none !important;
        display: inline-block !important;
    }
    
    .stPageLink a:hover {
        transform: scale(1.05) translateY(-3px) !important;
        box-shadow: 0 15px 35px rgba(5, 117, 230, 0.6) !important;
        background: linear-gradient(90deg, #0575E6, #00F260) !important;
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
        <p>Empowering farmers to discover and implement field-tested irrigation schedules. Get personalized, data-driven recommendations optimized for your unique location, crop, and soil.</p>
        <div class="award-badge">🏆 Based on IEEE IS-Tech 2026 Award-Winning Research</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<h2 class='section-title'>Why Optimize Your Irrigation?</h2>", unsafe_allow_html=True)

# Metrics Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="metric-card-glass">
            <div class="metric-icon">💧</div>
            <div class="metric-label-glass">Extreme Water Savings</div>
            <p class="metric-desc-glass">Research proves that small changes—like upgrading from a checkbook method to a sensor network—can reduce water usage by <b>20% or more!</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="metric-card-glass">
            <div class="metric-icon">🌱</div>
            <div class="metric-label-glass">Maximum Yield Growth</div>
            <p class="metric-desc-glass">Healthier plants produce better harvests. Precision soil moisture targeting allows your crops to reach their absolute maximum growth potential.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="metric-card-glass">
            <div class="metric-icon">📈</div>
            <div class="metric-label-glass">Cost Reduction</div>
            <p class="metric-desc-glass">Lower pumping energy, reduced fertilizer leaching, and operational efficiency translate directly into significantly higher farm profits.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# CTA Section
st.markdown("<div class='cta-glass'>", unsafe_allow_html=True)
st.markdown("<div class='cta-title'>Ready to transform your farm?</div>", unsafe_allow_html=True)
st.markdown("<div class='cta-subtitle'>Get personalized estimates for plant yield improvements, water usage, and payback periods in seconds.</div>", unsafe_allow_html=True)

# Using st.page_link for robust multi-page navigation styling
col_empty1, col_btn, col_empty2 = st.columns([1, 2, 1])
with col_btn:
    st.markdown(
        '''
        <a href="Irrigation_Tool" target="_self" style="
            background: linear-gradient(90deg, #00F260, #0575E6);
            color: white;
            font-family: 'Outfit', sans-serif;
            font-size: 1.3rem;
            font-weight: 700;
            padding: 1rem 3rem;
            border-radius: 50px;
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: 0 10px 25px rgba(0, 242, 96, 0.4);
            display: inline-block;
            text-align: center;
            width: 100%;
            box-sizing: border-box;
        ">
            💧 Get Your Recommendation 🚀
        </a>
        ''',
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)
