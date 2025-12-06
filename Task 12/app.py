from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = 'model_svc.pkl'
model = None

try:
    if os.path.exists(MODEL_PATH):
        model = pickle.load(open(MODEL_PATH, 'rb'))
        print("Model loaded successfully!")
    else:
        print("Warning: Model file not found. Please train the model first.")
except Exception as e:
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({
                'error': 'Model not loaded. Please train the model first.',
                'success': False
            })

        # Get data from form
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        diabetes_pedigree = float(request.form['diabetes_pedigree'])
        
        # Create feature array (excluding Diabetes which is the target)
        features = np.array([[pregnancies, glucose, blood_pressure, 
                            skin_thickness, insulin, diabetes_pedigree]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Get prediction probability if available
        try:
            prediction_proba = model.predict_proba(features)[0]
            confidence = max(prediction_proba) * 100
        except:
            confidence = None
        
        result = {
            'prediction': int(prediction),
            'prediction_text': 'Diabetic' if prediction == 1 else 'Non-Diabetic',
            'confidence': f"{confidence:.2f}%" if confidence else "N/A",
            'success': True
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        })

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        if model is None:
            return jsonify({
                'error': 'Model not loaded',
                'success': False
            })
        
        data = request.get_json()
        features = np.array([[
            data['pregnancies'],
            data['glucose'],
            data['blood_pressure'],
            data['skin_thickness'],
            data['insulin'],
            data['diabetes_pedigree']
        ]])
        
        prediction = model.predict(features)[0]
        
        return jsonify({
            'prediction': int(prediction),
            'prediction_text': 'Diabetic' if prediction == 1 else 'Non-Diabetic',
            'success': True
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
