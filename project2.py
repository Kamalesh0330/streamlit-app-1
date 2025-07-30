import streamlit as st
import mysql.connector

st.set_page_config(page_title='Zomato App',layout='wide',page_icon="🍽️")
st.markdown("""
    <style>
        .banner {
            background-color: #f63366;
            padding: 20px;
            border-radius: 12px;
            color: white;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# Display the banner
st.markdown('<div class="banner">🍽️ Welcome to Kamalesh’s Food Court!</div>', unsafe_allow_html=True)
st.subheader("Order Your Favorite Dishes!")

st.markdown("""
    <style>
        .food-card {
            background-color: #ffffff;
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .food-title {
            font-size: 24px;
            font-weight: bold;
            color: #f63366;
        }
        .food-desc {
            font-size: 16px;
            margin: 10px 0;
            color: #555;
        }
        .food-price {
            font-size: 18px;
            font-weight: bold;
            color: #007bff;
        }
        .order-button {
            margin-top: 10px;
            padding: 8px 16px;
            background-color: #f63366;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)





def conct():
    return mysql.connector.connect(host='localhost',database='sales',user='root',password='keerthi@0330kamalesh')

with st.sidebar:
    food_type=st.selectbox("Choose your wish!",['Veg','Non-veg'])
    


if food_type=='Veg':
    fname=st.text_input("Your First Name")
    lname=st.text_input("Your Last Name")
    phone=st.text_input("Mobile Number")
    email=st.text_input("Email")

    v_food=st.selectbox("Choose your dish",['Paneer'])
    quant1=st.number_input("How many you want")
    add1=st.text_input("Enter Your address")
    if v_food=='Paneer':
        place1=st.checkbox(f"Place Order {v_food}")
        if place1:
            connection=conct()
            cursor=connection.cursor()
            cursor.execute("select item_id from items where item_name=%s",(v_food,))
            r=cursor.fetchone()
            item_id=r[0]
            query1="insert into customers(first_name,last_name,phone_number,email) values(%s, %s, %s, %s)"
            cursor.execute(query1,(fname,lname,phone,email))
            connection.commit()
            user_id=cursor.lastrowid
            query="insert into orders(user_id,item_id,quantity,delivery_address,item_name) values(%s, %s, %s, %s, %s)"
            cursor.execute(query,(user_id,item_id,quant1,add1,v_food))
            connection.commit()
            st.success("Your Order Placed Successfully")
            
            cursor.close()
            connection.close()

else:
    fname=st.text_input("Your First Name")
    lname=st.text_input("Your Last Name")
    phone=st.text_input("Mobile Number")
    email=st.text_input("Email")
    n_food=st.selectbox("Choose your dish",['Biriyani','Butter Chicken'])
    quant2=st.number_input("How many you want")
    add2=st.text_input("Enter Your address")
    if n_food=='Biriyani':
        place2=st.checkbox(f"Place Order {n_food}")
        if place2:
            connection=conct()
            cursor=connection.cursor()
            cursor.execute("Select item_id from items where item_name=%s",(n_food,))
            r=cursor.fetchone()
            if r:
                item_id=r[0]
            query1="insert into customers(first_name,last_name,phone_number,email) values(%s, %s, %s, %s)"
            cursor.execute(query1,(fname,lname,phone,email))
            connection.commit()
            user_id=cursor.lastrowid
            query="insert into orders(user_id,item_id,quantity,delivery_address,item_name) values(%s, %s, %s, %s, %s)"
            cursor.execute(query,(user_id,item_id,quant2,add2,n_food))
            connection.commit()
            st.success("Your Order Placed Successfully")
            
            cursor.close()
            connection.close()
    elif n_food=='Butter Chicken':
        place3=st.checkbox(f"Place Order {n_food}")
        if place3:
            connection=conct()
            cursor=connection.cursor()
            cursor.execute("select item_id from items where item_name=%s",(n_food,))
            r=cursor.fetchone()
            if r:
                
                item_id=r[0]
            query1="insert into customers(first_name,last_name,phone_number,email) values(%s, %s, %s, %s)"
            cursor.execute(query1,(fname,lname,phone,email))
            connection.commit()
            user_id=cursor.lastrowid
            query="insert into orders(user_id,item_id,quantity,delivery_address,item_name) values(%s, %s, %s, %s, %s)"
            cursor.execute(query,(user_id,item_id,quant2,add2,n_food))
            connection.commit()
            st.success("your Order Placed Successfully")
            
            cursor.close()
            connection.close()