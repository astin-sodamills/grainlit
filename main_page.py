import streamlit as st
import pandas as pd

st.markdown("""
# Hello, :red[Soda]!

---  
""")
st.code("a=10\nb=100")
df = pd.dataframe({
  "name":["Eric","Bob","Tom"],
  "age”:[12,15,11]
})

df

st.button("Click me!")

"---"
