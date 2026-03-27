import streamlit as st

st.set_page_config(
    page_title="About Us",
    page_icon="👩‍💻",
    layout="wide"
)

st.markdown(
    """
    <style>
    .bio-container {
        background-color: #f7fff7;
        padding: 3rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-left: 5px solid #2e8b57;
    }
    .bio-header {
        font-size: 2.5rem;
        color: #2e8b57;
        margin-bottom: 1.5rem;
        font-weight: 800;
        font-family: sans-serif;
    }
    .bio-text {
        font-size: 1.2rem;
        line-height: 1.8;
        color: #333;
        text-align: justify;
    }
    .photo-placeholder {
        width: 100%;
        height: 400px;
        background-color: #f0f0f0;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #888;
        font-size: 1.2rem;
        border: 2px dashed #ccc;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    .photo-placeholder:hover {
        transform: scale(1.02);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #222; margin-bottom: 3rem; font-weight: 800;'>Meet the Creator</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("<div class='photo-placeholder'>🖼️ Your Photo Here</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; margin-top: 1rem;'><em>Sruthi</em></p>", unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        <div class="bio-container">
            <div class="bio-header">Hi, I'm Sruthi! 👋</div>
            <div class="bio-text">
                <p>I am a sophomore at Basis Independent Silicon Valley in California. I have six years of coding experience and love exploring the intersection of algorithms and data science to promote sustainability.</p>
                <p>I do environmental advocacy with the Silicon Valley Climate Youth Action. In my free time, I love reading, playing the violin, and biking with my family.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
