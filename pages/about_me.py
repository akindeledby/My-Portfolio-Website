import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Me") #  This pops up as a dialog box
def show_contact_form():
    contact_form()


col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image("./assets/Profile.jpg", width = 250)
with col2:
    st.title("Akindele Adebayo.", anchor = False)
    st.write("Senior Software Developer.")
    st.write("Founder, Matrax Systems and I.T. Services.")
    if st.button("Contact Me"):
        show_contact_form()

st.write("\n")
st.subheader("Experience and Qualifications", anchor = False)
st.write(
    """
    - 5+ years experience as a software developer with project based experience.
    - Strong and Hands-on experience in Javascript and Python.
    - Excellent team-player and displaying a strong sense of initiative on tasks.
    - Good understanding of data representation, interpretation and analysis.
    """
)

st.write("\n")
st.subheader("Hard Skills", anchor = False)
st.write(
    """
    - Skillful in Web development using HTML/CSS, JavaScript/React Js, Node Js, Express Js, Python-Streamit.
    - Skillfull in Blockchain/DApp development using Solidity, Ethers, Truffle, Hardhat, Ethereum.
    - Mobile and Desktop App development using React Native and Python(PyQt5 and Kivy).
    - Data Analysis skills using Numpy, Pandas and SQL.
    """
)