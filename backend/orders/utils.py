import africastalking
import os
import dotenv

dotenv.load_dotenv()

africastalking.initialize(os.getenv("AFRICASTALKING_USERNAME"), os.getenv("AFRICASTALKING_API_KEY"))
sms = africastalking.SMS

def send_order_notification(phone_number, message):
    sms.send(message, [phone_number])
