import json

import requests
from flask import Blueprint, current_app, jsonify, request
from redis import RedisError
from requests import ConnectionError, HTTPError

from src.db import redis_client

base = Blueprint("base", __name__)


@base.route("/", methods=["GET"])
def status():
    return jsonify({"status": "running"})


@base.route("/weather", methods=["GET"])
def get_weather():
    # Get query parameters
    location = request.args.get("location", "")
    start_date = request.args.get("start", "")
    end_date = request.args.get("end", "")

    # Build redis key
    redis_key = f"{location}_{start_date}_{end_date}"

    # Return cached value, if any
    try:
        value = redis_client.get(redis_key)
        if value:
            return jsonify(json.loads(value))
    except RedisError as e:
        return jsonify({"error": "Redis Error", "message": str(e)}), 500

    # Retrieve parameters from .env file
    api_key = current_app.config.get("VISUALCROSSING_API_KEY", None)
    cache_expiry = current_app.config.get("CACHE_EXPIRY_SECONDS", 43200)  # 12 hours

    try:
        # Execute request to 3rd party weather API
        response = requests.get(
            f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}",
            params={"key": api_key},
            timeout=10,
        )
        response.raise_for_status()

        # Cache response data
        redis_client.set(redis_key, response.text, ex=cache_expiry)

        return jsonify(response.json())
    except HTTPError as e:
        status_code = e.response.status_code
        error_message = e.response.text
        return jsonify({"error": status_code, "message": error_message}), status_code
    except ConnectionError as e:
        return jsonify({"error": "Service Unavailable", "message": str(e)}), 503
    except Exception as e:
        return jsonify({"error": "Unexpected Error", "message": str(e)}), 500
