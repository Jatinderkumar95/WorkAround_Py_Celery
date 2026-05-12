from celery import Celery


app = Celery("run",broker="redis://localhost:6379/0")

print("1. I am about to 'send' an email...")

# We use send_task and refer to the task by its string name
app.send_task(
    'tasks.send_email_task', 
    args=["boss@company.com", "The report is ready"],
    kwargs={}
)

print("Task sent to Redis. Producer is done.")
