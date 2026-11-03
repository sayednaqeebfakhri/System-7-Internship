# Day 05 – Neural Networks

## Overview
ThE work of this covers the fundamentals of Artificial Neural Networks (ANNs), including perceptrons, forward propagation, backpropagation, gradient descent, activation functions, and optimizers.

Two practical exercises were completed using NumPy and TensorFlow/Keras.

## 1. Single Perceptron – AND Gate

### Objective
Implement a single-layer perceptron using NumPy that learns the AND logical operation.

### Concepts Covered
- Perceptron architecture
- Weights and bias
- Step activation function
- Weighted sum
- Prediction error
- Perceptron learning rule
- Weight and bias updates

### AND Gate Truth Table

| Input A | Input B | Output |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### Technologies
- Python
- NumPy

## 2. Student Result Prediction Using Neural Networks

### Objective
Build a neural network using TensorFlow/Keras to predict whether a student will pass or fail based on study hours and attendance.

### Dataset Features

| Feature | Description |
|---|---|
| Study Hours | Daily study hours |
| Attendance | Student attendance |
| Result | 0 = Fail, 1 = Pass |

A small manually created dataset of 20 student records was used for this educational experiment.

### Data Preprocessing
- Separated input features and target labels.
- Split the dataset into 80% training and 20% testing.
- Applied StandardScaler to normalize the input features.

### Neural Network Architecture

| Layer | Neurons | Activation |
|---|---:|---|
| Input | 2 | — |
| Hidden Layer 1 | 8 | ReLU |
| Hidden Layer 2 | 4 | ReLU |
| Output | 1 | Sigmoid |

### Model Configuration
- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Evaluation Metric: Accuracy
- Epochs: 50
- Batch Size: 4

### Model Evaluation
The model was evaluated using unseen test data.

- Training accuracy: 66.67%
- Validation accuracy: 25%
- Test accuracy: 50%

**Observation:** The model achieved limited predictive performance. The small dataset and limited training examples make it difficult to assess generalization reliably.

## 3. Optimizer Comparison

Two optimizers were compared using the same neural network architecture.

| Metric | SGD | Adam |
|---|---:|---:|
| Training Loss | 0.4947 | 0.5892 |
| Validation Loss | 0.4978 | 0.6161 |

**Observation:** SGD achieved lower training and validation loss in this experiment. Results may vary with different datasets, initial weights, and hyperparameters.

## 4. Visualization

Training and validation loss curves were plotted using Matplotlib to observe the model's learning progress.

The experiment also compared the training loss of SGD and Adam.

## 5. Key Learnings

- Understanding artificial neurons and perceptrons.
- Learning how weights and biases work.
- Implementing a perceptron from scratch using NumPy.
- Understanding activation functions: ReLU, Sigmoid, and Softmax.
- Understanding forward propagation and backpropagation.
- Learning gradient descent and learning rates.
- Understanding epochs and batch sizes.
- Building neural networks using TensorFlow/Keras.
- Comparing SGD and Adam optimizers.
- Evaluating and visualizing neural network performance.

## Technologies Used
- Python
- NumPy
- Pandas
- Scikit-learn
- TensorFlow / Keras
- Matplotlib

## Conclusion
Day 19 provided practical experience with neural networks, from implementing a basic perceptron with NumPy to building and evaluating a neural network with TensorFlow/Keras.