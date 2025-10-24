# Import the required library
import pandas as pd

# Load the dataset (replace 'your_dataset.csv' with your actual file name)
df = pd.read_csv('Restaurant.csv')

# Display the first few rows (optional, just to explore)
print("First 5 rows of the dataset:")
print(df.head())

# Identify the number of rows and columns
rows, cols = df.shape
print("\nNumber of rows:", rows)
print("Number of columns:", cols)
