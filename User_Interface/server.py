from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('customer_segmentation_model.pkl')

@app.route('/')
def home():
    return 'Welcome to Customer Segmentation Model'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        cluster = model.predict(features)[0]
        
        return jsonify({'cluster': int(cluster)})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)
    