# you need a separate terminal to run the Worker. This process sits and waits for tasks to appear in broker.
# run this command: celery -A tasks_copy worker --loglevel=info


from celery import Celery
import time

# first param takes current module name
# When you run Redis on WSL, Windows hasn't exposed its localhost:6379 directly. Use below PS command to connect window's ip& port to the WSL IP & port address instead:
# 1. Find your WSL IP address (run in WSL terminal): ip addr show eth0 | grep "inet "
# 2  netsh interface portproxy add v4tov4 listenport=6379 listenaddress=127.0.0.1 connectport=6379 connectaddress=<WSL_IP>
app = Celery('tasks_copy', broker='redis://localhost:6379/0')

# Change your Celery configuration to use the solo pool instead of the default prefork pool
app.conf.worker_pool = 'solo'

@app.task
def send_email_task(recipient_email:str,message:str):
    print(f"DEBUG: Starting to send email to {recipient_email}")
    # Simulate the delay of connecting to an email server
    time.sleep(5)
    print(f"DEBUG: Email successfully sent to {recipient_email}!")
    return f"Email sent to {recipient_email}"