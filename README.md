# Web server project

This project contains a dockerized FastAPI web server for predicting house prices based on input features, using a pre-trained regression model. The application exposes the API endpoint `/predict` where users can send data to get a price prediction. A GitHub Action configuration to build, tag, deploy, and manage the docker image on a remote server is also provided.

## Running locally
To run the web server locally using Docker, follow these steps:
```sh
docker compose build
docker compose up -d
```

## Test the prediction API

Send a POST request to the `/predict` endpoint (locally: http://localhost:5000/predict) with a JSON body containing:
- `size` (float) for the size of the house.
- `nb_rooms` (int) for the number of rooms.
- `garden` (bool) whether the house has a garden.

Example:
```json
{
  "size": 100.0,
  "nb_rooms": 3,
  "garden": true
}
```