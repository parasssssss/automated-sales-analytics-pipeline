import pandas as pd

def load_and_clean_data():
    df = pd.read_csv('dataset/data.csv', encoding='latin-1')
    
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # Convert date columns
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')
    
    # Missing values check
    print("\nMissing Values Before:\n", df.isnull().sum())

    #Handle duplicates using aggregation
    df = df.groupby(['order_id', 'product_id'], as_index=False).agg({
        'order_date': 'first',
        'product_name': 'first',
        'category': 'first',
        'sales': 'sum',
        'profit': 'sum',
        'quantity': 'sum',
        'discount': 'mean',
        'region': 'first'
    })
    
    # Fill optional columns
    df['discount'] = df['discount'].fillna(0)
    df['quantity'] = df['quantity'].fillna(1)

    # Final check
    print("\nMissing Values After:\n", df.isnull().sum())
    
    return df