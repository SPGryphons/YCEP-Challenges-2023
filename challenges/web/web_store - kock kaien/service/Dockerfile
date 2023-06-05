FROM python:3.7.13-alpine3.16

COPY app.py .
COPY index.html . 
COPY login.html .
COPY static /static
COPY init.sql .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]