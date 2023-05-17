FROM python:3
WORKDIR /tree3
COPY solution.py .
COPY flag.txt .

RUN pip install binarytree
EXPOSE 3005
CMD [ "python", "./solution.py" ]