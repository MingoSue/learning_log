from learning_log.celery import app

@app.task
def hello_world():
    print('Welcome to learning log')