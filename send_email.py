import smtplib , ssl
import os
from dotenv import load_dotenv

def send_email(email_message):
    email, password = None, None
    
    try:
        load_dotenv(override=True)
    except:
        print("No '.env' file exists")
    
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("EMAIL")
    
    if email and password:
        host = "smtp.gmail.com"
        port = 465

        context = ssl.create_default_context()

        # Format to use subject on the email: Put backslash before 'Subject:' keyword
        # message = """\
        # Subject: Contact Me
        # Hi!
        # How are you?
        # Bye!
        # """
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(email, password)
            server.sendmail(email, receiver, email_message)
        return True
    else:
        return False