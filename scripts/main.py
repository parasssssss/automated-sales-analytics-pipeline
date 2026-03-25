from data_cleaning import load_and_clean_data
from analysis import analyze_data
from db_insert import insert_data

def main():
    df = load_and_clean_data()
    
    analyze_data(df)     # analysis
    insert_data(df)      # DB insert

if __name__ == "__main__":
    main()