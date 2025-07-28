import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Sales Products')
st.header("Retail Data for Analysis")
st.title("Retail Dataset")

# Step 1: Fetch data from API
response = requests.get("https://fakestoreapi.com/products")

if response.status_code==200:
    data=response.json()
    df=pd.DataFrame(data)

    st.dataframe(df[['title','price','category','rating']])

    category=df['category'].unique()
    s_category=st.selectbox("Select the Category",category)

    filtered=df[df["category"]==s_category]

    min_price=int(filtered['price'].min())
    max_price=int(filtered['price'].max())

    price_range=st.slider("Select the price range",min_value=min_price,max_value=max_price,value=(min_price,max_price))

    price_filter=filtered[(df['price']>=price_range[0]) & (df['price']<=price_range[1])]

    top_n=st.number_input("Enter the rating",min_value=1,max_value=10,value=5)
    
    price_filter['rate_value']=price_filter['rating'].apply(lambda x: x['rate'])

    st.dataframe(price_filter[['title','price','category','rating','rate_value']])
    top=price_filter.sort_values(by='rate_value',ascending=False).head(top_n)

    fig,ax=plt.subplots(figsize=(10,15))
    ax.barh(top['title'],top['price'],edgecolor='black',color='purple')
    ax.set_title("Top Products by price")
    ax.set_ylabel("Product")
    ax.set_xlabel("Price")
    ax.grid(axis='x')

    plt.tight_layout()
    st.pyplot(fig)