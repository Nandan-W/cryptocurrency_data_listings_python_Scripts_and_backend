import time
import pandas as pd
from data_fetcher import fetch_crypto_data
from data_analyzer import analyze_data

def update_excel_files():
    data = fetch_crypto_data()
    if not data:
        print("Failed to fetch data.")
        return

    data_file = 'output/crypto_data.xlsx'
    pd.DataFrame(data).to_excel(data_file, index=False)
    print(f"Updated: {data_file}")

    analysis = analyze_data(data)
    analysis_file = 'output/crypto_analysis.xlsx'

    with pd.ExcelWriter(analysis_file) as writer:
        pd.DataFrame(analysis["top_5_by_market_cap"]).to_excel(writer, sheet_name="Top 5 by Market Cap", index=False)
        pd.DataFrame([{"Average Price": analysis["average_price"]}]).to_excel(writer, sheet_name="Average Price", index=False)
        pd.DataFrame(analysis["highest_change"]).to_excel(writer, sheet_name="Highest Change", index=False)
        pd.DataFrame(analysis["lowest_change"]).to_excel(writer, sheet_name="Lowest Change", index=False)

    print(f"Updated: {analysis_file}")

if __name__ == '__main__':
    print("Starting updater script...")
    while True:
        update_excel_files()
        print("Waiting 5 minutes before next update...")
        time.sleep(300)  
