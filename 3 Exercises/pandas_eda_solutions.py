import pandas as pd
import numpy as np
import pickle
import os

# Helper to get absolute path relative to this script
def get_data_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, 'files', filename)

# 6.1: Combine datasets
def combine_data():
    # country_2022_population
    ser_data = {"Kabul": 41128771, "Tirana": 2842321}
    country_2022_population = pd.Series(ser_data)
    
    # country_rank
    rank = [36, 138, 34]
    index = ["Kabul", "Tirana", "Algiers"]
    country_rank = pd.Series(rank, index=index)
    
    # country_data
    country_data = pd.DataFrame({"Rank": country_rank, "2022 population": country_2022_population})
    
    # further_country_data
    further_data = {"Rank": [213, 203], "2022 population": [44273, 79824]}
    further_index = ["Pago Pago", "Andorra la Vella"]
    further_country_data = pd.DataFrame(further_data, index=further_index)
    
    # all_country_data
    all_country_data = pd.concat([country_data, further_country_data])
    
    # capitals
    capital_countries = pd.DataFrame({
        "Country": ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra"],
        "Capital": ["Kabul", "Tirana", "Algiers", "Pago Pago", "Andorra la Vella"]},
        index=["Kabul", "Tirana", "Algiers", "Pago Pago", "Andorra la Vella"])
    
    capitals = pd.concat([capital_countries, all_country_data], axis=1)
    
    return capitals

# 6.1 (continued): Schiphol data
def schiphol_analysis():
    flights_path = get_data_path("all_flights.p")
    types_path = get_data_path("all_aircraftTypes.p")
    
    try:
        with open(flights_path, "rb") as f:
            all_flights = pickle.load(f)
        with open(types_path, "rb") as f:
            all_aircraftTypes = pickle.load(f)
            
        df = pd.DataFrame(all_flights)
        aircraft_types = pd.DataFrame(all_aircraftTypes)
        
        # Step 1: Converting dict-column to Series
        aircraft_series = df['aircraftType'].apply(pd.Series)
        df = pd.concat([df.drop('aircraftType', axis=1), aircraft_series], axis=1)
        
        # Step 2: Merge with aircraft_types
        df_merged = df.merge(aircraft_types, on='iataMain', how='left')
        return df_merged
    except FileNotFoundError as e:
        print(f"Error loading Schiphol data: {e}")
        return None

# 6.5: Diamonds EDA
def diamonds_eda():
    path = get_data_path("diamonds.csv")
    try:
        df = pd.read_csv(path, index_col=0)
        
        # Ordered Categorical
        cut_order = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
        clarity_order = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
        
        df['cut'] = pd.Categorical(df['cut'], categories=cut_order, ordered=True)
        df['clarity'] = pd.Categorical(df['clarity'], categories=clarity_order, ordered=True)
        
        # Statistical analysis (outliers)
        outliers = df[(df['y'] < 3) | (df['y'] > 20)]
        
        # Correlation matrix
        numeric_df = df.select_dtypes(include=[np.number])
        corr_matrix = numeric_df.corr()
        
        return df.head(), outliers, corr_matrix
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        return None, None, None

if __name__ == "__main__":
    print("Testing Pandas Exercises...")
    capitals = combine_data()
    print(f"Capitals Shape: {capitals.shape}")
    
    schiphol = schiphol_analysis()
    if schiphol is not None:
        print(f"Schiphol Merged Shape: {schiphol.shape}")
        
    diamonds_head, outliers, corr = diamonds_eda()
    if diamonds_head is not None:
        print("Diamonds Head:")
        print(diamonds_head)
        print(f"Diamonds Outliers Count: {len(outliers)}")
        print("Correlation with Price:")
        print(corr['price'])
