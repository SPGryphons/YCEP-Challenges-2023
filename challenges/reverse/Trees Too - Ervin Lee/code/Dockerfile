FROM python:3
WORKDIR /tree2
COPY solution.py .
COPY flag.txt .

RUN pip install binarytree
EXPOSE 3004
CMD [ "python3", "./solution.py" ]