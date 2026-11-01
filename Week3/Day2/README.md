**Internship:** System-7  
**Week:** 3  
**Day:** 2  
**Topic:** Model Tuning and Comparison

This folder contains my Day 16 internship work, focused on understanding model fitting, preprocessing, hyperparameter tuning, and comparing machine learning models using Scikit-learn.

## Topics Covered

### 1. Overfitting and Underfitting
- Understanding overfitting and underfitting.
- Exploring how model complexity affects performance.
- Training Decision Tree models with different `max_depth` values.
- Comparing training and testing accuracy.

### 2. Feature Scaling and Encoding
- Understanding feature scaling.
- Using `StandardScaler` and `MinMaxScaler`.
- Applying `OneHotEncoder` to categorical features.
- Combining numerical and categorical preprocessing using `ColumnTransformer`.

### 3. GridSearchCV
- Understanding hyperparameter tuning.
- Searching for the best hyperparameter combination.
- Using `GridSearchCV` with Support Vector Machine (SVM).
- Applying cross-validation to evaluate parameter combinations.

### 4. RandomizedSearchCV
- Understanding randomized hyperparameter search.
- Using `RandomizedSearchCV` to test selected parameter combinations.
- Comparing GridSearchCV and RandomizedSearchCV based on best scores and execution time.

### 5. Model Comparison
Trained and compared the following classification algorithms:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

Evaluated model performance using accuracy and identified the highest-scoring model.

## Tools and Libraries
- Python
- Pandas
- Scikit-learn
- Matplotlib
- NumPy

## Learning Outcomes
By completing these exercises, I learned how to:
- Identify overfitting and underfitting.
- Understand the effect of model complexity on performance.
- Scale numerical features and encode categorical features.
- Apply preprocessing using ColumnTransformer.
- Tune model hyperparameters using GridSearchCV and RandomizedSearchCV.
- Compare different machine learning models using evaluation metrics.

## Folder Structure

```text
day-16-tuning-model-comparison/
│
├── overfitting_underfitting.py
├── column_transformer.py
├── grid_search.py
├── randomized_search.py
├── model_comparison.py
└── README.md