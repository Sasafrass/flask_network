"""For all python email related purposes."""
from threading import Thread

from flask import render_template
from flask_mail import Message

from app import app, mail


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
    Thread(target=send_async_email, args=(app, msg)).start()


def send_password_reset_email(user):
    """Send an email to reset a user's password.

    Args:
        user: User object from database to send email to.
    """
    token = user.get_reset_password_token()
    send_email(
        "[Microblog] Reset Your Password",
        sender=app.config["ADMINS"][0],
        recipients=[user.email],
        text_body=render_template("email/reset_password.txt", user=user, token=token),
        html_body=render_template("email/reset_password.html", user=user, token=token),
    )
