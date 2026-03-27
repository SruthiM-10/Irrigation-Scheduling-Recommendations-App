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

    .stMainBlockContainer, .stMain {
        font-family: 'Inter', sans-serif;
    }
    
    .stMain h1, .stMain h2, .stMain h3 {
        font-family: 'Outfit', sans-serif !important;
    }

    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.3)), 
                    url("https://png.pngtree.com/thumb_back/fw800/background/20251102/pngtree-center-pivot-irrigation-in-a-field-at-sunset-light-image_20201383.webp");
        background-attachment: scroll;
        background-size: cover;
    }
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

    .metric-card-glass {
        background: linear-gradient(
            105deg, 
            rgba(255, 255, 255, 0.98) 0%, 
            rgba(255, 255, 255, 0.95) 40%,
            rgba(0, 77, 64, 0.95) 100%
        );
        
        backdrop-filter: blur(20px);
        padding: 2.2rem 1.8rem;
        border-radius: 24px;
        text-align: left;
        
        border-left: 8px solid #004d40;
        border: 1px solid rgba(0, 77, 64, 0.1);
        border-top: 1px solid rgba(255, 255, 255, 0.8);
        
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        height: 100%;

        color: #002d26; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
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
        letter-spacing: 0.5px;
    }
    
    .metric-desc-glass {
        color: #555;
        font-size: 1.05rem;
    }

    h2.section-title {
        text-align: left;
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
    
    .cta-title {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        text-align: center;
        border: 2px solid #2e8b57;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border-radius: 20px;
        
        color: #2e8b57;
        font-size: 2.5rem;
        font-weight: 800;
        margin-top: 1rem;
    }
    
    .cta-subtitle {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border-radius: 20px;
        
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
        <h1>Simple Irrigation Scheduling Method Recommendation</h1>
        <p>Empowering farmers to discover field-tested irrigation schedules. <b>Get personalized suggestions that take very little time and effort to implement!</b> Start applying optimal methods right away to match your desired workflow.</p>
        <div class="award-badge">🏆 Based on Research presented at IEEE Technologies for Sustainability 2026</div>
    </div>
    """,
    unsafe_allow_html=True
)
#         <div class="award-badge">🏆 Based on Award-winning Projects and Research presented at IEEE Technologies for Sustainability 2026</div>

st.markdown("<div class='title-wrapper'><h2 class='section-title'>Why Follow our Recommendations?</h2></div>", unsafe_allow_html=True)

# Metrics Rows
st.markdown(
    """
    <div class="metric-card-glass">
        <div class="metric-icon">⚡ Low Effort</div>
        <p class="metric-desc-glass">Quick to start and very easy to implement. Personalized to the kind of system YOU prefer.</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="metric-card-glass">
        <div class="metric-icon">💧Water Savings</div>
        <p class="metric-desc-glass">Small irrigation scheduling method changes, such as between a sensor network and a checkbook balancing method, can cut water usage by 20% or more!</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="metric-card-glass">
        <div class="metric-icon">🌱Higher Yield</div>
        <p class="metric-desc-glass">Healthier plants and robust harvests. Correct soil moisture maximizes your crops' absolute growth potential.</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="metric-card-glass">
        <div class="metric-icon">📉Cost Reduction</div>
        <p class="metric-desc-glass">Lowering pumping energy and minimizing fertilizer runoff efficiently transforms into greater operational profit.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='cta-title'>Ready to transform your farm?</div>", unsafe_allow_html=True)
st.markdown("<div class='cta-subtitle'>Get personalized estimates requiring minimal effort for plant yield and water usage improvements.</div>", unsafe_allow_html=True)

col_empty1, col_btn, col_empty2 = st.columns([1, 2, 1])
with col_btn:
    if st.button("💧 Get Your Recommendation Now 🚀", use_container_width=True):
        try:
            st.switch_page("pages/1_Irrigation_Tool.py")
        except Exception:
            # Fallback for Streamlit Cloud paths
            st.write("Navigation error! Please select the tool manually from the sidebar.")

st.markdown("</div>", unsafe_allow_html=True)
