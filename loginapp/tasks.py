from celery import Celery
from celery import shared_task
from time import sleep
import yagmail


app = Celery(
    'tasks',
        backend='redis://localhost',
        broker='redis://localhost',
)

@shared_task
def send(email, subject, body):
    receiver = email
    subject = subject
    body = body
    password = "peryag888"

    yag = yagmail.SMTP("peryagtest@gmail.com")
    yag.send(
        to=receiver,
        subject=subject,
        contents=body, 
    )



