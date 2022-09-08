import streamlit as st
st.title("Hello StreamLit")
st.subheader("Working on square of a number")
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
