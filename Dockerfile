# Build Stage
FROM python:3.7-alpine as builder
RUN apk add --update python3-dev gcc build-base
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install --user -r requirements.txt
COPY . .

FROM python:3.7-alpine as app
ENV FLASK_APP pytinifier.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY --from=builder /root/.local /root/.local
COPY --from=builder /code/ /code/
WORKDIR /code
ENV PATH=/root/.local/bin:$PATH
CMD ["flask", "run"]
