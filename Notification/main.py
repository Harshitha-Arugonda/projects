#working in terminal
import time
from plyer import notification
from datetime import datetime

def get_notification_details():
    title = input("Enter the notification title: ")
    message = input("Enter the notification message: ")
    notification_time = input("Enter the notification time (in HH:MM format): ")
    return title, message, notification_time

def calculate_delay(notification_time):
    current_time = datetime.now().strftime("%H:%M")
    current_hour, current_minute = map(int, current_time.split(':'))
    notification_hour, notification_minute = map(int, notification_time.split(':'))
    
    if notification_hour < current_hour or (notification_hour == current_hour and notification_minute < current_minute):
        # If the notification time has already passed for today, schedule it for the next day
        notification_hour += 24
    
    delay_hours = notification_hour - current_hour
    delay_minutes = notification_minute - current_minute
    delay_seconds = delay_hours * 3600 + delay_minutes * 60
    
    return delay_seconds

def send_notification(title, message, delay):
    time.sleep(delay)
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def main():
    title, message, notification_time = get_notification_details()
    delay = calculate_delay(notification_time)
    send_notification(title, message, delay)

if __name__ == '__main__':
    main()