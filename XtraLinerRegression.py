import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno




df = pd.read_csv("netflix_titles.csv")
df.head()
df.info()
df.isnull().sum()
msno.matrix(df)
df.describe()


# Data Cleaning
# Filling missing values (we will drop 'director' and 'cast' missing values)
df_cleaned = df.dropna(subset=['director', 'cast'])

# Filling missing 'country' values with 'Unknown'
df_cleaned.loc[:, 'country'] = df_cleaned['country'].fillna('Unknown')

# Filling missing 'rating' values with the most common rating
most_common_rating = df_cleaned['rating'].mode()[0]
df_cleaned.loc[:, 'rating'] = df_cleaned['rating'].fillna(most_common_rating)

# Filling missing 'date_added' values with a placeholder
df_cleaned.loc[:, 'date_added'] = df_cleaned['date_added'].fillna('Unknown')

# Verifying that missing values are handled
df_cleaned.isnull().sum()



plt.figure(figsize=(6, 6))
sns.countplot(data=df_cleaned, x='type', palette='coolwarm')
plt.title('Distribution of Content Types (Movies vs TV Shows)')
#plt.show()



# Top 10 Countries Producing Netflix Content
plt.figure(figsize=(10, 6))
top_10_countries = df_cleaned['country'].value_counts().head(10)
sns.barplot(x=top_10_countries.index, y=top_10_countries.values, palette='magma')
plt.title('Top 10 Countries Producing Netflix Content')
plt.xticks(rotation=45)
#plt.show()


# Distribution of content ratings
plt.figure(figsize=(10, 6))
sns.countplot(data=df_cleaned, x='rating', palette='Set2', order=df_cleaned['rating'].value_counts().index)
plt.title('Distribution of Content Ratings')
plt.xticks(rotation=45)
plt.show()


# Converting 'release_year' to datetime
df_cleaned.loc[:, 'release_year'] = pd.to_datetime(df_cleaned['release_year'], format='%Y')



# Replace infinity values with NaN in the cleaned DataFrame
df_cleaned.replace([np.inf, -np.inf], np.nan, inplace=True)
# Number of titles released per year
plt.figure(figsize=(10, 6))
sns.histplot(data=df_cleaned, x='release_year', bins=20, kde=True, color='blue')
plt.title('Number of Titles Released per Year')
plt.show()



# Top 10 directors with most Netflix titles
plt.figure(figsize=(10, 6))
top_10_directors = df_cleaned['director'].value_counts().head(10)
sns.barplot(x=top_10_directors.index, y=top_10_directors.values, palette='cool')
plt.title('Top 10 Directors with Most Netflix Titles')
plt.xticks(rotation=45)
plt.show()



# Top 10 actors/actresses appearing in Netflix titles
plt.figure(figsize=(10, 6))
df_cleaned['cast'] = df_cleaned['cast'].apply(lambda x: x.split(', ') if pd.notna(x) else [])
all_cast = df_cleaned['cast'].explode().value_counts().head(10)
sns.barplot(x=all_cast.index, y=all_cast.values, palette='coolwarm')
plt.title('Top 10 Actors/Actresses Appearing in Netflix Titles')
plt.xticks(rotation=45)
plt.show()



# Creating a 'duration' column for numeric analysis (only for movies)
df_movies = df_cleaned[df_cleaned['type'] == 'Movie']
df_movies['duration'] = df_movies['duration'].str.replace(' min', '').astype(float)

plt.figure(figsize=(10, 6))
sns.histplot(data=df_movies, x='duration', bins=30, kde=True, color='green')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration (minutes)')
plt.show()