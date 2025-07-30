# 🚀 Streamlit App 1 – Interactive Dashboards & Food Ordering System

This repository contains two professional-level **Streamlit applications**:

1. 🛍️ **Sales Products Dashboard** – A real-time dashboard that fetches product data from an online API and displays insights.
2. 🍽️ **Zomato-style Food Ordering System** – A database-integrated food ordering app using MySQL and Streamlit.

These projects demonstrate your skills in front-end UI, backend database integration, API handling, and data visualization.

---

## 📁 Project Structure

streamlit-app-1/
├── sales_products.py # Streamlit dashboard using API data
├── zomato_app.py # Streamlit app integrated with MySQL
├── requirements.txt # Python dependencies
└── README.md # Project documentation

sql
Copy
Edit

---

## 1️⃣ `sales_products.py` – 🛒 Sales Product Dashboard

### 📌 Description
An interactive dashboard that fetches real-time product data from the [Fake Store API](https://fakestoreapi.com/products) and visualizes it with filters.

### ✅ Features
- Dynamic product list with images
- Category-based filtering
- Price range and rating filters
- Top N product visualization (using horizontal bar chart)
- Clean layout with product cards and insights

### 📸 Sample Preview
> *(Add screenshot here if available)*

---

## 2️⃣ `zomato_app.py` – 🍛 Zomato-Style Food Ordering App

### 📌 Description
A restaurant ordering system where users can select vegetarian or non-vegetarian items and place an order. All data is stored in a MySQL database.

### ✅ Features
- Category-based sidebar navigation
- Form to collect customer info and delivery address
- Inserts orders into multiple related MySQL tables
- Dynamic response and success messages

### 💾 Database Used
**MySQL** – All customer, item, and order data is stored in a normalized schema.

---

## 🗃️ MySQL Database Schema (sales)

Before running `zomato_app.py`, create the following schema:

```sql
CREATE DATABASE sales;
USE sales;

CREATE TABLE customers (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100),
    price DECIMAL(10,2),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    item_id INT,
    quantity INT,
    delivery_address VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES customers(user_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);
⚙️ Setup Instructions
🧰 1. Clone the repository
bash
Copy
Edit
git clone https://github.com/Kamalesh0330/streamlit-app-1.git
cd streamlit-app-1
📦 2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🚀 3. Run the apps
Sales Product Dashboard:
bash
Copy
Edit
streamlit run sales_products.py
Zomato-style Food Ordering App:
Make sure MySQL is running and DB is set up.

bash
Copy
Edit
streamlit run zomato_app.py
📜 requirements.txt
text
Copy
Edit
streamlit
pandas
requests
mysql-connector-python
matplotlib
👨‍💻 Author
Kamalesh D
🎓 B.E. Computer Science & Engineering
💼 Big Data Engineering Learner
🔗 LinkedIn
🐙 GitHub

🌟 Feedback & Contributions
If you find this project useful:

Give a ⭐️ to support this repo

Fork and contribute to make it better

Raise issues for bugs or feature requests

📣 License
This project is open-source and free to use.

yaml
Copy
Edit

---

✅ You can now copy this whole content and paste it directly into a new file named `README.md` in y