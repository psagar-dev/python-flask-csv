from flask import Flask, jsonify, render_template
from sales_trends_api import SalesTrendsAPI
from customer_analysis import CustomerAnalysis
from data_manager import DataManager

# Initialize Flask app
app = Flask(__name__)
data_manager = DataManager()

sales_trends_api = SalesTrendsAPI(data_manager)
customer_analysis_api = CustomerAnalysis(data_manager)

@app.route('/')
def home():
    return render_template('index.html')

# Define a route to get sales trends by product category
@app.route('/sales_trends', methods=['GET'])
def sales_trends():
    trends = sales_trends_api.get_sales_trends()

    # Convert the results to JSON
    trends_json = trends.to_dict(orient='records')
    return jsonify(trends_json)

# Define a route to get top customers with their products
@app.route('/top_customers', methods=['GET'])
def top_customers():
    top_customers_data = customer_analysis_api.get_top_customers_with_products()

    # Convert the results to JSON
    return jsonify(top_customers_data)

@app.route('/top_regions', methods=['GET'])
def top_regions():
    top_regions_data = sales_trends_api.get_top_regions()
    top_regions_json = top_regions_data.to_dict(orient='records')
    return jsonify(top_regions_json)

@app.route('/top_categories', methods=['GET'])
def top_categories():
    top_categories_data = sales_trends_api.get_top_categories()
    top_categories_json = top_categories_data.to_dict(orient='records')
    return jsonify(top_categories_json)

@app.route('/latest_orders', methods=['GET'])
def latest_orders():
    latest_orders_data = sales_trends_api.get_latest_orders()
    latest_orders_json = latest_orders_data.to_dict(orient='records')
    return jsonify(latest_orders_json)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')