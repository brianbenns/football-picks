FROM python:2.7
RUN pip install flask
COPY . /app
WORKDIR /app
CMD python app_start.py
EXPOSE 8080