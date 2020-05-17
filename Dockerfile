FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP pytinifier.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip; pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]