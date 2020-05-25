FROM python:3.7

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["celery", "worker", "-A", "app.workers.post_worker", "-l", "info", "-Q","test-queue", "-c", "1"]