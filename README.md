# 🍕 QuickBite | Food Delivery Backend API with FastAPI

> **A RESTful backend application built with FastAPI that simulates a real-world food delivery platform, featuring menu management, cart operations, order processing, search, sorting, pagination, and complete CRUD functionality.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-499848)
![Swagger](https://img.shields.io/badge/Swagger-API%20Documentation-85EA2D?logo=swagger)

---

## 📖 Project Overview

Modern food delivery platforms rely on robust backend systems to efficiently manage menus, customer orders, shopping carts, and business operations. Building scalable APIs is essential for delivering fast, reliable, and maintainable services.

**QuickBite** is a RESTful backend application developed using **FastAPI**, designed to simulate the core functionalities of a food delivery system. The project demonstrates backend development concepts including API design, request validation, CRUD operations, modular architecture, and automatic API documentation.

The application provides a complete backend workflow for menu management, order processing, shopping cart operations, advanced searching, sorting, and pagination.

---

## 🎯 Project Objectives

* Develop RESTful APIs using FastAPI
* Implement complete CRUD operations
* Validate request and response data using Pydantic
* Design modular backend workflows
* Handle search, sorting, filtering, and pagination
* Demonstrate modern backend development practices

---

## ✨ Key Features

### 🍽️ Menu Management

* Add new menu items
* Update existing items
* Delete menu items
* View complete menu
* Duplicate item validation

### 🛒 Cart System

* Add products to cart
* Quantity management
* Calculate cart total
* Checkout workflow

### 📦 Order Management

* Create customer orders
* Retrieve all orders
* Search customer orders
* Sort orders by total price

### 🔍 Advanced Search

* Keyword search
* Sorting by multiple fields
* Pagination
* Combined filtering and browsing

### 📑 API Documentation

* Interactive Swagger UI
* Automatic endpoint documentation
* Request validation
* Response schemas

---

## 🏗️ System Architecture

```text
Client (Browser / Postman)
            │
            ▼
      FastAPI Application
            │
 ┌──────────┼──────────┐
 │          │          │
 ▼          ▼          ▼
Menu API  Cart API  Order API
            │
            ▼
 Business Logic Layer
            │
            ▼
In-Memory Data Storage
```

---

## 📌 REST API Endpoints

## Home

| Method | Endpoint | Description     |
| ------ | -------- | --------------- |
| GET    | `/`      | Welcome message |

### Menu

| Method | Endpoint          | Description                |
| ------ | ----------------- | -------------------------- |
| GET    | `/menu`           | Retrieve all menu items    |
| GET    | `/menu/{item_id}` | Retrieve a menu item by ID |
| POST   | `/menu`           | Add a new menu item        |
| PUT    | `/menu/{item_id}` | Update a menu item         |
| DELETE | `/menu/{item_id}` | Delete a menu item         |
| GET    | `/menu/search`    | Search menu items          |
| GET    | `/menu/sort`      | Sort menu items            |
| GET    | `/menu/page`      | Paginate menu items        |
| GET    | `/menu/browse`    | Search + Sort + Pagination |
| GET    | `/menu/summary`   | Menu statistics            |

### Orders

| Method | Endpoint         | Description          |
| ------ | ---------------- | -------------------- |
| POST   | `/orders`        | Create a new order   |
| GET    | `/orders`        | Retrieve all orders  |
| GET    | `/orders/search` | Search orders        |
| GET    | `/orders/sort`   | Sort customer orders |

### Cart

| Method | Endpoint         | Description        |
| ------ | ---------------- | ------------------ |
| POST   | `/cart/add`      | Add item to cart   |
| GET    | `/cart`          | View shopping cart |
| POST   | `/cart/checkout` | Checkout cart      |

---

## 🛠️ Technology Stack

| Category          | Technologies |
| ----------------- | ------------ |
| Programming       | Python       |
| Backend Framework | FastAPI      |
| Data Validation   | Pydantic     |
| ASGI Server       | Uvicorn      |
| API Documentation | Swagger UI   |
| Architecture      | RESTful APIs |

---

## 📂 Project Structure

```text
QuickBite/
│
├── main.py
├── requirements.txt
├── README.md
└── __pycache__/
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/pranjalsalvi/quickbite-fastapi-food-delivery.git

cd quickbite-fastapi-food-delivery
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## 💡 Key Highlights

* RESTful API development with FastAPI
* Full CRUD operations
* Request validation using Pydantic
* Interactive Swagger documentation
* Cart and checkout workflow
* Order management system
* Search, sorting, and pagination
* Clean and modular backend architecture

---

## 📌 Applications

This backend architecture can be adapted for:

* Food Delivery Platforms
* Restaurant Management Systems
* E-commerce Applications
* Inventory Management
* Online Ordering Systems
* Retail Backend Services

---

## 🚀 Future Enhancements

* Database integration with PostgreSQL or MySQL
* SQLAlchemy ORM support
* JWT-based authentication
* Role-based authorization
* Payment gateway integration
* Docker containerization
* Redis caching
* Cloud deployment (AWS, Azure, or Render)
* Unit and integration testing with Pytest

---

## 👨‍💻 About Me

**Pranjal Salvi**

Aspiring **Data Analyst & AI Engineer** with a strong interest in Backend Development, Data Analytics, Machine Learning, and Generative AI.

### Connect with me

* 🔗 LinkedIn: https://www.linkedin.com/in/pranjal-salvi-380732227/
* 💻 GitHub: https://github.com/pranjalsalvi

---

## ⭐ Support

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.

Your support motivates me to continue building and sharing open-source projects in Backend Development, Data Science, and AI.

---

### Thank you for visiting this repository! 🚀
