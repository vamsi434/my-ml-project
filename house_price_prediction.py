import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Generate some random data
X = np.random.rand(100, 1) * 1000  # house size (in square feet)
y = X * 100 + np.random.randn(100, 1) * 10000  # house price

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model on the training set
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model on the testing set
y_pred = model.predict(X_test)

# Print the model's coefficients and R^2 score
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)
print('R^2 score:', model.score(X_test, y_test))
