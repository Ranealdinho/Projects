# Import required libraries
import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="My Job Application Website", page_icon=":guardsman:")

# Add header
st.header("Welcome to My Job Application Website!")

# Add subheader
st.subheader("About Me")

# Add text description
st.write(
    """
    Hi, my name is Rane Najera and I'm a University of Delaware graduate, as well as a graduate of the Data Science Career Track at Springboard. 
    I have experience in Data Science/ Machine Learning, Data Engineering, Data Analysis, and I specialize in automating pythonic issues to solve complex problems.
    I am passionate about leveraging technology to solve real-world problems and make a positive impact in the world.
    """
)

st.write(
    "[Learn more here at my github! >](https://github.com/Ranealdinho/Springboard)"
)

# Add section for work experience
st.subheader("Work Experience")

# Add a table with work experience
work_experience = {
    "Company": ["Springboard", "Bridge Corp."],
    "Position": ["Data Science Career Track", "Data Analyst/Engineer"],
    "Duration": ["March 2021 - Feb 2022", "March 2022 - Present"],
}
st.table(work_experience)

# Add section for education
st.subheader("Education")

# Add a table with education
education = {
    "Degree": ["Bachelor of Science in Wildlife Ecology"],
    "University": ["University of Delaware"],
    "Graduation Year": ["2018"],
}
st.table(education)

# Add section for skills
st.subheader("Skills")

# Add a list of skills
skills = [
    "Python",
    "SQL",
    "AWS",
    "Airflow",
    "Git",
    "Machine Learning",
    "Data Analysis",
    "Excel",
    "Looker",
    "Tableau",
    "Matillion",
    "Redshift",
]
st.write(skills)

# Add section for contact information
st.subheader("Contact Me")

# Add a contact form with name, email and message
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
if st.button("Submit"):
    st.success(
        "Thank you for your message. I will get back to you as soon as possible."
    )

