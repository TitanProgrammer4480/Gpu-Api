# GPU Price API

This is a Python-based API that scrapes **Newegg.ca** for the latest GPU prices. The API is built using **Flask** for the backend and **Requests** for making HTTP requests. It allows users to fetch current GPU prices in real-time. The entire API is hosted on **Vercel**.

## 🚀 Features

- Scrapes GPU prices from Newegg.ca
- Provides real-time price data through an API
- Built using Flask and Requests
- Deployed and hosted on Vercel

## 📌 Requirements

- Python 3.x
- Flask
- Requests

## 🛠 Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gpu-price-api
   cd gpu-price-api
   ```
  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open http://localhost:5000 to access the API locally.

## 📡 API Endpoints
### GPU Price Endpoint
GET /api/gpu-prices – Fetches the latest GPU prices from Newegg.ca.

### 📤 Deployment
This API is deployed on Vercel, offering automatic deployments on every push to the main branch.

##📜 License
This project is licensed under the MIT License.
