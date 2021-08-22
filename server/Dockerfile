FROM python:3.9.6

WORKDIR /usr/src

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000
# ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]