# dsGuviPhoneplusPrj1
Phoneplus project - Guvi project1
Transaction & Insurance Analytics Dashboard
This project provides a complete pipeline to connect to a MySQL database, store insurance transaction records, and visualize the data using a Plotly dashboard.
🚀 Features
•	Database Integration: Automated connection and schema creation.
•	Data Ingestion: Script to clean and insert transaction data into MySQL.
•	Interactive Dashboard: Visualizes insurance amount and transaction trends using .2s formatting for readability.
Setup Instructions
1. Database Configuration
Create a database named dbproject and a table for transactions.
SQL
CREATE DATABASE dbproject;
Created 9 tables aggregated,Users,Map (3 table eavh)

2. Connect and Store Data
Inserted the data through python code
The dashboard pulls data directly from the transactions table and renders a visual overview through streamlit
________________________________________
📊 Dashboard Overview
The dashboard includes the following KPIs and charts:
•	Total Transaction: Aggregated sum of all "Paid" transactions.
•	Total Insurance: Aggregated sum of all insurance



