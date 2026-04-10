from fastapi import FastAPI, Query, Response, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

# -------------------------------
# DATA STORAGE
# -------------------------------
menu = [
    {"id": 1, "name": "Margherita Pizza", "price": 250, "category": "Pizza", "is_available": True},
    {"id": 2, "name": "Veg Burger", "price": 120, "category": "Burger", "is_available": True},
    {"id": 3, "name": "Coke", "price": 50, "category": "Drink", "is_available": True},
    {"id": 4, "name": "Chocolate Cake", "price": 180, "category": "Dessert", "is_available": False},
    {"id": 5, "name": "Paneer Pizza", "price": 300, "category": "Pizza", "is_available": True},
    {"id": 6, "name": "Fries", "price": 100, "category": "Snack", "is_available": True},
]

orders = []
cart = []

order_counter = 1


# -------------------------------
# ROOT
# -------------------------------
@app.get("/")
def home():
    return {"message": "Welcome to QuickBite Food Delivery"}


# -------------------------------
# HELPERS
# -------------------------------
def find_menu_item(item_id: int):
    for item in menu:
        if item["id"] == item_id:
            return item
    return None


def calculate_bill(price, quantity, order_type="delivery"):
    total = price * quantity
    if order_type == "delivery":
        total += 30
    return total


def filter_menu_logic(category=None, max_price=None, is_available=None):
    result = menu.copy()

    if category is not None:
        result = [i for i in result if i["category"].lower() == category.lower()]

    if max_price is not None:
        result = [i for i in result if i["price"] <= max_price]

    if is_available is not None:
        result = [i for i in result if i["is_available"] == is_available]

    return result


# -------------------------------
# MENU ENDPOINTS (STATIC FIRST)
# -------------------------------
@app.get("/menu/search")
def search_menu(keyword: str):
    result = [
        i for i in menu
        if keyword.lower() in i["name"].lower()
        or keyword.lower() in i["category"].lower()
    ]

    if not result:
        return {"message": "No items found"}

    return {"total_found": len(result), "items": result}


@app.get("/menu/sort")
def sort_menu(sort_by: str = "price", order: str = "asc"):
    if sort_by not in ["price", "name", "category"]:
        raise HTTPException(status_code=400, detail="Invalid sort field")

    reverse = order == "desc"
    sorted_menu = sorted(menu, key=lambda x: x[sort_by], reverse=reverse)

    return {"sorted_by": sort_by, "order": order, "items": sorted_menu}


@app.get("/menu/page")
def paginate_menu(page: int = 1, limit: int = 3):
    start = (page - 1) * limit
    end = start + limit

    total = len(menu)
    total_pages = (total + limit - 1) // limit

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": total_pages,
        "items": menu[start:end]
    }


@app.get("/menu/browse")
def browse_menu(
    keyword: Optional[str] = None,
    sort_by: str = "price",
    order: str = "asc",
    page: int = 1,
    limit: int = 4
):
    result = menu

    if keyword:
        result = [
            i for i in result
            if keyword.lower() in i["name"].lower()
            or keyword.lower() in i["category"].lower()
        ]

    reverse = order == "desc"
    result = sorted(result, key=lambda x: x[sort_by], reverse=reverse)

    start = (page - 1) * limit
    end = start + limit

    total = len(result)
    total_pages = (total + limit - 1) // limit

    return {
        "page": page,
        "total_items": total,
        "total_pages": total_pages,
        "items": result[start:end]
    }


# VARIABLE ROUTE (MUST BE LAST)
@app.get("/menu/{item_id}")
def get_item(item_id: int):
    item = find_menu_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# -------------------------------
# MENU CRUD
# -------------------------------
class NewMenuItem(BaseModel):
    name: str = Field(..., min_length=2)
    price: int = Field(..., gt=0)
    category: str = Field(..., min_length=2)
    is_available: bool = True


@app.post("/menu", status_code=201)
def add_item(item: NewMenuItem):
    for m in menu:
        if m["name"].lower() == item.name.lower():
            raise HTTPException(status_code=400, detail="Item already exists")

    new_id = max(i["id"] for i in menu) + 1

    new_item = item.dict()
    new_item["id"] = new_id

    menu.append(new_item)
    return new_item


@app.put("/menu/{item_id}")
def update_item(
    item_id: int,
    price: Optional[int] = None,
    is_available: Optional[bool] = None
):
    item = find_menu_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if price is not None:
        item["price"] = price

    if is_available is not None:
        item["is_available"] = is_available

    return item


@app.delete("/menu/{item_id}")
def delete_item(item_id: int):
    item = find_menu_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    menu.remove(item)
    return {"message": f"{item['name']} deleted successfully"}


# -------------------------------
# ORDERS
# -------------------------------
class OrderRequest(BaseModel):
    customer_name: str = Field(..., min_length=2)
    item_id: int
    quantity: int = Field(..., gt=0, le=20)
    delivery_address: str = Field(..., min_length=10)
    order_type: str = "delivery"


@app.get("/orders")
def get_orders():
    return {"total_orders": len(orders), "orders": orders}


@app.post("/orders", status_code=201)
def create_order(order: OrderRequest):
    global order_counter

    item = find_menu_item(order.item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if not item["is_available"]:
        raise HTTPException(status_code=400, detail="Item not available")

    total_price = calculate_bill(item["price"], order.quantity, order.order_type)

    new_order = {
        "order_id": order_counter,
        "customer_name": order.customer_name,
        "item": item["name"],
        "quantity": order.quantity,
        "total_price": total_price
    }

    orders.append(new_order)
    order_counter += 1

    return new_order


@app.get("/orders/search")
def search_orders(customer_name: str):
    result = [
        o for o in orders
        if customer_name.lower() in o["customer_name"].lower()
    ]
    return {"results": result}


@app.get("/orders/sort")
def sort_orders(order: str = "asc"):
    reverse = order == "desc"
    return sorted(orders, key=lambda x: x["total_price"], reverse=reverse)


# -------------------------------
# CART SYSTEM
# -------------------------------
class CheckoutRequest(BaseModel):
    customer_name: str
    delivery_address: str


@app.post("/cart/add")
def add_to_cart(item_id: int, quantity: int = 1):
    item = find_menu_item(item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if not item["is_available"]:
        raise HTTPException(status_code=400, detail="Item not available")

    for c in cart:
        if c["item_id"] == item_id:
            c["quantity"] += quantity
            return {"message": "Cart updated", "cart": cart}

    cart.append({
        "item_id": item_id,
        "name": item["name"],
        "price": item["price"],
        "quantity": quantity
    })

    return {"message": "Added to cart", "cart": cart}


@app.get("/cart")
def view_cart():
    total = sum(i["price"] * i["quantity"] for i in cart)
    return {"items": cart, "grand_total": total}


@app.post("/cart/checkout", status_code=201)
def checkout(data: CheckoutRequest):
    global order_counter

    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")

    placed_orders = []
    grand_total = 0

    for item in cart:
        total_price = calculate_bill(item["price"], item["quantity"], "delivery")

        new_order = {
            "order_id": order_counter,
            "customer_name": data.customer_name,
            "item": item["name"],
            "quantity": item["quantity"],
            "total_price": total_price
        }

        orders.append(new_order)
        placed_orders.append(new_order)

        grand_total += total_price
        order_counter += 1

    cart.clear()

    return {
        "orders": placed_orders,
        "grand_total": grand_total
    }