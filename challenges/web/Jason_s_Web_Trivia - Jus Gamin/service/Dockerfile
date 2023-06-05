FROM debian:stable

COPY app .

RUN apt update && apt install python3 -y

RUN apt install python3-pip -y

RUN pip3 install -r requirements.txt

EXPOSE 1337

ENV PYTHONDONTWRITEBYTECODE=1

CMD ["python3", "app.py"]