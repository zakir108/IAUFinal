def CleanedData(df):
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
    return df_cleaned

def CleanYear(df_cleaned,pd,np):

    # Converting 'release_year' to datetime
    df_cleaned.loc[:, 'release_year'] = pd.to_datetime(df_cleaned['release_year'], format='%Y')


    # Replace infinity values with NaN in the cleaned DataFrame
    df_cleaned.replace([np.inf, -np.inf], np.nan, inplace=True)
