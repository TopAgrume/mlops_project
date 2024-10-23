FROM python:3.10.14-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
COPY ./web_server ./web_server
COPY ./pretrained_model ./pretrained_model

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "web_server/model_app.py"]
