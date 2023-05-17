FROM python:3
WORKDIR /tree1
COPY solution.py .
COPY flag.txt .

RUN pip install binarytree
EXPOSE 3003
CMD [ "python3", "./solution.py" ]