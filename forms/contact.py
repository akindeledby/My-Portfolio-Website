import streamlit as st
import re
import requests

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            #st.success("Message succesfully sent!")
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later")
                st.stop()

            if not name:
                st.error("Please provide your name.")
                st.stop()

            if not email:
                st.error("Please provide your email address.")
                st.stop()

            if not message:
                st.error("Please provide a mmessage or feedback")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide a valid emial address")
                st.stop()

            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json = data)

            if response.status_code == 200:
                st.success("Your message has been submitted!")
            else:
                st.error("There was an error sending your message")




# After the user/contact enters the necessary information, we can use various tools to send the message directly to an email address.
# Or simply add/send it to a database. To do this, we can use "WEBHOOK". 
# A Webhook is an HTTP request, triggered by an event in a source system and sent to a destination system, ofter with a payload of data. It is a method of augmenting or altering the behavior of a web page or web application.
# We may also need to do some validations and checks to ensure that the user/contact enters infarmation in the form in the required format.
# An online resources we can use as our webhook provider is Pabbly - www.connect.pabbly.com, signup, and from the dashboard, click on workflow and get /copy the Webhook UR and paste it at the variable.
# We can also use other methods like connecting an email address such as gmail, or google sheet, etc.
# Also we can creare a .gitignore file and put the secret.toml file
