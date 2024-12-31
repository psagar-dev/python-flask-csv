# Docker Setup Guide

This guide provides instructions for setting up and running the Python-based data analysis application using Docker.

## Prerequisites

- Docker installed on your system.
- Docker Compose installed.
- Clone or download the project repository.

---

## Steps to Run the Application

### 1. Start the Application Using Docker Compose

Run the following command to start the application and its dependencies:

```bash
docker compose up
```

This command will:
- Build the Docker images if not already built.
- Start the application container.
- Bind the Flask application to port `5000`.

Access the application at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---
## ---------------------- OR ------------------------
---

### 1. Build a Docker Image Manually

If you want to build the application Docker image manually, use the following command:

```bash
docker image build -t data-analysis-python-app .
```

This command will:
- Use the `Dockerfile` in the project directory to build the image.
- Tag the image as `data-analysis-python-app`.

---

### 2. Run the Application Container

Run the application container with the following command:

```bash
docker container run -d --name data-analysis-python-app -p 5000:5000 data-analysis-python-app
```

This command will:
- Start a container named `data-analysis-python-app`.
- Expose the application on port `5000`.

Access the application at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Troubleshooting

- Ensure Docker is running before executing the commands.
- Verify there are no conflicts on port `5000`.
- Check container logs if the application does not start:
  ```bash
  docker logs data-analysis-python-app
  ```

---

### Available Routes

Below are the available routes for this application:

- **[Sales Trends](http://127.0.0.1:5000/sales_trends)**: Provides sales trends grouped by product category and month.
- **[Top Customers](http://127.0.0.1:5000/top_customers)**: Lists the top 5 customers based on total purchases.
- **[Top Regions](http://127.0.0.1:5000/top_regions)**: Displays the top 5 regions with the highest sales performance.
- **[Top Categories](http://127.0.0.1:5000/top_categories)**: Provides detailed insights into the top 5 categories with the highest sales.
- **[Latest Orders](http://127.0.0.1:5000/latest_orders)**: Fetches the 5 most recent orders with customer and product details.

---