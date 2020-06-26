FROM python:3.8-alpine
WORKDIR /n4flood
ADD . /n4flood
RUN pip install -r requirements.txt
CMD ["python","app.py"]

