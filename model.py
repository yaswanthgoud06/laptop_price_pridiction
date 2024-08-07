import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the dataset
file_path = r"C:\Users\yaswa\OneDrive\Desktop\laptop_price\laptop_PRICE.csv"
data = pd.read_csv(file_path)

# Display the column names to verify them
print(data.columns)

# Use the correct column names based on the dataset
features = ['Company', 'Cpu brand', 'Ram', 'Inches', 'Weight']
target = 'Price'

X = data[features]
y = data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
numeric_features = ['Ram', 'Inches', 'Weight']
categorical_features = ['Company', 'Cpu brand']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Building the pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
score = model.score(X_test, y_test)
print(f'Model R^2 Score: {score}')

# Save the model to a file
with open('laptop_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)
