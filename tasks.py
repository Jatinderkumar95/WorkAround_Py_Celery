# you need a separate terminal to run the Worker. This process sits and waits for tasks to appear in broker.
# run this command: celery -A tasks worker --loglevel=info


from celery import Celery
import time

# first param takes current module name
# When you run Redis on WSL, Windows hasn't exposed its localhost:6379 directly. Use below PS command to connect window's ip& port to the WSL IP & port address instead:
# 1. Find your WSL IP address (run in WSL terminal): ip addr show eth0 | grep "inet "
# 2  netsh interface portproxy add v4tov4 listenport=6379 listenaddress=127.0.0.1 connectport=6379 connectaddress=<WSL_IP>
app = Celery('tasks', broker='redis://localhost:6379/0')

# Change your Celery configuration to use the solo pool instead of the default prefork pool
app.conf.worker_pool = 'solo'

# name of task
@app.task
def send_email_task(recipient_email:str,message:str):
    print(f"DEBUG: Starting to send email to {recipient_email}")
    # Simulate the delay of connecting to an email server
    time.sleep(5)
    print(f"DEBUG: Email successfully sent to {recipient_email}!")
    return f"Email sent to {recipient_email}"

@app.task
def parse_document(doc_name:str):
    print(f"----- Task 1 : Parsing {doc_name} ---")
    # Simulating PDF reading
    time.sleep(5)
    extracted_text = f"Content of {doc_name}: The AI revolution is here."
    return extracted_text

@app.task
def summarize_text(text):
    print(f"--- Task 2: AI Summarizing text ---")
    time.sleep(3) # Simulating LLM call
    summary = f"SUMMARY -> {text[:20]}..."
    return summary

@app.task
def index_in_vector_db(summary):
    print(f"--- Task 3: Storing in Vector DB ---")
    time.sleep(1) # Simulating DB write
    return f"SUCCESS: '{summary}' has been indexed."