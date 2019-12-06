from celery import Celery
from celery import shared_task
from time import sleep
import yagmail

# app = Celery()
# app.config_from_object('celeryconfig')

app = Celery(
    'tasks',
        backend='redis://localhost',
        broker='redis://localhost',
)

# @shared_task
# def add(x, y):
#     return x + y

# @shared_task
# def sleepy(duration):
#     sleep(duration)
#     return None


@shared_task
def send(email, subject, body):
    receiver = email
    subject = subject
    body = body
    password = "peryag888"
    # password = input("Type your password and press enter: peryag888")

    yag = yagmail.SMTP("peryagtest@gmail.com")
    yag.send(
        to=receiver,
        subject=subject,
        contents=body, 
    )












# @shared_task
# def sendEmail(email, body):
#     receiver = "peryagtest@gmail.com"
#     body = "Hello there from Yagmail"
#     password = input("Type your password and press enter: peryag888")

#     yag = yagmail.SMTP("peryagtest@gmail.com")
#     yag.send(
#         to=receiver,
#         subject="Yagmail test",
#         contents=body, 
#     )