import os
import time
import speedtest
from influxdb import InfluxDBClient

influx = InfluxDBClient(host=os.getenv('INFLUX_HOST'),
                        username=os.getenv('INFLUX_USER'),
                        password=os.getenv('INFLUX_PASSWORD'),
                        database=os.getenv('INFLUX_DB'),
                        port=os.getenv('INFLUX_PORT'))

# create database if it doesn't exist
influx.create_database(os.getenv('INFLUX_DB'))


def sendInflux(download, upload, ping):
    data = [{"measurement": "networkspeed",
             "tags": {
                 "host": os.uname()[1]
             },
             "fields": {
                 "download": download,
                 "upload": upload,
                 "ping": ping
             }}]
    influx.write_points(data)

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


if __name__ == '__main__':
    print("start speedtest")
    while True:
        down, up, ping = test()
        print('Download: {:.2f} Kb/s'.format(down / 1024))
        print('Upload: {:.2f} Kb/s'.format(up / 1024))
        print('Ping: {}'.format(ping))
        sendInflux(down, up, ping)
