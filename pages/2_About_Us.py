import streamlit as st

st.set_page_config(
    page_title="About Us",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Outfit:wght@400;700;900&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.3)), 
                    url("https://png.pngtree.com/thumb_back/fw800/background/20251102/pngtree-center-pivot-irrigation-in-a-field-at-sunset-light-image_20201383.webp");
        background-attachment: scroll;
        background-size: cover;
    }

    /* Container for the About Section */
    .about-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 4rem 2rem;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 30px;
        border: 1px solid rgba(0, 0, 0, 0.1);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        max-width: 1100px;
        margin: 2rem auto;
        animation: slideUp 0.8s ease-out forwards;
        
        font-family: 'Outfit', sans-serif;
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 3rem;
        color: #2e8b57;
        text-align: center;
    }

    .bio-content {
        font-size: 1.2rem;
        line-height: 1.8;
        color: #333;
        background: rgba(240, 248, 240, 0.8);
        padding: 2.5rem;
        border-radius: 20px;
        border-left: 5px solid #2e8b57;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }

    .bio-content p {
        margin-bottom: 1.5rem;
    }

    .photo-area {
        width: 100%;
        height: 400px;
        background: #f7f9fc;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: #666;
        border: 2px dashed #b0c4b1;
        transition: transform 0.4s ease, border-color 0.4s ease;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.02);
    }

    .photo-area:hover {
        transform: translateY(-5px);
        border-color: #2e8b57;
        background: #f0f7f2;
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

st.markdown("<div class='about-wrapper'>Meet the Creator</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.markdown(
        f"""
        <div style='text-align: center; margin-bottom: -10px;'>
            <img src='https://lh3.googleusercontent.com/sitesv/APaQ0SRyaltfvKr4EJOIX0z0GutKqfAs0l6ZVk-HpBolwhxUx60Z3CTpkg3mMD62LOozDze-iMtJpmCInQUl3V9_34bw7AFmn3gIcGAWiaPXL7JboxNUWxNjbTodkopPv9wfltcbVXRyIuyQawPQiF0uw5N0mYW5TWzfw6m7OFBvO28qT9h-UnMiO_nFg_1LPC_BBpKzsK1LwxPMJG3BueCtHw5lRZqVQfRgWWV0=w1280' 
                 style='width: 140px; height: 140px; border-radius: 20px; object-fit: cover;'>
            <p style='font-family: Outfit; font-weight: 700; font-size: 1.2rem; color: #111; margin-top: 5px; margin-bottom: 0;'>
                Sruthi
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="bio-content">
            <h3 style="font-family: 'Outfit'; color: #2e8b57; font-size: 2.2rem; margin-bottom: 1.5rem;">Hi, I'm Sruthi! 👋</h3>
            <p>I am a sophomore at Basis Independent Silicon Valley in California. I have six years of coding experience and love exploring the intersection of algorithms and data science to promote sustainability.</p>
            <p>I do environmental advocacy with the Silicon Valley Climate Youth Action. In my free time, I love reading, playing the violin, and biking with my family.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)
