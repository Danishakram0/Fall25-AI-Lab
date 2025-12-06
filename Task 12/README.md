# Diabetes Prediction System

A Flask web application for predicting diabetes risk using machine learning.

## Features

- User-friendly web interface for inputting patient data
- Real-time diabetes prediction using SVM model
- Responsive design that works on desktop and mobile
- Input validation and error handling
- RESTful API endpoint for programmatic access

## Installation

1. Install required packages:
```bash
pip install flask scikit-learn pandas numpy
```

2. Make sure you have the trained model file (`model_svc.pkl`) in the project directory.

## Usage

### Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Using the Web Interface

1. Open your browser and navigate to `http://localhost:5000`
2. Fill in the patient information:
   - Pregnancies: Number of times pregnant
   - Glucose Level: Plasma glucose concentration (mg/dL)
   - Blood Pressure: Diastolic blood pressure (mm Hg)
   - Skin Thickness: Triceps skin fold thickness (mm)
   - Insulin: 2-hour serum insulin (μU/mL)
   - Diabetes Pedigree Function: Genetic influence score
3. Click "Predict Diabetes Risk"
4. View the prediction result

### Using the API

Send a POST request to `/api/predict` with JSON data:

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "pregnancies": 6,
    "glucose": 148,
    "blood_pressure": 72,
    "skin_thickness": 35,
    "insulin": 0,
    "diabetes_pedigree": 0.627
  }'
```

## Project Structure

```
Task 12/
├── app.py                  # Flask application
├── model_svc.pkl          # Trained SVM model
├── diabetes.csv           # Dataset
├── task11.ipynb           # Training notebook
├── templates/
│   └── index.html         # Web interface
├── static/
│   └── style.css          # Styling
└── README.md              # Documentation
```

## Model Information

The application uses a Support Vector Machine (SVM) classifier trained on the diabetes dataset. The model predicts whether a patient is likely to have diabetes based on various medical measurements.

## Input Features

1. **Pregnancies**: Number of times pregnant (0-17)
2. **Glucose**: Plasma glucose concentration (70-200 mg/dL)
3. **Blood Pressure**: Diastolic blood pressure (60-120 mm Hg)
4. **Skin Thickness**: Triceps skin fold thickness (10-50 mm)
5. **Insulin**: 2-hour serum insulin (0-846 μU/mL)
6. **Diabetes Pedigree Function**: Genetic influence (0.078-2.42)

## Output

- **Prediction**: Diabetic or Non-Diabetic
- **Confidence**: Prediction confidence percentage (if available)
- **Input Summary**: Review of submitted values
