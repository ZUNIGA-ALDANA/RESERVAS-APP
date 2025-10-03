FROM python:3.11-slim

WORKDIR /reservas-app

COPY templates/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY reservas-app.py .

EXPOSE 5000

CMD ["python", "reservas-app.py"]
