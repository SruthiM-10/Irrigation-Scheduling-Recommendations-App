import streamlit as st

st.set_page_config(
    page_title="About Us",
    page_icon="👩‍💻",
    layout="wide"
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Outfit:wght@400;700;900&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at top right, #0a192f, #020c1b);
        color: white;
    }

    /* Container for the About Section */
    .about-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 4rem 2rem;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        max-width: 1000px;
        margin: 0 auto;
        animation: slideUp 0.8s ease-out forwards;
    }

    .about-title {
        font-family: 'Outfit', sans-serif;
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 3rem;
        background: linear-gradient(135deg, #00F260, #0575E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }

    .bio-content {
        font-size: 1.2rem;
        line-height: 1.8;
        color: rgba(255, 255, 255, 0.85);
        background: rgba(255, 255, 255, 0.05);
        padding: 2.5rem;
        border-radius: 20px;
        border-left: 4px solid #00F260;
    }

    .bio-content p {
        margin-bottom: 1.5rem;
    }

    .photo-area {
        width: 100%;
        height: 400px;
        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.02));
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: rgba(255,255,255,0.5);
        border: 2px dashed rgba(255,255,255,0.2);
        transition: transform 0.4s ease, border-color 0.4s ease;
    }

    .photo-area:hover {
        transform: translateY(-10px);
        border-color: #00F260;
        background: linear-gradient(135deg, rgba(0,242,96,0.1), rgba(5,117,230,0.1));
    }

    .photo-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='about-title'>Meet the Creator</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.markdown(
        """
        <div class='photo-area'>
            <div class='photo-icon'>📸</div>
            <div style='font-family: Outfit; font-weight: 700; font-size: 1.5rem;'>Sruthi</div>
            <div style='font-size: 0.9rem; margin-top: 0.5rem;'>Photo Placeholder</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="bio-content">
            <h3 style="font-family: 'Outfit'; color: white; font-size: 2rem; margin-bottom: 1.5rem;">Hi, I'm Sruthi! 👋</h3>
            <p>I am a sophomore at Basis Independent Silicon Valley in California. I have six years of coding experience and love exploring the intersection of algorithms and data science to promote sustainability.</p>
            <p>I do environmental advocacy with the Silicon Valley Climate Youth Action. In my free time, I love reading, playing the violin, and biking with my family.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
