import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Ketki Kaushik | Marketing Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

    /* Main page */
    .main {
        padding-top: 2rem;
    }

    /* Hero section */
    .hero {
        padding: 3rem 1rem 2.5rem 1rem;
        text-align: center;
    }

    .hero h1 {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }

    .hero h3 {
        font-size: 1.25rem;
        font-weight: 400;
        margin-bottom: 1.5rem;
    }

    .tagline {
        font-size: 1.35rem;
        font-weight: 600;
        margin: 1.5rem auto;
        max-width: 800px;
    }

    /* Section headings */
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    /* Project cards */
    .project-card {
        padding: 1.5rem;
        border: 1px solid #dddddd;
        border-radius: 14px;
        margin-bottom: 1rem;
        min-height: 210px;
    }

    .project-card h3 {
        margin-bottom: 0.7rem;
    }

    /* Skill cards */
    .skill-card {
        padding: 1.2rem;
        border: 1px solid #dddddd;
        border-radius: 12px;
        margin-bottom: 1rem;
        min-height: 130px;
    }

    .skill-card h4 {
        margin-bottom: 0.5rem;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        margin-top: 3rem;
        border-top: 1px solid #dddddd;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("Ketki Kaushik")

    st.markdown("""
    **PGDM Marketing**

    Branding • Digital Marketing  
    Consumer Insights • Strategy
    """)

    st.divider()

    st.markdown("### Navigate")

    st.markdown("""
    - 🏠 Home
    - 👩‍💼 About Me
    - 🛠️ Skills
    - 📂 Projects
    - 🎯 Career Interests
    - 📬 Connect
    """)

    st.divider()

    st.markdown("### Portfolio")

    st.caption(
        "Academic and professional work across marketing, branding, "
        "digital marketing, strategy and project management."
    )


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero">

<h1>Ketki Kaushik</h1>

<h3>
PGDM Marketing | Branding | Digital Marketing | Project Management
</h3>

<div class="tagline">
I turn consumer insights into ideas, campaigns and practical marketing solutions.
</div>

<p>
Exploring the intersection of consumer understanding, creativity,
strategy and execution.
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# QUICK INTRO
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Focus", "Marketing")

with col2:
    st.metric("Core Strength", "Consumer Insights")

with col3:
    st.metric("Approach", "Creative + Analytical")


st.divider()


# --------------------------------------------------
# ABOUT ME
# --------------------------------------------------

st.markdown(
    '<div class="section-title">👩‍💼 About Me</div>',
    unsafe_allow_html=True
)

st.write("""
I am a PGDM student specializing in Marketing, with a strong interest in
understanding customers, building brands, creating digital campaigns,
and using insights to support business decisions.
""")

st.write("""
I enjoy exploring how brands connect with consumers and how marketing
strategies can turn customer insights into meaningful business outcomes.
Through my academic projects and practical experiences, I have worked
across branding, digital marketing, market research, consumer insights,
analytics and project management.
""")


# --------------------------------------------------
# WHAT I BRING
# --------------------------------------------------

st.markdown(
    '<div class="section-title">💡 What I Bring</div>',
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="skill-card">
    <h4>🎯 Customer Understanding</h4>
    I focus on understanding consumer needs, behaviours and pain points
    before developing marketing solutions.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="skill-card">
    <h4>📊 Analytical Thinking</h4>
    I use data and structured analysis to identify patterns and support
    marketing decisions.
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="skill-card">
    <h4>✨ Creative Thinking</h4>
    I enjoy converting insights into campaign ideas, content concepts
    and brand experiences.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="skill-card">
    <h4>🚀 Execution Mindset</h4>
    I believe a good strategy should be practical, measurable and
    possible to execute.
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# SKILLS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🛠️ Skills & Tools</div>',
    unsafe_allow_html=True
)

skill1, skill2, skill3, skill4 = st.columns(4)

with skill1:
    st.markdown("""
    <div class="skill-card">
    <h4>Marketing</h4>
    Brand Strategy<br>
    STP<br>
    Consumer Behaviour<br>
    Market Research<br>
    Campaign Planning
    </div>
    """, unsafe_allow_html=True)

with skill2:
    st.markdown("""
    <div class="skill-card">
    <h4>Digital Marketing</h4>
    Google Ads<br>
    Meta Ads<br>
    Social Media<br>
    Content Strategy<br>
    Digital Campaigns
    </div>
    """, unsafe_allow_html=True)

with skill3:
    st.markdown("""
    <div class="skill-card">
    <h4>Analytics</h4>
    Excel<br>
    Power BI<br>
    Data Analysis<br>
    Reporting<br>
    Visualization
    </div>
    """, unsafe_allow_html=True)

with skill4:
    st.markdown("""
    <div class="skill-card">
    <h4>Project Management</h4>
    WBS<br>
    Gantt Chart<br>
    Network Diagram<br>
    Critical Path<br>
    RACI & Risk Management
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# PROJECTS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📂 Featured Projects</div>',
    unsafe_allow_html=True
)

st.write(
    "A selection of projects demonstrating my work across branding, "
    "digital marketing, research, strategy and project management."
)

# Project 1
with st.container():
    st.markdown("""
    <div class="project-card">
    <h3>🎨 Arata — Brand Analysis & Campaign Proposal</h3>
    <p>
    A brand analysis and festive campaign project focused on positioning,
    competitors, content strategy and campaign execution.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View Arata Project",
        "https://github.com/Ketki-Kaushik/Ketki-portfolio/tree/main/projects/arata"
    )


# Project 2
with st.container():
    st.markdown("""
    <div class="project-card">
    <h3>📊 Britannia — Marketing Hackathon</h3>
    <p>
    A marketing research project exploring changing snacking habits,
    health-conscious consumers, competitive positioning and opportunities
    for Britannia NutriChoice.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View Britannia Project",
        "https://github.com/Ketki-Kaushik/Ketki-portfolio/tree/main/projects/britannia"
    )


# Project 3
with st.container():
    st.markdown("""
    <div class="project-card">
    <h3>📱 Sahayak+ — Digital Marketing Capstone</h3>
    <p>
    A digital marketing project covering customer personas, competitor
    analysis, marketing funnel, content strategy and paid media.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View Sahayak+ Project",
        "https://github.com/Ketki-Kaushik/Ketki-portfolio/tree/main/projects/sahayak"
    )


# Project 4
with st.container():
    st.markdown("""
    <div class="project-card">
    <h3>🚀 Rapido — Workforce Management Project</h3>
    <p>
    A project management capstone focused on designing a scalable workforce
    management system for driver onboarding across cities.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View Rapido Project",
        "https://github.com/Ketki-Kaushik/Ketki-portfolio/tree/main/projects/rapido"
    )


# Project 5
with st.container():
    st.markdown("""
    <div class="project-card">
    <h3>👔 CampusFit — Sales & Strategy</h3>
    <p>
    A business concept focused on affordable professional clothing rentals
    for college students preparing for interviews, internships and formal events.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View CampusFit Project",
        "https://github.com/Ketki-Kaushik/Ketki-portfolio/tree/main/projects/campusfit"
    )


# --------------------------------------------------
# CAREER INTERESTS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🎯 Career Interests</div>',
    unsafe_allow_html=True
)

career1, career2, career3 = st.columns(3)

with career1:
    st.markdown("""
    ### Brand Management
    Building meaningful brands through consumer understanding,
    positioning and strategic thinking.
    """)

with career2:
    st.markdown("""
    ### Digital Marketing
    Creating campaigns and content that connect brands with
    consumers across digital platforms.
    """)

with career3:
    st.markdown("""
    ### Customer Development
    Using customer insights, reporting and coordination to
    support business growth.
    """)


# --------------------------------------------------
# CONNECT
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📬 Connect With Me</div>',
    unsafe_allow_html=True
)

st.write(
    "I am open to learning opportunities, marketing roles and "
    "conversations around brands, consumers and digital marketing."
)

contact1, contact2 = st.columns(2)

with contact1:
    st.link_button(
        "LinkedIn",
        "https://www.linkedin.com/in/ketki-kaushik-6b159527b"
    )

with contact2:
    st.link_button(
        "Email Me",
        "mailto:27-Ketki@fiib.edu.in"
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">

<b>Ketki Kaushik</b>

<br>

PGDM Marketing | Branding | Digital Marketing | Project Management

<br><br>

<i>Turning insights into ideas, and ideas into action.</i>

</div>
""", unsafe_allow_html=True)
