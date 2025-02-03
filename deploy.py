import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query 
import pandas as pd
import numpy as np 

st.title("Pemerolehan Informasi Al-Quran Bahasa Indonesia")

st.text_input("Masukkan Kueri")
st.button("Search")

# connection to database
connection = st.connection("supabase", type=SupabaseConnection)
database = execute_query(connection.table("data_manualisasi").select("id, indoText"), ttl=None)

print(database)