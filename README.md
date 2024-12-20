# Driver Behavior Prediction API

This project provides a RESTful API to predict driver behavior based on accelerometer and gyroscope data. The API uses a pre-trained machine learning model to classify behavior into categories such as `AGGRESSIVE`, `NORMAL`, and `SLOW`.

## Features
- Accepts sensor data (accelerometer, gyroscope, and timestamp) via a POST request.
- Predicts driver behavior using a machine learning model.
- Provides interactive API documentation using Swagger.

## Requirements
- Python 3.8 or higher
- Flask
- Flask-CORS
- Flask-Compress
- Flasgger
- joblib
- numpy

## Access Backend Using 
```bash
  python API/app.py
```

## Then Open Swagger UI and Try Backend

```bash
  http://127.0.0.1:8890/apidocs
```




