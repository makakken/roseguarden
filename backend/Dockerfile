FROM python:3
ADD . /backend
WORKDIR /backend

ENV FLASK_ENV=development

RUN pip install -r requirements.txt
CMD flask run --host=0.0.0.0