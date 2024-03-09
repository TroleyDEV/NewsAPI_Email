import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "mateusz.mlynarczyk82@gmail.com"
    password = "PASSWORD_PORTFOLIO_APP"

    receiver = "mateusz.mlynarczyk82@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
