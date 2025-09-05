import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(workflow_name, repo_name, workflow_run_id):
    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECIEVER_EMAIL")
    pswd = os.getenv("APP_PASSWORD")

    subject = f"Workflow {workflow_name} success for the repository {repo_name}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email  
    message["Subject"] = subject

    body = f"""
Congratulations, {workflow_name} successfully executed for the repository {repo_name}.

More details:
Workflow ID: {workflow_run_id}.

This is a system generated mail by Sadique's Ubuntu machine.
"""

    message.attach(MIMEText(body,'plain'))

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender_email,pswd)
        server.sendmail(sender_email,receiver_email,message.as_string())
        print(f"Email sent successfully to {receiver_email}")

send_email(os.getenv('WORKFLOW_NAME'),os.getenv('REPO_NAME'),os.getenv('WORKFLOW_RUN_ID'))