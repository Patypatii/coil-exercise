import numpy as np
import os

# Helper to get absolute path relative to this script
def get_data_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, 'files', filename)

# Step 1: Loading (Quantity, InvoiceDate, UnitPrice, CustomerID, CountryCode)
def load_sales():
    path = get_data_path('sales.csv')
    try:
        raw_data = np.genfromtxt(path, delimiter=',', dtype=object, encoding=None, skip_header=1)
        quantity = raw_data[:, 0].astype(float).astype(int)
        # InvoiceDate = raw_data[:, 1]
        unit_price = raw_data[:, 2].astype(float)
        customer_id = raw_data[:, 3].astype(float)
        country_code = raw_data[:, 4].astype(object)
        return quantity, unit_price, customer_id, country_code, raw_data
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        return None

# Step 2: UnitPrice statistics
def unit_price_stats(unit_price):
    return {
        "min": np.min(unit_price),
        "max": np.max(unit_price),
        "mean": np.mean(unit_price),
        "median": np.median(unit_price),
        "std": np.std(unit_price)
    }

# Step 3: Revenue analysis
def revenue_analysis(quantity, unit_price, country_code):
    revenue = quantity * unit_price
    total_revenue = np.sum(revenue)
    
    countries = np.unique(country_code)
    revenue_per_country = {}
    for country in countries:
        mask = country_code == country
        revenue_per_country[country] = np.sum(revenue[mask])
    
    return total_revenue, revenue_per_country

# Step 1: Wine data loading
def load_wine():
    path = get_data_path('wine.csv')
    try:
        data = np.genfromtxt(path, delimiter=',', dtype=float)
        # Remove rows with NaNs
        data = data[~np.isnan(data).any(axis=1)]
        return data
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        return None

# Step 2: Normalization (Min-Max)
def min_max_scale(data):
    min_vals = np.min(data, axis=0)
    max_vals = np.max(data, axis=0)
    range_vals = max_vals - min_vals
    range_vals[range_vals == 0] = 1
    return (data - min_vals) / range_vals

# Step 3: Z-Score
def z_score_scale(data):
    mean_vals = np.mean(data, axis=0)
    std_vals = np.std(data, axis=0)
    std_vals[std_vals == 0] = 1
    return (data - mean_vals) / std_vals

if __name__ == "__main__":
    print("Testing Sales & Wine Exercises...")
    sales_data = load_sales()
    if sales_data:
        q, up, cid, cc, raw = sales_data
        print(f"Sales Stats: {unit_price_stats(up)}")
        tr, rpc = revenue_analysis(q, up, cc)
        print(f"Total Revenue: {tr}")
    
    wine = load_wine()
    if wine is not None:
        print(f"Wine Shape: {wine.shape}")
        normalized_wine = min_max_scale(wine)
        print(f"Normalized Wine Range: {np.min(normalized_wine)} to {np.max(normalized_wine)}")
