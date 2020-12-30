# speedtest-influx

this project monitors your networkspeed with the speedtest-cli and saves it inside a timeseries database

## quick start

start all the containers:
```
docker-compose up -d
```

to import the default dashboard visit http://localhost:8888/sources/0/dashboards and click on `Import Dashboard`, choose the `networkspeed.json` provided in this repository
