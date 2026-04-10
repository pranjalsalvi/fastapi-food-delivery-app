# 🍕 FastAPI Food Delivery App (QuickBite)

A complete backend system built using **FastAPI** as part of the **Innomatics Research Labs Internship (GenAI Track)**.  
This project simulates a real-world food delivery backend with full API functionality including menu management, order processing, cart system, and advanced search features.

## 🚀 Project Overview

This project demonstrates how a modern backend system works using FastAPI. It is designed to handle real-world food delivery operations such as:

- Managing restaurant menu items
- Placing and tracking customer orders
- Cart management with checkout workflow
- Searching, sorting, and filtering data
- Pagination and combined query handling
- Full CRUD (Create, Read, Update, Delete) operations

The project also follows proper API structuring, validation using Pydantic, and modular helper functions.

## 🛠 Tech Stack

- **Python 3**
- **FastAPI**
- **Pydantic** (for data validation)
- **Uvicorn** (ASGI server)
- **REST API architecture**

## 📌 Features Implemented

### 🔹 1. Basic APIs
- `GET /` → Welcome message
- `GET /menu` → Fetch all menu items
- `GET /menu/{item_id}` → Get single item by ID
- `GET /menu/summary` → Menu statistics (total, available, categories)

### 🔹 2. Order Management
- `POST /orders` → Create new order with validation
- `GET /orders` → View all orders
- `GET /orders/search` → Search orders by customer name
- `GET /orders/sort` → Sort orders by total price

### 🔹 3. Cart System
- `POST /cart/add` → Add items to cart with quantity handling
- `GET /cart` → View cart with grand total
- `POST /cart/checkout` → Convert cart items into confirmed orders

### 🔹 4. Menu Management (CRUD Operations)
- `POST /menu` → Add new menu item (with duplicate check)
- `PUT /menu/{item_id}` → Update price or availability
- `DELETE /menu/{item_id}` → Delete menu item

### 🔹 5. Advanced Features
- `GET /menu/search` → Search items by keyword
- `GET /menu/sort` → Sort menu by price/name/category
- `GET /menu/page` → Pagination support
- `GET /menu/browse` → Combined search + sort + pagination

## 📂 Project Structure
```
Food Delivery App/
│
├── main.py # FastAPI backend code
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── pycache/ # Python cache files
```

## ▶️ How to Run This Project

### 1. Install dependencies
```
pip install -r requirements.txt
```
### 2. Run FastAPI server  
```
uvicorn main:app --reload
```
### 3. Open API documentation  
http://127.0.0.1:8000/docs  

## 🧪 API Testing

All endpoints are tested using Swagger UI (/docs).
You can directly:
Send requests
View responses
Test CRUD operations in real time

## 📌 Key Learning Outcomes
- Building REST APIs using FastAPI
- Working with Pydantic validation models
- Implementing CRUD operations
- Designing real-world backend workflows
- Handling query parameters and path variables
- API testing using Swagger UI


## 👨‍💻 Author
Pranjal Salvi  
GenAI Internship - Innomatics Research Labs  
