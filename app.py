import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="AI Ethics Literacy - TUM",
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
    }

    /* Remove Streamlit default padding and margins from the main container */
    .main .block-container {
        padding: 0 !important;
    }

    /* Add padding to the top of the body to prevent content from being hidden behind the fixed navbar */
    body {
        padding-top: 100px; /* Adjust this value based on your navbar's height */
    }

    /* Navigation Bar */
    .navbar {
        background-color: #E1EBDD;
        padding: 1.5rem 0;
        position: fixed;
        width: 100%;
        top: 0;
        left: 0;
        right: 0;
        z-index: 10;
    }

    .nav-links {
        display: flex;
        align-items: center;
        justify-content: space-between;
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
        color: #222222 !important;
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
        background: none !important;
    }

    .nav-link:visited {
        text-decoration: none !important;
        color: #222222 !important;
    }

    .nav-link:hover {
        text-decoration: none !important;
        color: #333;
        background-color: rgba(255, 255, 255, 0.2);
        border-radius: 4px;
    }

    .nav-link:active {
        text-decoration: none !important;
        color: #222222 !important;
    }

    .nav-link.active {
        font-weight: 500;
        background-color: rgba(255, 255, 255, 0.3);
        border-radius: 4px;
        color: #222222 !important;
    }

    .nav-divider {
        width: 2px;
        height: 24px;
        background-color: #FF6B6B;
        margin: 0 0.5rem;
        opacity: 0.8;
    }

    /* Full-width green line */
    .green-line {
        position: fixed;
        top: 60px; /* Position right below the navbar */
        width: 100%;
        height: 10px; /* Adjust height as needed */
        background-color: #A0C3A0; /* Example green color */
        z-index: 9; /* Place just below the navbar */
    }

    /* CSS to make images in columns align to the very edge */
    /* This targets the div that wraps the columns and removes the gap */
    .st-emotion-cache-1xw8zd6 {
        gap: 0 !important;
    }

    /* Add padding to the central content column */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) {
        padding: 0 1rem !important;
    }

    /* Custom styles for the text content */
    .custom-header {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 48px;
        line-height: 60px;
        color: #FFFFFF; /* Changed to white for contrast */
        letter-spacing: 0;
        padding: 1.5rem; /* Added padding */
        border-radius: 8px; /* Added rounded corners */
        margin-bottom: 1rem; /* Added some space below the header */
    }

    .custom-text {
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        font-size: 16px;
        line-height: 180%;
        color: #000000; /* Black */
        letter-spacing: 0;
    }
    
    /* Styles for Publications Section */
    .publications-title {
        display: inline-block;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 24px;
        padding: 0.5rem 1.5rem;
        margin: 4rem 0 1.5rem 0;
        background-color: rgba(225, 235, 221, 0.8); /* Semi-transparent green */
        border-bottom: 2px dashed #A0C3A0;
    }

    .publication-item {
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }

    .publication-item strong {
        font-weight: 800; /* Extra Bold */
    }

    .image-spacer {
        height: 20rem; /* Adjusted for better spacing */
    }

    .image-spacer1 {
        height: 6rem; /* Adjusted for better spacing */
    }

    /* New styles for the custom bullet list */
    .list-item {
        display: flex;
        align-items: flex-start;
        margin-bottom: 2rem; /* Space between list items */
        margin-top: 1.5rem;
    }
    .list-bullet {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        margin-right: 15px;
        flex-shrink: 0;
        margin-top: 5px;
    }
    .bullet-red { background-color: #F08080; }
    .bullet-green { background-color: #90EE90; }
    .bullet-orange { background-color: #FFA500; }

    .list-content h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 18px;
        margin: 0 0 5px 0;
    }
    .list-content p {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        margin: 0;
    }

    /* New Card Styles */
    .card {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 2rem;
        height: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.1);
    }

    .card h4 {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 20px;
        color: #466480;
        margin-bottom: 0.75rem;
    }

    .card p {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        line-height: 1.6;
        color: #333;
    }
    
    .oecd-section-title {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 24px;
        text-align: center;
        padding: 1rem;
        margin: 2rem 0;
        background-color: #f7f7f7;
        border-left: 5px solid #A0C3A0;
    }
    
    .oecd-item {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .oecd-item img {
        max-width: 150px;
        margin-bottom: 1rem;
    }
    
    .oecd-item h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 20px;
        margin-bottom: 0.5rem;
    }
    
    .oecd-item p {
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        max-width: 600px;
        margin: 0 auto; /* Center the text block */
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

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

        .custom-header {
            font-size: 32px; /* Adjust font size for smaller screens */
            line-height: 40px;
            padding: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


# Load CSS
load_css()


# Navigation
def create_navigation():
    st.markdown("""
    <div class="navbar">
        <div class="nav-links">
            <span class="nav-link active">Home</span>
            <span class="nav-divider"></span>
            <a href="ai_ethics_activities.py" class="nav-link" target="_self">AI Ethics Activities</a>
            <span class="nav-divider"></span>
            <a href="ai_ethics_scenarios.py" class="nav-link" target="_self">AI Ethics Scenarios</a>
            <span class="nav-divider"></span>
            <a href="oecd_principles.py" class="nav-link" target="_self">OECD Principles</a>
            <span class="nav-divider"></span>
            <a href="research.py" class="nav-link" target="_self">Research</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


def create_green_line():
    st.markdown("""
    <div class="green-line"></div>
    """, unsafe_allow_html=True)


# Main App
def main():
    # Create navigation
    create_navigation()
    # Create the green line
    create_green_line()

    # --- PRIMARY THREE-COLUMN LAYOUT FOR THE ENTIRE PAGE ---
    sidebar_left, main_content, sidebar_right = st.columns([1, 3, 1], gap="small")

    with sidebar_left:
        # All content for the left sidebar. It will extend down the page.
        st.image('images/leftside_picture.png', use_container_width=True)
        st.image('images/leftside_down_picture.png', use_container_width=True)

    with main_content:
        # This is the main central column.

        # --- Top part of the main content (nested 2-column layout) ---
        top_col2, top_col3 = st.columns(2)

        with top_col2:
            # Content from the original second column
            st.header("Practicing AI ethics literacy through Generative AI and tangible crafts")
            st.markdown("""
            <p class="custom-text">
            This website was funded and created through the Co-designing a Risk-Assessment Dashboard for AI Ethics Literacy in EdTech project. 
            Our focus is to develop practical guidance for decision-makers to help them navigate through the process of ethical decision-making in applying AI EdTech.
            </p>
            """, unsafe_allow_html=True)
            st.markdown('<div class="image-spacer"></div>', unsafe_allow_html=True)
            st.image('images/Rectangle_green.png', use_container_width=True)
            st.markdown('<div class="image-spacer1"></div>', unsafe_allow_html=True)

        with top_col3:
            # Content from the original third column
            st.image('images/Rectangle_green.png', use_container_width=True)
            st.markdown('<div class="image-spacer1"></div>', unsafe_allow_html=True)
            st.markdown("""
                   <div>
                       <div class="list-item">
                           <div class="list-bullet bullet-red"></div>
                           <div class="list-content">
                               <h3>What is AI?</h3>
                               <p>AI systems leverage advanced machine learning from vast datasets to generate diverse content (text, images, videos, audio) and can process multi-modal data to engage in natural conversations.</p>
                           </div>
                       </div>
                       <div class="list-item">
                           <div class="list-bullet bullet-green"></div>
                           <div class="list-content">
                               <h3>What is AI ethics?</h3>
                               <p>AI ethics is a critical field that addresses the implications of artificial intelligence in everyday life such as in smartphones or search results. It grapples with ethical concerns such as biases, privacy, and misuse.</p>
                           </div>
                       </div>
                       <div class="list-item">
                           <div class="list-bullet bullet-orange"></div>
                           <div class="list-content">
                               <h3>What is AI ethics literacy?</h3>
                               <p>Practices that foster a process of deliberating implications of AI on what's being learned and how, in relation to the AI ethics principles, as well as knowing the actors involved and their relationships (e.g., who is responsible and who is affected).</p>
                           </div>
                       </div>
                   </div>
                   """, unsafe_allow_html=True)
            st.markdown('<div class="image-spacer1"></div>', unsafe_allow_html=True)

        # --- Fused part of the main content (full width of main_content) ---
        # This content appears directly below the nested columns above.
        st.markdown("---")
        st.header("AI ethics scenarios and activities")
        # Create two columns for the cards
        st.markdown('<div class="image-spacer1"></div>', unsafe_allow_html=True)

        card_col1, card_col2 = st.columns(2, gap="large")

        with card_col1:
            st.markdown("""
                    <div class="card">
                        <h4>AI Ethics Activities</h4>
                        <p>The scenarios encourage conversations about AI ethics related to the  OECD AI principles. Each scenario contains conversation prompts associated with three of the OECD AI Ethics Principles to facilitate discussions about the relevance of AI ethics and to foster AI ethics literacy.</p>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown('<div class="image-spacer1"></div>', unsafe_allow_html=True)

        with card_col2:
            st.markdown("""
                    <div class="card">
                        <h4>AI Ethics Scenarios</h4>
                        <p>The scenarios encourage conversations about AI ethics related to the  OECD AI principles. Each scenario contains conversation prompts associated with three of the OECD AI Ethics Principles to facilitate discussions about the relevance of AI ethics and to foster AI ethics literacy.</p>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown('<div class="image-spacer1"></div>', unsafe_allow_html=True)

        st.header("OECD AI Principles codebook and guiding questions")
        st.markdown('<div class="image-spacer1"></div>', unsafe_allow_html=True)

        st.markdown("""
               <div class="oecd-item">
                   <img src="images/OECD_Codebook.png" alt="OECD Codebook Icon">
                   <h3>OECD Codebook</h3>
                   <p>The OECD AI principles codebook provides a guide for educators and practitioners to identify AI ethics in action. The codebook was developed through the analysis of youth workshops on developing AI ethics literacy.</p>
               </div>
               """, unsafe_allow_html=True)

        st.markdown("""
               <div class="oecd-item">
                   <img src="images/OECD_Guiding_Questions.png" alt="OECD Guiding Questions Icon">
                   <h3>OECD Guiding Questions</h3>
                   <p>The OECD AI principles codebook provides a guide for educators and practitioners to identify AI ethics in action. The codebook was developed through the analysis of youth workshops on developing AI ethics literacy.</p>
               </div>
               """, unsafe_allow_html=True)
        st.markdown('<div class="image-spacer1"></div>', unsafe_allow_html=True)

        st.header("Publications and related research")
        st.markdown('<div class="image-spacer1"></div>', unsafe_allow_html=True)

        st.markdown("""
                <p class="publication-item">
                Humburg, M., Han, A., Zheng, J., Rosé, C., Chao, J., Araujo Melo, N., Chávez, V., Higgs, J., Kaimana, M., Isero, M., Relmasira, S., Donaldson, J., <strong>Keune, A., Hurtado, S.</strong>, McCune, D., Huang, J., Zhang, Y., Smyslova, D., Li, Q., Jiang, S., Ritchie, D., Saito-Stehberger, D., Tate, T., Warschauer, M., Han, S., Corrigan, S., Peppler, K., Jackson, D. W., Scheuneman, S. M., Ramdath, K., Goehrig, F., Nwogu, I. & Waight, N. (2025). Humanizing AI for Education: Conversations with the JLS 2026 Special Issue Contributors. <em>International Society of the Learning Sciences 2025 Annual Meeting (ISLS 2025)</em>. Symposium submission. Helsinki, Finland.
                </p>
                """, unsafe_allow_html=True)

        st.markdown("""
                <p class="publication-item">
                <strong>Keune, A., Hurtado, S.</strong> & Simšić, Ž. (2024). Exploring AI Ethics through educational scenarios with AI generative arts apps. In Lindgren, R., Asino, T. I., Kyza, E. A., Looj, C. K., Keifert, D. T., & Suárez, E. (Eds.). <em>Proceedings of the 18th International Conference of the Learning Sciences - ICLS 2024 (pp. 1818-1821)</em>. International Society of the Learning Sciences.
                </p>
                """, unsafe_allow_html=True)

    with sidebar_right:
        # All content for the right sidebar. It will extend down the page.
        st.image('images/rightside_picture.png', use_container_width=True)
        st.image('images/rightside_down_picture.png', use_container_width=True)


if __name__ == "__main__":
    main()
