import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(workflow_name, repo_name, workflow_run_id):
    sender_email = os.getenv("SEN_MA")
    receiver_email = os.getenv("REC_MA")
    PSWD = os.getenv("APP_PASS")

    subject = f"Workflow {workflow_name} failed for the repository {repo_name}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    body = f"""
    Hey, the workflow {workflow_name} failed for the repository {repo_name}.
    Kindly Check.

    More details:
    Workflow ID: {workflow_run_id}.

    This is a system generated mail don't reply to it.
    """

    message.attach(MIMEText(body,'plain'))

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender_email,PSWD)
        server.sendmail(sender_email,receiver_email,message.as_string())
        print(f"Email sent successfully to {receiver_email}")

send_email(os.getenv('WORKFLOW_NAME'),os.getenv('REPO_NAME'),os.getenv('WORKFLOW_RUN_ID'))