FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 3000

CMD ["python", "app.py"]
CMD ["gunicorn", "credit_model:app", "--bind=0.0.0:3000", "-w", "4"]
