# Day 18 – PCA and Machine Learning Pipelines

## Topics Covered

1. **Principal Component Analysis (PCA)**
   - Dimensionality reduction
   - Principal components
   - Explained variance ratio
   - PCA visualization

2. **Feature Engineering**
   - Creating new features
   - Transforming existing features
   - Feature selection

3. **Imbalanced Datasets**
   - Oversampling and undersampling
   - SMOTE
   - Class weights
   - Precision, recall, and F1-score

4. **Data Leakage**
   - Understanding data leakage
   - Incorrect and correct scaling approaches
   - Preventing test data from influencing training

5. **Scikit-learn Pipelines**
   - Combining preprocessing and model training
   - StandardScaler
   - PCA
   - Logistic Regression

## Practical Project: Customer Segmentation

Implemented customer segmentation using K-Means clustering.

### Steps
- Created a customer dataset.
- Selected annual income and spending score as features.
- Standardized the features using StandardScaler.
- Used the Elbow Method to explore the number of clusters.
- Applied K-Means clustering.
- Evaluated clusters using silhouette score.
- Applied PCA to visualize the customer clusters.

## Tools and Libraries

- Python
- Pandas
- Matplotlib
- Scikit-learn

## Learning Outcome

Learned how to reduce dimensionality, engineer features, handle imbalanced datasets, prevent data leakage, build machine learning pipelines, and perform customer segmentation using clustering.