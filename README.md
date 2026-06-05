# Handwritten Character Recognition System

## Overview

A Deep Learning project that recognizes handwritten digits (0–9) and alphabets (A–Z) using Convolutional Neural Networks (CNN). The system is trained on MNIST and EMNIST datasets and deployed using a Streamlit web application for real-time character prediction.

## Features
* Data Loading and Preprocessing (MNIST & EMNIST)
* Image Normalization and Reshaping
* CNN Model for Feature Extraction
* Model Training and Evaluation
* Real-time Handwritten Character Prediction
* Interactive Drawing Canvas using Streamlit
* Probability-based Confidence Output
* Model Deployment using Streamlit

## Dataset Features
* MNIST Dataset (Digits 0–9)
* EMNIST Dataset (Alphabets A–Z)
* 28×28 Grayscale Images
* Labeled Character Classes
* Training and Testing Splits

## Results
* MNIST Model Accuracy: ~99.2%
* EMNIST Model Accuracy: ~93.5%
* Real-time Prediction: Successfully working with Streamlit UI
* Robust performance after preprocessing (normalization + inversion fix)

## Technologies Used
* Python
* TensorFlow / Keras
* Convolutional Neural Networks (CNN)
* NumPy
* Pandas
* OpenCV
* PIL (Pillow)
* Streamlit
* streamlit-drawable-canvas

## Project Structure
* app/ → Streamlit application
* models/ → Trained CNN models (MNIST & EMNIST)
* notebook/ → Training and experimentation notebooks
* screenshots/ → Output results and predictions
* README.md → Project documentation

## Author

* Shivansh Tripathi
CodeAlpha Machine Learning Intern
