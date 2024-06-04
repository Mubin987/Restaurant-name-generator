import streamlit as st
import lang_chain

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Pakistani","Turkish","Arabic","Spanish","Mexican","Chinese","Italian"))


if cuisine:
    response = lang_chain.generate_restaurant_name_and_menuitems(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)
    
    