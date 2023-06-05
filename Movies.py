#!/usr/bin/env python
# coding: utf-8

# # Load the data into your project using pandas:
# 
# - Open a Python environment or **Jupyter Notebook**.
# - Import the pandas library: **import pandas as pd**.
# - Use the copied link addresses to **read each file into a DataFrame()**:

# In[1]:


# Imports
import pandas as pd
import numpy as np


# In[2]:


basics_url = "https://datasets.imdbws.com/title.basics.tsv.gz"
akas_url = "https://datasets.imdbws.com/title.akas.tsv.gz"
ratings_url = "https://datasets.imdbws.com/title.ratings.tsv.gz"

basics = pd.read_csv(basics_url, sep='\t', low_memory=False)
akas = pd.read_csv(akas_url, sep='\t', low_memory=False)
ratings = pd.read_csv(ratings_url, sep='\t', low_memory=False)
print("CSV Readings complete")


# In[3]:


basics.head()


# # Perform data preprocessing and filtering:
# 
# - Replace "\N" with np.nan in each DataFrame: basics.replace({'\\N': np.nan}, inplace=True), akas.replace({'\\N': np.nan}, inplace=True), ratings.replace({'\\N': np.nan}, inplace=True).
# - Filter the basics DataFrame based on the provided specifications:

# In[4]:


basics = pd.DataFrame(basics).replace({'\\N': np.nan})
akas = pd.DataFrame(akas).replace({'\\N': np.nan})
ratings = pd.DataFrame(ratings).replace({'\\N': np.nan})

print("NaNs were Replaced Succesfully")


# In[5]:


basics = basics.dropna(subset=['runtimeMinutes', 'genres'])
basics = basics[basics['titleType'] == 'movie']
basics['startYear'] = pd.to_numeric(basics['startYear'], errors='coerce') # Convert 'startYear' to numeric type
basics = basics[(basics['startYear'] >= 2000) & (basics['startYear'] <= 2021)]
basics = basics[~basics['genres'].str.contains('documentary', case=False)]


# ### Filter the basics DataFrame to include only US movies based on the akas DataFrame:

# In[6]:


keepers = basics['tconst'].isin(akas[akas['region'] == 'US']['titleId'])
basics = basics[keepers]


# # Save the filtered DataFrames to compressed CSV files:
# 
# - Create a "Data" folder within your repository if it doesn't already exist.
# - Use the to_csv method to save each DataFrame with compression:

# In[7]:


basics.to_csv("Data/title_basics.csv.gz", compression='gzip', index=False)
akas.to_csv("Data/title_akas.csv.gz", compression='gzip', index=False)
ratings.to_csv("Data/title_ratings.csv.gz", compression='gzip', index=False)


# In[9]:


print("Check \"Data\" Folder")

