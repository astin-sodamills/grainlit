import streamlit as st
import pandas as pd
import csv

st.markdown("""
# Hello, :red[Soda]!

---  
""")
st.code("a=10\nb=100")
df = pd.DataFrame({
  "name":["Eric","Bob","Tom"],
  "age":[12,15,11]
})

return df.to_csv(index=False)

st.button("Click me!")
  
"---"
