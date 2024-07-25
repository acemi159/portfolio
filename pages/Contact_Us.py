import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="contact_me"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your Message")
    
    button = st.form_submit_button("Submit")
    
    message = f"""\
Subject: New email from Portfolio website.
Sent by {user_email}
    
{raw_message}
"""
    
    if button:
        if send_email(email_message=message):
            st.info("Your email was sent successfully.")
        else:
            st.info("Failed to send email.")
        
