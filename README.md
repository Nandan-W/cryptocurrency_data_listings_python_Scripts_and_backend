# Cryptocurrency Data Listings

## Objective
The goal of this project is to fetch live cryptocurrency data for the top 50 cryptocurrencies, analyze it, and present the data in a live-updating Excel sheet. 
The Excel sheet continuously updates with the latest cryptocurrency prices.

This is made available through two mediums:- a React-based frontend and a standalone python script

## Backend
### React Frontend's Backend
The backend for the React frontend is a Flask application that fetches and serves cryptocurrency data. The Flask application is deployed on Railways.
The Frontend URL is https://cryptocurrency-data-listings-frontend-qch29l4r7.vercel.app/

#### Flask Application
- **File**: app.py
- **Endpoints**:
    /api/crypto-data: Fetches live cryptocurrency data.
    /api/crypto-analysis: Provides analysis of the cryptocurrency data.

![image](https://github.com/user-attachments/assets/7154861b-dd77-4f2d-b078-e089434dd24f)

Fresh data is fetched every 5 minutes.

## Standalone Python Script
The standalone Python script fetches live cryptocurrency data, performs analysis, and updates an Excel sheet with the latest data.

### Python Script
- **File**: python_script_for_dataFetch_analysis_and_update.py
- **Functionality**:
  - Fetches live cryptocurrency data.
  - Performs analysis on the data.
  - Updates corresponding Excel sheets with the latest data.

### Running the Standalone Script
To run the standalone script and have regular updated data in Excel, follow these steps:

**Clone the Repository**:
``` 
git clone https://github.com/Nandan-W/cryptocurrency_data_listings_python_Scripts_and_backend.git
```

**Install Dependencies**:
```
pip install -r requirements.txt
```

**Run the Script**:
```
python python_script_for_dataFetch_analysis_and_update.py
```



