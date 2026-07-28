import time
from plyer import notification

while True:
    print("Drink water..............!")
    notification.notify(title="Drink Water Reminder", message="Pani  pile lo bhai", timeout=5)
    time.sleep(60*60)