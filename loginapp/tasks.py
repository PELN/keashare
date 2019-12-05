from celery import Celery
import yagmail

app = Celery()
app.config_from_object('celeryconfig')

# @app.task
# def add(x, y):
#     return x + y

receiver = "peryagtest@gmail.com"
body = "Hello there from Yagmail"
password = input("Type your password and press enter: peryag888")

yag = yagmail.SMTP("peryagtest@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test",
    contents=body, 
)
