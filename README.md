# Cognifyz_Level1_DA
## Restaurant Data Analysis Project
***Overview***

This project focuses on exploring and analyzing a restaurant dataset using Python. The main objectives are:

Explore the dataset and understand its structure.

Preprocess the data by handling missing values and data type conversions.

Analyze numerical and categorical variables.

Visualize restaurant distributions across cities, countries, and cuisines.

Perform geospatial analysis to map restaurant locations.

Explore correlations between restaurant location and ratings.

This analysis can help businesses or users understand restaurant distribution, popularity of cuisines, and ratings patterns geographically.

Dataset

The dataset contains the following information about restaurants:

Column Name	Description
Restaurant ID	Unique identifier for each restaurant
Country Code	Code representing the country of the restaurant
City	City where the restaurant is located
Cuisines	Type(s) of cuisine offered
Latitude	Latitude coordinate of the restaurant
Longitude	Longitude coordinate of the restaurant
Aggregate rating	Average rating given by users/customers
Votes	Number of user votes/reviews
Other columns	May include additional details like restaurant name
Tasks Performed

# 1. Data Exploration
Objective: Understand dataset structure and identify basic properties.
Checked number of rows and columns:
df.shape

Checked column data types:
df.dtypes

Viewed first few rows for understanding:
df.head()

# 2. Handling Missing Values

Checked missing values in each column:
df.isnull().sum()


Filled missing values:
Numerical columns → filled with mean.
Categorical columns → filled with mode.

df['Aggregate rating'] = df['Aggregate rating'].fillna(df['Aggregate rating'].mean())
df['City'] = df['City'].fillna(df['City'].mode()[0])

# 3. Data Type Conversion

Ensured all columns had appropriate data types.
Example: Converted Aggregate rating to numeric:

df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

# 4. Numerical Data Analysis

Calculated basic statistics:
Mean, median, standard deviation, min, max, quartiles

df.describe()
df['Aggregate rating'].median()


Example insight:
Average restaurant rating = 3.40
Ratings range from 0 to 5

# 5. Categorical Data Analysis

Analyzed Country Code, City, and Cuisines.
Identified top cuisines and cities:

df['Cuisines'].value_counts().head(10)
df['City'].value_counts().head(10)


Visualized distributions using bar plots:
sns.barplot(x=city_counts.values, y=city_counts.index, palette='magma', hue=city_counts.index, dodge=False, legend=False)

# 6. Geospatial Analysis

Plotted restaurants on a map using folium:
import folium

restaurant_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=5)

for idx, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=3,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        popup=row['Restaurant Name'] if 'Restaurant Name' in df.columns else None
    ).add_to(restaurant_map)

restaurant_map


# Optional: Used MarkerCluster for large datasets to avoid overcrowding.

# Optional Enhancement: Colored markers by rating:

Green → high-rated
Orange → medium-rated
Red → low-rated

# 7. Correlation Analysis

Checked if restaurant location correlates with ratings:
df[['Latitude','Longitude','Aggregate rating']].corr()
sns.heatmap(df[['Latitude','Longitude','Aggregate rating']].corr(), annot=True, cmap='coolwarm')

Insight: Ratings show weak correlation with location (Latitude/Longitude), meaning high ratings are not strongly dependent on geographic coordinates.

## Libraries Used

pandas → Data handling and preprocessing

numpy → Numerical operations

matplotlib → Basic visualization

seaborn → Advanced visualization

folium → Geospatial visualization

folium.plugins.MarkerCluster → Clustering map markers

### Insights & Observations

Restaurant Distribution: Most restaurants are concentrated in a few major cities.

Popular Cuisines: North Indian, Chinese, and Italian are the most common.

Ratings: Majority of restaurants have ratings between 3 and 4.5.

Geospatial Patterns: Interactive maps help visualize clusters of restaurants; high-rated restaurants are distributed across multiple cities.

Correlation: Aggregate rating is not strongly dependent on location.

***How to Run***

Install required libraries:

pip install pandas numpy matplotlib seaborn folium


***Place the dataset (Restaurant.csv) in the same folder as the notebook.***

Open the Jupyter Notebook and run the cells in order.

***All exploration, preprocessing, visualizations, and maps will be generated.***
