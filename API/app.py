from flask import Flask, request, jsonify
import joblib
import numpy as np 
import warnings
import threading
from flask_cors import CORS
from flask_compress import Compress
from flasgger import Swagger, swag_from


warnings.filterwarnings("ignore")

app = Flask(__name__)

CORS(app)

Compress(app)

swagger = Swagger(app)

# Initialize global variables
model = None

#____________________________________________________________
# Lock for thread safety
model_lock = threading.Lock()
count = 0
#____________________________________________________________
def initialize_models():
    """
    Initialize machine learning models.
    """
    global count
    count += 1
    print("Initializing models for the {} time".format(count))
    global model
    with model_lock:

        if model is None:
            try : 
                model = joblib.load('ML Model\model.pkl') 

            except FileNotFoundError:
                raise Exception("Model file not found. Please check the file path.")




initialize_models()

# Initialize Flask app
@app.route('/predict_driver_behavior', methods=['POST'])
@swag_from({
    'tags': ['Driver Behavior Prediction'],
    'parameters': [
        {
            'name': 'acc_x',
            'in': 'formData',
            'type': 'number',
            'required': True,
            'description': 'Accelerometer data along the x-axis'
        },
        {
            'name': 'acc_y',
            'in': 'formData',
            'type': 'number',
            'required': True,
            'description': 'Accelerometer data along the y-axis'
        },
        {
            'name': 'acc_z',
            'in': 'formData',
            'type': 'number',
            'required': True,
            'description': 'Accelerometer data along the z-axis'
        },
        {
            'name': 'giro_x',
            'in': 'formData',
            'type': 'number',
            'required': True,
            'description': 'Gyroscope data along the x-axis'
        },
        {
            'name': 'giro_y',
            'in': 'formData',
            'type': 'number',
            'required': True,
            'description': 'Gyroscope data along the y-axis'
        },
        {
            'name': 'giro_z',
            'in': 'formData',
            'type': 'number',
            'required': True,
            'description': 'Gyroscope data along the z-axis'
        },
        {
            'name': 'timestamp',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': 'Timestamp of the sensor data'
        }
    ],
    'responses': {
        200: {
            'description': 'Prediction results',
            'examples': {
                'application/json': {
                    'message': 'Data is predicted successfully',
                    'input_data': {
                        'acc_x': 0.1,
                        'acc_y': 0.2,
                        'acc_z': 0.3,
                        'giro_x': 0.4,
                        'giro_y': 0.5,
                        'giro_z': 0.6,
                        'timestamp': 1234567890
                    },
                    'prediction_label': 2,
                    'prediction_class': 'NORMAL'
                }
            }
        },
        400: {
            'description': 'Invalid input or missing fields'
        }
    }
})
def handle_sensor_data():
    try:
        data = request.form
        if not data:
            return jsonify({'mess': "No data provided" }) , 400

        # Extract data from form
        acc_x = float(data.get('acc_x'))
        acc_y = float(data.get('acc_y'))
        acc_z = float(data.get('acc_z'))
        giro_x = float(data.get('giro_x'))
        giro_y = float(data.get('giro_y'))
        giro_z = float(data.get('giro_z'))
        timestamp = int(data.get('timestamp'))   

        # Combine into a dictionary for processing
        input_data = {
            "acc_x": acc_x,
            "acc_y": acc_y,
            "acc_z": acc_z,
            "giro_x": giro_x,
            "giro_y": giro_y,
            "giro_z": giro_z,
            "timestamp" : timestamp
        }

        # Combine the data into a single feature vector
        raw_features = np.array([[acc_x, acc_y, acc_z, giro_x, giro_y, giro_z,timestamp]])

        prediction_numeric = model.predict(raw_features)[0]

        # Map numeric prediction to corresponding label
        label_mapping = {1: "AGGRESSIVE", 2: "NORMAL", 3: "SLOW"}

        prediction_label = label_mapping.get(prediction_numeric, "UNKNOWN")
        # Example response (you can process and predict here)
        return jsonify({
            "message": "Data is predicterd successfully",
            "input_data": input_data,
            "prediction_label" : int(prediction_numeric) , 
            "prediction_class" : prediction_label 
        }) , 200
    
    except (TypeError, ValueError):
        return jsonify({'mess': "All fields are required and must be valid numbers"}), 400
 
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port = "8890")
