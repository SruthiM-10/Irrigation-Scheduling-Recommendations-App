import streamlit as st

st.set_page_config(
    page_title="Irrigation Scheduling Method Recommendation System - Home",
    page_icon="🌾",v
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.3)), 
                    url("https://png.pngtree.com/thumb_back/fw800/background/20251102/pngtree-center-pivot-irrigation-in-a-field-at-sunset-light-image_20201383.webp");
        background-attachment: scroll;
        background-size: cover;
    }}
    /* Gradient Background for Hero Section */
    .hero {
        background: linear-gradient(135deg, #2e8b57 0%, #1e5c3a 100%);
        padding: 4rem 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }
    .hero h1 {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        color: #ffffff;
    }
    .hero p {
        font-size: 1.5rem;
        font-weight: 300;
        opacity: 0.95;
    }
    
    /* Metrics section */
    .metric-card {
        background-color: white;
        padding: 2.5rem 1.5rem;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #e0e0e0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .metric-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(46, 139, 87, 0.15);
        border-color: #2e8b57;
    }
    .metric-value {
        font-size: 3.5rem;
        font-weight: 800;
        color: #2e8b57;
        margin-bottom: 0.5rem;
    }
    .metric-label {
        font-size: 1.3rem;
        font-weight: 600;
        color: #333;
    }
    .metric-desc {
        margin-top: 1rem;
        color: #666;
        font-size: 1rem;
        line-height: 1.5;
    }
    
    /* Call to Action */
    .cta-container {
        text-align: center;
        margin-top: 4rem;
        padding: 2rem;
        background-color: #f7fff7;
        border-radius: 15px;
        border: 1px dashed #2e8b57;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff8a00, #e52e71);
        color: white;
        border: none;
        padding: 1rem 3rem !important;
        font-size: 1.2rem !important;
        font-weight: bold;
        border-radius: 30px !important;
        box-shadow: 0 5px 15px rgba(229, 46, 113, 0.4);
        transition: all 0.3s ease !important;
        width: 100% !important;
        max-width: 400px;
        display: block;
        margin: 0 auto;
    }
    .stButton>button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 8px 20px rgba(229, 46, 113, 0.6) !important;
        background: linear-gradient(90deg, #e52e71, #ff8a00) !important;
        color: white !important;
        border: none !important;
    }
    .stButton>button:focus {
        border: none !important;
        box-shadow: 0 8px 20px rgba(229, 46, 113, 0.6) !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <h1>Smart Irrigation Scheduling Recommendations</h1>
        <p>Empowering farmers to interpret and discover experiments that have been conducted near the location for what irrigation management schedules have worked well in the past. Personalized suggestions that can take as much as or as little time to implement as the farmer desires.</p>
        <p>Award-winning project, transforming a dataset from a paper published at the 2026 IEEE Technologies for Sustainability Conference, into a recommendation system</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<h2 style='text-align: center; margin-bottom: 3rem; color: #222; font-weight: 700;'>Why Choose Our Method?</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Water Savings</div>
            <p class="metric-desc">Research shows that small changes in irrigation scheduling methods, even the difference between using a checkbook balancing method or a sensor network can lead to 20% or more differences in water usage!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Yield Increase</div>
            <p class="metric-desc">Healthier plants produce better harvests. Optimizing soil moisture allows your crops to reach their maximum growth potential.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Cost Reduction</div>
            <p class="metric-desc">Lower pumping costs, reduced fertilizer leaching, and energy efficiency translate directly to higher profit margins.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div class='cta-container'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #2e8b57; margin-bottom: 0.5rem;'>Ready to optimize your farm?</h3>", unsafe_allow_html=True)
st.markdown("<p style='color: #555; margin-bottom: 2rem; font-size: 1.1rem;'>It's easy to get started. Find your optimal irrigation method in seconds.</p>", unsafe_allow_html=True)
st.markdown("<p style='color: #555; margin-bottom: 2rem; font-size: 1.1rem;'>We offer personalized estimates for approximate improvement in plant yield, water usage, and payback period!</p>", unsafe_allow_html=True)

col_empty1, col_btn, col_empty2 = st.columns([1, 2, 1])
with col_btn:
    if st.button("🚀 Start Using the Recommendation Tool"):
        st.switch_page("pages/1_Irrigation_Tool.py")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>Explore the sidebar to navigate between our tools and learn more about our mission.</p>", unsafe_allow_html=True)
