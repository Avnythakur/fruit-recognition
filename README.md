# Fruit Recognition Using Deep Learning  
## A Comparative Study Between Custom CNN and Transfer Learning Approach

This repository contains the implementation of a **fruit recognition system using deep learning**, based on my research work titled:

**“Fruit Recognition Using Deep Learning: A Comparative Study Between Custom CNN and Transfer Learning Approach”**

The project compares a **custom-built Convolutional Neural Network (CNN)** with **transfer learning models** to evaluate their performance on fruit image classification.

---

## 📖 Project Overview
The objective of this project is to classify images of different fruits using deep learning techniques and to analyze the performance differences between:

- A **custom CNN architecture**
- **Pre-trained models** using transfer learning

This work combines **academic research** with **practical implementation**, focusing on real-world challenges such as data variation and generalization.

---

## 📂 Project Structure

```text
fruit-recognition/
│
├── notebook/
│   ├── fruit_recognition_training.ipynb
│   └── fruit_recognition_test.ipynb
│
├── src/
│   └── app.py
│
├── paper/
│   └── fruit_recognition_research_paper.pdf
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 🧠 Methodology

This project follows a comparative deep learning approach for fruit image classification.

### 1. Data Preprocessing
- Image resizing and normalization
- Data augmentation to reduce overfitting

### 2. Custom CNN Model
- Designed a custom Convolutional Neural Network
- Trained from scratch on the fruit image dataset

### 3. Transfer Learning Approach
- Used pre-trained deep learning models
- Fine-tuned final layers for fruit classification

### 4. Model Evaluation
- Compared models based on accuracy and performance
- Analyzed generalization on unseen test data

## 📊 Results and Discussion

- Transfer learning models converged faster compared to the custom CNN
- Custom CNN allowed greater architectural flexibility
- Performance was affected by lighting variations and visually similar fruits

  ## 🚀 How to Run the Project

## 🚀 How to Run the Project

1. Ensure Python 3 is installed.

2. Install the required libraries:
- NumPy
- Pandas
- Matplotlib
- OpenCV
- TensorFlow / Keras

3. Run the application:
```bash
python src/app.py
