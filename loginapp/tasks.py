from celery import Celery
# import yagmail

# app = Celery()
# app.config_from_object('celeryconfig')

app = Celery(
    'tasks',
        backend='redis://localhost',
        broker='redis://localhost',
)

# app.autodiscover_tasks()

@app.task
def add(x, y):
    return x + y


# @app.task
# def sendEmail(email):
#     receiver = "peryagtest@gmail.com"
#     body = "Hello there from Yagmail"
#     password = input("Type your password and press enter: peryag888")

#     yag = yagmail.SMTP("peryagtest@gmail.com")
#     yag.send(
#         to=receiver,
#         subject="Yagmail test",
#         contents=body, 
#     )
