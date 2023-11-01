# Sends notification to desktop
# Notifications need to be enabled on Windows in order to work

# import necessary
import time
from plyer import notification

if __name__ == '__main__':
    # call notification class
    notification.notify(
        title="NOTIFICATION",
        message="I AM NOTIFYING YOU",

        # time to display
        timeout=5
    )
    # pause
    time.sleep(7)