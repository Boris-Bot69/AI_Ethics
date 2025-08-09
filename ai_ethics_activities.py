import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="AI Ethics Activities - TUM",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
def load_css():
    st.markdown("""
    <style>
    /* Reset and Base Styles */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
        color: #333;
        background-color: #ffffff;
        margin: 0;
        padding: 0;
    }

    /* Remove Streamlit default margins */
    .main {
        margin: 0 !important;
        padding: 0 !important;
    }

    .main .block-container {
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Custom CSS for Streamlit */
    .main .block-container {
        padding-top: 0;
        padding-bottom: 0;
    }

    /* Navigation Bar */
    .navbar {
        background-color: #E1EBDD;
        padding: 1.5rem 0;
        margin-bottom: 2rem;
        position: relative;
        width: 100%;
        margin-top: 0;
        top: 0;
        left: 0;
        right: 0;
    }

    .nav-links {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
        position: relative;
        z-index: 2;
        color: #222222;
    }

    .nav-link {
        text-decoration: none;
        color: #222222;
        font-size: 16px;
        font-weight: 400;
        font-family: 'Inter', sans-serif;
        letter-spacing: -0.02em;
        padding: 0.5rem 0.5rem;
        transition: all 0.3s ease;
        position: relative;
        white-space: nowrap;
        text-decoration: none !important;
        border-bottom: none !important;
    }

    .nav-link:visited {
        text-decoration: none !important;
        color: #222222;
    }

    .nav-link:hover {
        text-decoration: none !important;
        color: #333;
        background-color: rgba(255, 255, 255, 0.2);
        border-radius: 4px;
    }

    .nav-link:active {
        text-decoration: none !important;
        color: #222222;
    }

    .nav-link.active {
        font-weight: 500;
        background-color: rgba(255, 255, 255, 0.3);
        border-radius: 4px;
        color: #222222;
    }

    .nav-divider {
        width: 2px;
        height: 24px;
        background-color: #FF6B6B;
        margin: 0 0.5rem;
        opacity: 0.8;
    }

    /* Page Content */
    .page-content {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    .page-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 1.5rem;
        text-align: center;
    }

    .page-description {
        font-size: 1.1rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .nav-links {
            flex-wrap: wrap;
            gap: 0.5rem;
            padding: 0 1rem;
        }

        .nav-link {
            font-size: 16px;
            padding: 0.3rem 0.5rem;
        }

        .nav-divider {
            display: none;
        }

        .page-title {
            font-size: 2rem;
        }
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Navigation
def create_navigation():
    st.markdown("""
    <div class="navbar">
        <div class="nav-links">
            <a href="app.py" class="nav-link">TUM AI ethics literacy activities</a>
            <span class="nav-divider"></span>
            <a href="ai_ethics_activities.py" class="nav-link active">AI Ethics Activities</a>
            <span class="nav-divider"></span>
            <a href="ai_ethics_scenarios.py" class="nav-link">AI Ethics Scenarios</a>
            <span class="nav-divider"></span>
            <a href="oecd_principles.py" class="nav-link">OECD Principles</a>
            <span class="nav-divider"></span>
            <a href="research.py" class="nav-link">Research</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main App
def main():
    # Create navigation
    create_navigation()
    
    # Page content
    st.markdown("""
    <div class="page-content">
        <h1 class="page-title">AI Ethics Activities</h1>
        <p class="page-description">
            Explore interactive activities designed to enhance AI ethics literacy through hands-on learning experiences.
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 