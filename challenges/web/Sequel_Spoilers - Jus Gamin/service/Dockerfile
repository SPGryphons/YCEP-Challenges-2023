FROM python:3.11-slim-bullseye

COPY app .

RUN pip3 install -r requirements.txt --

EXPOSE 1337

ENV PYTHONDONTWRITEBYTECODE=1

CMD ["python3", "app.py"]
