## Weather API with Flask, Redis, and Flask-Limiter
Solution to the roadmap.sh project Weather API https://roadmap.sh/projects/weather-api-wrapper-service

### Project Task

Build a weather API that fetches and returns weather data.

### Features

- Python 3.12+ support
- Flask
- Redis
- Dockerized
- Rate Limiting with Flask-Limiter
- Formatting using black

### Installation Guide

You need following to run this project:

- Python 3.12
- [Docker with Docker Compose](https://docs.docker.com/compose/install/)
- [Poetry](https://python-poetry.org/docs/#installation)

Once you have installed the above and have cloned the repository, you can follow the following steps to get the project up and running:

1. Copy the `.env.example` file to `.env` and update the values as per your needs.

2. Run the Flask API and redis containers:

```bash
docker-compose up -d
```

The server should now be running on `http://localhost:5000`

## Usage

Example:
```
curl "http://127.0.0.1:5000/weather?location=Milan&start=2024-12-25&end=2024-12-31"
```
location (required) – is the address, partial address or latitude,longitude location for which to retrieve weather data. You can also use US ZIP Codes. If you would like to submit multiple locations in the same request, consider our Multiple Location Timeline Weather API.

date1 (optional) – is the start date for which to retrieve weather data. If a date2 value is also given, then it represents the first date for which to retrieve weather data. If no date2 is specified then weather data for a single day is retrieved, and that date is specified in date1. All dates and times are in local time of the location specified. Dates should be in the format yyyy-MM-dd. For example 2020-10-19 for October 19th, 2020 or 2017-02-03 for February 3rd, 2017.

Instead of an exact date, you can specify a dynamic date period. See below for more details. You may also supply the in “UNIX time”. In this case provide the number of seconds since 1st January 1970 UTC. For example 1612137600 for Midnight on 1st February 2021.

You can also request the information for a specific time for a single date by including time into the date1 field using the format yyyy-MM-ddTHH:mm:ss. For example 2020-10-19T13:00:00.

The results are returned in the ‘currentConditions’ field and are truncated to the hour requested (i.e. 2020-10-19T13:59:00 will return data at 2020-10-19T13:00:00).

date2 (optional) – is the end date for which to retrieve weather data. This value may only be used when a date1 value is given. When both date1 and date2 values are given, the query is inclusive of date2 and the weather data request period will end on midnight of the date2 value. All dates and times are in local time of the specified location and should be in the format yyyy-MM-dd.

When no date1 or date2 is specified, the request will retrieve the forecast at the requested location for the next 15 days.

## Feedback

Feedbacks are higly welcome. If you have feedback on the solution, open an issue or a pull request.

Make sure to leave an upvote if you liked this solution.
