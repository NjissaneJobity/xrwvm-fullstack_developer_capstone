import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlencode

# Load environment variables from .env file
load_dotenv()

# Define backend and sentiment analyzer URLs
backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    # Construct query parameters from kwargs
    if kwargs:
        params = urlencode(kwargs)  
        request_url = f"{backend_url}{endpoint}?{params}"
    else:
        request_url = f"{backend_url}{endpoint}"

    print(f"GET from {request_url}")

    try:
        # Perform the GET request
        response = requests.get(request_url)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None


def analyze_review_sentiments(text):
    request_url = f"{sentiment_analyzer_url}analyze/{text}"

    try:
        # Perform the GET request
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None


def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"

    try:
        # Perform the POST request with the provided data
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status() 
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Network exception occurred: {err}")
        return None
