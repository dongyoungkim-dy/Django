import requests
import pandas as pd

# Example function to fetch GDP data
def fetch_gdp(country_code='ALL'):
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD?format=json"
    response = requests.get(url)
    data = response.json()
    # Convert to DataFrame and clean data
    df = pd.DataFrame(data[1])
    return df[['date', 'value']].rename(columns={'date': 'Year', 'value': 'GDP'})

# Example function to fetch Inflation data
def fetch_inflation(country_code='ALL'):
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/FP.CPI.TOTL.ZG?format=json"
    response = requests.get(url)
    data = response.json()
    # Convert to DataFrame and clean data
    df = pd.DataFrame(data[1])
    return df[['date', 'value']].rename(columns={'date': 'Year', 'value': 'Inflation'})

# Function to merge datasets
def merge_data(gdp_df, inflation_df):
    merged_df = pd.merge(gdp_df, inflation_df, on="Year", how="inner")
    return merged_df.dropna()

# Fetch and clean data
gdp_data = fetch_gdp()
inflation_data = fetch_inflation()
cleaned_data = merge_data(gdp_data, inflation_data)
