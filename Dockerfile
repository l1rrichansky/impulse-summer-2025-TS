FROM python:3.10

RUN mkdir /ruapi
COPY ruapi /ruapi

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /ruapi

COPY start.sh /start.sh

ENTRYPOINT ["sh", "/start.sh"]