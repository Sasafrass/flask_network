"""For all python email related purposes."""
from threading import Thread

from flask import render_template, current_app
from flask_mail import Message

from app import mail


def send_async_email(app: app, msg: str):
    """Send an asynchronous email.

    Args:
        app: Our application instance.
        msg: Message to send over our app.
    """
    with app.app_context():
        mail.send(msg)


def send_email(
    subject: str, sender: str, recipients: list, text_body: str, html_body: str
):
    """Send an email.

    Args:
        subject: Title of your email.
        sender: Address from which to send the email.
        recipients: List of people receiving this email.
        text_body: Text in the body of your email.
        html_body: HTML formatted text in your email.
    """
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body

    # Current_app is a context-aware variable, with no value in a different thread!
    # Thus this requires the use of get_current_object()
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
