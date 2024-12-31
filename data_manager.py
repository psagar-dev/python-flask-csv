import pandas as pd

class DataManager:
    def __init__(self):
        # Paths to the datasets
        self.customers_data_path = 'data/Customers_Data.csv'
        self.products_data_path = 'data/Products_Data.csv'
        self.sales_data_path = 'data/Sales_Data.csv'

    def load_data(self):
        """
        Load the data from CSV files.
        """
        customers_data = pd.read_csv(self.customers_data_path)
        products_data = pd.read_csv(self.products_data_path)
        sales_data = pd.read_csv(self.sales_data_path)
        return customers_data, products_data, sales_data
