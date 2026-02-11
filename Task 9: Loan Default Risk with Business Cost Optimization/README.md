Task 9: Loan Default Risk with Business Cost Optimization

Objective: To predict the likelihood of loan default using machine learning and optimize the decision threshold based on business cost analysis.

Dataset: Home Credit Default Risk Dataset


Steps:

1. Data Cleaning & Preprocessing
2. Removed unnecessary identifier columns
3. Handled missing values using: Median imputation for numerical features, Mode imputation for categorical features
5. Encoded categorical variables using one-hot encoding
6. Split data into training and testing sets
7. Trained binary classification model to predict loan default: Logistic Regression
8. Model performance was evaluated using: Confusion Matrix, Classification Report, ROC-AUC Score

Results:

1. Standard accuracy-based evaluation is not sufficient for financial risk problems
2. Cost-sensitive threshold optimization significantly reduces business losses
3. Model decisions are better aligned with real-world financial impact
