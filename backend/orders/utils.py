# import africastalking
# import os
# import dotenv

# dotenv.load_dotenv()

# africastalking.initialize(os.getenv("AFRICASTALKING_USERNAME"), os.getenv("AFRICASTALKING_API_KEY"))
# sms = africastalking.SMS

# def send_order_notification(phone_number, message):
#     sms.send(message, [phone_number])
import africastalking
import os
import dotenv

dotenv.load_dotenv()

# print("Username:", os.getenv("AFRICASTALKING_USERNAME"))  # Should print 'sandbox'
# print("API Key:", os.getenv("AFRICASTALKING_API_KEY"))

username = os.getenv("AFRICASTALKING_USERNAME", "sandbox")
api_key = os.getenv("AFRICASTALKING_API_KEY")


print(f"Using Username: {username}, API Key: {'HIDDEN' if api_key else 'MISSING'}")

# Initialize Africa's Talking
africastalking.initialize(username, api_key)
sms = africastalking.SMS

def send_order_notification(phone_number, message):
    try:
        response = sms.send(message, [phone_number])
        print("SMS Sent Successfully:", response)
    except Exception as e:
        print("Error Sending SMS:", str(e))

# Test sending
send_order_notification("+254712345678", "Your order has been placed successfully!")
