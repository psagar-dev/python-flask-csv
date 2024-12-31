class CustomerAnalysis:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def merge_data(self, customers_data, products_data, sales_data):
        """Merge customers, products, and sales data."""
        merged_data = sales_data.merge(customers_data, on="CustomerID", how="left")
        merged_data = merged_data.merge(products_data, on="ProductID", how="left")
        return merged_data

    def get_top_customers(self, merged_data):
        """Get the top 5 customers based on total sales."""
        merged_data["TotalSales"] = merged_data["Quantity"] * merged_data["PricePerUnit"]
        top_customers = (
            merged_data.groupby("CustomerID")["TotalSales"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
            .reset_index()
        )
        return top_customers

    def get_top_customer_products(self, merged_data, top_customers):
        """Get the products purchased by the top 5 customers."""
        top_customer_data = merged_data[merged_data["CustomerID"].isin(top_customers["CustomerID"])]
        customer_products = (
            top_customer_data.groupby(["CustomerID", "CustomerName"])["ProductName"]
            .apply(list)
            .reset_index()
        )
        return customer_products

    def get_top_customers_with_products(self):
        """Main method to get top 5 customers and their products."""
        customers_data, products_data, sales_data = self.data_manager.load_data()
        merged_data = self.merge_data(customers_data, products_data, sales_data)
        top_customers = self.get_top_customers(merged_data)
        top_customers_with_products = self.get_top_customer_products(merged_data, top_customers)
        # Format output as required
        result = [
            {
                "customer_id": row["CustomerID"],
                "customer_name": row["CustomerName"],
                "products": row["ProductName"]
            }
            for _, row in top_customers_with_products.iterrows()
        ]
        print(result)
        return result