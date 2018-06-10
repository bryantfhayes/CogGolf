FROM python:2

COPY app.py /
COPY coggolf.py /
COPY database.py /
COPY challenges.py /

COPY data.json /
COPY words.txt /

COPY challenges/ /challenges/
COPY templates/ /templates/
COPY static/ /static/

RUN pip install requests
RUN pip install flask
RUN pip install six

CMD [ "python", "./app.py" ]
