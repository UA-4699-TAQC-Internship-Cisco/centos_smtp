import smtplib
import os
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT"))
from_addr = os.getenv("FROM_ADDR")
to_addr = os.getenv("TO_ADDR")


def send_email(smtp_server, smtp_port, from_addr, to_addr, subject, body):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        server.ehlo()
        server.sendmail(from_addr, to_addr, msg.as_string())
        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print("SMTP error occurred: %s" % str(e))
    except Exception as e:
        print("Error occurred: %s" % str(e))
    finally:
        try:
            server.quit()
        except:
            pass


if __name__ == "__main__":
    send_email(
        smtp_server=os.getenv("SMTP_SERVER"),
        smtp_port=int(os.getenv("SMTP_PORT")),
        from_addr=os.getenv("FROM_ADDR"),
        to_addr=os.getenv("TO_ADDR"),
        subject="Test Subject email from PyCharm",
        body="This is a test email text sent from PyCharm. 07.27"
    )
