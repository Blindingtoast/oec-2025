import smtplib
import os

from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
from twilio.rest import Client


# Load environment variables from .env file
load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = int(os.getenv("PORT"))

ACCOUNT_SSID = os.getenv("ACCOUNT_SSID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

def email_alert(subject: str, body: str, email_address: str) -> None:
    """
    Send an email alert.

    Args:
        subject (str): The subject of the email.
        body (str): The body content of the email.
        email_address (str): The recipient's email address.

    Example:
        email_alert("Test Subject", "Hello World", "btran0820003@gmail.com")
    """
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = email_address
    msg["from"] = USER  # Add the sender's email address

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(SMTP_SERVER, PORT) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(USER, PASSWORD)  # Login to the email server
            server.send_message(msg)  # Send the email
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")


def sms_alert(subject: str, body: str, phone_number: str) -> None:
    """
    Send an SMS alert.

    Args:
        subject (str): The subject of the SMS.
        body (str): The body content of the SMS.
        phone_number (str): The recipient's phone number.

    Example:
        sms_alert("Test Subject", "Hello World", "+16138544327")
    """
    client = Client(ACCOUNT_SSID, AUTH_TOKEN)
    message_to_send = f"{subject}\n\n{body}"
    message = client.messages.create(
        to=phone_number, from_=PHONE_NUMBER, body=message_to_send
    )
    print(message.sid)  # Print the message SID for confirmation


def send_alerts(subject: str, body: str, email_address: str, phone_number: str) -> None:
    """
    Send both email and SMS alerts.

    Args:
        subject (str): The subject of the alerts.
        body (str): The body content of the alerts.
        email_address (str): The recipient's email address.
        phone_number (str): The recipient's phone number.

    Example:
        send_alerts("Test Subject", "Hello World", "btran0820003@gmail.com", "+16138544327")
    """
    email_alert(subject, body, email_address)  # Send email alert
    sms_alert(subject, body, phone_number)  # Send SMS alert
