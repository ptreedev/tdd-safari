FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py duty.py duty_controller.py ./
COPY templates/ ./templates/

ENV DUTIES_FILE=/data/duties.json
RUN mkdir -p /data

EXPOSE 5001

CMD ["python", "app.py"]