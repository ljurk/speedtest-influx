FROM python:3.8-alpine

WORKDIR /opt/speedtest

#copy requirements first, so that the package installation will be cached
COPY requirements.txt .
#RUN apk add --no-cache g++ gcc unixodbc-dev python-dev git freetds-dev \
    RUN pip install --no-cache-dir -r requirements.txt 
#    && apk del git g++ gcc

#copy all files to workdir
COPY test.py .

# define default environment variables
ENV INFLUX_HOST="" \
    INFLUX_DB="" \
    INFLUX_USER="" \
    INFLUX_PASSWORD="" \
    INFLUX_PORT=8086

CMD ["python", "-u", "test.py"]
