# Student Comfort Prediction in the Kendeda Building  
*Post-Occupancy Analysis Using IEQ Sensor Data and Machine Learning*  
(Reference: Undergraduate Research Symposium Poster)  
:contentReference[oaicite:0]{index=0}

## Overview
This project investigates how Indoor Environmental Quality (IEQ) conditions influence student comfort in the Kendeda Building at Georgia Tech. By combining subjective survey feedback and objective IEQ sensor data, we evaluate whether machine learning models can predict indoor conditions—and eventually occupant comfort—based on real-time environmental measurements.

## Research Goals
- Assess how measured IEQ factors (temperature, humidity, lighting, noise, particulate matter) relate to perceived student comfort.  
- Build time-series prediction models for IEQ variables to support real-time comfort forecasting.  
- Lay the foundation for connecting model predictions to student satisfaction trends.

## Data Collection
### Subjective Survey Data
- Adapted CBE survey distributed via QR-coded fliers.
- 145+ student responses collected.
- Satisfaction ratings recorded across thermal, humidity, lighting, air quality, and acoustic comfort.

### Objective Sensor Data
- Atmocube IoT devices installed across classrooms.
- Continuous measurements of temperature, humidity, PM, sound, and light.
- Data logged from Fall 2024 onward.

## Observational Trends
### Humidity
- Higher measured humidity is associated with higher comfort satisfaction.  
- Indicates students prefer mid-range, stable humidity levels.

### Temperature
- Inverse relationship between measured temperature and perceived comfort.  
- Students tend to prefer cooler indoor temperatures.

## Data Processing
- Missing values handled and features normalized using MinMaxScaler.
- Time-series transformation: input windows of 3 steps predict the next step.
- Train/test split: 80% / 20%.
- All processing performed in Python and visualized with Matplotlib.

## Machine Learning Models
Two models were evaluated for temperature prediction in Classroom 230:

### LSTM
- Epochs: 50  
- Batch size: 16  
- Learning rate: 0.005  
- Captures long-term dependencies, suitable for IEQ time series.

### Random Forest
- n_estimators: 200  
- max_depth: 10  
- Handles non-linear structure well; trains quickly.

## Model Performance
| Model | MSE | RMSE | R² |
|-------|------|--------|--------|
| LSTM | 0.02 | 0.12 | -5.69 |
| Random Forest | 0.01 | 0.11 | -4.25 |

Random Forest outperformed LSTM with slightly lower error metrics.  
Negative R² values indicate insufficient data or missing features, suggesting limited learnability under current dataset conditions.

## Interpretation
- IEQ sensor data alone was not sufficient for strong predictive performance.  
- Additional features, longer time-series sequences, and richer contextual data may improve model accuracy.  
- Once reliable IEQ prediction is achieved, the next step is training models to estimate student comfort directly from predicted IEQ trends.

## Future Work
- Expand sample size and duration of sensing.  
- Add more features (occupancy, weather, schedules).  
- Refine hyperparameters and explore hybrid or multivariate forecasting models.  
- Develop models that translate predicted IEQ conditions into satisfaction-level forecasts.

## Acknowledgements
This work was conducted in the Workplace Ecology Lab at Georgia Tech.  
Special thanks to Dr. Yang Eunhwa, Abdurrahaman Baru, and lab members for guidance and support.

