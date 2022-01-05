FROM python:2.7
LABEL maintainer="Fadwa Fuad"

WORKDIR /app
COPY ./techtrends /app

RUN pip install -r requirements.txt
RUN python init_db.py
EXPOSE 3111

# command to run on container start
CMD [ "python", "app.py" ]
