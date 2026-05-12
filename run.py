from tasks import send_email_task

print("1. I am about to 'send' an email...")

# Cannot access attribute "delay" for class "FunctionType,  Attribute "delay" is unknown
send_email_task.delay('abc@gmail.com','message')