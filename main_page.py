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

csv_data = df.to_csv(index=False)

with open("00.csv", "w", encoding="utf-8") as file:
  writer = csv.writer(file)
  writer.writerow(csv_data)
  
"---"
