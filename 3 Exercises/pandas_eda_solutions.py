import pandas as pd
import numpy as np
import pickle

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
    all_flights = pickle.load(open("files/all_flights.p", "rb"))
    all_aircraftTypes = pickle.load(open("files/all_aircraftTypes.p", "rb"))
    
    df = pd.DataFrame(all_flights)
    aircraft_types = pd.DataFrame(all_aircraftTypes)
    
    # Step 1: Converting dict-column to Series
    # The aircraftType in all_flights is a dict, e.g., {'iatamain': '789', ...}
    aircraft_series = df['aircraftType'].apply(pd.Series)
    df = pd.concat([df.drop('aircraftType', axis=1), aircraft_series], axis=1)
    
    # Step 2: Merge with aircraft_types
    # Merge on iatamain or related
    df_merged = df.merge(aircraft_types, left_on='iatamain', right_on='iatamain', how='left')
    
    return df_merged

# 6.5: Diamonds EDA
def diamonds_eda():
    df = pd.read_csv("files/diamonds.csv", index_col=0)
    
    # Ordered Categorical
    cut_order = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
    clarity_order = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
    
    df['cut'] = pd.Categorical(df['cut'], categories=cut_order, ordered=True)
    df['clarity'] = pd.Categorical(df['clarity'], categories=clarity_order, ordered=True)
    
    # Statistical analysis (outliers)
    # y-size smaller than 3 or bigger than 20
    outliers = df[(df['y'] < 3) | (df['y'] > 20)]
    
    # Correlation matrix
    numeric_df = df.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()
    
    return df.head(), outliers, corr_matrix

if __name__ == "__main__":
    print("Testing Pandas Exercises...")
    capitals = combine_data()
    print(f"Capitals Shape: {capitals.shape}")
    
    try:
        schiphol = schiphol_analysis()
        print(f"Schiphol Merged Shape: {schiphol.shape}")
    except Exception as e:
        print(f"Schiphol skipped (files likely missing/differ): {e}")
        
    diamonds_head, outliers, corr = diamonds_eda()
    print("Diamonds Head:")
    print(diamonds_head)
    print(f"Diamonds Outliers Count: {len(outliers)}")
    print("Correlation with Price:")
    print(corr['price'])
