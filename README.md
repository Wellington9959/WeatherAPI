## WeatherAPI 
Weather API (https://roadmap.sh/projects/weather-api-wrapper-service)

### Project Task

Build a weather API that fetches and returns weather data.

### Features

- Python 3.12+ support
- Flask
- Redis
- Dockerized
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

## Feedback

Feedbacks are higly welcome. If you have feedback on the solution, open an issue or a pull request.
Make sure to leave an upvote if you liked this solution.
