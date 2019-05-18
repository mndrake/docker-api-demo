FROM python:3.7.3-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY credit_model /app/credit_model

EXPOSE 3000

CMD ["gunicorn", "credit_model:app", "--bind=0.0.0:3000", "-w", "4"]
