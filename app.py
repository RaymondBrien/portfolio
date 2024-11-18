import streamlit as st

st.title("Raymond Brien")
st.balloons()

# sections
st.markdown("---")
with st.expander("About Me"):
    st.write(
        "I am a software engineer with a passion for building products that help people. \n"
        "My expertise spans software development, machine learning, and UX/UI design, "
        "with a focus on creating accessible and impactful solutions."
    )

with st.expander("Services"):
    st.write("I offer a wide range of services, including:")
    st.markdown("""
    - **Web Development**: Front-end and back-end solutions tailored to your needs.
    - **Mobile Development**: Cross-platform mobile app development.
    - **Software Consulting**: From prototypes to scaling production-level applications.
    - **Accessibility Testing**: Comprehensive audits and reports.
    """)
    st.write("I am currently available for freelance and full-time work.")

with st.expander("Projects"):
    st.write(
        "I have worked on a variety of projects, including:\n"
        "- Web and mobile applications\n"
        "- Machine learning tools for predictive analytics\n"
        "- Research and development for educational technology"
    )
    st.write("Currently, I am building a project to help people learn how to code.")

st.header("Skills")
with st.expander("Skills Summary"):
    st.write("""
    - **Machine Learning**: Predictive analytics, data visualization
    - **Web Scraping**: Automated data collection and processing
    - **UI/UX Design**: Accessibility testing, prototyping
    """)
    st.write("---")
    st.write("### Front-End Skills:")
    st.write("""
    - **Languages**: HTML, CSS, JavaScript
    - **Frameworks**: Bootstrap
    - **Design Tools**: Figma, Adobe Creative Suite (Photoshop, Illustrator, InDesign)
    """)
    st.write("---")
    st.write("### Back-End Skills:")
    st.write("""
    - **Languages**: Python, SQL, (Learning: Java, Swift)
    - **Frameworks**: Django, Streamlit, Flask, FastAPI, TensorFlow
    - **Libraries**: nltk, gspread
    - **Databases**: PostgreSQL, SQLite
    """)
    st.write("---")
    st.write("### Testing & Deployment:")
    st.write("""
    - **Testing Tools**: Pytest, Jest
    - **Cloud Tools**: Heroku, Docker, Google Colab
    """)
    st.write("---")
    st.write("### Other Tools:")
    st.write("""
    - **Productivity**: Slack, Zoom, Google Suite, Notion, Obsidian
    - **Music Tools**: Ableton Live, MaxMSP
    """)

with st.expander("Contact"):
    st.write("You can contact me by email at **raytbrien@gmail.com**.")
    st.write("""
    You can also connect with me on:
    - [LinkedIn](https://www.linkedin.com/in/raymondbrien/)
    - [GitHub](https://github.com/RaymondBrien)
    """)

st.markdown("---")
st.write("### Future Goals")
st.write(
    "I am currently learning **Java** and **Swift**, and I aim to expand my expertise into mobile app development using native frameworks."
)
