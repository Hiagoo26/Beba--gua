import time
from plyer import notification

def lembrete():
    notification.notify(
        title = "Lembrete",
        message = "Vamo Beber água",
        timeout = 10
    )

while True:
    lembrete()
    time.sleep(1800)