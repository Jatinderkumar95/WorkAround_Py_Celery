from celery import Celery,chain
from tasks import summarize_text,index_in_vector_db,parse_document

# app = Celery("run",broker="redis://localhost:6379/0")

print("1. I am about to 'send' an email...")

# We use send_task and refer to the task by its string name
# app.send_task(
#     'tasks.send_email_task', 
#     args=["boss@company.com", "The report is ready"],
#     kwargs={}
# )

#A chain passes the output of Task 1 as the first argument to Task 2, and so on.
workflow = chain(
    # .s() stands for Signature. It’s like a "ready-to-go" task that hasn't been fired yet.
    parse_document.s("knowledge.pdf"),
    summarize_text.s(),
    index_in_vector_db.s()
)
rsult = workflow.apply_async()
print("Task sent to Redis. Producer is done.")
