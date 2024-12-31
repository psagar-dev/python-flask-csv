from data_manager import DataManager
import pandas as pd

class SalesTrendsAPI:
    def __init__(self, data_manager):
        # Initialize DataManager
        self.data_manager = data_manager

    def merge_data(self, customers_data, products_data, sales_data):
        """
        Merge the sales data with product data to include category information.
        """
        return sales_data.merge(products_data, on="ProductID", how="left")

    def calculate_sales_trends(self, data):
        """
        Calculate sales trends by aggregating data by category and month.
        """
        data['SaleDate'] = pd.to_datetime(data['SaleDate'])
        data['Month'] = data['SaleDate'].dt.to_period('M')

        sales_trends = data.groupby(['Category', 'Month']).agg({
            'Quantity': 'sum',
            'PricePerUnit': 'mean'
        }).reset_index()

        sales_trends['Month'] = sales_trends['Month'].astype(str)
        return sales_trends

    def get_sales_trends(self):
        """
        Main method to return sales trends by processing the data.
        """
        customers_data, products_data, sales_data = self.data_manager.load_data()
        data = self.merge_data(customers_data, products_data, sales_data)
        return self.calculate_sales_trends(data)
    
    def merge_data_customer(self, customers_data, products_data, sales_data):
        return sales_data.merge(customers_data, on="CustomerID", how="left").merge(products_data, on="ProductID", how="left")

    def get_top_regions(self):
        customers_data, products_data, sales_data = self.data_manager.load_data()
        data = self.merge_data_customer(customers_data, products_data, sales_data)
        
        # Debug: Ensure 'Region' column exists
        if 'Region' not in data.columns:
            raise KeyError("'Region' column not found in the merged dataset.")

        # Aggregate sales by region
        region_sales = data.groupby('Region').agg({
            'Quantity': 'sum'
        }).reset_index()

        # Get top 5 regions
        top_regions = region_sales.nlargest(5, 'Quantity')
        return top_regions
    
    def merge_data_categories(self, customers_data, products_data, sales_data):
        return sales_data.merge(customers_data, on="CustomerID", how="left").merge(products_data, on="ProductID", how="left")
    
    def get_top_categories(self):
        customers_data, products_data, sales_data = self.data_manager.load_data()
        data = self.merge_data_categories(customers_data, products_data, sales_data)

        # Aggregate sales by category
        category_sales = data.groupby(['Category']).agg({
            'Quantity': 'sum'
        }).reset_index()

        # Get top 5 categories by total quantity sold
        top_categories = category_sales.nlargest(5, 'Quantity')

        # Get details of the top categories
        top_category_details = data[data['Category'].isin(top_categories['Category'])]
        top_category_details = top_category_details.groupby(['Category', 'ProductName', 'CustomerName', 'CustomerID']).agg({
            'Quantity': 'sum',
            'PricePerUnit': 'mean'
        }).reset_index()

        # Limit to 5 records per category
        top_category_details = top_category_details.groupby('Category').head(5).reset_index(drop=True)
        return top_category_details
    
    def get_latest_orders(self):
        customers_data, products_data, sales_data = self.data_manager.load_data()
        data = self.merge_data_categories(customers_data, products_data, sales_data)

        # Sort by SaleDate in descending order and limit to top 5
        latest_orders = data.sort_values(by='SaleDate', ascending=False).head(5)
        return latest_orders