# Anomaly Detection and Event Prediction in Sensor Networks

## Project Overview

Our client, a leading provider of innovative sensor network solutions, aims to revolutionize sensor network technology. This project focuses on developing an Anomaly Detection and Event Prediction system for sensor networks. The goal is to create a system capable of detecting anomalies and predicting events in real-time, enabling proactive responses to potential issues, and significantly enhancing monitoring capabilities within sensor networks.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Goal](#project-goal)
- [Dataset Description](#dataset-description)
- [Feature Importance](#feature-importance)
- [Model Evaluation](#model-evaluation)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Goal

The goal of this project is to develop sophisticated algorithms to analyze sensor data, identify anomalies, and predict events. The system should offer actionable insights to optimize resource allocation and operational efficiency.

## Dataset Description

The dataset used in this project includes the following features:
1. Area
2. Sensing Range
3. Transmission Range
4. Number of Sensor Nodes
5. Target Variable: Number of Barriers

The dataset consists of 182 rows.

## Feature Importance

We used the Gradient Boosting model to determine the importance of each feature. The key findings are:
- **Number of Sensor Nodes**: Most critical for detecting anomalies and predicting events.
- **Transmission Range**: Significantly impacts the prediction accuracy.
- **Area**: Important factor influencing the model's performance.
- **Sensing Range**: Contributes to the model’s predictions but is less important compared to other features.

<!--![Feature Importance](path/to/your/image.png)-->

## Model Evaluation

We evaluated multiple models and their performance metrics are as follows:

- **Linear Regression**
  - Training MSE: 467.2886
  - Testing MSE: 634.1047
  - Training R2: 0.8875
  - Testing R2: 0.8500

- **Decision Tree**
  - Training MSE: 0.0000
  - Testing MSE: 135.8108
  - Training R2: 1.0000
  - Testing R2: 0.9679

- **Random Forest**
  - Training MSE: 6.7802
  - Testing MSE: 66.6437
  - Training R2: 0.9984
  - Testing R2: 0.9842

- **Gradient Boosting**
  - Training MSE: 1.5239
  - Testing MSE: 42.9771
  - Training R2: 0.9996
  - Testing R2: 0.9898

- **XGBoost**
  - Training MSE: 0.0058
  - Testing MSE: 81.1483
  - Training R2: 1.0000
  - Testing R2: 0.9808

- **AdaBoost**
  - Training MSE: 137.4871
  - Testing MSE: 311.1356
  - Training R2: 0.9669
  - Testing R2: 0.9264

## Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Anomaly-Detection-Sensor-Networks.git
